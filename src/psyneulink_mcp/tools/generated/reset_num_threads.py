"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = 'cb269c8da1a2bc89f8075e26b888df3980a19fce78d30077c7e03240fc6c15bb'
__pnl_qualname__ = 'psyneulink.reset_num_threads'
__pnl_kind__ = 'function'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'reset_num_threads'
TOOL_DESCRIPTION = 'Call this tool to restore PsyNeuLink\'s thread count to the platform default (cpu_count()) after a previous `set_num_threads` call has changed it. Use it at the end of a run where you temporarily reduced parallelism, or to recover from an unknown thread configuration. Returns nothing; the effect is immediate and global.\n\nParameters (JSON Schema):\n{\n  "properties": {},\n  "required": [],\n  "type": "object"\n}\n\nNotes:\nThis function takes no arguments. It resets the internal `_num_threads` global to the value of `multiprocessing.cpu_count()` captured at import time, then re-applies environment variables and library settings via `set_num_threads`. The reset is process-wide and affects all subsequent PsyNeuLink computations in the same Python session.'
TOOL_PARAMETERS = {'properties': {}, 'required': [], 'type': 'object'}
TOOL_NOTES = 'This function takes no arguments. It resets the internal `_num_threads` global to the value of `multiprocessing.cpu_count()` captured at import time, then re-applies environment variables and library settings via `set_num_threads`. The reset is process-wide and affects all subsequent PsyNeuLink computations in the same Python session.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.reset_num_threads
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
    def reset_num_threads(args: dict[str, Any] | None = None) -> Any:
        "Call this tool to restore PsyNeuLink's thread count to the platform default (cpu_count()) after a previous `set_num_threads` call has changed it."
        return _impl(args or {})
