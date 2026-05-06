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
TOOL_DESCRIPTION = 'Call this tool when you need to initialize a random 2D weight matrix for use as a connection matrix or parameter in a PsyNeuLink model. It returns a 2D numpy array of shape (num_rows, num_cols) where each element is (random_uniform[0,1) + offset) * scale — by default, values are in [0, 1). Use offset and scale to shift or stretch the value range before passing the matrix to a mechanism or projection.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "num_cols": {\n      "description": "Number of columns in the output matrix.",\n      "type": "integer"\n    },\n    "num_rows": {\n      "description": "Number of rows in the output matrix.",\n      "type": "integer"\n    },\n    "offset": {\n      "default": 0,\n      "description": "Value added to each random entry before scaling. Pass \'ZERO_CENTER\' (case-insensitive) as a shorthand for -0.5, which centers the range on 0. Any other string raises an error.",\n      "oneOf": [\n        {\n          "type": "number"\n        },\n        {\n          "enum": [\n            "ZERO_CENTER",\n            "zero_center"\n          ],\n          "type": "string"\n        }\n      ]\n    },\n    "scale": {\n      "default": 1,\n      "description": "Multiplicative factor applied after the offset shift. Narrows (< 1) or widens (> 1) the value range.",\n      "type": "number"\n    }\n  },\n  "required": [\n    "num_rows",\n    "num_cols"\n  ],\n  "type": "object"\n}\n\nNotes:\nThe \'ZERO_CENTER\' string is case-insensitive in the source (checked via .upper()), so \'zero_center\', \'Zero_Center\', etc. all work. The docstring incorrectly states it maps to -.05; the actual source maps it to -0.5. With ZERO_CENTER and default scale=1.0, values are in [-0.5, 0.5). Any string other than \'ZERO_CENTER\' (case-insensitive) raises UtilitiesError.'
TOOL_PARAMETERS = { 'properties': { 'num_cols': { 'description': 'Number of columns in the output '
                                               'matrix.',
                                'type': 'integer'},
                  'num_rows': { 'description': 'Number of rows in the output matrix.',
                                'type': 'integer'},
                  'offset': { 'default': 0,
                              'description': 'Value added to each random entry before '
                                             "scaling. Pass 'ZERO_CENTER' "
                                             '(case-insensitive) as a shorthand for '
                                             '-0.5, which centers the range on 0. Any '
                                             'other string raises an error.',
                              'oneOf': [ {'type': 'number'},
                                         { 'enum': ['ZERO_CENTER', 'zero_center'],
                                           'type': 'string'}]},
                  'scale': { 'default': 1,
                             'description': 'Multiplicative factor applied after the '
                                            'offset shift. Narrows (< 1) or widens (> '
                                            '1) the value range.',
                             'type': 'number'}},
  'required': ['num_rows', 'num_cols'],
  'type': 'object'}
TOOL_NOTES = "The 'ZERO_CENTER' string is case-insensitive in the source (checked via .upper()), so 'zero_center', 'Zero_Center', etc. all work. The docstring incorrectly states it maps to -.05; the actual source maps it to -0.5. With ZERO_CENTER and default scale=1.0, values are in [-0.5, 0.5). Any string other than 'ZERO_CENTER' (case-insensitive) raises UtilitiesError."


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
        'Call this tool when you need to initialize a random 2D weight matrix for use as a connection matrix or parameter in a PsyNeuLink model.'
        return _impl(args or {})
