"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '693829b046690d40138444e9e983359a0e3821cf4689b9cf2f3901b62950187a'
__pnl_qualname__ = 'psyneulink.core.components.functions.nonstateful.transferfunctions.get_validator_by_function'
__pnl_kind__ = 'function'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'get_validator_by_function'
TOOL_DESCRIPTION = 'Call this tool when you need to create a reusable parameter validator for a PsyNeuLink Parameters class, given a predicate function that tests whether a candidate value is acceptable. The result is a validator method (FunctionType) that returns None on success or an error string on failure, suitable for direct assignment to a Parameter\'s validator slot.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "function": {\n      "description": "The qualified name (e.g. \'psyneulink.core.globals.utilities.is_numeric\') of a Python callable that accepts exactly one positional argument and returns True if the value is valid, False otherwise. Must be resolvable at call time.",\n      "type": "string"\n    }\n  },\n  "required": [\n    "function"\n  ],\n  "type": "object"\n}\n\nNotes:\nThe `function` parameter must be a Python callable at runtime, but MCP serializes arguments as JSON. Pass the fully qualified dotted name of a module-level callable; the host must resolve it. Anonymous lambdas or locally-defined functions cannot be passed. The returned validator is a closure — it is not itself JSON-serializable and must be used immediately in the same Python session (e.g., assigned to a Parameter definition). If the predicate returns False, the validator error message will be \'{function.__name__} returned False\', so use a descriptively named predicate for readable errors.'
TOOL_PARAMETERS = { 'properties': { 'function': { 'description': 'The qualified name (e.g. '
                                               "'psyneulink.core.globals.utilities.is_numeric') "
                                               'of a Python callable that accepts '
                                               'exactly one positional argument and '
                                               'returns True if the value is valid, '
                                               'False otherwise. Must be resolvable at '
                                               'call time.',
                                'type': 'string'}},
  'required': ['function'],
  'type': 'object'}
TOOL_NOTES = "The `function` parameter must be a Python callable at runtime, but MCP serializes arguments as JSON. Pass the fully qualified dotted name of a module-level callable; the host must resolve it. Anonymous lambdas or locally-defined functions cannot be passed. The returned validator is a closure — it is not itself JSON-serializable and must be used immediately in the same Python session (e.g., assigned to a Parameter definition). If the predicate returns False, the validator error message will be '{function.__name__} returned False', so use a descriptively named predicate for readable errors."


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.get_validator_by_function
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
    def get_validator_by_function(args: dict[str, Any] | None = None) -> Any:
        'Call this tool when you need to create a reusable parameter validator for a PsyNeuLink Parameters class, given a predicate function that tests whether a candidate value is acceptable.'
        return _impl(args or {})
