"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '6d28d897d60c870e594c9f86b4bd494f1eca58027f2e2bc93bd553518a011b97'
__pnl_qualname__ = 'psyneulink.RecurrentTransferMechanism'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_recurrent_transfer_mechanism'
TOOL_DESCRIPTION = 'Call this tool to instantiate a RecurrentTransferMechanism — a single-layer auto-recurrent network node whose output projects back to its own input via an AutoAssociativeProjection. Use it when building Hopfield-like attractor networks, leaky integrators with lateral inhibition, or any mechanism that needs recurrent self-excitation or mutual inhibition. Returns a RecurrentTransferMechanism instance ready to be added to a Composition.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "auto": {\n      "description": "Self-connection (diagonal) weights. A scalar applies the same weight to all units; a 1D array of length n sets each unit\'s self-weight individually. Takes precedence over the diagonal of matrix. Can be modified by ControlMechanism.",\n      "type": [\n        "number",\n        "array",\n        "null"\n      ]\n    },\n    "clip": {\n      "description": "Hard bounds [min, max] applied to output values after the transfer function.",\n      "items": {\n        "type": "number"\n      },\n      "maxItems": 2,\n      "minItems": 2,\n      "type": "array"\n    },\n    "combination_function": {\n      "description": "Function used to combine RECURRENT and EXTERNAL InputPorts when has_recurrent_input_port=True. Must accept a 2D array with two rows of equal length and return a 1D array of the same length. Default is LinearCombination (addition).",\n      "type": "string"\n    },\n    "enable_learning": {\n      "default": false,\n      "description": "If True, configures Hebbian learning on the recurrent projection at construction. If False (default), learning cannot be enabled later without calling configure_learning().",\n      "type": "boolean"\n    },\n    "function": {\n      "description": "Transfer function applied to each unit\'s net input (e.g., \'Logistic\', \'Linear\', \'ReLU\', \'Tanh\'). Defaults to Linear.",\n      "type": "string"\n    },\n    "has_recurrent_input_port": {\n      "default": false,\n      "description": "If True, the recurrent projection targets a separate RECURRENT InputPort; external input arrives at EXTERNAL InputPort; both are combined via combination_function before the transfer function. If False (default), recurrent projection feeds directly into the primary InputPort.",\n      "type": "boolean"\n    },\n    "hetero": {\n      "description": "Lateral (off-diagonal) connection weights. A scalar applies the same weight to all non-self connections; a 2D array of shape n\\u00d7n sets them individually (diagonal entries are zeroed). Takes precedence over the off-diagonal of matrix. Can be modified by ControlMechanism.",\n      "type": [\n        "number",\n        "array",\n        "null"\n      ]\n    },\n    "input_shapes": {\n      "description": "Number of units in the recurrent layer (determines both input and recurrent matrix size). E.g., 4 creates a 4-unit network with a 4x4 recurrent matrix.",\n      "type": "integer"\n    },\n    "integration_rate": {\n      "description": "Smoothing factor (0\\u20131) controlling integration speed when integrator_mode=True. 1.0 = no smoothing (instantaneous), 0.0 = no update. Default 0.5.",\n      "type": "number"\n    },\n    "integrator_mode": {\n      "default": false,\n      "description": "If True, input is integrated over time using integrator_function (AdaptiveIntegrator by default) before the transfer function is applied, making the mechanism a leaky integrator.",\n      "type": "boolean"\n    },\n    "learning_condition": {\n      "default": "UPDATE",\n      "description": "When the LearningMechanism executes: UPDATE runs after every execution of this mechanism; CONVERGENCE runs only when the termination_threshold is satisfied (WhenFinished condition). Default UPDATE.",\n      "enum": [\n        "UPDATE",\n        "CONVERGENCE"\n      ],\n      "type": "string"\n    },\n    "learning_function": {\n      "description": "Learning rule applied by the LearningMechanism (default \'Hebbian\'). Must accept a 1D activation array and return a square matrix of the same dimensionality. Only meaningful when enable_learning=True.",\n      "type": "string"\n    },\n    "learning_rate": {\n      "description": "Learning rate for the AutoAssociativeLearningMechanism. None uses the LearningMechanism framework default. Only meaningful when enable_learning=True.",\n      "type": [\n        "number",\n        "null"\n      ]\n    },\n    "matrix": {\n      "description": "Recurrent weight matrix. Default is \'HOLLOW_MATRIX\' (zeros on diagonal, ones off-diagonal). Accepts a 2D list/array or keyword strings (\'FULL_CONNECTIVITY_MATRIX\', \'IDENTITY_MATRIX\', etc.). Overridden by auto (diagonal) and/or hetero (off-diagonal) if those are specified.",\n      "type": [\n        "array",\n        "string"\n      ]\n    },\n    "name": {\n      "description": "Name for this mechanism instance.",\n      "type": "string"\n    },\n    "noise": {\n      "description": "Noise added to each unit\'s input. Scalar or array matching input_shapes.",\n      "type": [\n        "number",\n        "array"\n      ]\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\nMatrix/auto/hetero precedence rules are non-obvious and must be respected: (1) if all three are specified, matrix is silently ignored and the result is auto+hetero; (2) if auto+matrix are specified, diagonal comes from auto, off-diagonal from matrix; (3) if hetero+matrix are specified, diagonal from matrix, off-diagonal from hetero. The default matrix is HOLLOW_MATRIX (self-connections are zero, lateral connections are 1), not FULL_CONNECTIVITY_MATRIX — agents modeling purely excitatory self-connections need to set auto explicitly (e.g., auto=1). Learning is completely inert unless enable_learning=True at construction or configure_learning() is called afterward; attempting to set learning_enabled=True on an unconfigured instance only emits a warning and is silently ignored. The docstring incorrectly states learning_rate default is "False"; the Parameters class default is None — pass None to use the framework default rate. combination_function is only active when has_recurrent_input_port=True; setting it without that flag has no effect. ENERGY and ENTROPY are available as named output ports via standard_output_ports and can be added via output_ports kwarg. The recurrent projection feeds output back on the next execution step, not within the same step.'
TOOL_PARAMETERS = { 'properties': { 'auto': { 'description': 'Self-connection (diagonal) weights. A '
                                           'scalar applies the same weight to all '
                                           'units; a 1D array of length n sets each '
                                           "unit's self-weight individually. Takes "
                                           'precedence over the diagonal of matrix. '
                                           'Can be modified by ControlMechanism.',
                            'type': ['number', 'array', 'null']},
                  'clip': { 'description': 'Hard bounds [min, max] applied to output '
                                           'values after the transfer function.',
                            'items': {'type': 'number'},
                            'maxItems': 2,
                            'minItems': 2,
                            'type': 'array'},
                  'combination_function': { 'description': 'Function used to combine '
                                                           'RECURRENT and EXTERNAL '
                                                           'InputPorts when '
                                                           'has_recurrent_input_port=True. '
                                                           'Must accept a 2D array '
                                                           'with two rows of equal '
                                                           'length and return a 1D '
                                                           'array of the same length. '
                                                           'Default is '
                                                           'LinearCombination '
                                                           '(addition).',
                                            'type': 'string'},
                  'enable_learning': { 'default': False,
                                       'description': 'If True, configures Hebbian '
                                                      'learning on the recurrent '
                                                      'projection at construction. If '
                                                      'False (default), learning '
                                                      'cannot be enabled later without '
                                                      'calling configure_learning().',
                                       'type': 'boolean'},
                  'function': { 'description': 'Transfer function applied to each '
                                               "unit's net input (e.g., 'Logistic', "
                                               "'Linear', 'ReLU', 'Tanh'). Defaults to "
                                               'Linear.',
                                'type': 'string'},
                  'has_recurrent_input_port': { 'default': False,
                                                'description': 'If True, the recurrent '
                                                               'projection targets a '
                                                               'separate RECURRENT '
                                                               'InputPort; external '
                                                               'input arrives at '
                                                               'EXTERNAL InputPort; '
                                                               'both are combined via '
                                                               'combination_function '
                                                               'before the transfer '
                                                               'function. If False '
                                                               '(default), recurrent '
                                                               'projection feeds '
                                                               'directly into the '
                                                               'primary InputPort.',
                                                'type': 'boolean'},
                  'hetero': { 'description': 'Lateral (off-diagonal) connection '
                                             'weights. A scalar applies the same '
                                             'weight to all non-self connections; a 2D '
                                             'array of shape n×n sets them '
                                             'individually (diagonal entries are '
                                             'zeroed). Takes precedence over the '
                                             'off-diagonal of matrix. Can be modified '
                                             'by ControlMechanism.',
                              'type': ['number', 'array', 'null']},
                  'input_shapes': { 'description': 'Number of units in the recurrent '
                                                   'layer (determines both input and '
                                                   'recurrent matrix size). E.g., 4 '
                                                   'creates a 4-unit network with a '
                                                   '4x4 recurrent matrix.',
                                    'type': 'integer'},
                  'integration_rate': { 'description': 'Smoothing factor (0–1) '
                                                       'controlling integration speed '
                                                       'when integrator_mode=True. 1.0 '
                                                       '= no smoothing '
                                                       '(instantaneous), 0.0 = no '
                                                       'update. Default 0.5.',
                                        'type': 'number'},
                  'integrator_mode': { 'default': False,
                                       'description': 'If True, input is integrated '
                                                      'over time using '
                                                      'integrator_function '
                                                      '(AdaptiveIntegrator by default) '
                                                      'before the transfer function is '
                                                      'applied, making the mechanism a '
                                                      'leaky integrator.',
                                       'type': 'boolean'},
                  'learning_condition': { 'default': 'UPDATE',
                                          'description': 'When the LearningMechanism '
                                                         'executes: UPDATE runs after '
                                                         'every execution of this '
                                                         'mechanism; CONVERGENCE runs '
                                                         'only when the '
                                                         'termination_threshold is '
                                                         'satisfied (WhenFinished '
                                                         'condition). Default UPDATE.',
                                          'enum': ['UPDATE', 'CONVERGENCE'],
                                          'type': 'string'},
                  'learning_function': { 'description': 'Learning rule applied by the '
                                                        'LearningMechanism (default '
                                                        "'Hebbian'). Must accept a 1D "
                                                        'activation array and return a '
                                                        'square matrix of the same '
                                                        'dimensionality. Only '
                                                        'meaningful when '
                                                        'enable_learning=True.',
                                         'type': 'string'},
                  'learning_rate': { 'description': 'Learning rate for the '
                                                    'AutoAssociativeLearningMechanism. '
                                                    'None uses the LearningMechanism '
                                                    'framework default. Only '
                                                    'meaningful when '
                                                    'enable_learning=True.',
                                     'type': ['number', 'null']},
                  'matrix': { 'description': 'Recurrent weight matrix. Default is '
                                             "'HOLLOW_MATRIX' (zeros on diagonal, ones "
                                             'off-diagonal). Accepts a 2D list/array '
                                             'or keyword strings '
                                             "('FULL_CONNECTIVITY_MATRIX', "
                                             "'IDENTITY_MATRIX', etc.). Overridden by "
                                             'auto (diagonal) and/or hetero '
                                             '(off-diagonal) if those are specified.',
                              'type': ['array', 'string']},
                  'name': { 'description': 'Name for this mechanism instance.',
                            'type': 'string'},
                  'noise': { 'description': "Noise added to each unit's input. Scalar "
                                            'or array matching input_shapes.',
                             'type': ['number', 'array']}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = 'Matrix/auto/hetero precedence rules are non-obvious and must be respected: (1) if all three are specified, matrix is silently ignored and the result is auto+hetero; (2) if auto+matrix are specified, diagonal comes from auto, off-diagonal from matrix; (3) if hetero+matrix are specified, diagonal from matrix, off-diagonal from hetero. The default matrix is HOLLOW_MATRIX (self-connections are zero, lateral connections are 1), not FULL_CONNECTIVITY_MATRIX — agents modeling purely excitatory self-connections need to set auto explicitly (e.g., auto=1). Learning is completely inert unless enable_learning=True at construction or configure_learning() is called afterward; attempting to set learning_enabled=True on an unconfigured instance only emits a warning and is silently ignored. The docstring incorrectly states learning_rate default is "False"; the Parameters class default is None — pass None to use the framework default rate. combination_function is only active when has_recurrent_input_port=True; setting it without that flag has no effect. ENERGY and ENTROPY are available as named output ports via standard_output_ports and can be added via output_ports kwarg. The recurrent projection feeds output back on the next execution step, not within the same step.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.RecurrentTransferMechanism
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
    def create_recurrent_transfer_mechanism(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to instantiate a RecurrentTransferMechanism — a single-layer auto-recurrent network node whose output projects back to its own input via an AutoAssociativeProjection.'
        return _impl(args or {})
