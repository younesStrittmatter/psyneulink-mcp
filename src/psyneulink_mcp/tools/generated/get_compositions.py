"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = 'e475b8c2390ebe60d2992965757a024e04b3b7dd13eec9f4a01c7aa285db8002'
__pnl_qualname__ = 'psyneulink.get_compositions'
__pnl_kind__ = 'function'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'get_compositions'
TOOL_DESCRIPTION = 'Call this tool to retrieve a list of all Composition objects that exist in the current execution namespace. Returns an array of Composition instances. NOTE: Due to how this function uses frame inspection, it will only find Compositions created within the MCP tool dispatch scope — not Compositions built in a prior tool call and stored elsewhere. In practice this tool will almost always return an empty list when called via MCP; prefer tracking Compositions by the names returned when you created them.\n\nParameters (JSON Schema):\n{\n  "properties": {},\n  "required": [],\n  "type": "object"\n}\n\nNotes:\nCritical limitation: get_compositions() works by inspecting `inspect.currentframe().f_back.f_locals` — it scans the *caller\'s* local variable scope for Composition instances. When invoked through MCP, the caller is the tool dispatch wrapper, which holds no user-defined variables. Any Compositions created in earlier tool calls will not be visible here. This function was designed for interactive Python sessions (REPL, Jupyter) where Compositions live in the local namespace, not for MCP/RPC contexts. Expect an empty list in virtually all MCP usage.'
TOOL_PARAMETERS = {'properties': {}, 'required': [], 'type': 'object'}
TOOL_NOTES = "Critical limitation: get_compositions() works by inspecting `inspect.currentframe().f_back.f_locals` — it scans the *caller's* local variable scope for Composition instances. When invoked through MCP, the caller is the tool dispatch wrapper, which holds no user-defined variables. Any Compositions created in earlier tool calls will not be visible here. This function was designed for interactive Python sessions (REPL, Jupyter) where Compositions live in the local namespace, not for MCP/RPC contexts. Expect an empty list in virtually all MCP usage."


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.get_compositions
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
    def get_compositions(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to retrieve a list of all Composition objects that exist in the current execution namespace.'
        return _impl(args or {})
