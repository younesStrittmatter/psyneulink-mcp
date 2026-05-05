"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '6ca3e702938a0103b497e44786709f5f4ecacc19162e05e4a710ca0d96bcf39b'
__pnl_qualname__ = 'psyneulink.Kohonen'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_kohonen'
TOOL_DESCRIPTION = 'Call this tool to instantiate a Kohonen (self-organizing map) learning function that computes a matrix of weight changes using the Kohonen/SOM learning rule. Use it when building a KohonenMechanism or any autoassociative network where weights should be updated based on proximity to the winning unit. The result is a 2D weight-change matrix scaled by input-weight differences and distance from the best-matching unit.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "distance_function": {\n      "default": "gaussian",\n      "description": "Method for computing each unit\'s distance from the winning (best-matching) unit. \'gaussian\' (default) gives a bell-curve neighbourhood; \'linear\' gives a linearly decaying neighbourhood; \'exponential\' gives an exponentially decaying neighbourhood.",\n      "enum": [\n        "gaussian",\n        "linear",\n        "exponential"\n      ],\n      "type": "string"\n    },\n    "learning_rate": {\n      "default": 0.05,\n      "description": "Scales the weight-change matrix. Scalar multiplies the whole matrix; 1d array applies elementwise to variable before computing changes; 2d array applies elementwise to the final weight-change matrix. Defaults to 0.05 if not set here or on the owning LearningMechanism.",\n      "type": "number"\n    },\n    "name": {\n      "description": "Name for this Kohonen function instance.",\n      "type": "string"\n    },\n    "params": {\n      "additionalProperties": true,\n      "description": "Optional parameter dictionary overriding constructor arguments. Keys are PsyNeuLink parameter keywords; values override the corresponding arguments.",\n      "type": "object"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\n- `variable` at call time must be a 3-element list: [input_pattern (1d), activity_array (1d), weight_matrix (2d square)]. All three must share the same length N, and the matrix must be N×N. Passing mismatched shapes raises FunctionError.\n- The activity array (variable[1]) is assumed to be the dot product of the input pattern and the weight matrix — the unit with the highest activity is treated as the best-matching unit (BMU).\n- The constructor parameter is `distance_function`, not `distance_measure` (the docstring header uses `distance_measure` but the actual argument is `distance_function`).\n- A custom callable can be passed as `distance_function` at the Python level, but this tool only exposes the three named string options; pass such callables via `params` if needed.\n- If `learning_rate` is a 1d array it is applied to `variable` before computing distances, not to the final matrix — this can produce a different magnitude than a scalar with the same values.'
TOOL_PARAMETERS = { 'properties': { 'distance_function': { 'default': 'gaussian',
                                         'description': 'Method for computing each '
                                                        "unit's distance from the "
                                                        'winning (best-matching) unit. '
                                                        "'gaussian' (default) gives a "
                                                        'bell-curve neighbourhood; '
                                                        "'linear' gives a linearly "
                                                        'decaying neighbourhood; '
                                                        "'exponential' gives an "
                                                        'exponentially decaying '
                                                        'neighbourhood.',
                                         'enum': ['gaussian', 'linear', 'exponential'],
                                         'type': 'string'},
                  'learning_rate': { 'default': 0.05,
                                     'description': 'Scales the weight-change matrix. '
                                                    'Scalar multiplies the whole '
                                                    'matrix; 1d array applies '
                                                    'elementwise to variable before '
                                                    'computing changes; 2d array '
                                                    'applies elementwise to the final '
                                                    'weight-change matrix. Defaults to '
                                                    '0.05 if not set here or on the '
                                                    'owning LearningMechanism.',
                                     'type': 'number'},
                  'name': { 'description': 'Name for this Kohonen function instance.',
                            'type': 'string'},
                  'params': { 'additionalProperties': True,
                              'description': 'Optional parameter dictionary overriding '
                                             'constructor arguments. Keys are '
                                             'PsyNeuLink parameter keywords; values '
                                             'override the corresponding arguments.',
                              'type': 'object'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = '- `variable` at call time must be a 3-element list: [input_pattern (1d), activity_array (1d), weight_matrix (2d square)]. All three must share the same length N, and the matrix must be N×N. Passing mismatched shapes raises FunctionError.\n- The activity array (variable[1]) is assumed to be the dot product of the input pattern and the weight matrix — the unit with the highest activity is treated as the best-matching unit (BMU).\n- The constructor parameter is `distance_function`, not `distance_measure` (the docstring header uses `distance_measure` but the actual argument is `distance_function`).\n- A custom callable can be passed as `distance_function` at the Python level, but this tool only exposes the three named string options; pass such callables via `params` if needed.\n- If `learning_rate` is a 1d array it is applied to `variable` before computing distances, not to the final matrix — this can produce a different magnitude than a scalar with the same values.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.Kohonen
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
    def create_kohonen(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to instantiate a Kohonen (self-organizing map) learning function that computes a matrix of weight changes using the Kohonen/SOM learning rule.'
        return _impl(args or {})
