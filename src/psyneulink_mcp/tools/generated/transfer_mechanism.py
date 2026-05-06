"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '5e251c67921a291bd9bc38725c6a38a8b4ff5438ce8f609ae14d47df83d81856'
__pnl_qualname__ = 'psyneulink.library.components.mechanisms.processing.transfer.recurrenttransfermechanism.TransferMechanism'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_transfer_mechanism'
TOOL_DESCRIPTION = 'Call this tool to create a `TransferMechanism` — the standard PsyNeuLink node that applies a transfer function (Linear, Logistic, ReLU, Tanh, SoftMax) to an input vector, with optional noise, output clipping, or leaky integration. Returns a handle string for use in Composition tools. All constructor arguments are passed as direct top-level properties of the input object — do NOT add an extra "args" wrapper key around them.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "clip": {\n      "description": "Two-element [min, max] pair clamping every output element. Omit for no clipping. First element must be less than the second.",\n      "items": {\n        "type": "number"\n      },\n      "maxItems": 2,\n      "minItems": 2,\n      "type": "array"\n    },\n    "default_variable": {\n      "description": "2-D list setting input shape and initial value, e.g. [[0,0,0]] for a single 3-element port. MUTUALLY EXCLUSIVE with input_shapes \\u2014 use one or the other, never both. Must be a list-of-lists; a flat list is rejected.",\n      "items": {\n        "items": {\n          "type": "number"\n        },\n        "type": "array"\n      },\n      "type": "array"\n    },\n    "function": {\n      "description": "Name of the transfer function: \'Linear\' (default), \'Logistic\', \'ReLU\', \'Tanh\', \'SoftMax\'. Must be a TransferFunction or SelectionFunction subclass name; an unrecognised string raises ComponentError.",\n      "type": "string"\n    },\n    "initial_value": {\n      "description": "2-D starting value for the integrator when integrator_mode is true. Must match the shape of default_variable (list-of-lists).",\n      "items": {\n        "items": {\n          "type": "number"\n        },\n        "type": "array"\n      },\n      "type": "array"\n    },\n    "input_shapes": {\n      "description": "Length of the input vector (e.g. 8 for an 8-element input port). MUTUALLY EXCLUSIVE with default_variable \\u2014 use one or the other, never both.",\n      "type": "integer"\n    },\n    "integration_rate": {\n      "default": 0.5,\n      "description": "Rate of integration in [0, 1] when integrator_mode is true. Higher values converge faster toward new input. Values outside [0, 1] raise a validation error.",\n      "type": "number"\n    },\n    "integrator_function": {\n      "default": "AdaptiveIntegrator",\n      "description": "Name of the IntegratorFunction subclass to use when integrator_mode is true, e.g. \'AdaptiveIntegrator\', \'SimpleIntegrator\'.",\n      "type": "string"\n    },\n    "integrator_mode": {\n      "default": false,\n      "description": "When true, input is first accumulated through integrator_function (leaky integration) before the transfer function is applied.",\n      "type": "boolean"\n    },\n    "name": {\n      "description": "Name for this mechanism; auto-assigned if omitted.",\n      "type": "string"\n    },\n    "noise": {\n      "default": 0,\n      "description": "Scalar offset added to the result on each execution. For per-execution random noise use a DistributionFunction (not expressible as a JSON number).",\n      "type": "number"\n    },\n    "on_resume_integrator_mode": {\n      "default": "CURRENT_VALUE",\n      "description": "Value the integrator uses when integration is resumed after being paused.",\n      "enum": [\n        "CURRENT_VALUE",\n        "LAST_INTEGRATED_VALUE",\n        "RESET"\n      ],\n      "type": "string"\n    },\n    "output_ports": {\n      "description": "Output port specifiers. Default [\'RESULTS\'] auto-generates one output per InputPort. Add \'COMBINE\' for an element-wise sum across all outputs.",\n      "items": {\n        "type": "string"\n      },\n      "type": "array"\n    },\n    "termination_comparison_op": {\n      "default": "<=",\n      "description": "Comparison operator applied between termination_measure_value and termination_threshold.",\n      "enum": [\n        "<",\n        "<=",\n        ">",\n        ">=",\n        "==",\n        "!="\n      ],\n      "type": "string"\n    },\n    "termination_threshold": {\n      "description": "When set, execution repeats until termination_measure_value satisfies this threshold (requires execute_until_finished=True on the Composition).",\n      "type": "number"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\nCRITICAL — all properties (name, function, default_variable, etc.) must be passed as direct top-level keys in the input object. Do NOT nest them under an extra "args" key. Wrong: {"args": {"name": "x"}}. Right: {"name": "x"}.\n\nCRITICAL — input_shapes and default_variable are mutually exclusive. Passing both raises ComponentError ("input_shapes and default_variable conflict"). Use input_shapes=N (integer) to specify vector length by size, or default_variable=[[0,...,0]] (2-D list) to specify shape by example. Never supply both in the same call.\n\ndefault_variable must be a 2-D list (list-of-lists), e.g. [[0, 0, 0]] for a single 3-element input port. A flat list like [0, 0, 0] is rejected at construction time.\n\nintegration_rate must be in [0, 1]; values outside this range raise a validation error.\n\nnoise type is fixed at construction time: if specified as a scalar, it cannot later be changed to an array, and vice versa.\n\nfunction must be the string name of a TransferFunction or SelectionFunction subclass (e.g. \'Linear\', \'Logistic\', \'ReLU\', \'Tanh\', \'SoftMax\'). Passing an unrecognised name raises ComponentError.'
TOOL_PARAMETERS = { 'properties': { 'clip': { 'description': 'Two-element [min, max] pair clamping every '
                                           'output element. Omit for no clipping. '
                                           'First element must be less than the '
                                           'second.',
                            'items': {'type': 'number'},
                            'maxItems': 2,
                            'minItems': 2,
                            'type': 'array'},
                  'default_variable': { 'description': '2-D list setting input shape '
                                                       'and initial value, e.g. '
                                                       '[[0,0,0]] for a single '
                                                       '3-element port. MUTUALLY '
                                                       'EXCLUSIVE with input_shapes — '
                                                       'use one or the other, never '
                                                       'both. Must be a list-of-lists; '
                                                       'a flat list is rejected.',
                                        'items': { 'items': {'type': 'number'},
                                                   'type': 'array'},
                                        'type': 'array'},
                  'function': { 'description': 'Name of the transfer function: '
                                               "'Linear' (default), 'Logistic', "
                                               "'ReLU', 'Tanh', 'SoftMax'. Must be a "
                                               'TransferFunction or SelectionFunction '
                                               'subclass name; an unrecognised string '
                                               'raises ComponentError.',
                                'type': 'string'},
                  'initial_value': { 'description': '2-D starting value for the '
                                                    'integrator when integrator_mode '
                                                    'is true. Must match the shape of '
                                                    'default_variable (list-of-lists).',
                                     'items': { 'items': {'type': 'number'},
                                                'type': 'array'},
                                     'type': 'array'},
                  'input_shapes': { 'description': 'Length of the input vector (e.g. 8 '
                                                   'for an 8-element input port). '
                                                   'MUTUALLY EXCLUSIVE with '
                                                   'default_variable — use one or the '
                                                   'other, never both.',
                                    'type': 'integer'},
                  'integration_rate': { 'default': 0.5,
                                        'description': 'Rate of integration in [0, 1] '
                                                       'when integrator_mode is true. '
                                                       'Higher values converge faster '
                                                       'toward new input. Values '
                                                       'outside [0, 1] raise a '
                                                       'validation error.',
                                        'type': 'number'},
                  'integrator_function': { 'default': 'AdaptiveIntegrator',
                                           'description': 'Name of the '
                                                          'IntegratorFunction subclass '
                                                          'to use when integrator_mode '
                                                          'is true, e.g. '
                                                          "'AdaptiveIntegrator', "
                                                          "'SimpleIntegrator'.",
                                           'type': 'string'},
                  'integrator_mode': { 'default': False,
                                       'description': 'When true, input is first '
                                                      'accumulated through '
                                                      'integrator_function (leaky '
                                                      'integration) before the '
                                                      'transfer function is applied.',
                                       'type': 'boolean'},
                  'name': { 'description': 'Name for this mechanism; auto-assigned if '
                                           'omitted.',
                            'type': 'string'},
                  'noise': { 'default': 0,
                             'description': 'Scalar offset added to the result on each '
                                            'execution. For per-execution random noise '
                                            'use a DistributionFunction (not '
                                            'expressible as a JSON number).',
                             'type': 'number'},
                  'on_resume_integrator_mode': { 'default': 'CURRENT_VALUE',
                                                 'description': 'Value the integrator '
                                                                'uses when integration '
                                                                'is resumed after '
                                                                'being paused.',
                                                 'enum': [ 'CURRENT_VALUE',
                                                           'LAST_INTEGRATED_VALUE',
                                                           'RESET'],
                                                 'type': 'string'},
                  'output_ports': { 'description': 'Output port specifiers. Default '
                                                   "['RESULTS'] auto-generates one "
                                                   'output per InputPort. Add '
                                                   "'COMBINE' for an element-wise sum "
                                                   'across all outputs.',
                                    'items': {'type': 'string'},
                                    'type': 'array'},
                  'termination_comparison_op': { 'default': '<=',
                                                 'description': 'Comparison operator '
                                                                'applied between '
                                                                'termination_measure_value '
                                                                'and '
                                                                'termination_threshold.',
                                                 'enum': [ '<',
                                                           '<=',
                                                           '>',
                                                           '>=',
                                                           '==',
                                                           '!='],
                                                 'type': 'string'},
                  'termination_threshold': { 'description': 'When set, execution '
                                                            'repeats until '
                                                            'termination_measure_value '
                                                            'satisfies this threshold '
                                                            '(requires '
                                                            'execute_until_finished=True '
                                                            'on the Composition).',
                                             'type': 'number'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = 'CRITICAL — all properties (name, function, default_variable, etc.) must be passed as direct top-level keys in the input object. Do NOT nest them under an extra "args" key. Wrong: {"args": {"name": "x"}}. Right: {"name": "x"}.\n\nCRITICAL — input_shapes and default_variable are mutually exclusive. Passing both raises ComponentError ("input_shapes and default_variable conflict"). Use input_shapes=N (integer) to specify vector length by size, or default_variable=[[0,...,0]] (2-D list) to specify shape by example. Never supply both in the same call.\n\ndefault_variable must be a 2-D list (list-of-lists), e.g. [[0, 0, 0]] for a single 3-element input port. A flat list like [0, 0, 0] is rejected at construction time.\n\nintegration_rate must be in [0, 1]; values outside this range raise a validation error.\n\nnoise type is fixed at construction time: if specified as a scalar, it cannot later be changed to an array, and vice versa.\n\nfunction must be the string name of a TransferFunction or SelectionFunction subclass (e.g. \'Linear\', \'Logistic\', \'ReLU\', \'Tanh\', \'SoftMax\'). Passing an unrecognised name raises ComponentError.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.TransferMechanism
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
    def create_transfer_mechanism(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to create a `TransferMechanism` — the standard PsyNeuLink node that applies a transfer function (Linear, Logistic, ReLU, Tanh, SoftMax) to an input vector, with optional noise, output clipping, or leaky integration.'
        return _impl(args or {})
