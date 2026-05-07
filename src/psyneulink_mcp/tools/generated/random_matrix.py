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
TOOL_DESCRIPTION = 'Call this tool to generate a 2D NumPy array of random floats for use as a weight matrix or connectivity pattern in PsyNeuLink models. Returns a (num_rows × num_cols) array with values drawn from a uniform distribution, optionally shifted and scaled — ready to pass as a `matrix` parameter to a MappingProjection or similar.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "num_cols": {\n      "description": "Number of columns in the output matrix.",\n      "type": "integer"\n    },\n    "num_rows": {\n      "description": "Number of rows in the output matrix.",\n      "type": "integer"\n    },\n    "offset": {\n      "default": 0,\n      "description": "Amount added to each random value before scaling. Pass \'zero_center\' (or \'ZERO_CENTER\') to use -0.5, which centers the distribution around 0.",\n      "oneOf": [\n        {\n          "type": "number"\n        },\n        {\n          "enum": [\n            "zero_center",\n            "ZERO_CENTER"\n          ],\n          "type": "string"\n        }\n      ]\n    },\n    "scale": {\n      "default": 1,\n      "description": "Multiplicative scale applied after the offset. Widens or narrows the value range.",\n      "type": "number"\n    }\n  },\n  "required": [\n    "num_rows",\n    "num_cols"\n  ],\n  "type": "object"\n}\n\nNotes:\nValues are drawn from np.random.rand (uniform [0, 1]) then transformed as (rand + offset) * scale. With defaults, output is in [0.0, 1.0]. Using offset=-0.5 / \'zero_center\' shifts the range to [-0.5, 0.5]; applying scale=2 further widens it to [-1.0, 1.0]. The docstring contains a typo: \'zero_center\' maps to -0.5, not -.05 as stated. Any offset string other than \'zero_center\' / \'ZERO_CENTER\' raises a UtilitiesError. There is no seed parameter — output is non-deterministic each call.'
TOOL_PARAMETERS = { 'properties': { 'num_cols': { 'description': 'Number of columns in the output '
                                               'matrix.',
                                'type': 'integer'},
                  'num_rows': { 'description': 'Number of rows in the output matrix.',
                                'type': 'integer'},
                  'offset': { 'default': 0,
                              'description': 'Amount added to each random value before '
                                             "scaling. Pass 'zero_center' (or "
                                             "'ZERO_CENTER') to use -0.5, which "
                                             'centers the distribution around 0.',
                              'oneOf': [ {'type': 'number'},
                                         { 'enum': ['zero_center', 'ZERO_CENTER'],
                                           'type': 'string'}]},
                  'scale': { 'default': 1,
                             'description': 'Multiplicative scale applied after the '
                                            'offset. Widens or narrows the value '
                                            'range.',
                             'type': 'number'}},
  'required': ['num_rows', 'num_cols'],
  'type': 'object'}
TOOL_NOTES = "Values are drawn from np.random.rand (uniform [0, 1]) then transformed as (rand + offset) * scale. With defaults, output is in [0.0, 1.0]. Using offset=-0.5 / 'zero_center' shifts the range to [-0.5, 0.5]; applying scale=2 further widens it to [-1.0, 1.0]. The docstring contains a typo: 'zero_center' maps to -0.5, not -.05 as stated. Any offset string other than 'zero_center' / 'ZERO_CENTER' raises a UtilitiesError. There is no seed parameter — output is non-deterministic each call."


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
        'Call this tool to generate a 2D NumPy array of random floats for use as a weight matrix or connectivity pattern in PsyNeuLink models.'
        return _impl(args or {})
