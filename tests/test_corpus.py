"""Tests for the read-only corpus client and the brainlike curated tools.

The `gh` CLI is mocked at the `subprocess.run` boundary throughout, so
these tests don't talk to GitHub and don't need `gh` installed.
"""

from __future__ import annotations

import json
import subprocess
from pathlib import Path
from typing import Any

import pytest

from psyneulink_mcp import corpus
from psyneulink_mcp.tools.curated import brainlike as curated_brainlike

# --------------------------------------------------------------------------- #
# helpers                                                                     #
# --------------------------------------------------------------------------- #


class FakeMCP:
    """Minimal stand-in for FastMCP — captures registered tools by name."""

    def __init__(self) -> None:
        self.tools: dict[str, Any] = {}

    def tool(self, **_kwargs: Any):
        def decorator(fn):
            self.tools[fn.__name__] = fn
            return fn

        return decorator


def _completed(stdout: str = "", stderr: str = "", returncode: int = 0):
    return subprocess.CompletedProcess(
        args=["gh"], returncode=returncode, stdout=stdout, stderr=stderr
    )


@pytest.fixture
def fake_corpus_env(monkeypatch, tmp_path) -> Path:
    """Make `gh` look installed and isolate the corpus cache to tmp_path."""
    monkeypatch.setattr(corpus.shutil, "which", lambda _exe: "/usr/local/bin/gh")
    monkeypatch.setenv(corpus.ENV_CORPUS_CACHE, str(tmp_path / "cache"))
    monkeypatch.setenv(corpus.ENV_CORPUS_REPO, "test-owner/test-corpus")
    monkeypatch.setenv(corpus.ENV_CORPUS_REF, "main")
    return tmp_path


# --------------------------------------------------------------------------- #
# config & subprocess seam                                                    #
# --------------------------------------------------------------------------- #


def test_corpus_repo_and_ref_use_env_overrides(monkeypatch) -> None:
    monkeypatch.setenv(corpus.ENV_CORPUS_REPO, "alice/x")
    monkeypatch.setenv(corpus.ENV_CORPUS_REF, "dev")
    assert corpus.corpus_repo() == "alice/x"
    assert corpus.corpus_ref() == "dev"


def test_corpus_repo_falls_back_to_default(monkeypatch) -> None:
    monkeypatch.delenv(corpus.ENV_CORPUS_REPO, raising=False)
    assert corpus.corpus_repo() == corpus.CORPUS_REPO_DEFAULT


def test_run_gh_raises_when_gh_missing(monkeypatch) -> None:
    monkeypatch.setattr(corpus.shutil, "which", lambda _exe: None)
    with pytest.raises(corpus.CorpusUnavailable, match="gh.*not found"):
        corpus._run_gh(["api", "repos/x/y"])


def test_run_gh_raises_on_auth_failure(monkeypatch, fake_corpus_env) -> None:
    def fake_run(*_a, **_kw):
        return _completed(stderr="error: not logged in. Run gh auth login.", returncode=1)

    monkeypatch.setattr(corpus.subprocess, "run", fake_run)
    with pytest.raises(corpus.CorpusUnavailable, match="not authenticated"):
        corpus._run_gh(["api", "repos/x/y"])


def test_run_gh_raises_on_generic_failure(monkeypatch, fake_corpus_env) -> None:
    def fake_run(*_a, **_kw):
        return _completed(stderr="HTTP 404: not found", returncode=1)

    monkeypatch.setattr(corpus.subprocess, "run", fake_run)
    with pytest.raises(corpus.CorpusUnavailable, match="HTTP 404"):
        corpus._run_gh(["api", "repos/x/y"])


# --------------------------------------------------------------------------- #
# fetch_brainlike_views                                                       #
# --------------------------------------------------------------------------- #


def _make_brainlike_run(yaml_files: dict[str, str]):
    """Build a subprocess.run side_effect that serves a fake corpus tree.

    `yaml_files` maps "<path within repo>" -> "<yaml string>". The fake
    inspects the gh args and dispatches:
      * tree request   -> returns a tree JSON enumerating `yaml_files`
      * contents fetch -> returns the matching raw yaml
    """

    def side_effect(args, **_kw):
        # subprocess.run is called as `subprocess.run(["gh", ...], ...)`.
        gh_args = args
        # Tree listing
        if len(gh_args) >= 3 and gh_args[1] == "api" and "git/trees" in gh_args[2]:
            tree = {
                "tree": [{"type": "blob", "path": p} for p in yaml_files]
                + [
                    {"type": "blob", "path": "README.md"},  # filtered out
                    {"type": "tree", "path": "community/brainlike"},  # filtered out
                ]
            }
            return _completed(stdout=json.dumps(tree))
        # Raw file fetch: args end with `repos/<repo>/contents/<path>?ref=<ref>`
        if "contents/" in gh_args[-1]:
            ref_split = gh_args[-1].split("contents/", 1)[1]
            path = ref_split.split("?", 1)[0]
            if path in yaml_files:
                return _completed(stdout=yaml_files[path])
            return _completed(stderr=f"not found: {path}", returncode=1)
        raise AssertionError(f"unexpected gh invocation in test: {gh_args}")

    return side_effect


def test_fetch_brainlike_views_parses_yaml_and_skips_schema(monkeypatch, fake_corpus_env) -> None:
    files = {
        "community/brainlike/_schema.yaml": "$id: schema",
        "community/brainlike/transfer.yaml": (
            "id: transfer\ntitle: Transfer\npredicates: [a, b]\n"
        ),
        "community/brainlike/examples/canonical.yaml": (
            "id: canonical\ntitle: Canonical example\n"
        ),
        "community/brainlike/.hidden.yaml": "id: hidden",
        "community/brainlike/notes.txt": "ignored",
    }
    monkeypatch.setattr(corpus.subprocess, "run", _make_brainlike_run(files))

    views = corpus.fetch_brainlike_views()

    ids = sorted(v["id"] for v in views)
    assert ids == ["canonical", "transfer"]
    for v in views:
        assert v["__source_repo__"] == "test-owner/test-corpus@main"
        assert v["__source_path__"].startswith("community/brainlike/")


def test_fetch_brainlike_views_caches_result(monkeypatch, fake_corpus_env) -> None:
    files = {
        "community/brainlike/transfer.yaml": "id: transfer\ntitle: T\n",
    }
    calls: list[list[str]] = []

    real_side_effect = _make_brainlike_run(files)

    def counting_run(args, **kw):
        calls.append(list(args))
        return real_side_effect(args, **kw)

    monkeypatch.setattr(corpus.subprocess, "run", counting_run)

    first = corpus.fetch_brainlike_views()
    n_first = len(calls)
    second = corpus.fetch_brainlike_views()  # should hit cache
    assert len(calls) == n_first, "second call must not hit gh"
    assert first == second


def test_fetch_brainlike_views_force_bypasses_cache(monkeypatch, fake_corpus_env) -> None:
    files = {"community/brainlike/transfer.yaml": "id: transfer\n"}
    calls: list[list[str]] = []
    real_side_effect = _make_brainlike_run(files)

    def counting_run(args, **kw):
        calls.append(list(args))
        return real_side_effect(args, **kw)

    monkeypatch.setattr(corpus.subprocess, "run", counting_run)
    corpus.fetch_brainlike_views()
    n_first = len(calls)
    corpus.fetch_brainlike_views(force=True)
    assert len(calls) > n_first


def test_fetch_brainlike_views_skips_malformed_yaml(monkeypatch, fake_corpus_env, capsys) -> None:
    files = {
        "community/brainlike/good.yaml": "id: good\ntitle: ok\n",
        "community/brainlike/bad.yaml": "id: [unbalanced",
        "community/brainlike/scalar.yaml": "just-a-string",
    }
    monkeypatch.setattr(corpus.subprocess, "run", _make_brainlike_run(files))

    views = corpus.fetch_brainlike_views()
    assert [v["id"] for v in views] == ["good"]
    err = capsys.readouterr().err
    assert "skipping" in err


# --------------------------------------------------------------------------- #
# fetch_pending_feedback_issues                                               #
# --------------------------------------------------------------------------- #


def _issue(
    *,
    number: int,
    title: str,
    body: str,
    labels: list[str] | None = None,
    author: str = "octocat",
    created: str = "2026-05-04T12:00:00Z",
    url: str | None = None,
) -> dict[str, Any]:
    return {
        "number": number,
        "url": url or f"https://github.com/test-owner/test-corpus/issues/{number}",
        "title": title,
        "body": body,
        "labels": [{"name": n} for n in (labels or ["feedback"])],
        "author": {"login": author},
        "createdAt": created,
    }


def test_fetch_pending_feedback_issues_parses_form_body(monkeypatch, fake_corpus_env) -> None:
    body = (
        "### Tool name\n\n"
        "psyneulink_create_mechanism\n\n"
        "### Issue type\n\n"
        "missing_arg\n\n"
        "### Description\n\n"
        "The schema lacks `name`.\n\n"
        "### Suggested fix\n\n"
        "Add `name: str` to the schema.\n\n"
        "### Agent context\n\n"
        "_No response_\n"
    )
    issues = [_issue(number=42, title="tool feedback", body=body)]
    monkeypatch.setattr(
        corpus.subprocess,
        "run",
        lambda *_a, **_kw: _completed(stdout=json.dumps(issues)),
    )

    envelopes = corpus.fetch_pending_feedback_issues()
    assert len(envelopes) == 1
    env = envelopes[0]
    assert env["source"] == "human-github"
    assert env["tool_name"] == "psyneulink_create_mechanism"
    assert env["payload"]["issue_number"] == 42
    assert env["payload"]["issue_type"] == "missing_arg"
    assert env["payload"]["description"] == "The schema lacks `name`."
    assert env["payload"]["suggested_fix"] == "Add `name: str` to the schema."
    assert env["payload"]["agent_context"] is None  # _No response_ → empty → None
    assert env["payload"]["author"] == "octocat"


def test_fetch_pending_feedback_issues_falls_back_when_unparseable(
    monkeypatch, fake_corpus_env
) -> None:
    issues = [_issue(number=7, title="freeform", body="just a free-form complaint")]
    monkeypatch.setattr(
        corpus.subprocess,
        "run",
        lambda *_a, **_kw: _completed(stdout=json.dumps(issues)),
    )

    envelopes = corpus.fetch_pending_feedback_issues()
    assert envelopes[0]["tool_name"] == "unknown"
    assert envelopes[0]["payload"]["description"] == "just a free-form complaint"


def test_fetch_pending_feedback_issues_filters_consumed(monkeypatch, fake_corpus_env) -> None:
    issues = [
        _issue(number=1, title="a", body="x", labels=["feedback"]),
        _issue(number=2, title="b", body="x", labels=["feedback", "consumed"]),
    ]
    monkeypatch.setattr(
        corpus.subprocess,
        "run",
        lambda *_a, **_kw: _completed(stdout=json.dumps(issues)),
    )

    envelopes = corpus.fetch_pending_feedback_issues()
    assert [e["payload"]["issue_number"] for e in envelopes] == [1]


# --------------------------------------------------------------------------- #
# find_existing_feedback_issue / open_feedback_issue                          #
# --------------------------------------------------------------------------- #


def test_find_existing_feedback_issue_returns_number_on_exact_title_match(
    monkeypatch, fake_corpus_env
) -> None:
    title = "[auto] my_tool: ValueError: bad x=42"
    issues = [
        {"number": 7, "title": "different title"},
        {"number": 8, "title": title},
    ]
    captured: dict[str, Any] = {}

    def fake_run(args, **_kw):
        captured["args"] = list(args)
        return _completed(stdout=json.dumps(issues))

    monkeypatch.setattr(corpus.subprocess, "run", fake_run)

    assert corpus.find_existing_feedback_issue(title) == 8
    # Must scope by both labels; otherwise we'd hit human-filed issues too.
    assert "feedback" in captured["args"]
    assert "auto" in captured["args"]
    assert any(arg.startswith("in:title") for arg in captured["args"])


def test_find_existing_feedback_issue_returns_none_when_no_match(
    monkeypatch, fake_corpus_env
) -> None:
    monkeypatch.setattr(
        corpus.subprocess,
        "run",
        lambda *_a, **_kw: _completed(stdout="[]"),
    )
    assert corpus.find_existing_feedback_issue("[auto] x: Y: z") is None


def test_find_existing_feedback_issue_ignores_partial_title_matches(
    monkeypatch, fake_corpus_env
) -> None:
    """`gh search` may return broader matches; we require an exact equal."""
    title = "[auto] my_tool: ValueError: bad x=42"
    issues = [{"number": 9, "title": title + " (and more)"}]
    monkeypatch.setattr(
        corpus.subprocess,
        "run",
        lambda *_a, **_kw: _completed(stdout=json.dumps(issues)),
    )
    assert corpus.find_existing_feedback_issue(title) is None


def test_find_existing_feedback_issue_raises_on_gh_failure(monkeypatch, fake_corpus_env) -> None:
    monkeypatch.setattr(
        corpus.subprocess,
        "run",
        lambda *_a, **_kw: _completed(stderr="HTTP 500", returncode=1),
    )
    with pytest.raises(corpus.CorpusUnavailable):
        corpus.find_existing_feedback_issue("anything")


def test_open_feedback_issue_invokes_gh_with_default_labels(monkeypatch, fake_corpus_env) -> None:
    captured: dict[str, Any] = {}

    def fake_run(args, **_kw):
        captured["args"] = list(args)
        return _completed(stdout="https://github.com/test-owner/test-corpus/issues/99\n")

    monkeypatch.setattr(corpus.subprocess, "run", fake_run)

    url = corpus.open_feedback_issue(title="t", body="b")

    assert url == "https://github.com/test-owner/test-corpus/issues/99"
    assert "create" in captured["args"]
    assert "--title" in captured["args"]
    assert "t" in captured["args"]
    # Default labels: feedback,auto, comma-joined for `gh issue create`.
    assert "--label" in captured["args"]
    assert "feedback,auto" in captured["args"]


def test_open_feedback_issue_honours_explicit_label_list(monkeypatch, fake_corpus_env) -> None:
    captured: dict[str, Any] = {}

    def fake_run(args, **_kw):
        captured["args"] = list(args)
        return _completed(stdout="https://example/issues/1")

    monkeypatch.setattr(corpus.subprocess, "run", fake_run)
    corpus.open_feedback_issue(title="t", body="b", labels=["alpha", "beta"])
    assert "alpha,beta" in captured["args"]


def test_open_feedback_issue_raises_on_gh_failure(monkeypatch, fake_corpus_env) -> None:
    monkeypatch.setattr(
        corpus.subprocess,
        "run",
        lambda *_a, **_kw: _completed(stderr="HTTP 422", returncode=1),
    )
    with pytest.raises(corpus.CorpusUnavailable):
        corpus.open_feedback_issue(title="t", body="b")


# --------------------------------------------------------------------------- #
# mark_issues_consumed                                                        #
# --------------------------------------------------------------------------- #


def test_mark_issues_consumed_comments_and_labels_each(monkeypatch, fake_corpus_env) -> None:
    calls: list[list[str]] = []

    def fake_run(args, **_kw):
        calls.append(list(args))
        return _completed(stdout="ok")

    monkeypatch.setattr(corpus.subprocess, "run", fake_run)

    succeeded = corpus.mark_issues_consumed([42, 43], regen_sha="deadbeef")

    assert succeeded == [42, 43]
    # Each issue should produce a comment + an edit (4 calls total)
    assert len(calls) == 4
    assert any("comment" in c and "deadbeef" in " ".join(c) for c in calls)
    assert any("edit" in c and "consumed" in c for c in calls)


def test_mark_issues_consumed_continues_on_per_issue_failure(
    monkeypatch, fake_corpus_env, capsys
) -> None:
    state = {"i": 0}

    def fake_run(args, **_kw):
        state["i"] += 1
        # Fail the first call (comment on #1); succeed everything else
        if state["i"] == 1:
            return _completed(stderr="HTTP 503", returncode=1)
        return _completed(stdout="ok")

    monkeypatch.setattr(corpus.subprocess, "run", fake_run)

    succeeded = corpus.mark_issues_consumed([1, 2], regen_sha="abc")
    assert succeeded == [2]
    assert "could not mark issue #1" in capsys.readouterr().err


# --------------------------------------------------------------------------- #
# brainlike curated tools                                                     #
# --------------------------------------------------------------------------- #


def test_get_my_brainlike_view_returns_empty_when_no_profile(monkeypatch, tmp_path) -> None:
    monkeypatch.setenv(
        curated_brainlike.ENV_PERSONAL_PROFILE,
        str(tmp_path / "missing.yaml"),
    )
    mcp = FakeMCP()
    curated_brainlike.register(mcp)

    out = mcp.tools["get_my_brainlike_view"]()
    assert out["view"] == {}
    assert out["configured"] is False
    assert out["source"].endswith("missing.yaml")


def test_get_my_brainlike_view_reads_yaml_profile(monkeypatch, tmp_path) -> None:
    profile = tmp_path / "me.yaml"
    profile.write_text("title: Mine\npredicates: [a, b]\n", encoding="utf-8")
    monkeypatch.setenv(curated_brainlike.ENV_PERSONAL_PROFILE, str(profile))

    mcp = FakeMCP()
    curated_brainlike.register(mcp)

    out = mcp.tools["get_my_brainlike_view"]()
    assert out["view"] == {"title": "Mine", "predicates": ["a", "b"]}
    assert out["configured"] is True
    assert out["source"] == str(profile)


def test_get_my_brainlike_view_rejects_non_mapping_yaml(monkeypatch, tmp_path) -> None:
    profile = tmp_path / "me.yaml"
    profile.write_text("- just\n- a list\n", encoding="utf-8")
    monkeypatch.setenv(curated_brainlike.ENV_PERSONAL_PROFILE, str(profile))

    mcp = FakeMCP()
    curated_brainlike.register(mcp)

    out = mcp.tools["get_my_brainlike_view"]()
    assert out["view"] == {}
    assert "must be a YAML mapping" in out["error"]


def test_get_community_brainlike_views_degrades_gracefully(monkeypatch, fake_corpus_env) -> None:
    def boom(*_a, **_kw):
        raise corpus.CorpusUnavailable("no network in this test")

    monkeypatch.setattr(corpus, "fetch_brainlike_views", boom)

    mcp = FakeMCP()
    curated_brainlike.register(mcp)

    out = mcp.tools["get_community_brainlike_views"]()
    assert out["views"] == []
    assert out["count"] == 0
    assert "no network" in out["error"]
    assert out["source"].startswith("test-owner/test-corpus@")


def test_get_community_brainlike_views_returns_views_on_success(
    monkeypatch, fake_corpus_env
) -> None:
    monkeypatch.setattr(
        corpus,
        "fetch_brainlike_views",
        lambda force=False: [{"id": "x", "title": "X"}],
    )

    mcp = FakeMCP()
    curated_brainlike.register(mcp)

    out = mcp.tools["get_community_brainlike_views"]()
    assert out["count"] == 1
    assert out["views"][0]["id"] == "x"
    assert "error" not in out


# --------------------------------------------------------------------------- #
# pnl:<symbol> labels (Phase 1 t5)                                            #
# --------------------------------------------------------------------------- #


def test_pnl_symbol_label_is_deterministic_and_prefixed() -> None:
    assert corpus.pnl_symbol_label("create_lca_mechanism") == ("pnl:create_lca_mechanism")
    assert corpus.pnl_symbol_label("add_node").startswith(corpus.PNL_SYMBOL_LABEL_PREFIX)


def test_ensure_label_exists_invokes_gh_label_create_with_force(
    monkeypatch, fake_corpus_env
) -> None:
    captured: dict[str, list[str]] = {}

    def fake_run(args, **_kw):
        captured["args"] = list(args)
        return _completed(stdout="created")

    monkeypatch.setattr(corpus.subprocess, "run", fake_run)
    assert corpus.ensure_label_exists("pnl:foo") is True

    args = captured["args"]
    assert "label" in args and "create" in args
    # The label name + idempotency `--force` flag must both be present so
    # a re-run on an existing label updates color/description rather than
    # exiting non-zero on collision.
    assert "pnl:foo" in args
    assert "--force" in args
    # Color + description default to the publisher's "this is a runtime
    # capture" cosmetics so all auto-minted labels look consistent.
    assert corpus.PNL_SYMBOL_LABEL_COLOR in args


def test_ensure_label_exists_treats_already_exists_as_success(monkeypatch, fake_corpus_env) -> None:
    """`gh label create` without --force returns rc=1 with 'already exists'.

    Even though we pass --force in production, an older `gh` build might
    emit the same shape under unrelated conditions; the helper must still
    return True when stderr says the label is already present.
    """
    monkeypatch.setattr(
        corpus.subprocess,
        "run",
        lambda *_a, **_kw: _completed(stderr="error: label 'pnl:foo' already exists", returncode=1),
    )
    assert corpus.ensure_label_exists("pnl:foo") is True


def test_ensure_label_exists_raises_on_real_failure(monkeypatch, fake_corpus_env) -> None:
    monkeypatch.setattr(
        corpus.subprocess,
        "run",
        lambda *_a, **_kw: _completed(stderr="HTTP 500: backend boom", returncode=1),
    )
    with pytest.raises(corpus.CorpusUnavailable):
        corpus.ensure_label_exists("pnl:foo")


# --------------------------------------------------------------------------- #
# fetch_historical_failures (Phase 1 t5 part B)                               #
# --------------------------------------------------------------------------- #


def _closed_issue(
    *,
    number: int,
    title: str,
    body: str = "",
    labels: list[str] | None = None,
    state_reason: str = "completed",
) -> dict[str, Any]:
    return {
        "number": number,
        "url": f"https://example/issues/{number}",
        "title": title,
        "body": body,
        "labels": [{"name": n} for n in (labels or [])],
        "stateReason": state_reason,
        "closedAt": "2026-05-01T00:00:00Z",
    }


def test_fetch_historical_failures_filters_wontfix_invalid_and_not_planned(
    monkeypatch, fake_corpus_env
) -> None:
    issues = [
        _closed_issue(number=10, title="legit fixed", labels=["pnl:t", "feedback"]),
        _closed_issue(
            number=11,
            title="design decision",
            labels=["pnl:t", "wontfix"],
        ),
        _closed_issue(number=12, title="operator error", labels=["pnl:t", "invalid"]),
        _closed_issue(
            number=13,
            title="explicitly not planned",
            labels=["pnl:t"],
            state_reason="not_planned",
        ),
        _closed_issue(number=14, title="another legit", labels=["pnl:t"]),
    ]
    monkeypatch.setattr(
        corpus.subprocess,
        "run",
        lambda *_a, **_kw: _completed(stdout=json.dumps(issues)),
    )

    out = corpus.fetch_historical_failures("t")
    numbers = [i["number"] for i in out]
    # Keep #10 and #14, drop #11 (wontfix), #12 (invalid), #13 (not_planned).
    # Sort by number desc — most recent issues first.
    assert numbers == [14, 10]


def test_fetch_historical_failures_respects_max_results(monkeypatch, fake_corpus_env) -> None:
    issues = [_closed_issue(number=n, title=f"t{n}", labels=["pnl:t"]) for n in range(50, 30, -1)]
    monkeypatch.setattr(
        corpus.subprocess,
        "run",
        lambda *_a, **_kw: _completed(stdout=json.dumps(issues)),
    )

    out = corpus.fetch_historical_failures("t", max_results=3)
    assert [i["number"] for i in out] == [50, 49, 48]


def test_fetch_historical_failures_returns_empty_on_empty_label(
    monkeypatch, fake_corpus_env
) -> None:
    """A label that has never been used returns an empty list, not an error."""
    monkeypatch.setattr(
        corpus.subprocess,
        "run",
        lambda *_a, **_kw: _completed(stdout="[]"),
    )
    assert corpus.fetch_historical_failures("never_used") == []


def test_fetch_historical_failures_searches_by_pnl_label(monkeypatch, fake_corpus_env) -> None:
    captured: dict[str, list[str]] = {}

    def fake_run(args, **_kw):
        captured["args"] = list(args)
        return _completed(stdout="[]")

    monkeypatch.setattr(corpus.subprocess, "run", fake_run)
    corpus.fetch_historical_failures("create_lca_mechanism")

    args = captured["args"]
    assert "issue" in args and "list" in args
    assert "--state" in args and "closed" in args
    # Must scope by the per-symbol label, not the generic feedback one.
    assert "pnl:create_lca_mechanism" in args
    # `stateReason` is what we use to drop not_planned closures.
    assert any("stateReason" in a for a in args)
