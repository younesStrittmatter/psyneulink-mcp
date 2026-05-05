"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = 'c4e6f1346e7cf3c9df4370645fffaea1bbb41deaac7206121d05755a94aecacd'
__pnl_qualname__ = 'psyneulink.core.components.functions.nonstateful.optimizationfunctions.is_function_type'
__pnl_kind__ = 'function'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'is_function_type'
TOOL_DESCRIPTION = 'Call this tool to check whether a given value qualifies as a PsyNeuLink function type — i.e., whether it is callable, a Function instance, a Python function/method, or a subclass of PsyNeuLink\'s Function base class. Returns a boolean: True if the value is a function type, False otherwise. Most useful as a server-side predicate when the value can be resolved to a live Python object; it is rarely useful to call from an agent with a plain JSON string.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "x": {\n      "description": "Name or string representation of the value to test. Note: since MCP transport is JSON, only serializable values can be passed; a plain string is not callable and will return False. Meaningful use requires the server to resolve the string to a live Python object before calling.",\n      "type": "string"\n    }\n  },\n  "required": [\n    "x"\n  ],\n  "type": "object"\n}\n\nNotes:\nMCP transport serializes arguments as JSON, so `x` arrives as a string. A plain string is not callable, not falsy (if non-empty), and not a Function instance or subclass, so it will always return False regardless of its content. This tool only yields True when the server can resolve `x` to a live callable or PsyNeuLink Function object before dispatching the call. The function short-circuits on falsy values (empty string, None, 0, etc.) and returns False immediately — it does NOT raise on unexpected types.'
TOOL_PARAMETERS = { 'properties': { 'x': { 'description': 'Name or string representation of the value to '
                                        'test. Note: since MCP transport is JSON, only '
                                        'serializable values can be passed; a plain '
                                        'string is not callable and will return False. '
                                        'Meaningful use requires the server to resolve '
                                        'the string to a live Python object before '
                                        'calling.',
                         'type': 'string'}},
  'required': ['x'],
  'type': 'object'}
TOOL_NOTES = 'MCP transport serializes arguments as JSON, so `x` arrives as a string. A plain string is not callable, not falsy (if non-empty), and not a Function instance or subclass, so it will always return False regardless of its content. This tool only yields True when the server can resolve `x` to a live callable or PsyNeuLink Function object before dispatching the call. The function short-circuits on falsy values (empty string, None, 0, etc.) and returns False immediately — it does NOT raise on unexpected types.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.is_function_type
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
    def is_function_type(args: dict[str, Any] | None = None) -> Any:
        "Call this tool to check whether a given value qualifies as a PsyNeuLink function type — i.e., whether it is callable, a Function instance, a Python function/method, or a subclass of PsyNeuLink's Function base class."
        return _impl(args or {})
