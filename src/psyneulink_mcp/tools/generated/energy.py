"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '2daa2ec3232cf0c6d177e1c7738c9b6160e6572e8b8ecc3a4eccc2aa80671408'
__pnl_qualname__ = 'psyneulink.Energy'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_energy'
TOOL_DESCRIPTION = 'Call this tool to create an Energy function that computes the Hopfield-style energy of a 1D array using a recurrent weight matrix. Use it when you need to measure the stability or attractor state of a network — lower energy indicates a more stable state. Returns a scalar energy value (optionally normalized by array length).\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "default_variable": {\n      "description": "1D array specifying shape and default values for the input over which energy is calculated. Mutually exclusive with input_shapes.",\n      "items": {\n        "type": "number"\n      },\n      "type": "array"\n    },\n    "input_shapes": {\n      "description": "Length of the input array; zero-initializes the variable. Use instead of default_variable when only the size matters. Raises an error if both are given and disagree.",\n      "type": "integer"\n    },\n    "matrix": {\n      "description": "Square recurrent weight matrix (list or 2D array) with width equal to len(variable). Defaults to INVERSE_HOLLOW_MATRIX. Non-hollow matrices are convolved with HOLLOW_MATRIX to strip self-connections before the energy calculation.",\n      "oneOf": [\n        {\n          "items": {\n            "items": {\n              "type": "number"\n            },\n            "type": "array"\n          },\n          "type": "array"\n        },\n        {\n          "description": "PsyNeuLink matrix keyword, e.g. \'INVERSE_HOLLOW_MATRIX\'",\n          "type": "string"\n        }\n      ]\n    },\n    "normalize": {\n      "description": "If true, divides the energy result by the length of variable, producing a per-element average. Default false.",\n      "type": "boolean"\n    },\n    "params": {\n      "description": "Optional parameter dictionary overriding constructor arguments. Keys are parameter keyword strings.",\n      "type": "object"\n    },\n    "transfer_fct": {\n      "description": "Name of a PsyNeuLink function applied to the matrix output before computing energy (e.g. \'Logistic\'). Omit for no transformation.",\n      "type": "string"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\nThe metric is fixed to ENERGY internally — do not attempt to pass a `metric` argument. The `matrix` default is INVERSE_HOLLOW_MATRIX (off-diagonal elements = -1), which is the standard Hopfield energy weight structure; passing a full matrix silently masks the diagonal via convolution with HOLLOW_MATRIX. `owner` and `prefs` are component-level wiring arguments rarely needed by agents; omit unless attaching this function to a specific PsyNeuLink Component. `input_shapes` is the runtime name for what the docstring calls `size` — use `input_shapes`, not `size`, in the constructor call.'
TOOL_PARAMETERS = { 'properties': { 'default_variable': { 'description': '1D array specifying shape and '
                                                       'default values for the input '
                                                       'over which energy is '
                                                       'calculated. Mutually exclusive '
                                                       'with input_shapes.',
                                        'items': {'type': 'number'},
                                        'type': 'array'},
                  'input_shapes': { 'description': 'Length of the input array; '
                                                   'zero-initializes the variable. Use '
                                                   'instead of default_variable when '
                                                   'only the size matters. Raises an '
                                                   'error if both are given and '
                                                   'disagree.',
                                    'type': 'integer'},
                  'matrix': { 'description': 'Square recurrent weight matrix (list or '
                                             '2D array) with width equal to '
                                             'len(variable). Defaults to '
                                             'INVERSE_HOLLOW_MATRIX. Non-hollow '
                                             'matrices are convolved with '
                                             'HOLLOW_MATRIX to strip self-connections '
                                             'before the energy calculation.',
                              'oneOf': [ { 'items': { 'items': {'type': 'number'},
                                                      'type': 'array'},
                                           'type': 'array'},
                                         { 'description': 'PsyNeuLink matrix keyword, '
                                                          'e.g. '
                                                          "'INVERSE_HOLLOW_MATRIX'",
                                           'type': 'string'}]},
                  'normalize': { 'description': 'If true, divides the energy result by '
                                                'the length of variable, producing a '
                                                'per-element average. Default false.',
                                 'type': 'boolean'},
                  'params': { 'description': 'Optional parameter dictionary overriding '
                                             'constructor arguments. Keys are '
                                             'parameter keyword strings.',
                              'type': 'object'},
                  'transfer_fct': { 'description': 'Name of a PsyNeuLink function '
                                                   'applied to the matrix output '
                                                   'before computing energy (e.g. '
                                                   "'Logistic'). Omit for no "
                                                   'transformation.',
                                    'type': 'string'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = 'The metric is fixed to ENERGY internally — do not attempt to pass a `metric` argument. The `matrix` default is INVERSE_HOLLOW_MATRIX (off-diagonal elements = -1), which is the standard Hopfield energy weight structure; passing a full matrix silently masks the diagonal via convolution with HOLLOW_MATRIX. `owner` and `prefs` are component-level wiring arguments rarely needed by agents; omit unless attaching this function to a specific PsyNeuLink Component. `input_shapes` is the runtime name for what the docstring calls `size` — use `input_shapes`, not `size`, in the constructor call.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.Energy
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
    def create_energy(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to create an Energy function that computes the Hopfield-style energy of a 1D array using a recurrent weight matrix.'
        return _impl(args or {})
