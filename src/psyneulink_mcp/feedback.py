"""Append-only JSONL log of agent reports and auto-captured runtime errors.

Two write paths feed the same file (`feedback/pending/issues.jsonl`):

* `log_agent_report` — called by the `report_tool_issue` MCP tool.
* `log_runtime_error` — called by the `captured_tool` wrapper when any
  registered tool raises.

Entries share a common envelope; the `source` field distinguishes them.
The next `scripts/generate_tools.py` run consumes pending entries and
archives them on success.
"""

from __future__ import annotations

import contextlib
import functools
import json
import os
import sys
import traceback as _tb
from collections.abc import Callable
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Literal

from . import __version__ as _server_version

ToolLayer = Literal["generated", "curated"]
IssueType = Literal[
    "unclear_description",
    "wrong_schema",
    "missing_arg",
    "wrong_behavior",
    "other",
]

_PACKAGE_DIR = Path(__file__).resolve().parent
_REPO_ROOT_DEFAULT = _PACKAGE_DIR.parent.parent

ENV_FEEDBACK_PATH = "PSYNEULINK_MCP_FEEDBACK_PATH"

_TOOL_LAYERS: dict[str, ToolLayer] = {}


def lookup_tool_layer(tool_name: str) -> ToolLayer:
    """Layer the tool was registered under, or "generated" if not found."""
    return _TOOL_LAYERS.get(tool_name, "generated")


def feedback_path() -> Path:
    override = os.environ.get(ENV_FEEDBACK_PATH)
    if override:
        return Path(override)
    return _REPO_ROOT_DEFAULT / "feedback" / "pending" / "issues.jsonl"


def _pnl_version() -> str:
    try:
        import psyneulink
    except Exception:
        return "unavailable"
    return getattr(psyneulink, "__version__", "unknown")


def _now_iso() -> str:
    return (
        datetime.now(timezone.utc)
        .isoformat(timespec="seconds")
        .replace("+00:00", "Z")
    )


def _write_entry(entry: dict[str, Any]) -> None:
    try:
        path = feedback_path()
        path.parent.mkdir(parents=True, exist_ok=True)
        line = json.dumps(entry, default=repr, ensure_ascii=False)
        with path.open("a", encoding="utf-8") as f:
            f.write(line + "\n")
    except Exception as e:  # noqa: BLE001
        with contextlib.suppress(Exception):
            print(f"[psyneulink-mcp] feedback log failed: {e!r}", file=sys.stderr)


def log_runtime_error(
    tool_name: str,
    tool_layer: ToolLayer,
    args: dict[str, Any],
    exc: BaseException,
) -> None:
    _write_entry(
        {
            "timestamp": _now_iso(),
            "source": "auto",
            "tool_name": tool_name,
            "tool_layer": tool_layer,
            "pnl_version": _pnl_version(),
            "server_version": _server_version,
            "payload": {
                "args": args,
                "exception_type": type(exc).__name__,
                "exception_message": str(exc),
                "traceback": "".join(
                    _tb.format_exception(type(exc), exc, exc.__traceback__)
                ),
            },
        }
    )


def log_agent_report(
    tool_name: str,
    tool_layer: ToolLayer,
    issue_type: IssueType,
    description: str,
    suggested_fix: str | None = None,
    agent_context: str | None = None,
) -> None:
    _write_entry(
        {
            "timestamp": _now_iso(),
            "source": "agent",
            "tool_name": tool_name,
            "tool_layer": tool_layer,
            "pnl_version": _pnl_version(),
            "server_version": _server_version,
            "payload": {
                "issue_type": issue_type,
                "description": description,
                "suggested_fix": suggested_fix,
                "agent_context": agent_context,
            },
        }
    )


def captured_tool(mcp: Any, layer: ToolLayer, **mcp_tool_kwargs: Any) -> Callable:
    """Register a tool with `mcp` and auto-log any exception it raises.

    Usage:

        @captured_tool(mcp, layer="curated")
        def my_tool(...): ...

    Equivalent to `@mcp.tool(**mcp_tool_kwargs)` but the wrapped function
    routes exceptions through `log_runtime_error` before re-raising.
    """

    def decorator(fn: Callable) -> Callable:
        _TOOL_LAYERS[fn.__name__] = layer

        @functools.wraps(fn)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                return fn(*args, **kwargs)
            except Exception as exc:
                log_runtime_error(
                    tool_name=fn.__name__,
                    tool_layer=layer,
                    args={"args": list(args), "kwargs": dict(kwargs)},
                    exc=exc,
                )
                raise

        return mcp.tool(**mcp_tool_kwargs)(wrapper)

    return decorator
