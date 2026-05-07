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
TOOL_DESCRIPTION = 'Call this tool to generate a 2D numpy array of random floats with a specified shape, useful for initializing weight matrices in PsyNeuLink Mechanisms and Projections. Returns a (num_rows × num_cols) numpy array where each entry equals (rand[0,1) + offset) * scale.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "num_cols": {\n      "description": "Number of columns in the output matrix.",\n      "type": "integer"\n    },\n    "num_rows": {\n      "description": "Number of rows in the output matrix.",\n      "type": "integer"\n    },\n    "offset": {\n      "default": 0,\n      "description": "Amount added to each random value before scaling. Pass \'zero_center\' (case-insensitive) as a convenience for -0.5, which centers values around 0. Any other string raises an error.",\n      "oneOf": [\n        {\n          "type": "number"\n        },\n        {\n          "enum": [\n            "zero_center",\n            "ZERO_CENTER"\n          ],\n          "type": "string"\n        }\n      ]\n    },\n    "scale": {\n      "default": 1,\n      "description": "Multiplicative scale applied after offset. Values > 1 widen the range; values < 1 narrow it.",\n      "type": "number"\n    }\n  },\n  "required": [\n    "num_rows",\n    "num_cols"\n  ],\n  "type": "object"\n}\n\nNotes:\nThe docstring contains a typo stating \'ZERO_CENTER\' = -.05; the actual source sets offset = -0.5 (negative one-half), producing values in [-0.5, 0.5) before scaling. The string comparison is case-insensitive so both \'zero_center\' and \'ZERO_CENTER\' are accepted. Any other string value for offset raises a UtilitiesError. The function uses np.random.rand (uniform [0,1)), not np.random.randn (normal), so output is always uniformly distributed.'
TOOL_PARAMETERS = { 'properties': { 'num_cols': { 'description': 'Number of columns in the output '
                                               'matrix.',
                                'type': 'integer'},
                  'num_rows': { 'description': 'Number of rows in the output matrix.',
                                'type': 'integer'},
                  'offset': { 'default': 0,
                              'description': 'Amount added to each random value before '
                                             "scaling. Pass 'zero_center' "
                                             '(case-insensitive) as a convenience for '
                                             '-0.5, which centers values around 0. Any '
                                             'other string raises an error.',
                              'oneOf': [ {'type': 'number'},
                                         { 'enum': ['zero_center', 'ZERO_CENTER'],
                                           'type': 'string'}]},
                  'scale': { 'default': 1,
                             'description': 'Multiplicative scale applied after '
                                            'offset. Values > 1 widen the range; '
                                            'values < 1 narrow it.',
                             'type': 'number'}},
  'required': ['num_rows', 'num_cols'],
  'type': 'object'}
TOOL_NOTES = "The docstring contains a typo stating 'ZERO_CENTER' = -.05; the actual source sets offset = -0.5 (negative one-half), producing values in [-0.5, 0.5) before scaling. The string comparison is case-insensitive so both 'zero_center' and 'ZERO_CENTER' are accepted. Any other string value for offset raises a UtilitiesError. The function uses np.random.rand (uniform [0,1)), not np.random.randn (normal), so output is always uniformly distributed."


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
        'Call this tool to generate a 2D numpy array of random floats with a specified shape, useful for initializing weight matrices in PsyNeuLink Mechanisms and Projections.'
        return _impl(args or {})
