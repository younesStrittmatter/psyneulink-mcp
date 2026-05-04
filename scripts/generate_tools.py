"""Regenerate `src/psyneulink_mcp/tools/generated/` from PsyNeuLink's public API.

This script:

1. Reads pending feedback (`feedback/pending/issues.jsonl`) and groups it by
   the tool it targets, so each tool's regeneration can include the relevant
   prior feedback in its LLM prompt.
2. (Stub) Calls an LLM adapter for each PNL public symbol to produce a tool
   description + JSON schema, writing the result under `tools/generated/`.
3. On overall success, archives the consumed feedback to
   `feedback/archive/<UTC-date>/issues.jsonl` and empties pending.
4. On failure, leaves pending untouched so the next run still sees it.

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
    pending = read_pending()
    feedback_by_tool = group_by_tool(pending)
    if pending:
        print(
            f"[generate_tools] consuming {len(pending)} feedback entries "
            f"across {len(feedback_by_tool)} tool(s)",
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

    # When codegen succeeds end-to-end, archive consumed feedback:
    # archive_pending()  # noqa: ERA001


if __name__ == "__main__":
    raise SystemExit(main())
