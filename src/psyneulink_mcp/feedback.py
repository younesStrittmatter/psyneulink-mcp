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
    entry: dict[str, Any] = {
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
    _write_entry(entry)
    _publish_runtime_error(entry)


def _publish_runtime_error(entry: dict[str, Any]) -> None:
    """Best-effort GitHub-issue mirror of the JSONL write.

    The local JSONL is the source of truth for the regen pipeline; this is
    an *additional* surface so failures show up across machines. Imported
    lazily so a broken/missing `feedback_publisher` can't break logging,
    and wrapped to swallow every exception (the runtime path must never
    raise from here).
    """
    try:
        from . import feedback_publisher

        feedback_publisher.try_file(entry)
    except Exception as e:  # noqa: BLE001
        with contextlib.suppress(Exception):
            print(
                f"[psyneulink-mcp] feedback publish dispatch failed: {e!r}",
                file=sys.stderr,
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

    Description compaction
    ----------------------

    The auto-generated tool modules pass ``description=TOOL_DESCRIPTION``
    where ``TOOL_DESCRIPTION`` inlines the full JSON-Schema parameter
    block AND a trailing ``Notes:`` section. With 354 generated tools
    that's ~258K tokens just for ``tools/list`` — past sonnet's 200K
    context window before any conversation has even started. We strip
    the schema/notes blocks here and park the full original in
    :mod:`psyneulink_mcp.tool_descriptions` so the
    ``describe_psyneulink_tool`` curated tool can hand it back on
    demand. No regen required — this works on every already-rendered
    module.
    """
    from . import tool_descriptions as _td

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

        # Stash the full description (and schema + PNL provenance, if
        # the calling module surfaced them) for describe_psyneulink_tool,
        # then replace the description the FastMCP registration sees
        # with the prose-only compact form.
        tool_kwargs = dict(mcp_tool_kwargs)
        full_desc = tool_kwargs.get("description") or ""
        tool_name = tool_kwargs.get("name") or fn.__name__
        if full_desc:
            module = _caller_module(fn)
            _td.register_full_description(
                tool_name,
                full_desc,
                parameters=_module_attr(module, "TOOL_PARAMETERS", dict),
                qualname=_module_attr(module, "__pnl_qualname__", str),
                kind=_module_attr(module, "__pnl_kind__", str),
            )
            tool_kwargs["description"] = _td.compact_description(full_desc)

        return mcp.tool(**tool_kwargs)(wrapper)

    return decorator


def _caller_module(fn: Callable) -> Any | None:
    """Return the live module object the tool function was defined in."""
    import sys

    module_name = getattr(fn, "__module__", None)
    if not module_name:
        return None
    return sys.modules.get(module_name)


def _module_attr(module: Any, name: str, expected_type: type) -> Any:
    """Return ``module.<name>`` if it's of ``expected_type``, else ``None``.

    Used to lift the generator-emitted module-scope markers
    (``TOOL_PARAMETERS``, ``__pnl_qualname__``, ``__pnl_kind__``) onto
    the description registry. Curated modules that don't define them
    get ``None``, which the registry treats as "no structured info".
    """
    if module is None:
        return None
    value = getattr(module, name, None)
    if value is None or not isinstance(value, expected_type):
        return None
    return value
