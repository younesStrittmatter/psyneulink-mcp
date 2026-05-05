"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '24996d0d4f2c2552ac13becf96ce7090f23081a7617eb03a6a82e42051f18bca'
__pnl_qualname__ = 'psyneulink.Hebbian'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_hebbian'
TOOL_DESCRIPTION = 'Call this tool to create a Hebbian learning function that computes a 2D weight-change matrix from a 1D activation vector using the correlational (Hebbian) rule: Δw_ij = learning_rate * a_i * a_j for i≠j, 0 on the diagonal. Use it when you need an autoassociative, unsupervised weight update — e.g., as the learning_function of a LearningMechanism or AutoAssociativeProjection. The result is a hollow (zero-diagonal) 2D array of the same rank as the outer product of the input.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "default_variable": {\n      "description": "1D array of activation values whose pairwise products form the weight-change matrix. Must have at least 2 elements; must not be 2D.",\n      "items": {\n        "type": "number"\n      },\n      "type": "array"\n    },\n    "learning_rate": {\n      "description": "Scales the weight-change matrix. Scalar: multiplied by the full matrix. 1D array: applied element-wise to the activation variable before the outer product. 2D array: applied element-wise to the resulting weight-change matrix. Defaults to 0.05 if omitted.",\n      "oneOf": [\n        {\n          "type": "number"\n        },\n        {\n          "items": {\n            "type": "number"\n          },\n          "type": "array"\n        },\n        {\n          "items": {\n            "items": {\n              "type": "number"\n            },\n            "type": "array"\n          },\n          "type": "array"\n        }\n      ]\n    },\n    "name": {\n      "description": "Optional name for this function instance.",\n      "type": "string"\n    },\n    "params": {\n      "description": "Optional parameter dictionary; values here override constructor arguments.",\n      "type": "object"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\n- `default_variable` must be a strictly 1D numeric array with ≥2 elements; a scalar raises ComponentError and a 2D+ array raises ComponentError.\n- Default learning_rate is 0.05, not None — omitting it silently applies 0.05.\n- The dimensionality of learning_rate changes HOW it is applied: 1D scales the variable before the outer product (not the matrix), while scalar or 2D scales the resulting matrix directly. This means a 1D learning_rate is NOT equivalent to a scalar with the same values.\n- The output matrix always has zeros on the diagonal regardless of learning_rate (hollow matrix).\n- `owner` is set automatically when attached to a Mechanism; do not pass it manually via the MCP tool.'
TOOL_PARAMETERS = { 'properties': { 'default_variable': { 'description': '1D array of activation values '
                                                       'whose pairwise products form '
                                                       'the weight-change matrix. Must '
                                                       'have at least 2 elements; must '
                                                       'not be 2D.',
                                        'items': {'type': 'number'},
                                        'type': 'array'},
                  'learning_rate': { 'description': 'Scales the weight-change matrix. '
                                                    'Scalar: multiplied by the full '
                                                    'matrix. 1D array: applied '
                                                    'element-wise to the activation '
                                                    'variable before the outer '
                                                    'product. 2D array: applied '
                                                    'element-wise to the resulting '
                                                    'weight-change matrix. Defaults to '
                                                    '0.05 if omitted.',
                                     'oneOf': [ {'type': 'number'},
                                                { 'items': {'type': 'number'},
                                                  'type': 'array'},
                                                { 'items': { 'items': { 'type': 'number'},
                                                             'type': 'array'},
                                                  'type': 'array'}]},
                  'name': { 'description': 'Optional name for this function instance.',
                            'type': 'string'},
                  'params': { 'description': 'Optional parameter dictionary; values '
                                             'here override constructor arguments.',
                              'type': 'object'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = '- `default_variable` must be a strictly 1D numeric array with ≥2 elements; a scalar raises ComponentError and a 2D+ array raises ComponentError.\n- Default learning_rate is 0.05, not None — omitting it silently applies 0.05.\n- The dimensionality of learning_rate changes HOW it is applied: 1D scales the variable before the outer product (not the matrix), while scalar or 2D scales the resulting matrix directly. This means a 1D learning_rate is NOT equivalent to a scalar with the same values.\n- The output matrix always has zeros on the diagonal regardless of learning_rate (hollow matrix).\n- `owner` is set automatically when attached to a Mechanism; do not pass it manually via the MCP tool.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.Hebbian
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
    def create_hebbian(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to create a Hebbian learning function that computes a 2D weight-change matrix from a 1D activation vector using the correlational (Hebbian) rule: Δw_ij = learning_rate * a_i * a_j for i≠j, 0 on the diagonal.'
        return _impl(args or {})
