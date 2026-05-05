"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = 'd774fb7bff4daa055bb8e45d2acf77b5a79ef69ed43ea86e069a8c2a6a3772e6'
__pnl_qualname__ = 'psyneulink.LearningMechanism'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_learning_mechanism'
TOOL_DESCRIPTION = 'Use this tool to explicitly instantiate a LearningMechanism that computes weight updates (learning_signal) and backpropagated error (error_signal) for a MappingProjection. Call this only when you need low-level control over learning; in most workflows, Composition\'s `add_backpropagation_learning_pathway` auto-creates LearningMechanisms for you. The result is a LearningMechanism object whose outputs — ERROR_SIGNAL and one or more LearningSignals — drive weight changes in learned MappingProjections.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "covariates_sources": {\n      "description": "InputPort(s) of the output_source Mechanism other than the one receiving the primary_learned_projection. Used when the output activation function takes more than one argument affecting its derivative (e.g., softmax with multiple inputs). Provide as a single InputPort or list.",\n      "type": "string"\n    },\n    "error_sources": {\n      "description": "Source(s) of the error signal. For single-layer learning or the final layer, must be a ComparatorMechanism or its ERROR_SIGNAL OutputPort. For hidden layers in multilayer learning, must be another LearningMechanism or its ERROR_SIGNAL OutputPort. Can be a single object or a list.",\n      "type": "string"\n    },\n    "function": {\n      "default": "BackPropagation",\n      "description": "Learning function used to compute learning_signal and error_signal. Default is BackPropagation. Must accept (input, output, error) as positional args and optionally a \'covariates\' keyword. Examples: \'BackPropagation\', \'Kohonen\', \'Hebbian\', \'TDLearning\'.",\n      "type": "string"\n    },\n    "learning_enabled": {\n      "default": "True",\n      "description": "Controls when LearningProjections execute. \'True\'/\'ONLINE\': update weights each time the mechanism runs. \'AFTER\': update weights at end of each TRIAL. \'False\': never update weights (mechanism still runs to propagate error signals upstream).",\n      "enum": [\n        "True",\n        "False",\n        "ONLINE",\n        "AFTER"\n      ],\n      "type": "string"\n    },\n    "learning_rate": {\n      "description": "Scalar learning rate passed to the learning function. Overrides any rate set in the function itself. If None, the function\'s own default is used.",\n      "type": "number"\n    },\n    "learning_signals": {\n      "description": "Specifies which MappingProjection matrix parameters to train. Each item can be a Projection, ParameterPort, tuple (name, Projection), or dict. Defaults to a single LEARNING_SIGNAL targeting the primary_learned_projection.",\n      "items": {\n        "type": "string"\n      },\n      "type": "array"\n    },\n    "modulation": {\n      "default": "ADDITIVE",\n      "description": "Default modulation type applied by all LearningSignals unless individually overridden. Typically \'ADDITIVE\' (weight += learning_signal) or \'MULTIPLICATIVE\'.",\n      "type": "string"\n    },\n    "name": {\n      "description": "Optional name for the LearningMechanism instance.",\n      "type": "string"\n    },\n    "variable": {\n      "description": "2d array with at least 3 items: [activation_input, activation_output, error_signal]. Each item must be a 1d numeric list or array. Additional items for extra error signals or covariates are appended after the first three.",\n      "items": {\n        "items": {\n          "type": "number"\n        },\n        "type": "array"\n      },\n      "type": "array"\n    }\n  },\n  "required": [\n    "variable",\n    "error_sources"\n  ],\n  "type": "object"\n}\n\nNotes:\n- LearningMechanism is almost always created automatically by Composition learning pathway methods (e.g., add_backpropagation_learning_pathway). Instantiating one manually outside a Composition triggers a runtime warning and requires careful wiring of Projections.\n- `variable` must have exactly 3 items at minimum: [ACTIVATION_INPUT, ACTIVATION_OUTPUT, ERROR_SIGNAL]; if there are multiple error_sources, additional ERROR_SIGNAL entries are appended; COVARIATES entries follow those.\n- `error_sources` and `covariates_sources` cannot be expressed as plain JSON strings at runtime — they must be live PNL objects (Mechanisms, OutputPorts, InputPorts). Pass them by name/reference in the composed PNL graph context.\n- `learning_enabled=False` disables weight updates but the mechanism STILL EXECUTES, so error signals continue to propagate to earlier layers — do not remove it from the Composition to pause learning.\n- The default function is BackPropagation, which assumes a Logistic activation derivative unless the receiving Mechanism\'s function provides its own derivative.\n- `error_matrices` are set automatically from the error_sources\' learned projections; for ObjectiveMechanism error sources they default to an identity matrix of the appropriate size.\n- `modulation` defaults to ADDITIVE (weights are incremented by learning_signal), which is the standard gradient-descent update rule.'
TOOL_PARAMETERS = { 'properties': { 'covariates_sources': { 'description': 'InputPort(s) of the '
                                                         'output_source Mechanism '
                                                         'other than the one receiving '
                                                         'the '
                                                         'primary_learned_projection. '
                                                         'Used when the output '
                                                         'activation function takes '
                                                         'more than one argument '
                                                         'affecting its derivative '
                                                         '(e.g., softmax with multiple '
                                                         'inputs). Provide as a single '
                                                         'InputPort or list.',
                                          'type': 'string'},
                  'error_sources': { 'description': 'Source(s) of the error signal. '
                                                    'For single-layer learning or the '
                                                    'final layer, must be a '
                                                    'ComparatorMechanism or its '
                                                    'ERROR_SIGNAL OutputPort. For '
                                                    'hidden layers in multilayer '
                                                    'learning, must be another '
                                                    'LearningMechanism or its '
                                                    'ERROR_SIGNAL OutputPort. Can be a '
                                                    'single object or a list.',
                                     'type': 'string'},
                  'function': { 'default': 'BackPropagation',
                                'description': 'Learning function used to compute '
                                               'learning_signal and error_signal. '
                                               'Default is BackPropagation. Must '
                                               'accept (input, output, error) as '
                                               'positional args and optionally a '
                                               "'covariates' keyword. Examples: "
                                               "'BackPropagation', 'Kohonen', "
                                               "'Hebbian', 'TDLearning'.",
                                'type': 'string'},
                  'learning_enabled': { 'default': 'True',
                                        'description': 'Controls when '
                                                       'LearningProjections execute. '
                                                       "'True'/'ONLINE': update "
                                                       'weights each time the '
                                                       "mechanism runs. 'AFTER': "
                                                       'update weights at end of each '
                                                       "TRIAL. 'False': never update "
                                                       'weights (mechanism still runs '
                                                       'to propagate error signals '
                                                       'upstream).',
                                        'enum': ['True', 'False', 'ONLINE', 'AFTER'],
                                        'type': 'string'},
                  'learning_rate': { 'description': 'Scalar learning rate passed to '
                                                    'the learning function. Overrides '
                                                    'any rate set in the function '
                                                    "itself. If None, the function's "
                                                    'own default is used.',
                                     'type': 'number'},
                  'learning_signals': { 'description': 'Specifies which '
                                                       'MappingProjection matrix '
                                                       'parameters to train. Each item '
                                                       'can be a Projection, '
                                                       'ParameterPort, tuple (name, '
                                                       'Projection), or dict. Defaults '
                                                       'to a single LEARNING_SIGNAL '
                                                       'targeting the '
                                                       'primary_learned_projection.',
                                        'items': {'type': 'string'},
                                        'type': 'array'},
                  'modulation': { 'default': 'ADDITIVE',
                                  'description': 'Default modulation type applied by '
                                                 'all LearningSignals unless '
                                                 'individually overridden. Typically '
                                                 "'ADDITIVE' (weight += "
                                                 'learning_signal) or '
                                                 "'MULTIPLICATIVE'.",
                                  'type': 'string'},
                  'name': { 'description': 'Optional name for the LearningMechanism '
                                           'instance.',
                            'type': 'string'},
                  'variable': { 'description': '2d array with at least 3 items: '
                                               '[activation_input, activation_output, '
                                               'error_signal]. Each item must be a 1d '
                                               'numeric list or array. Additional '
                                               'items for extra error signals or '
                                               'covariates are appended after the '
                                               'first three.',
                                'items': {'items': {'type': 'number'}, 'type': 'array'},
                                'type': 'array'}},
  'required': ['variable', 'error_sources'],
  'type': 'object'}
TOOL_NOTES = "- LearningMechanism is almost always created automatically by Composition learning pathway methods (e.g., add_backpropagation_learning_pathway). Instantiating one manually outside a Composition triggers a runtime warning and requires careful wiring of Projections.\n- `variable` must have exactly 3 items at minimum: [ACTIVATION_INPUT, ACTIVATION_OUTPUT, ERROR_SIGNAL]; if there are multiple error_sources, additional ERROR_SIGNAL entries are appended; COVARIATES entries follow those.\n- `error_sources` and `covariates_sources` cannot be expressed as plain JSON strings at runtime — they must be live PNL objects (Mechanisms, OutputPorts, InputPorts). Pass them by name/reference in the composed PNL graph context.\n- `learning_enabled=False` disables weight updates but the mechanism STILL EXECUTES, so error signals continue to propagate to earlier layers — do not remove it from the Composition to pause learning.\n- The default function is BackPropagation, which assumes a Logistic activation derivative unless the receiving Mechanism's function provides its own derivative.\n- `error_matrices` are set automatically from the error_sources' learned projections; for ObjectiveMechanism error sources they default to an identity matrix of the appropriate size.\n- `modulation` defaults to ADDITIVE (weights are incremented by learning_signal), which is the standard gradient-descent update rule."


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.LearningMechanism
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
    def create_learning_mechanism(args: dict[str, Any] | None = None) -> Any:
        'Use this tool to explicitly instantiate a LearningMechanism that computes weight updates (learning_signal) and backpropagated error (error_signal) for a MappingProjection.'
        return _impl(args or {})
