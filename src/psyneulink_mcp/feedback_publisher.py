"""Best-effort, fire-and-forget publisher of runtime captures to GitHub Issues.

The local JSONL written by `feedback.log_runtime_error` is and remains the
source of truth for the regen pipeline. This module is a *secondary* surface
that mirrors novel runtime failures into open GitHub issues on the corpus
repo, so they're visible across machines and humans/agents can comment on
them between regen cycles.

Hard rules (mirror `CLAUDE.md §Separation of concerns` + the agent task brief):

* Never block the agent's response. `try_file` returns immediately; the
  actual `gh` work happens on a daemon thread. If `gh` is slow or down,
  tool returns are unaffected.
* Never raise from the runtime path. Both `try_file` and the worker
  swallow every exception (`gh` missing, network down, JSON malformed,
  whatever) — at worst we lose the GitHub side; the local JSONL still
  has the full record.
* Dedup hard. Within one process we cache `(tool, exc_type, msg-hash)`
  triples and skip them outright. Across processes, we search the corpus
  for an open `feedback,auto` issue with the same deterministic title
  before opening a new one.
* Opt-out via `PSYNEULINK_MCP_AUTO_FILE_ISSUES=0` (also `false` / `no` /
  `off`). Default ON when `gh` is on PATH.
* No coupling to `psyneulink-corpus` source (this module never reads or
  edits that repo's files; it only calls `gh issue create / list`).
"""

from __future__ import annotations

import contextlib
import hashlib
import json
import os
import re
import shutil
import sys
import threading
from typing import Any

from . import __version__ as _server_version
from . import corpus

ENV_AUTO_FILE_ISSUES = "PSYNEULINK_MCP_AUTO_FILE_ISSUES"

# Truthy/falsy parsing for the opt-out env var.
_FALSY = {"0", "false", "no", "off", ""}

# Hard caps on body sub-sections so a deranged tool can't post a 10 MB issue.
_MAX_ARGS_CHARS = 2000
_MAX_TRACEBACK_CHARS = 3000
# 80 chars is the spec; gives a stable, search-friendly title.
_MAX_TITLE_MSG_CHARS = 80

# Process-scoped dedup cache. Tuple shape: (tool_name, exc_type, msg_sha1).
_SEEN: set[tuple[str, str, str]] = set()
# Per-process cache of ``pnl:<tool_name>`` labels we've already
# self-healed (created or confirmed-exists). One entry means "we've
# successfully ensured this label exists in the corpus during this
# process; don't waste a `gh label create` call on it again." The
# ``_attempted`` cache tracks labels we've TRIED to heal but failed
# on, so a second consecutive miss for the same label gives up
# instead of looping forever.
_HEALED_LABELS: set[str] = set()
_HEAL_ATTEMPTED: set[str] = set()
_LOCK = threading.Lock()


def reset_for_tests() -> None:
    """Clear the dedup cache. Call from test fixtures so each test is isolated."""
    with _LOCK:
        _SEEN.clear()
        _HEALED_LABELS.clear()
        _HEAL_ATTEMPTED.clear()


def _truthy_env(name: str, default: bool = True) -> bool:
    raw = os.environ.get(name)
    if raw is None:
        return default
    return raw.strip().lower() not in _FALSY


def _enabled() -> bool:
    """Cheap pre-flight check run on the agent thread before spawning a worker.

    Auth status is *not* probed here (that would mean a `gh auth status`
    subprocess call on the agent thread). We just check the env opt-out
    and that `gh` exists on PATH; if `gh` is unauthenticated, the worker
    will get a `CorpusUnavailable` and silently drop the issue. That's
    fine — the local JSONL still has the full record.
    """
    if not _truthy_env(ENV_AUTO_FILE_ISSUES, default=True):
        return False
    return shutil.which("gh") is not None


def _normalize_message(msg: str) -> str:
    """Collapse whitespace so equivalent messages produce identical titles."""
    return re.sub(r"\s+", " ", msg or "").strip()


def _msg_hash(msg: str) -> str:
    return hashlib.sha1(_normalize_message(msg).encode("utf-8", errors="replace")).hexdigest()


def _triple_from_entry(entry: dict[str, Any]) -> tuple[str, str, str] | None:
    """Extract the dedup key. Returns None for malformed entries."""
    try:
        tool = str(entry["tool_name"])
        payload = entry["payload"]
        exc_type = str(payload["exception_type"])
        msg = str(payload.get("exception_message", ""))
    except (KeyError, TypeError):
        return None
    return (tool, exc_type, _msg_hash(msg))


def _title_for(entry: dict[str, Any]) -> str:
    """Deterministic title shape: `[auto] <tool>: <ExcType>: <first 80 chars>`.

    Determinism is what makes cross-process dedup via `gh issue list
    --search 'in:title "..."' work — same triple → same title → search hit.
    """
    tool = entry["tool_name"]
    exc_type = entry["payload"]["exception_type"]
    msg = _normalize_message(entry["payload"].get("exception_message", ""))
    return f"[auto] {tool}: {exc_type}: {msg[:_MAX_TITLE_MSG_CHARS]}"


def _body_for(entry: dict[str, Any]) -> str:
    """Render the issue body in the same shape that the issue form produces.

    `corpus._parse_issue_body` already knows how to extract these `### Label`
    sections, so the regen pipeline reads auto-filed issues with the same
    parser it uses for human reports.
    """
    payload = entry.get("payload", {}) or {}
    tool = entry.get("tool_name", "unknown")
    exc_type = payload.get("exception_type", "Exception")
    exc_msg = payload.get("exception_message", "") or ""
    traceback_text = payload.get("traceback", "") or ""
    args = payload.get("args", {}) or {}
    server_version = entry.get("server_version", _server_version)

    # JSON-encode args defensively — `default=repr` means we never crash on
    # non-serialisable values; we just stringify them.
    try:
        args_json = json.dumps(args, default=repr, indent=2, ensure_ascii=False)
    except Exception:  # noqa: BLE001
        args_json = repr(args)
    if len(args_json) > _MAX_ARGS_CHARS:
        args_json = args_json[:_MAX_ARGS_CHARS] + "\n... (truncated)"

    # Tail of the traceback is the useful bit (innermost frames).
    if len(traceback_text) > _MAX_TRACEBACK_CHARS:
        traceback_text = "... (truncated)\n" + traceback_text[-_MAX_TRACEBACK_CHARS:]

    description = (
        f"**{exc_type}**: {exc_msg}\n\n"
        f"**Args:**\n```json\n{args_json}\n```\n\n"
        f"**Traceback (truncated):**\n```\n{traceback_text}\n```"
    )

    agent_context = f"auto-captured runtime error from psyneulink-mcp v{server_version}"

    return (
        f"### Tool name\n\n{tool}\n\n"
        f"### Issue type\n\nwrong_behavior\n\n"
        f"### Description\n\n{description}\n\n"
        f"### Suggested fix\n\n_No response_\n\n"
        f"### Agent context\n\n{agent_context}\n"
    )


def _stderr(msg: str) -> None:
    with contextlib.suppress(Exception):
        print(f"[psyneulink-mcp] feedback-publisher: {msg}", file=sys.stderr)


def _looks_like_missing_label(error_message: str, label: str) -> bool:
    """Heuristic — did `gh issue create` fail because ``label`` doesn't exist?

    `gh` reports missing labels with stderr like::

        could not add label: 'pnl:create_lca_mechanism' not found

    or::

        'pnl:foo' not found

    Match both shapes (and a few near-equivalents) so the self-heal
    triggers reliably. False positives are cheap — at worst we make
    one extra ``gh label create`` call for an unrelated failure;
    false negatives mean a stuck per-symbol label, so err generous.
    """
    msg = error_message.lower()
    if label.lower() in msg and "not found" in msg:
        return True
    return "could not add label" in msg and label.lower() in msg


def _try_heal_label(label: str) -> bool:
    """Best-effort self-heal: ensure ``label`` exists on the corpus.

    Returns ``True`` when the label exists at the end of the call.
    Returns ``False`` when the heal attempt failed or has already
    failed once in this process — the caller should not retry the
    issue create after a ``False`` return (avoids loops).
    """
    with _LOCK:
        if label in _HEALED_LABELS:
            return True
        if label in _HEAL_ATTEMPTED:
            # Second consecutive miss for the same label in one process
            # — give up rather than loop. The local JSONL still has
            # the full record.
            return False
        _HEAL_ATTEMPTED.add(label)
    try:
        corpus.ensure_label_exists(label)
    except corpus.CorpusUnavailable as e:
        _stderr(f"label-heal failed for {label}: {e}")
        return False
    except Exception as e:  # noqa: BLE001
        _stderr(f"label-heal raised unexpectedly for {label}: {e!r}")
        return False
    with _LOCK:
        _HEALED_LABELS.add(label)
    _stderr(f"self-healed missing label {label}")
    return True


def _file(entry: dict[str, Any], triple: tuple[str, str, str]) -> None:
    """Worker body run on the daemon thread. Never raises."""
    try:
        title = _title_for(entry)
        body = _body_for(entry)
        try:
            existing = corpus.find_existing_feedback_issue(title)
        except corpus.CorpusUnavailable as e:
            _stderr(f"search failed for {triple[0]}/{triple[1]}: {e}")
            return
        if existing is not None:
            return

        symbol_label = corpus.pnl_symbol_label(entry["tool_name"])
        labels = [corpus.FEEDBACK_LABEL, corpus.AUTO_LABEL, symbol_label]

        try:
            corpus.open_feedback_issue(title=title, body=body, labels=labels)
            return
        except corpus.CorpusUnavailable as e:
            # If the failure looks like a missing-label problem for our
            # per-symbol label, self-heal once and retry exactly once.
            # Any other failure (rate-limit, auth, unrelated) drops here.
            err_msg = str(e)
            if not _looks_like_missing_label(err_msg, symbol_label):
                _stderr(f"create failed for {triple[0]}/{triple[1]}: {e}")
                return
            if not _try_heal_label(symbol_label):
                _stderr(f"create failed for {triple[0]}/{triple[1]} and label-heal gave up: {e}")
                return
            try:
                corpus.open_feedback_issue(title=title, body=body, labels=labels)
            except corpus.CorpusUnavailable as retry_err:
                _stderr(f"create-retry failed for {triple[0]}/{triple[1]}: {retry_err}")
                return
    except Exception as e:  # noqa: BLE001
        _stderr(f"unexpected publisher failure: {e!r}")


def try_file(entry: dict[str, Any]) -> threading.Thread | None:
    """Best-effort, fire-and-forget. Returns the spawned worker thread, or
    `None` when the publisher short-circuited (opt-out, `gh` missing, dup,
    malformed entry, etc.).

    Production callers should ignore the return value. Tests can `.join()`
    on the returned thread to assert on side effects deterministically.

    Never raises. Never blocks for any meaningful duration on the calling
    thread (the only sync work is an env lookup, a `which("gh")` and a
    set membership check — all sub-millisecond).
    """
    try:
        if not _enabled():
            return None
        triple = _triple_from_entry(entry)
        if triple is None:
            return None
        with _LOCK:
            if triple in _SEEN:
                return None
            # Eager add: if the worker fails (network down, gh unauth, …)
            # we *do not* retry the same triple in this process. The local
            # JSONL still has the full record, and hammering `gh` from
            # background threads on a flaky link is its own anti-pattern.
            _SEEN.add(triple)
        worker = threading.Thread(
            target=_file,
            args=(entry, triple),
            name="psyneulink-mcp-issue-filer",
            daemon=True,
        )
        worker.start()
        return worker
    except Exception as e:  # noqa: BLE001
        _stderr(f"try_file dispatch failed: {e!r}")
        return None
