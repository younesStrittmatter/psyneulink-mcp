"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '5e251c67921a291bd9bc38725c6a38a8b4ff5438ce8f609ae14d47df83d81856'
__pnl_qualname__ = 'psyneulink.TransferMechanism'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_transfer_mechanism'
TOOL_DESCRIPTION = 'Call this tool to create a TransferMechanism — the standard building block for a processing node in a PsyNeuLink Composition that applies a transfer function (e.g., Linear, Logistic, ReLU) to its input. Use it when you need a feedforward unit, optionally with leaky integration over time (set integrator_mode=True). Returns a TransferMechanism instance ready to be added to a Composition via add_node.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "clip": {\n      "description": "Two-element [min, max] range to clamp output values; null items disable that bound. E.g., [0.0, 1.0].",\n      "items": {\n        "type": "number"\n      },\n      "maxItems": 2,\n      "minItems": 2,\n      "type": "array"\n    },\n    "default_variable": {\n      "description": "Sets the shape of the input. E.g., [0.0, 0.0] for a 2-element input. Ignored if input_shapes is provided.",\n      "items": {\n        "type": "number"\n      },\n      "type": "array"\n    },\n    "function": {\n      "description": "Transfer function to apply to input. Common values: \'Linear\', \'Logistic\', \'ReLU\', \'Tanh\', \'SoftMax\'. Defaults to Linear if omitted.",\n      "type": "string"\n    },\n    "initial_value": {\n      "description": "Starting value for the integrator when integrator_mode=True. Must match the shape of default_variable. Defaults to zeros.",\n      "items": {\n        "type": "number"\n      },\n      "type": "array"\n    },\n    "input_shapes": {\n      "description": "Scalar shorthand for default_variable size; e.g., 3 creates a 3-element input vector.",\n      "type": "integer"\n    },\n    "integration_rate": {\n      "default": 0.5,\n      "description": "Rate of integration in [0, 1] when integrator_mode=True. Higher = faster integration toward current input. Default 0.5.",\n      "maximum": 1,\n      "minimum": 0,\n      "type": "number"\n    },\n    "integrator_function": {\n      "default": "AdaptiveIntegrator",\n      "description": "Integrator function class name used when integrator_mode=True. Default \'AdaptiveIntegrator\'.",\n      "type": "string"\n    },\n    "integrator_mode": {\n      "default": false,\n      "description": "If true, input is integrated via integrator_function before passing to the transfer function, producing leaky integration. Default false.",\n      "type": "boolean"\n    },\n    "name": {\n      "description": "Name for the mechanism; auto-assigned if omitted.",\n      "type": "string"\n    },\n    "noise": {\n      "default": 0,\n      "description": "Constant offset added to the output (integrator_mode=False) or passed to the integrator function as noise (integrator_mode=True). Default 0.0.",\n      "type": "number"\n    },\n    "on_resume_integrator_mode": {\n      "default": "CURRENT_VALUE",\n      "description": "How to initialize the integrator when resuming integration: \'CURRENT_VALUE\' (default), \'LAST_INTEGRATED_VALUE\', or \'RESET\'.",\n      "enum": [\n        "CURRENT_VALUE",\n        "LAST_INTEGRATED_VALUE",\n        "RESET"\n      ],\n      "type": "string"\n    },\n    "output_ports": {\n      "description": "Output port specifications. Default [\'RESULTS\'] generates one output per input port. Use [\'COMBINE\'] for a single summed output across all input ports.",\n      "items": {\n        "type": "string"\n      },\n      "type": "array"\n    },\n    "termination_comparison_op": {\n      "default": "<=",\n      "description": "Comparison operator used to test termination: \'<\', \'<=\', \'>\', \'>=\', \'==\', \'!=\'. Default \'<=\'.",\n      "enum": [\n        "<",\n        "<=",\n        ">",\n        ">=",\n        "==",\n        "!="\n      ],\n      "type": "string"\n    },\n    "termination_threshold": {\n      "description": "If set, execution repeats until termination_measure falls below (or satisfies termination_comparison_op against) this value. Only effective when execute_until_finished is True.",\n      "type": "number"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\n- The noise parameter type (scalar vs. array) is fixed at construction: if you pass a float, you cannot later change it to an array, and vice versa.\n- integration_rate must be in [0, 1]; passing a value outside this range raises a validation error.\n- clip must satisfy clip[0] < clip[1]; if a clip bound is outside the function\'s output range after scale/offset, a warning is issued and that bound is silently ignored.\n- When integrator_mode=False (default), noise is added to the transfer function output directly. When integrator_mode=True, noise is forwarded to the integrator_function, not added afterward.\n- output_ports defaults to [\'RESULTS\'], which auto-generates one OutputPort per InputPort. If you specify multiple input_ports, this creates RESULT-0, RESULT-1, etc. Use [\'COMBINE\'] to get a single Hadamard-summed output instead.\n- termination_threshold / termination_comparison_op only matter if execute_until_finished is True on the Composition; without it, the mechanism always runs exactly once per trial.\n- function must be a TransferFunction or SelectionFunction subclass; passing an arbitrary function that changes the output shape will raise a TransferError.'
TOOL_PARAMETERS = { 'properties': { 'clip': { 'description': 'Two-element [min, max] range to clamp '
                                           'output values; null items disable that '
                                           'bound. E.g., [0.0, 1.0].',
                            'items': {'type': 'number'},
                            'maxItems': 2,
                            'minItems': 2,
                            'type': 'array'},
                  'default_variable': { 'description': 'Sets the shape of the input. '
                                                       'E.g., [0.0, 0.0] for a '
                                                       '2-element input. Ignored if '
                                                       'input_shapes is provided.',
                                        'items': {'type': 'number'},
                                        'type': 'array'},
                  'function': { 'description': 'Transfer function to apply to input. '
                                               "Common values: 'Linear', 'Logistic', "
                                               "'ReLU', 'Tanh', 'SoftMax'. Defaults to "
                                               'Linear if omitted.',
                                'type': 'string'},
                  'initial_value': { 'description': 'Starting value for the integrator '
                                                    'when integrator_mode=True. Must '
                                                    'match the shape of '
                                                    'default_variable. Defaults to '
                                                    'zeros.',
                                     'items': {'type': 'number'},
                                     'type': 'array'},
                  'input_shapes': { 'description': 'Scalar shorthand for '
                                                   'default_variable size; e.g., 3 '
                                                   'creates a 3-element input vector.',
                                    'type': 'integer'},
                  'integration_rate': { 'default': 0.5,
                                        'description': 'Rate of integration in [0, 1] '
                                                       'when integrator_mode=True. '
                                                       'Higher = faster integration '
                                                       'toward current input. Default '
                                                       '0.5.',
                                        'maximum': 1,
                                        'minimum': 0,
                                        'type': 'number'},
                  'integrator_function': { 'default': 'AdaptiveIntegrator',
                                           'description': 'Integrator function class '
                                                          'name used when '
                                                          'integrator_mode=True. '
                                                          'Default '
                                                          "'AdaptiveIntegrator'.",
                                           'type': 'string'},
                  'integrator_mode': { 'default': False,
                                       'description': 'If true, input is integrated '
                                                      'via integrator_function before '
                                                      'passing to the transfer '
                                                      'function, producing leaky '
                                                      'integration. Default false.',
                                       'type': 'boolean'},
                  'name': { 'description': 'Name for the mechanism; auto-assigned if '
                                           'omitted.',
                            'type': 'string'},
                  'noise': { 'default': 0,
                             'description': 'Constant offset added to the output '
                                            '(integrator_mode=False) or passed to the '
                                            'integrator function as noise '
                                            '(integrator_mode=True). Default 0.0.',
                             'type': 'number'},
                  'on_resume_integrator_mode': { 'default': 'CURRENT_VALUE',
                                                 'description': 'How to initialize the '
                                                                'integrator when '
                                                                'resuming integration: '
                                                                "'CURRENT_VALUE' "
                                                                '(default), '
                                                                "'LAST_INTEGRATED_VALUE', "
                                                                "or 'RESET'.",
                                                 'enum': [ 'CURRENT_VALUE',
                                                           'LAST_INTEGRATED_VALUE',
                                                           'RESET'],
                                                 'type': 'string'},
                  'output_ports': { 'description': 'Output port specifications. '
                                                   "Default ['RESULTS'] generates one "
                                                   'output per input port. Use '
                                                   "['COMBINE'] for a single summed "
                                                   'output across all input ports.',
                                    'items': {'type': 'string'},
                                    'type': 'array'},
                  'termination_comparison_op': { 'default': '<=',
                                                 'description': 'Comparison operator '
                                                                'used to test '
                                                                "termination: '<', "
                                                                "'<=', '>', '>=', "
                                                                "'==', '!='. Default "
                                                                "'<='.",
                                                 'enum': [ '<',
                                                           '<=',
                                                           '>',
                                                           '>=',
                                                           '==',
                                                           '!='],
                                                 'type': 'string'},
                  'termination_threshold': { 'description': 'If set, execution repeats '
                                                            'until termination_measure '
                                                            'falls below (or satisfies '
                                                            'termination_comparison_op '
                                                            'against) this value. Only '
                                                            'effective when '
                                                            'execute_until_finished is '
                                                            'True.',
                                             'type': 'number'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = "- The noise parameter type (scalar vs. array) is fixed at construction: if you pass a float, you cannot later change it to an array, and vice versa.\n- integration_rate must be in [0, 1]; passing a value outside this range raises a validation error.\n- clip must satisfy clip[0] < clip[1]; if a clip bound is outside the function's output range after scale/offset, a warning is issued and that bound is silently ignored.\n- When integrator_mode=False (default), noise is added to the transfer function output directly. When integrator_mode=True, noise is forwarded to the integrator_function, not added afterward.\n- output_ports defaults to ['RESULTS'], which auto-generates one OutputPort per InputPort. If you specify multiple input_ports, this creates RESULT-0, RESULT-1, etc. Use ['COMBINE'] to get a single Hadamard-summed output instead.\n- termination_threshold / termination_comparison_op only matter if execute_until_finished is True on the Composition; without it, the mechanism always runs exactly once per trial.\n- function must be a TransferFunction or SelectionFunction subclass; passing an arbitrary function that changes the output shape will raise a TransferError."


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
        'Call this tool to create a TransferMechanism — the standard building block for a processing node in a PsyNeuLink Composition that applies a transfer function (e.g., Linear, Logistic, ReLU) to its input.'
        return _impl(args or {})
