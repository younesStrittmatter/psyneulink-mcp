"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = 'b6ac68b92748809b40aa5782b77dbbc41fd17e3970c88d1c7e8d915903f948bc'
__pnl_qualname__ = 'psyneulink.array_from_matrix_string'
__pnl_kind__ = 'function'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'array_from_matrix_string'
TOOL_DESCRIPTION = 'Call this tool when you have a matrix represented as a human-readable string (e.g., \'1 2; 3 4\') and need to convert it to a numpy array for use in PsyNeuLink weight matrices, projections, or other numeric computations. Returns a 2D numpy ndarray with the specified dtype.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "col_sep": {\n      "default": " ",\n      "description": "Separator character between columns within a row. Defaults to a single space \' \'.",\n      "type": "string"\n    },\n    "dtype": {\n      "default": "float",\n      "description": "NumPy dtype for the result array, as a string such as \'float\', \'int\', \'float32\', \'complex\'. Defaults to \'float\'.",\n      "type": "string"\n    },\n    "row_sep": {\n      "default": ";",\n      "description": "Separator character between rows. Defaults to \';\'.",\n      "type": "string"\n    },\n    "s": {\n      "description": "Matrix descriptor string, e.g. \'1 2; 3 4\' for a 2x2 matrix.",\n      "type": "string"\n    }\n  },\n  "required": [\n    "s"\n  ],\n  "type": "object"\n}\n\nNotes:\nEmpty column tokens are silently filtered, so extra spaces between values in a row are harmless. The dtype parameter is a numpy DTypeLike at runtime — pass common dtype name strings (\'float\', \'int\', \'float32\', etc.) rather than Python type objects, since JSON cannot represent type objects. If row or column separators appear inside values, parsing will break silently; choose separators that do not conflict with element content. The function does not validate that all rows have the same length — a ragged string will produce a numpy object array rather than raising an error.'
TOOL_PARAMETERS = { 'properties': { 'col_sep': { 'default': ' ',
                               'description': 'Separator character between columns '
                                              'within a row. Defaults to a single '
                                              "space ' '.",
                               'type': 'string'},
                  'dtype': { 'default': 'float',
                             'description': 'NumPy dtype for the result array, as a '
                                            "string such as 'float', 'int', 'float32', "
                                            "'complex'. Defaults to 'float'.",
                             'type': 'string'},
                  'row_sep': { 'default': ';',
                               'description': 'Separator character between rows. '
                                              "Defaults to ';'.",
                               'type': 'string'},
                  's': { 'description': "Matrix descriptor string, e.g. '1 2; 3 4' for "
                                        'a 2x2 matrix.',
                         'type': 'string'}},
  'required': ['s'],
  'type': 'object'}
TOOL_NOTES = "Empty column tokens are silently filtered, so extra spaces between values in a row are harmless. The dtype parameter is a numpy DTypeLike at runtime — pass common dtype name strings ('float', 'int', 'float32', etc.) rather than Python type objects, since JSON cannot represent type objects. If row or column separators appear inside values, parsing will break silently; choose separators that do not conflict with element content. The function does not validate that all rows have the same length — a ragged string will produce a numpy object array rather than raising an error."


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.array_from_matrix_string
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
    def array_from_matrix_string(args: dict[str, Any] | None = None) -> Any:
        "Call this tool when you have a matrix represented as a human-readable string (e.g., '1 2; 3 4') and need to convert it to a numpy array for use in PsyNeuLink weight matrices, projections, or other numeric computations."
        return _impl(args or {})
