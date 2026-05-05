"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = 'f981141548660df9ed593d7f74188df609d18229b9cdcce35db139f4ad9e4b01'
__pnl_qualname__ = 'psyneulink.core.components.functions.nonstateful.learningfunctions.is_numeric'
__pnl_kind__ = 'function'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'is_numeric'
TOOL_DESCRIPTION = 'Call this tool to check whether a value is numeric before passing it to a PsyNeuLink component that requires a numeric input (e.g., a mechanism\'s variable, a function\'s parameter, or a matrix entry). Returns True if the value is compatible with numeric operations, False otherwise.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "x": {\n      "description": "The value to test for numeric compatibility. Typically a scalar number or a list/array of numbers.",\n      "oneOf": [\n        {\n          "type": "number"\n        },\n        {\n          "items": {\n            "type": "number"\n          },\n          "type": "array"\n        }\n      ]\n    }\n  },\n  "required": [\n    "x"\n  ],\n  "type": "object"\n}\n\nNotes:\nLength check is disabled (kwCompatibilityLength:0), so scalars and arrays of any length both pass. Only pure numeric values (int, float, or arrays thereof) return True; strings, None, and mixed-type collections return False.'
TOOL_PARAMETERS = { 'properties': { 'x': { 'description': 'The value to test for numeric compatibility. '
                                        'Typically a scalar number or a list/array of '
                                        'numbers.',
                         'oneOf': [ {'type': 'number'},
                                    {'items': {'type': 'number'}, 'type': 'array'}]}},
  'required': ['x'],
  'type': 'object'}
TOOL_NOTES = 'Length check is disabled (kwCompatibilityLength:0), so scalars and arrays of any length both pass. Only pure numeric values (int, float, or arrays thereof) return True; strings, None, and mixed-type collections return False.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.is_numeric
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
    def is_numeric(args: dict[str, Any] | None = None) -> Any:
        "Call this tool to check whether a value is numeric before passing it to a PsyNeuLink component that requires a numeric input (e.g., a mechanism's variable, a function's parameter, or a matrix entry)."
        return _impl(args or {})
