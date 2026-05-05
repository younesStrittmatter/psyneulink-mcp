"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = 'c7a216580570c62f0991f20cccfc5504fe6e1ecdbb71210385de4bcd063f6eea'
__pnl_qualname__ = 'psyneulink.is_Function'
__pnl_kind__ = 'function'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'is__function'
TOOL_DESCRIPTION = 'Call this tool to check whether a given value is a PsyNeuLink Function — either an instance of `psyneulink.core.components.functions.function.Function` or a subclass of it. Returns `true` if the check passes, `false` if the value is falsy or not a Function type.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "x": {\n      "description": "The value to test \\u2014 typically a PsyNeuLink Function class name (e.g. \'Linear\', \'Logistic\') or a stringified reference. The underlying call is psyneulink.is_Function(x).",\n      "type": "string"\n    }\n  },\n  "required": [\n    "x"\n  ],\n  "type": "object"\n}\n\nNotes:\nThe source checks falsy first (`if not x: return False`), then `isinstance(x, Function)`, then `issubclass(x, Function)`. In a JSON/MCP context the agent can only pass serializable values; passing a bare string will return False unless the host layer resolves it to an actual Python class before the call. If x is truthy but not a class or Function instance, `issubclass(x, Function)` will raise TypeError — the function has no guard for arbitrary non-class objects.'
TOOL_PARAMETERS = { 'properties': { 'x': { 'description': 'The value to test — typically a PsyNeuLink '
                                        "Function class name (e.g. 'Linear', "
                                        "'Logistic') or a stringified reference. The "
                                        'underlying call is psyneulink.is_Function(x).',
                         'type': 'string'}},
  'required': ['x'],
  'type': 'object'}
TOOL_NOTES = 'The source checks falsy first (`if not x: return False`), then `isinstance(x, Function)`, then `issubclass(x, Function)`. In a JSON/MCP context the agent can only pass serializable values; passing a bare string will return False unless the host layer resolves it to an actual Python class before the call. If x is truthy but not a class or Function instance, `issubclass(x, Function)` will raise TypeError — the function has no guard for arbitrary non-class objects.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.is_Function
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
    def is__function(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to check whether a given value is a PsyNeuLink Function — either an instance of `psyneulink.core.components.functions.function.Function` or a subclass of it.'
        return _impl(args or {})
