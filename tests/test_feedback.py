"""Tests for the feedback log + auto-capture wrapper + generator hooks."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import pytest

from psyneulink_mcp import feedback
from psyneulink_mcp.feedback import (
    captured_tool,
    log_agent_report,
    log_runtime_error,
)
from psyneulink_mcp.tools.curated import feedback as curated_feedback
from scripts.generate_tools import (
    archive_pending,
    group_by_tool,
    read_pending,
)


class FakeMCP:
    """Minimal stand-in for FastMCP — captures registered tools by name."""

    def __init__(self) -> None:
        self.tools: dict[str, Any] = {}

    def tool(self, **_kwargs: Any):
        def decorator(fn):
            self.tools[fn.__name__] = fn
            return fn

        return decorator


@pytest.fixture
def feedback_file(monkeypatch, tmp_path) -> Path:
    path = tmp_path / "issues.jsonl"
    monkeypatch.setenv(feedback.ENV_FEEDBACK_PATH, str(path))
    return path


def _read_jsonl(path: Path) -> list[dict[str, Any]]:
    return [json.loads(line) for line in path.read_text().splitlines() if line.strip()]


def test_log_agent_report_writes_well_formed_entry(feedback_file: Path) -> None:
    log_agent_report(
        tool_name="psyneulink_create_mechanism",
        tool_layer="generated",
        issue_type="unclear_description",
        description="Description didn't explain the `default_variable` arg.",
        suggested_fix="Add an example.",
        agent_context="Trying to build a TransferMechanism.",
    )

    entries = _read_jsonl(feedback_file)
    assert len(entries) == 1
    entry = entries[0]
    assert entry["source"] == "agent"
    assert entry["tool_name"] == "psyneulink_create_mechanism"
    assert entry["tool_layer"] == "generated"
    assert entry["payload"]["issue_type"] == "unclear_description"
    assert entry["payload"]["suggested_fix"] == "Add an example."
    assert entry["payload"]["agent_context"] == "Trying to build a TransferMechanism."
    assert "timestamp" in entry
    assert "server_version" in entry


def test_log_runtime_error_serializes_non_json_args(feedback_file: Path) -> None:
    class Unserializable:
        def __repr__(self) -> str:
            return "<Unserializable instance>"

    try:
        raise RuntimeError("kaboom")
    except RuntimeError as exc:
        log_runtime_error(
            tool_name="some_tool",
            tool_layer="generated",
            args={"weird": Unserializable(), "n": 7},
            exc=exc,
        )

    entries = _read_jsonl(feedback_file)
    assert len(entries) == 1
    entry = entries[0]
    assert entry["source"] == "auto"
    assert entry["payload"]["exception_type"] == "RuntimeError"
    assert entry["payload"]["exception_message"] == "kaboom"
    assert "kaboom" in entry["payload"]["traceback"]
    assert entry["payload"]["args"]["weird"] == "<Unserializable instance>"
    assert entry["payload"]["args"]["n"] == 7


def test_logger_swallows_own_exceptions(monkeypatch, capsys, tmp_path) -> None:
    blocker = tmp_path / "not_a_dir"
    blocker.write_text("file in the way")
    bad_path = blocker / "issues.jsonl"
    monkeypatch.setenv(feedback.ENV_FEEDBACK_PATH, str(bad_path))

    log_agent_report(
        tool_name="x",
        tool_layer="generated",
        issue_type="other",
        description="should not raise",
    )

    captured = capsys.readouterr()
    assert "feedback log failed" in captured.err


def test_captured_tool_reraises_after_logging(feedback_file: Path) -> None:
    mcp = FakeMCP()

    @captured_tool(mcp, layer="curated")
    def crashy(x: int) -> int:
        raise ValueError(f"bad x={x}")

    fn = mcp.tools["crashy"]
    with pytest.raises(ValueError, match="bad x=42"):
        fn(42)

    entries = _read_jsonl(feedback_file)
    assert len(entries) == 1
    entry = entries[0]
    assert entry["source"] == "auto"
    assert entry["tool_name"] == "crashy"
    assert entry["tool_layer"] == "curated"
    assert entry["payload"]["exception_type"] == "ValueError"
    assert entry["payload"]["args"]["args"] == [42]


def test_captured_tool_records_layer_in_registry(feedback_file: Path) -> None:
    mcp = FakeMCP()

    @captured_tool(mcp, layer="curated")
    def some_curated_tool() -> None:
        return None

    assert feedback.lookup_tool_layer("some_curated_tool") == "curated"
    # Unknown tool falls back to "generated"
    assert feedback.lookup_tool_layer("never_registered") == "generated"


def test_report_tool_issue_records_agent_entry(feedback_file: Path) -> None:
    mcp = FakeMCP()
    curated_feedback.register(mcp)

    report = mcp.tools["report_tool_issue"]
    result = report(
        tool_name="psyneulink_create_mechanism",
        issue_type="missing_arg",
        description="The schema lacks `name`.",
    )
    assert result == {"recorded": True}

    entries = _read_jsonl(feedback_file)
    assert len(entries) == 1
    entry = entries[0]
    assert entry["source"] == "agent"
    assert entry["tool_name"] == "psyneulink_create_mechanism"
    assert entry["payload"]["issue_type"] == "missing_arg"
    # report_tool_issue itself is curated; the *reported* tool's layer is
    # looked up via the registry — defaults to "generated" when unknown.
    assert entry["tool_layer"] == "generated"


# ---- generator script helpers ------------------------------------------------


def test_group_by_tool_groups_entries_by_name() -> None:
    entries = [
        {"tool_name": "a", "x": 1},
        {"tool_name": "b", "x": 2},
        {"tool_name": "a", "x": 3},
        {"x": "no_name"},  # ignored
    ]
    grouped = group_by_tool(entries)
    assert sorted(grouped) == ["a", "b"]
    assert len(grouped["a"]) == 2
    assert len(grouped["b"]) == 1


def test_read_pending_skips_blank_and_malformed_lines(tmp_path) -> None:
    path = tmp_path / "issues.jsonl"
    path.write_text(
        '{"tool_name": "a"}\n'
        "\n"
        "this is not json\n"
        '{"tool_name": "b"}\n'
    )
    entries = read_pending(path)
    assert [e["tool_name"] for e in entries] == ["a", "b"]


def test_read_pending_returns_empty_when_missing(tmp_path) -> None:
    assert read_pending(tmp_path / "nope.jsonl") == []


def test_archive_pending_moves_and_truncates(tmp_path) -> None:
    pending = tmp_path / "pending" / "issues.jsonl"
    pending.parent.mkdir(parents=True)
    pending.write_text('{"a": 1}\n{"b": 2}\n')

    archive_root = tmp_path / "archive"
    result = archive_pending(pending, archive_root, date="2026-05-04")

    assert result is not None
    assert result == archive_root / "2026-05-04" / "issues.jsonl"
    assert result.read_text() == '{"a": 1}\n{"b": 2}\n'
    assert pending.read_text() == ""


def test_archive_pending_appends_to_existing_date(tmp_path) -> None:
    pending = tmp_path / "pending" / "issues.jsonl"
    pending.parent.mkdir(parents=True)
    archive_root = tmp_path / "archive"

    pending.write_text('{"a": 1}\n')
    archive_pending(pending, archive_root, date="2026-05-04")

    pending.write_text('{"b": 2}\n')
    archive_pending(pending, archive_root, date="2026-05-04")

    final = (archive_root / "2026-05-04" / "issues.jsonl").read_text()
    assert final == '{"a": 1}\n{"b": 2}\n'


def test_archive_pending_noop_when_empty(tmp_path) -> None:
    pending = tmp_path / "pending" / "issues.jsonl"
    pending.parent.mkdir(parents=True)
    pending.write_text("")
    archive_root = tmp_path / "archive"

    assert archive_pending(pending, archive_root) is None
    assert not archive_root.exists()
