"""Tests for the HISTORICAL FAILURES regen pipeline (Phase 1 t5 part B).

Two layers under test:

* ``feedback_loop.gather_historical_failures`` — composes
  ``corpus.fetch_historical_failures`` over the selected tool names and
  degrades to "no history for that tool" on a per-tool corpus failure.
* ``orchestrator._augment_with_historical_failures`` — appends a
  deterministic ``## HISTORICAL FAILURES`` block to a generated
  :class:`ToolSpec`'s description, leaves the spec alone when the
  failure list is empty.

Both are pure-Python with no `gh` shell-out (the corpus seam is
parameterised at the call site).
"""

from __future__ import annotations

from typing import Any

from psyneulink_mcp import corpus
from psyneulink_mcp.generator import feedback_loop, orchestrator

# --------------------------------------------------------------------------- #
# helpers                                                                     #
# --------------------------------------------------------------------------- #


def _failure(
    *,
    number: int,
    title: str = "synthetic failure",
    body: str = "",
) -> dict[str, Any]:
    """Pre-filtered closed-issue payload (the shape orchestrator sees)."""
    return {
        "number": number,
        "title": title,
        "body": body,
        "url": f"https://example/issues/{number}",
    }


# --------------------------------------------------------------------------- #
# gather_historical_failures (composition + degradation)                      #
# --------------------------------------------------------------------------- #


def test_gather_historical_failures_calls_fetch_per_tool_and_groups_results() -> None:
    seen_calls: list[tuple[str, int]] = []

    def fake_fetch(name: str, *, max_results: int = 5) -> list[dict[str, Any]]:
        seen_calls.append((name, max_results))
        if name == "tool_a":
            return [_failure(number=10), _failure(number=11)]
        if name == "tool_b":
            return [_failure(number=20)]
        return []

    out = feedback_loop.gather_historical_failures(["tool_a", "tool_b", "tool_c"], fetch=fake_fetch)

    assert seen_calls == [("tool_a", 5), ("tool_b", 5), ("tool_c", 5)]
    # tool_c had no history → omitted entirely (caller does .get(name, []))
    assert set(out.keys()) == {"tool_a", "tool_b"}
    assert [i["number"] for i in out["tool_a"]] == [10, 11]
    assert [i["number"] for i in out["tool_b"]] == [20]


def test_gather_historical_failures_threads_max_per_tool_through() -> None:
    captured: list[int] = []

    def fake_fetch(_name: str, *, max_results: int) -> list[dict[str, Any]]:
        captured.append(max_results)
        return []

    feedback_loop.gather_historical_failures(["a", "b"], fetch=fake_fetch, max_per_tool=3)
    assert captured == [3, 3]


def test_gather_historical_failures_degrades_per_tool_on_corpus_failure(
    capsys,
) -> None:
    """A corpus error for one tool must not abort the whole gather."""

    def fake_fetch(name: str, *, max_results: int = 5) -> list[dict[str, Any]]:
        if name == "broken":
            raise corpus.CorpusUnavailable("HTTP 500")
        return [_failure(number=99)]

    out = feedback_loop.gather_historical_failures(["ok", "broken", "also_ok"], fetch=fake_fetch)

    err = capsys.readouterr().err
    assert "historical failures unavailable for broken" in err
    # The two healthy tools still get their history.
    assert set(out.keys()) == {"ok", "also_ok"}


# --------------------------------------------------------------------------- #
# _augment_with_historical_failures (description rendering)                   #
# --------------------------------------------------------------------------- #


def _spec(description: str = "Describe the tool.") -> dict[str, Any]:
    return {
        "description": description,
        "parameters": {"type": "object", "properties": {}, "required": []},
        "notes": "",
    }


def test_augment_with_empty_history_returns_spec_unchanged() -> None:
    spec = _spec()
    result = orchestrator._augment_with_historical_failures(spec, [])
    # No mutation; the returned object is the same spec.
    assert result is spec
    assert "HISTORICAL FAILURES" not in result["description"]


def test_augment_appends_section_after_existing_description() -> None:
    failures = [
        _failure(
            number=42,
            title="bad input",
            body="Agent passed `x=None`; raised TypeError",
        ),
        _failure(number=41, title="missing arg", body=""),
    ]
    result = orchestrator._augment_with_historical_failures(
        _spec("Original description here."), failures
    )

    desc = result["description"]
    assert desc.startswith("Original description here.")
    assert "## HISTORICAL FAILURES" in desc
    # Per-issue lines retain the issue number + title; first non-empty
    # line of body shows up as the inline summary; bodyless issues
    # collapse to title-only.
    assert "- #42 — bad input: Agent passed `x=None`" in desc
    assert "- #41 — missing arg" in desc


def test_augment_handles_empty_description_gracefully() -> None:
    failures = [_failure(number=7, title="fail")]
    result = orchestrator._augment_with_historical_failures(_spec(""), failures)
    desc = result["description"]
    assert desc.startswith("## HISTORICAL FAILURES")
    assert "- #7 — fail" in desc


def test_augment_preserves_spec_input_object() -> None:
    """Augment returns a fresh dict; the original spec must NOT be mutated."""
    failures = [_failure(number=1, title="x")]
    original = _spec("base")
    result = orchestrator._augment_with_historical_failures(original, failures)
    assert original["description"] == "base"  # untouched
    assert "HISTORICAL FAILURES" in result["description"]


def test_augment_truncates_long_body_summary_lines() -> None:
    long_body = "A" * 500
    failures = [_failure(number=99, title="long", body=long_body)]
    result = orchestrator._augment_with_historical_failures(_spec(""), failures)
    desc = result["description"]
    # Each summary line is bounded so a single deranged issue body
    # can't blow up every dependent tool's description.
    summary_line = [line for line in desc.splitlines() if line.startswith("- #99")][0]
    assert len(summary_line) <= 280  # generous; helper caps at ~240


def test_render_block_is_stable_across_calls() -> None:
    """Same input → same output (string equality), so re-runs don't churn."""
    failures = [
        _failure(number=12, title="b", body="bb"),
        _failure(number=10, title="a", body="aa"),
    ]
    a = orchestrator._render_historical_failures_block(failures)
    b = orchestrator._render_historical_failures_block(failures)
    assert a == b
    assert a.startswith("## HISTORICAL FAILURES")
