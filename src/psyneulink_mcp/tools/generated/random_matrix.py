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
TOOL_DESCRIPTION = 'Call this tool to generate a random 2D weight matrix for use as a connection matrix between PsyNeuLink mechanisms or projections. Returns a 2D numpy array of shape (num_rows, num_cols) where each entry is `(random_uniform[0,1) + offset) * scale`. Use when you need a randomized initial weight matrix rather than a fixed or identity matrix.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "num_cols": {\n      "description": "Number of columns in the output matrix; typically matches the size of the receiving layer.",\n      "type": "integer"\n    },\n    "num_rows": {\n      "description": "Number of rows in the output matrix; typically matches the size of the sending layer.",\n      "type": "integer"\n    },\n    "offset": {\n      "default": 0,\n      "description": "Amount added to each raw random value before scaling. Pass \'ZERO_CENTER\' (case-insensitive) as a shorthand for -0.5, which centers values around 0. Any other string raises an error.",\n      "oneOf": [\n        {\n          "type": "number"\n        },\n        {\n          "enum": [\n            "ZERO_CENTER",\n            "zero_center"\n          ],\n          "type": "string"\n        }\n      ]\n    },\n    "scale": {\n      "default": 1,\n      "description": "Multiplicative factor applied after offset. Use to widen or narrow the output range.",\n      "type": "number"\n    }\n  },\n  "required": [\n    "num_rows",\n    "num_cols"\n  ],\n  "type": "object"\n}\n\nNotes:\n- Raw random values are drawn from uniform [0, 1), so with defaults the output range is [0, 1).\n- \'ZERO_CENTER\' maps to offset=-0.5, giving an output range of [-0.5, 0.5) before scaling; note the docstring contains a typo (\'-.05\') but the source correctly uses -0.5.\n- Any string value for `offset` other than \'ZERO_CENTER\' (case-insensitive) raises a UtilitiesError at runtime.\n- The function uses `np.random.rand` with no seed control — results are non-deterministic. Set `np.random.seed` externally before calling if reproducibility is needed.\n- The returned array is a plain numpy ndarray, not a PsyNeuLink object; it can be passed directly to matrix parameters of projections or mechanisms.'
TOOL_PARAMETERS = { 'properties': { 'num_cols': { 'description': 'Number of columns in the output '
                                               'matrix; typically matches the size of '
                                               'the receiving layer.',
                                'type': 'integer'},
                  'num_rows': { 'description': 'Number of rows in the output matrix; '
                                               'typically matches the size of the '
                                               'sending layer.',
                                'type': 'integer'},
                  'offset': { 'default': 0,
                              'description': 'Amount added to each raw random value '
                                             "before scaling. Pass 'ZERO_CENTER' "
                                             '(case-insensitive) as a shorthand for '
                                             '-0.5, which centers values around 0. Any '
                                             'other string raises an error.',
                              'oneOf': [ {'type': 'number'},
                                         { 'enum': ['ZERO_CENTER', 'zero_center'],
                                           'type': 'string'}]},
                  'scale': { 'default': 1,
                             'description': 'Multiplicative factor applied after '
                                            'offset. Use to widen or narrow the output '
                                            'range.',
                             'type': 'number'}},
  'required': ['num_rows', 'num_cols'],
  'type': 'object'}
TOOL_NOTES = "- Raw random values are drawn from uniform [0, 1), so with defaults the output range is [0, 1).\n- 'ZERO_CENTER' maps to offset=-0.5, giving an output range of [-0.5, 0.5) before scaling; note the docstring contains a typo ('-.05') but the source correctly uses -0.5.\n- Any string value for `offset` other than 'ZERO_CENTER' (case-insensitive) raises a UtilitiesError at runtime.\n- The function uses `np.random.rand` with no seed control — results are non-deterministic. Set `np.random.seed` externally before calling if reproducibility is needed.\n- The returned array is a plain numpy ndarray, not a PsyNeuLink object; it can be passed directly to matrix parameters of projections or mechanisms."


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
        'Call this tool to generate a random 2D weight matrix for use as a connection matrix between PsyNeuLink mechanisms or projections.'
        return _impl(args or {})
