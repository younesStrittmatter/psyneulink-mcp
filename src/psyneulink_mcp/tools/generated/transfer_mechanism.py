"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '6272239673b3bb6083202e3f9fee4ae09942dc4a63a9358153f2b78075ea5043'
__pnl_qualname__ = 'psyneulink.TransferMechanism'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_transfer_mechanism'
TOOL_DESCRIPTION = 'Call this tool to create a TransferMechanism — a processing node that applies a transfer function (default: Linear) to its input and returns the transformed result. Use it when building a PsyNeuLink Composition that needs a unit performing weighted input summation, activation functions (Logistic, ReLU, Tanh, etc.), optional temporal integration, and optional output clipping. The tool returns a TransferMechanism instance that can be wired into a Composition via MappingProjections.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "clip": {\n      "description": "Two-element [min, max] array clamping output values. E.g. [0.0, 1.0] clips to unit interval. Omit for no clipping.",\n      "items": {\n        "type": "number"\n      },\n      "maxItems": 2,\n      "minItems": 2,\n      "type": "array"\n    },\n    "function": {\n      "description": "Name of the transfer function class to apply, e.g. \'Linear\', \'Logistic\', \'ReLU\', \'Tanh\', \'SoftMax\'. Defaults to \'Linear\'.",\n      "type": "string"\n    },\n    "initial_value": {\n      "description": "Starting value for the integrator when integrator_mode is true. Must match the shape of the input variable. Omit to default to zeros.",\n      "items": {\n        "type": "number"\n      },\n      "type": "array"\n    },\n    "input_shapes": {\n      "description": "Dimensionality of the input (number of units). Use this instead of default_variable when you only need to set the size. E.g. 4 creates a 4-unit mechanism.",\n      "type": "integer"\n    },\n    "integration_rate": {\n      "default": 0.5,\n      "description": "Rate of integration when integrator_mode is true. 0 = no update, 1 = full replacement. Default: 0.5.",\n      "maximum": 1,\n      "minimum": 0,\n      "type": "number"\n    },\n    "integrator_function": {\n      "default": "AdaptiveIntegrator",\n      "description": "Name of the IntegratorFunction class to use when integrator_mode is true. Default: \'AdaptiveIntegrator\'.",\n      "type": "string"\n    },\n    "integrator_mode": {\n      "default": false,\n      "description": "If true, the mechanism integrates its input over time using integrator_function before applying the transfer function. Required to be true for integration_rate and initial_value to have effect. Default: false.",\n      "type": "boolean"\n    },\n    "name": {\n      "description": "Optional name for this mechanism. Defaults to \'TransferMechanism-N\'.",\n      "type": "string"\n    },\n    "noise": {\n      "description": "Scalar offset added to each element of the result each execution. Use 0.0 (default) for no noise; for stochastic noise use the report_tool_issue tool to request DistributionFunction support.",\n      "type": "number"\n    },\n    "on_resume_integrator_mode": {\n      "default": "CURRENT_VALUE",\n      "description": "Controls what value the integrator uses when integration resumes after being paused. Default: \'CURRENT_VALUE\'.",\n      "enum": [\n        "CURRENT_VALUE",\n        "LAST_INTEGRATED_VALUE",\n        "RESET"\n      ],\n      "type": "string"\n    },\n    "output_ports": {\n      "description": "Names of OutputPorts to create. Default [\'RESULTS\'] creates one output port per InputPort. Pass [\'RESULTS\', \'COMBINE\'] to also get an element-wise sum port.",\n      "items": {\n        "type": "string"\n      },\n      "type": "array"\n    },\n    "termination_comparison_op": {\n      "default": "<=",\n      "description": "Comparison operator used to test termination_measure_value against termination_threshold. Default: \'<=\'.",\n      "enum": [\n        "<",\n        "<=",\n        ">",\n        ">=",\n        "==",\n        "!="\n      ],\n      "type": "string"\n    },\n    "termination_threshold": {\n      "description": "When set (non-null), execution repeats until termination_measure falls within this threshold. Only meaningful when execute_until_finished is True on the Composition. Default: null (single pass).",\n      "type": "number"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\n- `integrator_mode`, `integration_rate`, `initial_value`, and `on_resume_integrator_mode` only have effect when `integrator_mode=true`; setting them without enabling integrator_mode silently has no effect at runtime.\n- `clip` must satisfy clip[0] < clip[1]; if either bound falls outside the function\'s output range after scale/offset, PNL emits a warning and ignores that bound.\n- `noise` type cannot be changed after construction: if constructed with a scalar you cannot later assign an array, and vice versa.\n- `integration_rate` must be in the closed interval [0, 1]; values outside this range raise a validation error.\n- When `input_shapes` > 1 (or the variable has multiple items), the default `output_ports=[\'RESULTS\']` is automatically expanded to one named port per input item (e.g. \'RESULT-0\', \'RESULT-1\', …), not a single \'RESULT\' port — this surprises agents expecting a single output.\n- `function` must be a TransferFunction or SelectionFunction subclass; passing an arbitrary Python function is supported only if its output shape matches its input shape.\n- `termination_threshold` is only evaluated when the owning Composition has `execute_until_finished=True`; without that flag, the mechanism always executes exactly once per trial regardless of threshold.\n- `termination_measure` is not exposed as a JSON-serializable parameter here because it requires a PNL Function instance (e.g. Distance); if you need a custom termination measure, file a tool issue.\n- The COMBINE standard output port (element-wise sum of all value items) is available by adding \'COMBINE\' to `output_ports`, but requires all input items to have the same dimensionality.'
TOOL_PARAMETERS = { 'properties': { 'clip': { 'description': 'Two-element [min, max] array clamping '
                                           'output values. E.g. [0.0, 1.0] clips to '
                                           'unit interval. Omit for no clipping.',
                            'items': {'type': 'number'},
                            'maxItems': 2,
                            'minItems': 2,
                            'type': 'array'},
                  'function': { 'description': 'Name of the transfer function class to '
                                               "apply, e.g. 'Linear', 'Logistic', "
                                               "'ReLU', 'Tanh', 'SoftMax'. Defaults to "
                                               "'Linear'.",
                                'type': 'string'},
                  'initial_value': { 'description': 'Starting value for the integrator '
                                                    'when integrator_mode is true. '
                                                    'Must match the shape of the input '
                                                    'variable. Omit to default to '
                                                    'zeros.',
                                     'items': {'type': 'number'},
                                     'type': 'array'},
                  'input_shapes': { 'description': 'Dimensionality of the input '
                                                   '(number of units). Use this '
                                                   'instead of default_variable when '
                                                   'you only need to set the size. '
                                                   'E.g. 4 creates a 4-unit mechanism.',
                                    'type': 'integer'},
                  'integration_rate': { 'default': 0.5,
                                        'description': 'Rate of integration when '
                                                       'integrator_mode is true. 0 = '
                                                       'no update, 1 = full '
                                                       'replacement. Default: 0.5.',
                                        'maximum': 1,
                                        'minimum': 0,
                                        'type': 'number'},
                  'integrator_function': { 'default': 'AdaptiveIntegrator',
                                           'description': 'Name of the '
                                                          'IntegratorFunction class to '
                                                          'use when integrator_mode is '
                                                          'true. Default: '
                                                          "'AdaptiveIntegrator'.",
                                           'type': 'string'},
                  'integrator_mode': { 'default': False,
                                       'description': 'If true, the mechanism '
                                                      'integrates its input over time '
                                                      'using integrator_function '
                                                      'before applying the transfer '
                                                      'function. Required to be true '
                                                      'for integration_rate and '
                                                      'initial_value to have effect. '
                                                      'Default: false.',
                                       'type': 'boolean'},
                  'name': { 'description': 'Optional name for this mechanism. Defaults '
                                           "to 'TransferMechanism-N'.",
                            'type': 'string'},
                  'noise': { 'description': 'Scalar offset added to each element of '
                                            'the result each execution. Use 0.0 '
                                            '(default) for no noise; for stochastic '
                                            'noise use the report_tool_issue tool to '
                                            'request DistributionFunction support.',
                             'type': 'number'},
                  'on_resume_integrator_mode': { 'default': 'CURRENT_VALUE',
                                                 'description': 'Controls what value '
                                                                'the integrator uses '
                                                                'when integration '
                                                                'resumes after being '
                                                                'paused. Default: '
                                                                "'CURRENT_VALUE'.",
                                                 'enum': [ 'CURRENT_VALUE',
                                                           'LAST_INTEGRATED_VALUE',
                                                           'RESET'],
                                                 'type': 'string'},
                  'output_ports': { 'description': 'Names of OutputPorts to create. '
                                                   "Default ['RESULTS'] creates one "
                                                   'output port per InputPort. Pass '
                                                   "['RESULTS', 'COMBINE'] to also get "
                                                   'an element-wise sum port.',
                                    'items': {'type': 'string'},
                                    'type': 'array'},
                  'termination_comparison_op': { 'default': '<=',
                                                 'description': 'Comparison operator '
                                                                'used to test '
                                                                'termination_measure_value '
                                                                'against '
                                                                'termination_threshold. '
                                                                "Default: '<='.",
                                                 'enum': [ '<',
                                                           '<=',
                                                           '>',
                                                           '>=',
                                                           '==',
                                                           '!='],
                                                 'type': 'string'},
                  'termination_threshold': { 'description': 'When set (non-null), '
                                                            'execution repeats until '
                                                            'termination_measure falls '
                                                            'within this threshold. '
                                                            'Only meaningful when '
                                                            'execute_until_finished is '
                                                            'True on the Composition. '
                                                            'Default: null (single '
                                                            'pass).',
                                             'type': 'number'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = "- `integrator_mode`, `integration_rate`, `initial_value`, and `on_resume_integrator_mode` only have effect when `integrator_mode=true`; setting them without enabling integrator_mode silently has no effect at runtime.\n- `clip` must satisfy clip[0] < clip[1]; if either bound falls outside the function's output range after scale/offset, PNL emits a warning and ignores that bound.\n- `noise` type cannot be changed after construction: if constructed with a scalar you cannot later assign an array, and vice versa.\n- `integration_rate` must be in the closed interval [0, 1]; values outside this range raise a validation error.\n- When `input_shapes` > 1 (or the variable has multiple items), the default `output_ports=['RESULTS']` is automatically expanded to one named port per input item (e.g. 'RESULT-0', 'RESULT-1', …), not a single 'RESULT' port — this surprises agents expecting a single output.\n- `function` must be a TransferFunction or SelectionFunction subclass; passing an arbitrary Python function is supported only if its output shape matches its input shape.\n- `termination_threshold` is only evaluated when the owning Composition has `execute_until_finished=True`; without that flag, the mechanism always executes exactly once per trial regardless of threshold.\n- `termination_measure` is not exposed as a JSON-serializable parameter here because it requires a PNL Function instance (e.g. Distance); if you need a custom termination measure, file a tool issue.\n- The COMBINE standard output port (element-wise sum of all value items) is available by adding 'COMBINE' to `output_ports`, but requires all input items to have the same dimensionality."


def _impl(**kwargs: Any) -> Any:
    target = pnl.TransferMechanism
    instance = target(**kwargs)
    return repr(instance)


def register(mcp: Any) -> None:
    @captured_tool(mcp, layer="generated", name=TOOL_NAME, description=TOOL_DESCRIPTION)
    def create_transfer_mechanism(**kwargs: Any) -> Any:
        'Call this tool to create a TransferMechanism — a processing node that applies a transfer function (default: Linear) to its input and returns the transformed result.'
        return _impl(**kwargs)
