"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '693113c1f62e17a3448260c393b6613a50f95a30efec54ad8e2573ff58d7e06c'
__pnl_qualname__ = 'psyneulink.random_matrix'
__pnl_kind__ = 'function'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'random_matrix'
TOOL_DESCRIPTION = 'Call this tool when you need to initialize a weight matrix with random values for use as a MappingProjection matrix or any PsyNeuLink component that accepts a 2D array. Returns a 2D numpy array of shape (num_rows, num_cols) where each element is drawn from Uniform(0,1) shifted by offset and scaled by scale.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "num_cols": {\n      "description": "Number of columns in the output matrix (typically the size of the receiving layer).",\n      "type": "integer"\n    },\n    "num_rows": {\n      "description": "Number of rows in the output matrix (typically the size of the sending layer).",\n      "type": "integer"\n    },\n    "offset": {\n      "default": 0,\n      "description": "Value added to each random entry before scaling. Pass -0.5 or the string \'ZERO_CENTER\' to center values around 0. Defaults to 0.0, giving values in [0, 1].",\n      "oneOf": [\n        {\n          "type": "number"\n        },\n        {\n          "enum": [\n            "ZERO_CENTER",\n            "zero_center"\n          ],\n          "type": "string"\n        }\n      ]\n    },\n    "scale": {\n      "default": 1,\n      "description": "Multiplier applied after offset. Use values < 1 to compress range, > 1 to expand it.",\n      "type": "number"\n    }\n  },\n  "required": [\n    "num_rows",\n    "num_cols"\n  ],\n  "type": "object"\n}\n\nNotes:\nThe string \'ZERO_CENTER\' (case-insensitive) is treated as offset=-0.5, producing values in [-0.5, 0.5] before scaling. Any other string raises an error. With defaults (offset=0.0, scale=1.0), values are in [0.0, 1.0]. The result is a numpy array, not a Python list — downstream PNL components accept it directly as a matrix argument.'
TOOL_PARAMETERS = { 'properties': { 'num_cols': { 'description': 'Number of columns in the output matrix '
                                               '(typically the size of the receiving '
                                               'layer).',
                                'type': 'integer'},
                  'num_rows': { 'description': 'Number of rows in the output matrix '
                                               '(typically the size of the sending '
                                               'layer).',
                                'type': 'integer'},
                  'offset': { 'default': 0,
                              'description': 'Value added to each random entry before '
                                             'scaling. Pass -0.5 or the string '
                                             "'ZERO_CENTER' to center values around 0. "
                                             'Defaults to 0.0, giving values in [0, '
                                             '1].',
                              'oneOf': [ {'type': 'number'},
                                         { 'enum': ['ZERO_CENTER', 'zero_center'],
                                           'type': 'string'}]},
                  'scale': { 'default': 1,
                             'description': 'Multiplier applied after offset. Use '
                                            'values < 1 to compress range, > 1 to '
                                            'expand it.',
                             'type': 'number'}},
  'required': ['num_rows', 'num_cols'],
  'type': 'object'}
TOOL_NOTES = "The string 'ZERO_CENTER' (case-insensitive) is treated as offset=-0.5, producing values in [-0.5, 0.5] before scaling. Any other string raises an error. With defaults (offset=0.0, scale=1.0), values are in [0.0, 1.0]. The result is a numpy array, not a Python list — downstream PNL components accept it directly as a matrix argument."


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.random_matrix
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
    def random_matrix(args: dict[str, Any] | None = None) -> Any:
        'Call this tool when you need to initialize a weight matrix with random values for use as a MappingProjection matrix or any PsyNeuLink component that accepts a 2D array.'
        return _impl(args or {})
