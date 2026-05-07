"""Build-time feedback aggregation for the regen pipeline.

Collects local pending entries (``feedback/pending/issues.jsonl``) and open
``feedback``-labeled issues from ``psyneulink-corpus``, groups them by tool
name, and exposes archive helpers used after a successful regen.

Lives under ``generator/`` because it's only used at build time. The
runtime server never imports this module.
"""

from __future__ import annotations

import json
import sys
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from psyneulink_mcp import corpus

REPO_ROOT = Path(__file__).resolve().parents[3]
PENDING_PATH = REPO_ROOT / "feedback" / "pending" / "issues.jsonl"
ARCHIVE_ROOT = REPO_ROOT / "feedback" / "archive"


def read_pending(path: Path = PENDING_PATH) -> list[dict[str, Any]]:
    """Parse ``feedback/pending/issues.jsonl``; skip malformed lines."""
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

    ``fetch_remote`` is parameterised for tests; production code uses the
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
    successful_tool_names: set[str] | None = None,
) -> list[int]:
    """Return the GitHub issue numbers present in ``feedback_by_tool``.

    Used after a successful regen to know which corpus issues to mark as
    ``consumed``.

    ``successful_tool_names`` (optional) limits the result to issues
    whose tool actually got rewritten this run. Without it, we
    historically returned every gathered issue number — which silently
    consumed feedback for tools whose regen FAILED, since the
    orchestrator's main() didn't filter. Pass the set of tool names
    that successfully wrote to keep failed-tool feedback recoverable
    on the next regen.
    """
    seen: set[int] = set()
    for tool_name, entries in feedback_by_tool.items():
        if successful_tool_names is not None and tool_name not in successful_tool_names:
            continue
        for entry in entries:
            if entry.get("source") != "human-github":
                continue
            n = (entry.get("payload") or {}).get("issue_number")
            if isinstance(n, int):
                seen.add(n)
    return sorted(seen)


def gather_historical_failures(
    tool_names: list[str],
    fetch=corpus.fetch_historical_failures,
    *,
    max_per_tool: int = 5,
) -> dict[str, list[dict[str, Any]]]:
    """Closed corpus issues per ``pnl:<tool_name>`` label, filtered + capped.

    For each tool name, calls ``fetch(tool_name, max_results=max_per_tool)``
    (defaulting to :func:`corpus.fetch_historical_failures`) and stores
    the result in the returned dict. Tools with no qualifying history
    are simply omitted (the caller can ``.get(name, [])`` safely).

    A :class:`corpus.CorpusUnavailable` for any single tool degrades to
    "no historical failures for that tool" with a stderr note — never
    aborts the whole regen. ``fetch`` is parameterised for tests.
    """
    out: dict[str, list[dict[str, Any]]] = {}
    for name in tool_names:
        try:
            failures = fetch(name, max_results=max_per_tool)
        except corpus.CorpusUnavailable as e:
            print(
                f"[generate_tools] historical failures unavailable for {name}: {e}",
                file=sys.stderr,
            )
            continue
        if failures:
            out[name] = failures
    return out


def archive_pending(
    pending_path: Path = PENDING_PATH,
    archive_root: Path = ARCHIVE_ROOT,
    date: str | None = None,
    *,
    successful_tool_names: set[str] | None = None,
) -> Path | None:
    """Move pending entries to ``archive_root/<date>/issues.jsonl`` and
    truncate pending. If pending is empty or missing, this is a no-op.

    If a file already exists for ``date``, new entries are appended.
    Returns the archive file path, or ``None`` if nothing was archived.

    ``successful_tool_names`` (optional) makes archival per-tool-success
    aware: only entries whose ``tool_name`` field is in the set get
    archived; the rest are kept in pending so the next regen sees them
    again. Without this filter, *all* pending entries were archived
    after any successful regen, even when the entry's specific tool
    failed — which silently lost feedback whenever a per-symbol regen
    crashed (claude CLI timeout, stdin race, etc.). Pass the set of
    tool names that successfully wrote to make failures recoverable.
    """
    if not pending_path.exists() or pending_path.stat().st_size == 0:
        return None

    date = date or datetime.now(timezone.utc).date().isoformat()

    # Per-tool-success aware path: split entries, archive successful,
    # rewrite pending with the rest.
    if successful_tool_names is not None:
        kept: list[str] = []
        archived_lines: list[str] = []
        with pending_path.open("r", encoding="utf-8") as f:
            for raw in f:
                line = raw.rstrip("\n")
                if not line.strip():
                    continue
                try:
                    entry = json.loads(line)
                    tool_name = entry.get("tool_name", "")
                except (json.JSONDecodeError, AttributeError):
                    # Malformed line — preserve it in pending rather
                    # than silently dropping. A human can clean it up.
                    kept.append(line)
                    continue
                if tool_name in successful_tool_names:
                    archived_lines.append(line)
                else:
                    kept.append(line)

        if not archived_lines:
            # Nothing archivable this run — leave pending untouched.
            return None

        archive_dir = archive_root / date
        archive_dir.mkdir(parents=True, exist_ok=True)
        archive_file = archive_dir / "issues.jsonl"
        with archive_file.open("a", encoding="utf-8") as f:
            for line in archived_lines:
                f.write(line + "\n")
        # Rewrite pending with the kept (failed-tool / malformed)
        # entries — atomic via a temp + rename so a crash mid-write
        # doesn't lose the survivors.
        if kept:
            pending_path.write_text(
                "\n".join(kept) + "\n", encoding="utf-8"
            )
        else:
            pending_path.write_text("", encoding="utf-8")
        return archive_file

    # Legacy path (no filter): archive everything. Kept for callers
    # that don't yet know which tools succeeded.
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
