"""Regenerate `src/psyneulink_mcp/tools/generated/` from PsyNeuLink's public API.

This script:

1. Gathers pending feedback from two sources and merges them by tool name:
   * local JSONL (`feedback/pending/issues.jsonl`) — runtime captures and
     agent reports.
   * GitHub Issues on `psyneulink-corpus` with the `feedback` label, fetched
     via the `gh` CLI. If the corpus is unavailable, the run continues with
     local feedback only (logged to stderr).
2. (Stub) Calls an LLM adapter for each PNL public symbol to produce a tool
   description + JSON schema, writing the result under `tools/generated/`.
3. On overall success:
   * archives the consumed local feedback to
     `feedback/archive/<UTC-date>/issues.jsonl` and empties pending,
   * comments + labels `consumed` on each consumed corpus issue (no
     auto-close — humans verify and close).
4. On failure, leaves both local pending and corpus issues untouched so the
   next run still sees them.

The LLM adapter is intentionally a placeholder here — wiring it to an API
key or a Claude Max plan is a separate concern from the feedback loop.
"""

from __future__ import annotations

import json
import sys
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from psyneulink_mcp import corpus

REPO_ROOT = Path(__file__).resolve().parent.parent
PENDING_PATH = REPO_ROOT / "feedback" / "pending" / "issues.jsonl"
ARCHIVE_ROOT = REPO_ROOT / "feedback" / "archive"
GENERATED_DIR = REPO_ROOT / "src" / "psyneulink_mcp" / "tools" / "generated"


def read_pending(path: Path = PENDING_PATH) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    entries: list[dict[str, Any]] = []
    with path.open(encoding="utf-8") as f:
        for i, raw in enumerate(f, 1):
            line = raw.strip()
            if not line:
                continue
            try:
                entries.append(json.loads(line))
            except json.JSONDecodeError as e:
                print(
                    f"[generate_tools] skipping malformed line {i}: {e}",
                    file=sys.stderr,
                )
    return entries


def group_by_tool(entries: list[dict[str, Any]]) -> dict[str, list[dict[str, Any]]]:
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for entry in entries:
        name = entry.get("tool_name")
        if isinstance(name, str):
            grouped[name].append(entry)
    return dict(grouped)


def gather_feedback(
    pending_path: Path = PENDING_PATH,
    fetch_remote=corpus.fetch_pending_feedback_issues,
) -> dict[str, list[dict[str, Any]]]:
    """Local pending entries + corpus issues, grouped by tool name.

    `fetch_remote` is parameterised for tests; production code uses the
    default. Corpus failures degrade to local-only with a stderr note —
    they never abort regen.
    """
    local = group_by_tool(read_pending(pending_path))
    try:
        remote = group_by_tool(fetch_remote())
    except corpus.CorpusUnavailable as e:
        print(
            f"[generate_tools] corpus unavailable, using local feedback only: {e}",
            file=sys.stderr,
        )
        remote = {}

    merged: dict[str, list[dict[str, Any]]] = {}
    for source in (local, remote):
        for tool_name, entries in source.items():
            merged.setdefault(tool_name, []).extend(entries)
    return merged


def consumed_issue_numbers(
    feedback_by_tool: dict[str, list[dict[str, Any]]],
) -> list[int]:
    """Return the GitHub issue numbers present in `feedback_by_tool`.

    Used after a successful regen to know which corpus issues to mark as
    `consumed`.
    """
    seen: set[int] = set()
    for entries in feedback_by_tool.values():
        for entry in entries:
            if entry.get("source") != "human-github":
                continue
            n = (entry.get("payload") or {}).get("issue_number")
            if isinstance(n, int):
                seen.add(n)
    return sorted(seen)


def archive_pending(
    pending_path: Path = PENDING_PATH,
    archive_root: Path = ARCHIVE_ROOT,
    date: str | None = None,
) -> Path | None:
    """Move pending entries to `archive_root/<date>/issues.jsonl` and truncate
    pending. If pending is empty or missing, this is a no-op.

    If a file already exists for `date`, new entries are appended.
    Returns the archive file path, or None if nothing was archived.
    """
    if not pending_path.exists() or pending_path.stat().st_size == 0:
        return None

    date = date or datetime.now(timezone.utc).date().isoformat()
    archive_dir = archive_root / date
    archive_dir.mkdir(parents=True, exist_ok=True)
    archive_file = archive_dir / "issues.jsonl"

    contents = pending_path.read_text(encoding="utf-8")
    if not contents.endswith("\n") and contents:
        contents += "\n"
    with archive_file.open("a", encoding="utf-8") as f:
        f.write(contents)
    pending_path.write_text("", encoding="utf-8")
    return archive_file


def generate_tool_for_symbol(
    symbol_name: str,
    feedback_for_tool: list[dict[str, Any]],
) -> str:
    """STUB: in the real generator this calls the LLM adapter with the
    symbol's source + docstring + (optionally) prior feedback, and returns
    a generated Python module for the tool. Kept as a placeholder so the
    feedback-loop logic in this script is testable independently.
    """
    raise NotImplementedError(
        "LLM adapter is not wired up yet. Implement an adapter "
        "(API token or Claude Max plan) and call it here."
    )


def main() -> int:
    feedback_by_tool = gather_feedback()
    total_entries = sum(len(v) for v in feedback_by_tool.values())
    if total_entries:
        print(
            f"[generate_tools] consuming {total_entries} feedback entries "
            f"across {len(feedback_by_tool)} tool(s) "
            f"(local + corpus@{corpus.corpus_repo()}#{corpus.corpus_ref()})",
            file=sys.stderr,
        )

    # Real implementation iterates psyneulink public symbols here and calls
    # generate_tool_for_symbol(name, feedback_by_tool.get(name, [])) for each.
    # Until the LLM adapter is wired up, this script is a no-op for codegen
    # but exercises the feedback-consumption path so the rest of the loop
    # can be developed against it.
    print(
        "[generate_tools] LLM adapter not implemented — skipping codegen; "
        "feedback will not be archived this run.",
        file=sys.stderr,
    )
    return 0

    # When codegen succeeds end-to-end, archive consumed feedback and tag the
    # corpus issues that were merged in:
    # archive_pending()  # noqa: ERA001
    # corpus.mark_issues_consumed(  # noqa: ERA001
    #     consumed_issue_numbers(feedback_by_tool), regen_sha=...
    # )


if __name__ == "__main__":
    raise SystemExit(main())
