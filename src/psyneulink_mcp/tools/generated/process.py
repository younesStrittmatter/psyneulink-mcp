"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '6a6de01e3c446d5f3d9f3c715538eb0ae65a5a3d3e82a61d1ab068f19dd332fb'
__pnl_qualname__ = 'psyneulink.Process'
__pnl_kind__ = 'function'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'process'
TOOL_DESCRIPTION = 'Do NOT call this tool. `psyneulink.Process` is a deprecated stub that accepts no meaningful arguments and only emits a deprecation warning — it performs no computation and returns nothing useful. Use `Composition` or `PathwayComposition` instead to build processing pipelines.\n\nParameters (JSON Schema):\n{\n  "properties": {},\n  "required": [],\n  "type": "object"\n}\n\nNotes:\nThis function is a deprecated no-op. The body is `show_warning_sys_and_proc_warning()` followed by an implicit `None` return. Any arguments passed are silently ignored (`*args, **kwars` are never used). Agents should use `Composition` or `PathwayComposition` to construct processing pathways.'
TOOL_PARAMETERS = {'properties': {}, 'required': [], 'type': 'object'}
TOOL_NOTES = 'This function is a deprecated no-op. The body is `show_warning_sys_and_proc_warning()` followed by an implicit `None` return. Any arguments passed are silently ignored (`*args, **kwars` are never used). Agents should use `Composition` or `PathwayComposition` to construct processing pathways.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.Process
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
    def process(args: dict[str, Any] | None = None) -> Any:
        'Do NOT call this tool.'
        return _impl(args or {})
