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
__pnl_parents__ = []
__pnl_parent_sha256s__ = {}
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'random_matrix'
TOOL_DESCRIPTION = 'Call this tool to generate a 2D matrix of random float values with a specified shape, offset, and scale — for use as a weight matrix, input pattern, or any context requiring a random numpy array. Returns a 2D numpy array with shape (num_rows, num_cols) where each entry is (random_uniform[0,1] + offset) * scale.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "num_cols": {\n      "description": "Number of columns in the output matrix.",\n      "type": "integer"\n    },\n    "num_rows": {\n      "description": "Number of rows in the output matrix.",\n      "type": "integer"\n    },\n    "offset": {\n      "description": "Added to each random value before scaling. Pass the string \'zero_center\' (case-insensitive) as a shorthand for -0.5, which centers the default [0,1] range on 0. Otherwise pass a float. Default is 0.0.",\n      "oneOf": [\n        {\n          "type": "number"\n        },\n        {\n          "enum": [\n            "zero_center",\n            "ZERO_CENTER"\n          ],\n          "type": "string"\n        }\n      ]\n    },\n    "scale": {\n      "description": "Multiplicative factor applied after adding the offset. Widens or narrows the output range. Default is 1.0.",\n      "type": "number"\n    }\n  },\n  "required": [\n    "num_rows",\n    "num_cols"\n  ],\n  "type": "object"\n}\n\nNotes:\nThe docstring contains a typo: it says \'ZERO_CENTER\' is shorthand for -.05, but the source code sets offset = -0.5. The actual behavior is -0.5. With defaults (offset=0.0, scale=1.0), values are uniform floats in [0, 1). To get values in [-0.5, 0.5), use offset=-0.5 or offset=\'zero_center\'. Any string value for offset other than \'zero_center\' (case-insensitive) raises a UtilitiesError.'
TOOL_PARAMETERS = { 'properties': { 'num_cols': { 'description': 'Number of columns in the output '
                                               'matrix.',
                                'type': 'integer'},
                  'num_rows': { 'description': 'Number of rows in the output matrix.',
                                'type': 'integer'},
                  'offset': { 'description': 'Added to each random value before '
                                             "scaling. Pass the string 'zero_center' "
                                             '(case-insensitive) as a shorthand for '
                                             '-0.5, which centers the default [0,1] '
                                             'range on 0. Otherwise pass a float. '
                                             'Default is 0.0.',
                              'oneOf': [ {'type': 'number'},
                                         { 'enum': ['zero_center', 'ZERO_CENTER'],
                                           'type': 'string'}]},
                  'scale': { 'description': 'Multiplicative factor applied after '
                                            'adding the offset. Widens or narrows the '
                                            'output range. Default is 1.0.',
                             'type': 'number'}},
  'required': ['num_rows', 'num_cols'],
  'type': 'object'}
TOOL_NOTES = "The docstring contains a typo: it says 'ZERO_CENTER' is shorthand for -.05, but the source code sets offset = -0.5. The actual behavior is -0.5. With defaults (offset=0.0, scale=1.0), values are uniform floats in [0, 1). To get values in [-0.5, 0.5), use offset=-0.5 or offset='zero_center'. Any string value for offset other than 'zero_center' (case-insensitive) raises a UtilitiesError."


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
        'Call this tool to generate a 2D matrix of random float values with a specified shape, offset, and scale — for use as a weight matrix, input pattern, or any context requiring a random numpy array.'
        return _impl(args or {})
