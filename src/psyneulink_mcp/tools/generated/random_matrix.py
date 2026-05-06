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
TOOL_DESCRIPTION = 'Call this tool to generate a random 2D weight matrix for use as a connection matrix between PsyNeuLink mechanisms or as input to other numeric operations. Returns a 2D numpy array of shape (num_rows, num_cols) with values drawn from (random[0,1] + offset) * scale — by default, uniform floats in [0, 1].\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "num_cols": {\n      "description": "Number of columns in the output matrix.",\n      "type": "integer"\n    },\n    "num_rows": {\n      "description": "Number of rows in the output matrix.",\n      "type": "integer"\n    },\n    "offset": {\n      "default": 0,\n      "description": "Amount added to each random value before scaling. Use -0.5 (or the string \'ZERO_CENTER\') to center values around 0. Defaults to 0.0.",\n      "oneOf": [\n        {\n          "type": "number"\n        },\n        {\n          "enum": [\n            "ZERO_CENTER",\n            "zero_center"\n          ],\n          "type": "string"\n        }\n      ]\n    },\n    "scale": {\n      "default": 1,\n      "description": "Multiplicative scale applied after offset. Use values > 1 to widen the range, < 1 to narrow it. Defaults to 1.0.",\n      "type": "number"\n    }\n  },\n  "required": [\n    "num_rows",\n    "num_cols"\n  ],\n  "type": "object"\n}\n\nNotes:\nThe \'ZERO_CENTER\' convenience string sets offset to exactly -0.5 (not -0.05 as the docstring typo suggests). Any other string value for offset raises a UtilitiesError. The returned numpy array is not serializable as JSON directly — callers that need to pass it onward should convert to a nested list (e.g., `.tolist()`) if JSON transport is required.'
TOOL_PARAMETERS = { 'properties': { 'num_cols': { 'description': 'Number of columns in the output '
                                               'matrix.',
                                'type': 'integer'},
                  'num_rows': { 'description': 'Number of rows in the output matrix.',
                                'type': 'integer'},
                  'offset': { 'default': 0,
                              'description': 'Amount added to each random value before '
                                             'scaling. Use -0.5 (or the string '
                                             "'ZERO_CENTER') to center values around "
                                             '0. Defaults to 0.0.',
                              'oneOf': [ {'type': 'number'},
                                         { 'enum': ['ZERO_CENTER', 'zero_center'],
                                           'type': 'string'}]},
                  'scale': { 'default': 1,
                             'description': 'Multiplicative scale applied after '
                                            'offset. Use values > 1 to widen the '
                                            'range, < 1 to narrow it. Defaults to 1.0.',
                             'type': 'number'}},
  'required': ['num_rows', 'num_cols'],
  'type': 'object'}
TOOL_NOTES = "The 'ZERO_CENTER' convenience string sets offset to exactly -0.5 (not -0.05 as the docstring typo suggests). Any other string value for offset raises a UtilitiesError. The returned numpy array is not serializable as JSON directly — callers that need to pass it onward should convert to a nested list (e.g., `.tolist()`) if JSON transport is required."


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
        'Call this tool to generate a random 2D weight matrix for use as a connection matrix between PsyNeuLink mechanisms or as input to other numeric operations.'
        return _impl(args or {})
