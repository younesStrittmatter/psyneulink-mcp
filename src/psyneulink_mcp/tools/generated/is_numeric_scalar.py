"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '37d0e4ece713a0ea2cb227591959506aebdb6268b17287681f5e83cab102ea67'
__pnl_qualname__ = 'psyneulink.core.components.functions.nonstateful.learningfunctions.is_numeric_scalar'
__pnl_kind__ = 'function'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'is_numeric_scalar'
TOOL_DESCRIPTION = 'Call this tool to check whether a value qualifies as a numeric scalar — i.e., a Python number or a 0-dimensional numpy array with an integer or float dtype. Returns a boolean: True if the value is a numeric scalar, False otherwise. Use it before passing a value to PsyNeuLink APIs that require a single numeric quantity.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "obj": {\n      "description": "The value to test. Can be a Python number (int, float, complex, etc.) or a numpy array. Other types will return False.",\n      "type": [\n        "number",\n        "boolean",\n        "integer",\n        "string",\n        "array",\n        "object"\n      ]\n    }\n  },\n  "required": [\n    "obj"\n  ],\n  "type": "object"\n}\n\nNotes:\nA 0-dimensional numpy array (np.array(3.14)) is considered a numeric scalar only if its dtype kind is \'i\' (integer) or \'f\' (float) — complex arrays (\'c\' kind) return False. Python\'s numbers.Number subclasses (int, float, Decimal, Fraction) return True. A 1-element 1-D array (e.g., np.array([3.14])) returns False because ndim==1, not 0. JSON does not have a native numpy type; if passing a numpy scalar over MCP, send it as a plain Python number.'
TOOL_PARAMETERS = { 'properties': { 'obj': { 'description': 'The value to test. Can be a Python number '
                                          '(int, float, complex, etc.) or a numpy '
                                          'array. Other types will return False.',
                           'type': [ 'number',
                                     'boolean',
                                     'integer',
                                     'string',
                                     'array',
                                     'object']}},
  'required': ['obj'],
  'type': 'object'}
TOOL_NOTES = "A 0-dimensional numpy array (np.array(3.14)) is considered a numeric scalar only if its dtype kind is 'i' (integer) or 'f' (float) — complex arrays ('c' kind) return False. Python's numbers.Number subclasses (int, float, Decimal, Fraction) return True. A 1-element 1-D array (e.g., np.array([3.14])) returns False because ndim==1, not 0. JSON does not have a native numpy type; if passing a numpy scalar over MCP, send it as a plain Python number."


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.is_numeric_scalar
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
    def is_numeric_scalar(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to check whether a value qualifies as a numeric scalar — i.e., a Python number or a 0-dimensional numpy array with an integer or float dtype.'
        return _impl(args or {})
