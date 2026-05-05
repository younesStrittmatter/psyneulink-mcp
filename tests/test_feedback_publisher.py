"""Tests for the fire-and-forget GitHub-issue mirror of runtime captures.

The publisher must:
* Never block the caller (we still join on the returned thread for
  deterministic assertions, but `try_file` itself returns immediately).
* Never raise from the runtime path (every test path here uses the public
  `try_file` entry point and asserts no exception escapes).
* Dedup hard within a process (one triple → one search/create across
  many calls).
* Honor `PSYNEULINK_MCP_AUTO_FILE_ISSUES=0` and the absence of `gh` on
  PATH by silently no-op-ing.
* Skip the create call when an open issue with the same title already
  exists on the corpus.

`gh` is mocked at the `corpus` module boundary so these tests don't
shell out and don't hit GitHub.
"""

from __future__ import annotations

from typing import Any

import pytest

from psyneulink_mcp import corpus, feedback, feedback_publisher

# --------------------------------------------------------------------------- #
# fixtures + helpers                                                          #
# --------------------------------------------------------------------------- #


@pytest.fixture(autouse=True)
def _isolate_publisher(monkeypatch):
    """Ensure each test starts with a fresh dedup cache, `gh` "installed",
    and the auto-file env var explicitly enabled (so a developer's local
    opt-out can't poison the suite)."""
    feedback_publisher.reset_for_tests()
    monkeypatch.setattr(feedback_publisher.shutil, "which", lambda _exe: "/usr/local/bin/gh")
    monkeypatch.setenv(feedback_publisher.ENV_AUTO_FILE_ISSUES, "1")
    yield
    feedback_publisher.reset_for_tests()


def _entry(
    *,
    tool_name: str = "some_tool",
    exc_type: str = "ValueError",
    exc_message: str = "bad x=42",
    args: dict[str, Any] | None = None,
    server_version: str = "0.1.0",
) -> dict[str, Any]:
    return {
        "timestamp": "2026-05-04T00:00:00Z",
        "source": "auto",
        "tool_name": tool_name,
        "tool_layer": "curated",
        "pnl_version": "unknown",
        "server_version": server_version,
        "payload": {
            "args": args if args is not None else {"x": 42},
            "exception_type": exc_type,
            "exception_message": exc_message,
            "traceback": (
                "Traceback (most recent call last):\n"
                '  File "x.py", line 1, in <module>\n'
                f"{exc_type}: {exc_message}\n"
            ),
        },
    }


def _wait(thread) -> None:
    """Join the worker so the test can assert on the gh side effects."""
    if thread is not None:
        thread.join(timeout=5.0)
        assert not thread.is_alive(), "publisher worker did not finish"


# --------------------------------------------------------------------------- #
# title / body shape                                                          #
# --------------------------------------------------------------------------- #


def test_title_for_is_deterministic_and_capped() -> None:
    long_msg = "boom " * 200  # comfortably > 80 chars
    entry = _entry(exc_message=long_msg)
    title = feedback_publisher._title_for(entry)
    assert title.startswith("[auto] some_tool: ValueError: ")
    msg_part = title.split("ValueError: ", 1)[1]
    assert len(msg_part) <= 80
    # Re-rendering the same entry gives the same title (dedup join key).
    assert feedback_publisher._title_for(entry) == title


def test_title_normalizes_whitespace() -> None:
    a = feedback_publisher._title_for(_entry(exc_message="foo\n  bar\tbaz"))
    b = feedback_publisher._title_for(_entry(exc_message="foo bar baz"))
    assert a == b


def test_body_renders_issue_form_sections() -> None:
    body = feedback_publisher._body_for(_entry())
    # Same `### Label\n\n<value>\n\n` shape that `corpus._parse_issue_body`
    # parses for human-filed issues — keeps the regen pipeline format-clean.
    for label in (
        "### Tool name",
        "### Issue type",
        "### Description",
        "### Suggested fix",
        "### Agent context",
    ):
        assert label in body
    assert "wrong_behavior" in body
    assert "auto-captured runtime error from psyneulink-mcp" in body


# --------------------------------------------------------------------------- #
# enabled / disabled gating                                                   #
# --------------------------------------------------------------------------- #


def test_try_file_noop_when_env_disabled(monkeypatch) -> None:
    monkeypatch.setenv(feedback_publisher.ENV_AUTO_FILE_ISSUES, "0")

    def _boom(*_a, **_kw):
        raise AssertionError("must not reach corpus when disabled")

    monkeypatch.setattr(corpus, "find_existing_feedback_issue", _boom)
    monkeypatch.setattr(corpus, "open_feedback_issue", _boom)

    assert feedback_publisher.try_file(_entry()) is None


@pytest.mark.parametrize("falsy", ["0", "false", "FALSE", "no", "off", ""])
def test_try_file_treats_common_falsy_values_as_disabled(monkeypatch, falsy) -> None:
    monkeypatch.setenv(feedback_publisher.ENV_AUTO_FILE_ISSUES, falsy)
    assert feedback_publisher.try_file(_entry()) is None


def test_try_file_noop_when_gh_missing(monkeypatch) -> None:
    monkeypatch.setattr(feedback_publisher.shutil, "which", lambda _exe: None)

    def _boom(*_a, **_kw):
        raise AssertionError("must not reach corpus when gh is missing")

    monkeypatch.setattr(corpus, "find_existing_feedback_issue", _boom)
    monkeypatch.setattr(corpus, "open_feedback_issue", _boom)

    assert feedback_publisher.try_file(_entry()) is None


def test_try_file_returns_none_for_malformed_entry(monkeypatch) -> None:
    """Missing payload keys must short-circuit, not crash the runtime path."""
    bad = {"tool_name": "x"}  # no payload
    assert feedback_publisher.try_file(bad) is None


# --------------------------------------------------------------------------- #
# dedup (in-process)                                                          #
# --------------------------------------------------------------------------- #


def test_try_file_creates_one_issue_for_first_occurrence(monkeypatch) -> None:
    found_calls: list[str] = []
    create_calls: list[dict[str, Any]] = []

    monkeypatch.setattr(
        corpus,
        "find_existing_feedback_issue",
        lambda title: found_calls.append(title) or None,
    )

    def fake_open(*, title, body, labels):
        create_calls.append({"title": title, "body": body, "labels": labels})
        return "https://example/issues/1"

    monkeypatch.setattr(corpus, "open_feedback_issue", fake_open)

    _wait(feedback_publisher.try_file(_entry()))

    assert len(found_calls) == 1
    assert len(create_calls) == 1
    # The publisher applies three labels: the long-standing
    # `feedback` + `auto` pair plus a per-symbol `pnl:<tool>` label
    # so closed issues can be re-discovered at regen time as
    # historical failures (Phase 1 t5).
    assert create_calls[0]["labels"] == [
        corpus.FEEDBACK_LABEL,
        corpus.AUTO_LABEL,
        corpus.pnl_symbol_label("some_tool"),
    ]
    assert create_calls[0]["title"].startswith("[auto] some_tool: ValueError:")


def test_dedup_cache_prevents_re_fire_for_same_triple(monkeypatch) -> None:
    found_calls: list[str] = []
    create_calls: list[Any] = []

    monkeypatch.setattr(
        corpus,
        "find_existing_feedback_issue",
        lambda title: found_calls.append(title) or None,
    )
    monkeypatch.setattr(
        corpus,
        "open_feedback_issue",
        lambda **kw: create_calls.append(kw) or "url",
    )

    e = _entry()
    _wait(feedback_publisher.try_file(e))
    # Same triple → cache hit → second call returns None and does no I/O.
    assert feedback_publisher.try_file(e) is None
    _wait(feedback_publisher.try_file(e))

    assert len(found_calls) == 1
    assert len(create_calls) == 1


def test_different_triples_each_get_their_own_issue(monkeypatch) -> None:
    found_calls: list[str] = []
    create_calls: list[dict[str, Any]] = []

    monkeypatch.setattr(
        corpus,
        "find_existing_feedback_issue",
        lambda title: found_calls.append(title) or None,
    )
    monkeypatch.setattr(
        corpus,
        "open_feedback_issue",
        lambda **kw: create_calls.append(kw) or "url",
    )

    _wait(feedback_publisher.try_file(_entry(tool_name="tool_a")))
    _wait(feedback_publisher.try_file(_entry(tool_name="tool_b")))
    _wait(feedback_publisher.try_file(_entry(exc_type="RuntimeError")))
    _wait(feedback_publisher.try_file(_entry(exc_message="totally different msg")))

    assert len(create_calls) == 4


# --------------------------------------------------------------------------- #
# cross-process dedup via search                                              #
# --------------------------------------------------------------------------- #


def test_existing_issue_skips_create(monkeypatch) -> None:
    """If an open `feedback,auto` issue with the same title already exists
    on the corpus (e.g. from another machine), don't open a duplicate."""
    create_calls: list[Any] = []

    monkeypatch.setattr(corpus, "find_existing_feedback_issue", lambda title: 123)
    monkeypatch.setattr(
        corpus,
        "open_feedback_issue",
        lambda **kw: create_calls.append(kw) or "url",
    )

    _wait(feedback_publisher.try_file(_entry()))
    assert create_calls == []


# --------------------------------------------------------------------------- #
# never raises                                                                #
# --------------------------------------------------------------------------- #


def test_search_failure_does_not_raise(monkeypatch, capsys) -> None:
    def boom(_title):
        raise corpus.CorpusUnavailable("gh auth expired")

    monkeypatch.setattr(corpus, "find_existing_feedback_issue", boom)
    monkeypatch.setattr(
        corpus,
        "open_feedback_issue",
        lambda **kw: (_ for _ in ()).throw(AssertionError("must not create when search failed")),
    )
    _wait(feedback_publisher.try_file(_entry()))

    err = capsys.readouterr().err
    assert "search failed" in err


def test_create_failure_does_not_raise(monkeypatch, capsys) -> None:
    monkeypatch.setattr(corpus, "find_existing_feedback_issue", lambda _t: None)

    def boom(**_kw):
        raise corpus.CorpusUnavailable("gh got rate-limited")

    monkeypatch.setattr(corpus, "open_feedback_issue", boom)
    _wait(feedback_publisher.try_file(_entry()))

    err = capsys.readouterr().err
    assert "create failed" in err


def test_unexpected_worker_exception_is_swallowed(monkeypatch, capsys) -> None:
    def boom(_title):
        raise ZeroDivisionError("synthetic")

    monkeypatch.setattr(corpus, "find_existing_feedback_issue", boom)
    _wait(feedback_publisher.try_file(_entry()))

    err = capsys.readouterr().err
    assert "unexpected publisher failure" in err


# --------------------------------------------------------------------------- #
# integration with feedback.log_runtime_error                                 #
# --------------------------------------------------------------------------- #


def test_log_runtime_error_dispatches_to_publisher(monkeypatch, tmp_path) -> None:
    """The hook in `feedback.log_runtime_error` must invoke `try_file` with
    the same envelope it wrote to disk — that's the contract that lets the
    publisher's title/body match the JSONL record one-to-one."""
    monkeypatch.setenv(feedback.ENV_FEEDBACK_PATH, str(tmp_path / "issues.jsonl"))

    captured: list[dict[str, Any]] = []

    def fake_try_file(entry):
        captured.append(entry)
        return None

    monkeypatch.setattr(feedback_publisher, "try_file", fake_try_file)

    try:
        raise RuntimeError("kaboom")
    except RuntimeError as exc:
        feedback.log_runtime_error(
            tool_name="t",
            tool_layer="curated",
            args={"x": 1},
            exc=exc,
        )

    assert len(captured) == 1
    entry = captured[0]
    assert entry["tool_name"] == "t"
    assert entry["payload"]["exception_type"] == "RuntimeError"
    assert entry["payload"]["exception_message"] == "kaboom"


def test_log_runtime_error_swallows_publisher_dispatch_errors(
    monkeypatch, tmp_path, capsys
) -> None:
    """Even if the publisher import or call blows up, the runtime path must
    keep working — the local JSONL is still written and no exception leaks
    back to the agent."""
    monkeypatch.setenv(feedback.ENV_FEEDBACK_PATH, str(tmp_path / "issues.jsonl"))

    def boom(_entry):
        raise RuntimeError("publisher broken")

    monkeypatch.setattr(feedback_publisher, "try_file", boom)

    try:
        raise ValueError("explode")
    except ValueError as exc:
        # Must not raise.
        feedback.log_runtime_error(
            tool_name="t",
            tool_layer="curated",
            args={},
            exc=exc,
        )

    err = capsys.readouterr().err
    assert "feedback publish dispatch failed" in err
    # JSONL still written despite the publisher failure.
    contents = (tmp_path / "issues.jsonl").read_text()
    assert "explode" in contents


# --------------------------------------------------------------------------- #
# per-symbol pnl: label + publisher self-heal (Phase 1 t5 part A)             #
# --------------------------------------------------------------------------- #


def test_try_file_self_heals_missing_pnl_label_and_retries_once(monkeypatch) -> None:
    """Missing `pnl:<tool>` label → one `ensure_label_exists` + one retry.

    The first `open_feedback_issue` raises with stderr that names our
    per-symbol label and "not found"; the publisher self-heals via
    `ensure_label_exists`, then retries the create exactly once and
    succeeds.
    """
    monkeypatch.setattr(corpus, "find_existing_feedback_issue", lambda _t: None)

    create_calls: list[dict[str, Any]] = []
    label_create_calls: list[str] = []

    def fake_open(**kw):
        create_calls.append(kw)
        if len(create_calls) == 1:
            raise corpus.CorpusUnavailable("could not add label: 'pnl:some_tool' not found")
        return "https://example/issues/2"

    def fake_ensure_label(name, **_kw):
        label_create_calls.append(name)
        return True

    monkeypatch.setattr(corpus, "open_feedback_issue", fake_open)
    monkeypatch.setattr(corpus, "ensure_label_exists", fake_ensure_label)

    _wait(feedback_publisher.try_file(_entry()))

    assert label_create_calls == ["pnl:some_tool"]
    assert len(create_calls) == 2  # initial + one retry
    assert create_calls[0]["labels"][-1] == "pnl:some_tool"


def test_try_file_does_not_retry_when_label_heal_fails(monkeypatch, capsys) -> None:
    """If ensure_label_exists itself fails, don't loop — drop the issue.

    The local JSONL still has the full record; hammering `gh` from
    background threads on a flaky link is its own anti-pattern.
    """
    monkeypatch.setattr(corpus, "find_existing_feedback_issue", lambda _t: None)

    create_calls: list[Any] = []

    def fake_open(**kw):
        create_calls.append(kw)
        raise corpus.CorpusUnavailable("could not add label: 'pnl:some_tool' not found")

    def fake_ensure_label(_name, **_kw):
        raise corpus.CorpusUnavailable("HTTP 500 from gh label create")

    monkeypatch.setattr(corpus, "open_feedback_issue", fake_open)
    monkeypatch.setattr(corpus, "ensure_label_exists", fake_ensure_label)

    _wait(feedback_publisher.try_file(_entry()))
    err = capsys.readouterr().err
    # Heal failure surfaces as a single stderr note, not a retry loop.
    assert "label-heal failed" in err
    assert len(create_calls) == 1


def test_try_file_does_not_retry_unrelated_failures(monkeypatch, capsys) -> None:
    """A non-label failure (rate-limit, auth, generic 500) drops without retry.

    Self-heal is targeted at the missing-label race only — a generic
    `gh` failure shouldn't waste a `gh label create` call (and the
    associated rate-limit budget) on a guess.
    """
    monkeypatch.setattr(corpus, "find_existing_feedback_issue", lambda _t: None)

    create_calls: list[Any] = []
    label_calls: list[Any] = []

    def fake_open(**kw):
        create_calls.append(kw)
        raise corpus.CorpusUnavailable("API rate limit exceeded for IP")

    def fake_ensure_label(name, **_kw):
        label_calls.append(name)
        return True

    monkeypatch.setattr(corpus, "open_feedback_issue", fake_open)
    monkeypatch.setattr(corpus, "ensure_label_exists", fake_ensure_label)

    _wait(feedback_publisher.try_file(_entry()))
    err = capsys.readouterr().err
    assert "create failed" in err
    assert len(create_calls) == 1
    assert label_calls == []  # no self-heal triggered for unrelated failure


def test_self_heal_gives_up_on_repeat_misses_for_same_label(monkeypatch) -> None:
    """Second consecutive miss for the same label in one process — give up.

    Different triples for the same tool would normally both apply the
    same `pnl:<tool>` label. Once the first missed-label heal attempt
    fails, the second triple shouldn't re-attempt the heal — the
    `_HEAL_ATTEMPTED` set tracks that.
    """
    monkeypatch.setattr(corpus, "find_existing_feedback_issue", lambda _t: None)

    create_calls: list[Any] = []
    label_calls: list[Any] = []

    def fake_open(**kw):
        create_calls.append(kw)
        raise corpus.CorpusUnavailable("could not add label: 'pnl:some_tool' not found")

    def fake_ensure_label(name, **_kw):
        label_calls.append(name)
        raise corpus.CorpusUnavailable("HTTP 500 from gh label create")

    monkeypatch.setattr(corpus, "open_feedback_issue", fake_open)
    monkeypatch.setattr(corpus, "ensure_label_exists", fake_ensure_label)

    # Two distinct triples (different exception messages) for same tool.
    _wait(feedback_publisher.try_file(_entry(exc_message="boom-a")))
    _wait(feedback_publisher.try_file(_entry(exc_message="boom-b")))

    # Two issue creates attempted (one per triple), but only ONE heal
    # call — the second is short-circuited by `_HEAL_ATTEMPTED`.
    assert len(create_calls) == 2
    assert label_calls == ["pnl:some_tool"]


def test_self_heal_caches_success_within_process(monkeypatch) -> None:
    """One successful heal applies to subsequent triples for same label.

    After the first triple self-heals the missing label, the second
    triple's create attempt succeeds outright (because the label now
    exists) — but if it ever needed to re-heal, the cache should
    skip the redundant `ensure_label_exists` call.
    """
    monkeypatch.setattr(corpus, "find_existing_feedback_issue", lambda _t: None)

    create_calls: list[Any] = []
    label_calls: list[Any] = []
    label_exists = {"created": False}

    def fake_open(**kw):
        create_calls.append(kw)
        if not label_exists["created"]:
            raise corpus.CorpusUnavailable("could not add label: 'pnl:some_tool' not found")
        return "https://example/issues/N"

    def fake_ensure_label(name, **_kw):
        label_calls.append(name)
        label_exists["created"] = True
        return True

    monkeypatch.setattr(corpus, "open_feedback_issue", fake_open)
    monkeypatch.setattr(corpus, "ensure_label_exists", fake_ensure_label)

    _wait(feedback_publisher.try_file(_entry(exc_message="boom-a")))
    _wait(feedback_publisher.try_file(_entry(exc_message="boom-b")))

    # First triple: create → 404 label → heal → retry create → ok (2 creates)
    # Second triple: create → ok (1 create, because the label is real now)
    # Total: 3 creates, 1 heal call (no second heal needed).
    assert len(create_calls) == 3
    assert label_calls == ["pnl:some_tool"]


def test_self_heal_logs_action_to_stderr(monkeypatch, capsys) -> None:
    """Operators want to see when the publisher self-heals.

    Visibility helps diagnose flaky label state across machines without
    being noisy on stderr (the message fires at most once per label per
    process).
    """
    monkeypatch.setattr(corpus, "find_existing_feedback_issue", lambda _t: None)

    label_exists = {"created": False}

    def fake_open(**kw):
        if not label_exists["created"]:
            raise corpus.CorpusUnavailable("could not add label: 'pnl:some_tool' not found")
        return "url"

    def fake_ensure_label(_name, **_kw):
        label_exists["created"] = True
        return True

    monkeypatch.setattr(corpus, "open_feedback_issue", fake_open)
    monkeypatch.setattr(corpus, "ensure_label_exists", fake_ensure_label)

    _wait(feedback_publisher.try_file(_entry()))
    err = capsys.readouterr().err
    assert "self-healed missing label pnl:some_tool" in err
