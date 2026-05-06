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
TOOL_DESCRIPTION = 'Call this tool when you need to generate a random 2D weight matrix for initializing a PsyNeuLink Projection or Mechanism parameter. Returns a 2D numpy array of shape (num_rows × num_cols) where each entry is (uniform_random[0,1] + offset) * scale — by default, floats uniformly distributed in [0, 1].\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "num_cols": {\n      "description": "Number of columns in the output matrix (e.g., size of the receiving layer).",\n      "type": "integer"\n    },\n    "num_rows": {\n      "description": "Number of rows in the output matrix (e.g., size of the sending layer).",\n      "type": "integer"\n    },\n    "offset": {\n      "default": 0,\n      "description": "Amount added to each random value before scaling. Use -0.5 or the string \'zero_center\' to center values around 0 (range [-0.5, 0.5] before scaling). Any other string raises an error.",\n      "oneOf": [\n        {\n          "type": "number"\n        },\n        {\n          "enum": [\n            "zero_center",\n            "ZERO_CENTER"\n          ],\n          "type": "string"\n        }\n      ]\n    },\n    "scale": {\n      "default": 1,\n      "description": "Multiplicative factor applied after offset. Use values > 1 to widen the range, < 1 to narrow it.",\n      "type": "number"\n    }\n  },\n  "required": [\n    "num_rows",\n    "num_cols"\n  ],\n  "type": "object"\n}\n\nNotes:\nThe docstring incorrectly states \'ZERO_CENTER\' maps to -0.05; the source code maps it to -0.5. Trust the source: \'zero_center\' → offset = -0.5, producing values in roughly [-0.5, 0.5] before scaling. The string comparison is case-insensitive (offset.upper() == \'ZERO_CENTER\'). Any other string value for offset raises UtilitiesError. The return value is a numpy ndarray, not a Python list — pass it directly as a matrix argument to PsyNeuLink components.'
TOOL_PARAMETERS = { 'properties': { 'num_cols': { 'description': 'Number of columns in the output matrix '
                                               '(e.g., size of the receiving layer).',
                                'type': 'integer'},
                  'num_rows': { 'description': 'Number of rows in the output matrix '
                                               '(e.g., size of the sending layer).',
                                'type': 'integer'},
                  'offset': { 'default': 0,
                              'description': 'Amount added to each random value before '
                                             'scaling. Use -0.5 or the string '
                                             "'zero_center' to center values around 0 "
                                             '(range [-0.5, 0.5] before scaling). Any '
                                             'other string raises an error.',
                              'oneOf': [ {'type': 'number'},
                                         { 'enum': ['zero_center', 'ZERO_CENTER'],
                                           'type': 'string'}]},
                  'scale': { 'default': 1,
                             'description': 'Multiplicative factor applied after '
                                            'offset. Use values > 1 to widen the '
                                            'range, < 1 to narrow it.',
                             'type': 'number'}},
  'required': ['num_rows', 'num_cols'],
  'type': 'object'}
TOOL_NOTES = "The docstring incorrectly states 'ZERO_CENTER' maps to -0.05; the source code maps it to -0.5. Trust the source: 'zero_center' → offset = -0.5, producing values in roughly [-0.5, 0.5] before scaling. The string comparison is case-insensitive (offset.upper() == 'ZERO_CENTER'). Any other string value for offset raises UtilitiesError. The return value is a numpy ndarray, not a Python list — pass it directly as a matrix argument to PsyNeuLink components."


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
        'Call this tool when you need to generate a random 2D weight matrix for initializing a PsyNeuLink Projection or Mechanism parameter.'
        return _impl(args or {})
