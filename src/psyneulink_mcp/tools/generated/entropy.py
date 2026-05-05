"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '5a308ea6d45af79435a872838607630672e8b99d94e135b62d63215644bf3ac0'
__pnl_qualname__ = 'psyneulink.Entropy'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_entropy'
TOOL_DESCRIPTION = 'Call this tool to instantiate an Entropy function that measures the Shannon entropy of a 1D activation array — use it when building a model that needs to quantify the disorder or uncertainty in a neural representation. The result is a scalar entropy value (optionally normalized by array length) suitable for assigning as the objective function of a mechanism or composition.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "default_variable": {\n      "description": "1D array specifying the shape and default values for the input over which entropy is calculated. Omit if using input_shapes instead.",\n      "items": {\n        "type": "number"\n      },\n      "type": "array"\n    },\n    "input_shapes": {\n      "description": "Length of the input array; alternative to default_variable. Initializes variable to zeros of this length. Error if both are given and input_shapes != len(default_variable).",\n      "type": "integer"\n    },\n    "matrix": {\n      "description": "Square recurrent weight matrix (list or 2D array) applied before entropy calculation. Defaults to INVERSE_HOLLOW_MATRIX (pass the string \'INVERSE_HOLLOW_MATRIX\' to use the default). Non-hollow matrices are convolved with HOLLOW_MATRIX to remove self-connections.",\n      "oneOf": [\n        {\n          "items": {\n            "items": {\n              "type": "number"\n            },\n            "type": "array"\n          },\n          "type": "array"\n        },\n        {\n          "type": "string"\n        }\n      ]\n    },\n    "name": {\n      "description": "Name for this Entropy function instance.",\n      "type": "string"\n    },\n    "normalize": {\n      "default": false,\n      "description": "If true, divides the computed entropy by the length of variable, yielding a value in [0, 1]. Default false.",\n      "type": "boolean"\n    },\n    "params": {\n      "additionalProperties": true,\n      "description": "Optional parameter dictionary overriding constructor arguments. Keys are parameter names, values override defaults.",\n      "type": "object"\n    },\n    "transfer_fct": {\n      "description": "Name of a PsyNeuLink transfer function to apply to the matrix output before computing entropy. Pass as a string identifier (e.g. \'Logistic\'). Omit if no pre-transform is needed.",\n      "type": "string"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\nThe matrix must be square with width equal to len(variable); mismatches raise an error at construction time. Passing matrix=None in Python uses INVERSE_HOLLOW_MATRIX as the default — to explicitly request the default via this tool, omit the matrix parameter entirely or pass the string \'INVERSE_HOLLOW_MATRIX\'. The metric is fixed to ENTROPY (hardcoded in __init__); there is no way to override it via params. owner and prefs are advanced PNL component-wiring arguments; omit them unless explicitly wiring the function into a larger PNL object graph. normalize=True is useful when comparing entropy across arrays of different lengths.'
TOOL_PARAMETERS = { 'properties': { 'default_variable': { 'description': '1D array specifying the shape '
                                                       'and default values for the '
                                                       'input over which entropy is '
                                                       'calculated. Omit if using '
                                                       'input_shapes instead.',
                                        'items': {'type': 'number'},
                                        'type': 'array'},
                  'input_shapes': { 'description': 'Length of the input array; '
                                                   'alternative to default_variable. '
                                                   'Initializes variable to zeros of '
                                                   'this length. Error if both are '
                                                   'given and input_shapes != '
                                                   'len(default_variable).',
                                    'type': 'integer'},
                  'matrix': { 'description': 'Square recurrent weight matrix (list or '
                                             '2D array) applied before entropy '
                                             'calculation. Defaults to '
                                             'INVERSE_HOLLOW_MATRIX (pass the string '
                                             "'INVERSE_HOLLOW_MATRIX' to use the "
                                             'default). Non-hollow matrices are '
                                             'convolved with HOLLOW_MATRIX to remove '
                                             'self-connections.',
                              'oneOf': [ { 'items': { 'items': {'type': 'number'},
                                                      'type': 'array'},
                                           'type': 'array'},
                                         {'type': 'string'}]},
                  'name': { 'description': 'Name for this Entropy function instance.',
                            'type': 'string'},
                  'normalize': { 'default': False,
                                 'description': 'If true, divides the computed entropy '
                                                'by the length of variable, yielding a '
                                                'value in [0, 1]. Default false.',
                                 'type': 'boolean'},
                  'params': { 'additionalProperties': True,
                              'description': 'Optional parameter dictionary overriding '
                                             'constructor arguments. Keys are '
                                             'parameter names, values override '
                                             'defaults.',
                              'type': 'object'},
                  'transfer_fct': { 'description': 'Name of a PsyNeuLink transfer '
                                                   'function to apply to the matrix '
                                                   'output before computing entropy. '
                                                   'Pass as a string identifier (e.g. '
                                                   "'Logistic'). Omit if no "
                                                   'pre-transform is needed.',
                                    'type': 'string'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = "The matrix must be square with width equal to len(variable); mismatches raise an error at construction time. Passing matrix=None in Python uses INVERSE_HOLLOW_MATRIX as the default — to explicitly request the default via this tool, omit the matrix parameter entirely or pass the string 'INVERSE_HOLLOW_MATRIX'. The metric is fixed to ENTROPY (hardcoded in __init__); there is no way to override it via params. owner and prefs are advanced PNL component-wiring arguments; omit them unless explicitly wiring the function into a larger PNL object graph. normalize=True is useful when comparing entropy across arrays of different lengths."


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.Entropy
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
    def create_entropy(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to instantiate an Entropy function that measures the Shannon entropy of a 1D activation array — use it when building a model that needs to quantify the disorder or uncertainty in a neural representation.'
        return _impl(args or {})
