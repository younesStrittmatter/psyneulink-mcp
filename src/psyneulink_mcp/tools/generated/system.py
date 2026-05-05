"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '6b7d8eb5f3944dcc451604dca3c3e630e57ba2019e9d735d630403f9e547baf7'
__pnl_qualname__ = 'psyneulink.System'
__pnl_kind__ = 'function'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'system'
TOOL_DESCRIPTION = 'Do NOT call this tool to build models. `psyneulink.System` is a deprecated stub that only emits a deprecation warning and returns nothing — it does not create a runnable system. Call this tool only if an existing script explicitly references `System` and you need to understand why it triggers a warning. For all new model construction, use the `Composition` tool instead.\n\nParameters (JSON Schema):\n{\n  "properties": {},\n  "required": [],\n  "type": "object"\n}\n\nNotes:\n`System` was PsyNeuLink\'s original top-level container, fully replaced by `Composition`. The entire function body is `show_warning_sys_and_proc_warning()` — it accepts any args/kwargs but silently discards them and returns `None`. Any model-building code that passes arguments to `System` will appear to succeed but produce no object. Always use `Composition` for constructing networks.'
TOOL_PARAMETERS = {'properties': {}, 'required': [], 'type': 'object'}
TOOL_NOTES = "`System` was PsyNeuLink's original top-level container, fully replaced by `Composition`. The entire function body is `show_warning_sys_and_proc_warning()` — it accepts any args/kwargs but silently discards them and returns `None`. Any model-building code that passes arguments to `System` will appear to succeed but produce no object. Always use `Composition` for constructing networks."


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.System
    resolved = handles.resolve_in(kwargs)
    result = target(**resolved)
    try:
        json.dumps(result)
    except (TypeError, ValueError):
        payload = handles.register_handle(result)
        handles.record_call(
            TOOL_NAME,
            kwargs,
            result_handle=payload.get('handle') if isinstance(payload, dict) else None,
            tool_layer="generated",
        )
        return payload
    handles.record_call(TOOL_NAME, kwargs, result_handle=None, tool_layer="generated")
    return result


def register(mcp: Any) -> None:
    @captured_tool(mcp, layer="generated", name=TOOL_NAME, description=TOOL_DESCRIPTION)
    def system(args: dict[str, Any] | None = None) -> Any:
        'Do NOT call this tool to build models.'
        return _impl(args or {})
