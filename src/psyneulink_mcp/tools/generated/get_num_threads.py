"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '8e7f02596ef61c94e98c93cd24c0c53268fc0db22df9848e101a663ebf12ca50'
__pnl_qualname__ = 'psyneulink.get_num_threads'
__pnl_kind__ = 'function'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'get_num_threads'
TOOL_DESCRIPTION = 'Call this tool to query the current global thread count used by PsyNeuLink — useful before scheduling parallel runs or to confirm that a prior `set_num_threads` call took effect. Returns a single integer: the active thread count, or the platform default if `set_num_threads` was never called.\n\nParameters (JSON Schema):\n{\n  "properties": {},\n  "required": [],\n  "type": "object"\n}\n\nNotes:\nThis function takes no arguments. The returned value reflects the global `_num_threads` state, which is the platform default until `set_num_threads` is explicitly called. The platform default is typically the CPU core count but is not guaranteed to be a fixed value across machines.'
TOOL_PARAMETERS = {'properties': {}, 'required': [], 'type': 'object'}
TOOL_NOTES = 'This function takes no arguments. The returned value reflects the global `_num_threads` state, which is the platform default until `set_num_threads` is explicitly called. The platform default is typically the CPU core count but is not guaranteed to be a fixed value across machines.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.get_num_threads
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
    def get_num_threads(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to query the current global thread count used by PsyNeuLink — useful before scheduling parallel runs or to confirm that a prior `set_num_threads` call took effect.'
        return _impl(args or {})
