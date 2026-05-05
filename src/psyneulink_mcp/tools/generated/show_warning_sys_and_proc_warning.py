"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = 'bda66fb7639a0018130b48227376ccb3449c4f65a3c6e2d036b9021da359d73b'
__pnl_qualname__ = 'psyneulink.show_warning_sys_and_proc_warning'
__pnl_kind__ = 'function'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'show_warning_sys_and_proc_warning'
TOOL_DESCRIPTION = 'Call this tool only if you specifically need to surface the PsyNeuLink deprecation error for System/Process to the user or a downstream caller. It unconditionally raises a ComponentError stating that \'System\' and \'Process\' are no longer supported and must be replaced with \'Composition\' and/or \'Pathway\'. It never returns a value — every call results in an exception.\n\nParameters (JSON Schema):\n{\n  "properties": {},\n  "required": [],\n  "type": "object"\n}\n\nNotes:\nThis function has no parameters and always raises ComponentError — it cannot succeed. Do not call it expecting any result. Its sole purpose is to emit a hard deprecation signal. If your modeling code references System or Process, migrate to Composition and/or Pathway before proceeding.'
TOOL_PARAMETERS = {'properties': {}, 'required': [], 'type': 'object'}
TOOL_NOTES = 'This function has no parameters and always raises ComponentError — it cannot succeed. Do not call it expecting any result. Its sole purpose is to emit a hard deprecation signal. If your modeling code references System or Process, migrate to Composition and/or Pathway before proceeding.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.show_warning_sys_and_proc_warning
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
    def show_warning_sys_and_proc_warning(args: dict[str, Any] | None = None) -> Any:
        'Call this tool only if you specifically need to surface the PsyNeuLink deprecation error for System/Process to the user or a downstream caller.'
        return _impl(args or {})
