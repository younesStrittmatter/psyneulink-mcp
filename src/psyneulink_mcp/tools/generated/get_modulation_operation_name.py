"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '4d1fc4b162461c1c7e4f2eee6d1753ccc28cef6668dcfbaf7a0a87741d839077'
__pnl_qualname__ = 'psyneulink.get_modulationOperation_name'
__pnl_kind__ = 'function'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'get_modulation_operation_name'
TOOL_DESCRIPTION = 'Call this tool to identify the name of a PsyNeuLink modulation operation from its callable implementation. It probes the callable with (1, 2) and returns "MODULATION_OVERRIDE", "MODULATION_MULTIPLY", or "MODULATION_ADD" as a string, or False if the operation is not one of the three recognized modulation types. Use this when you have a modulation operation object and need to know which symbolic constant it corresponds to.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "operation": {\n      "description": "The name of the modulation operation callable to identify. Must be a reference to a callable that accepts two numeric arguments; recognized operations are the PsyNeuLink modulation lambdas corresponding to OVERRIDE (returns first arg), MULTIPLY (multiplies args), and ADD (adds args).",\n      "type": "string"\n    }\n  },\n  "required": [\n    "operation"\n  ],\n  "type": "object"\n}\n\nNotes:\nThe underlying function requires a Python callable, not a string — it calls operation(1, 2) and inspects the result. Passing a plain string will raise a TypeError. This tool is only useful in contexts where the host layer can resolve the string name to an actual callable before invoking the function. Returns the boolean False (not a string) for unrecognized operations, so callers must check the return type. The three recognized results map to: result==1 → MODULATION_OVERRIDE, result==2 → MODULATION_MULTIPLY, result==3 → MODULATION_ADD.'
TOOL_PARAMETERS = { 'properties': { 'operation': { 'description': 'The name of the modulation operation '
                                                'callable to identify. Must be a '
                                                'reference to a callable that accepts '
                                                'two numeric arguments; recognized '
                                                'operations are the PsyNeuLink '
                                                'modulation lambdas corresponding to '
                                                'OVERRIDE (returns first arg), '
                                                'MULTIPLY (multiplies args), and ADD '
                                                '(adds args).',
                                 'type': 'string'}},
  'required': ['operation'],
  'type': 'object'}
TOOL_NOTES = 'The underlying function requires a Python callable, not a string — it calls operation(1, 2) and inspects the result. Passing a plain string will raise a TypeError. This tool is only useful in contexts where the host layer can resolve the string name to an actual callable before invoking the function. Returns the boolean False (not a string) for unrecognized operations, so callers must check the return type. The three recognized results map to: result==1 → MODULATION_OVERRIDE, result==2 → MODULATION_MULTIPLY, result==3 → MODULATION_ADD.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.get_modulationOperation_name
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
    def get_modulation_operation_name(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to identify the name of a PsyNeuLink modulation operation from its callable implementation.'
        return _impl(args or {})
