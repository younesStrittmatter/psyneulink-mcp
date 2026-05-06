"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '5e251c67921a291bd9bc38725c6a38a8b4ff5438ce8f609ae14d47df83d81856'
__pnl_qualname__ = 'psyneulink.library.components.mechanisms.processing.transfer.kohonenmechanism.TransferMechanism'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_transfer_mechanism'
TOOL_DESCRIPTION = 'Call this tool to create a TransferMechanism — a processing node that applies a transfer function (default: Linear) to its input, optionally with temporal integration, noise injection, and output clipping. Returns a handle string referencing the constructed object, which can be passed to Composition tools. Use this when you need a standard feedforward unit in a PsyNeuLink network; for leaky competition dynamics use LCAMechanism instead.\n\nCRITICAL CALLING CONVENTION: pass constructor kwargs as a flat dict directly to `args`, e.g. `args={"name": "my_mech", "input_shapes": 5}`. Do NOT nest an inner "args" key: `args={"args": {"name": "my_mech"}}` passes the literal key "args" to the PNL constructor and raises ComponentError: Illegal argument \'args\'.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "clip": {\n      "description": "Two-element [min, max] array that clamps output values elementwise. First element must be strictly less than second.",\n      "items": {\n        "type": "number"\n      },\n      "maxItems": 2,\n      "minItems": 2,\n      "type": "array"\n    },\n    "default_variable": {\n      "description": "Input shape as a 2D list-of-lists, one inner list per input port (e.g., [[0,0,0]] for one 3-element port). MUTUALLY EXCLUSIVE with input_shapes \\u2014 providing both raises a shape conflict error. Use this only when you need multiple input ports or exact initial values.",\n      "items": {\n        "items": {\n          "type": "number"\n        },\n        "type": "array"\n      },\n      "type": "array"\n    },\n    "function": {\n      "description": "Name of the transfer function to apply as a string: \'Linear\' (default), \'Logistic\', \'ReLU\', \'Tanh\', \'SoftMax\', \'Gaussian\', etc.",\n      "type": "string"\n    },\n    "initial_value": {\n      "description": "Starting value for integrator_function when integrator_mode=true. Must match the shape of the mechanism\'s variable.",\n      "items": {\n        "type": "number"\n      },\n      "type": "array"\n    },\n    "input_shapes": {\n      "description": "Size of a single input port as an integer (e.g., 5 creates one port with 5 elements). MUTUALLY EXCLUSIVE with default_variable \\u2014 providing both raises a shape conflict error. Prefer this over default_variable when you only need to set port size.",\n      "type": "integer"\n    },\n    "integration_rate": {\n      "description": "Rate of integration when integrator_mode=true; must be in [0, 1]. Higher values converge faster toward the current input. Default: 0.5.",\n      "maximum": 1,\n      "minimum": 0,\n      "type": "number"\n    },\n    "integrator_function": {\n      "description": "Name of the IntegratorFunction used when integrator_mode=true. Default: \'AdaptiveIntegrator\'.",\n      "type": "string"\n    },\n    "integrator_mode": {\n      "description": "When true, input is first integrated via integrator_function before the primary transfer function, enabling temporal dynamics. Default: false.",\n      "type": "boolean"\n    },\n    "name": {\n      "description": "Name for the mechanism. Auto-assigned if omitted.",\n      "type": "string"\n    },\n    "noise": {\n      "description": "Scalar added to the output (when integrator_mode=False) or forwarded as noise to integrator_function (when integrator_mode=True). Default: 0.0.",\n      "type": "number"\n    },\n    "on_resume_integrator_mode": {\n      "description": "Value used by integrator_function when integration resumes after being paused. Default: \'CURRENT_VALUE\'.",\n      "enum": [\n        "CURRENT_VALUE",\n        "LAST_INTEGRATED_VALUE",\n        "RESET"\n      ],\n      "type": "string"\n    },\n    "output_ports": {\n      "description": "Output port specifiers. Default [\'RESULTS\'] yields one port per input port. Use [\'COMBINE\'] to Hadamard-sum all outputs into a single 1D array.",\n      "items": {\n        "type": "string"\n      },\n      "type": "array"\n    },\n    "termination_comparison_op": {\n      "description": "Comparator applied between termination_measure_value and termination_threshold. Default: \'<=\'.",\n      "enum": [\n        "<",\n        "<=",\n        ">",\n        ">=",\n        "==",\n        "!="\n      ],\n      "type": "string"\n    },\n    "termination_threshold": {\n      "description": "If set, execution repeats until termination_measure meets this value. Only active when the owning Composition has execute_until_finished=True. Default: null (run once).",\n      "type": "number"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\nMOST COMMON BUG — double-nested args: the tool receives a single `args` dict whose contents are passed as PNL constructor kwargs. Call as `args={"name": "foo", "input_shapes": 5}`. Never nest: `args={"args": {"name": "foo"}}` — that passes the literal string "args" as a constructor kwarg and raises ComponentError: Illegal argument \'args\'.\n\ninput_shapes and default_variable are mutually exclusive: passing both causes a shape conflict error regardless of values. Use input_shapes (integer) for simple single-port sizing; use default_variable (2D list) only when you need multiple ports or specific initial values.\n\ndefault_variable must be 2D: [[0, 0, 0]] for one 3-element port, not [0, 0, 0].\n\nfunction must be a string name, not a Python object: pass "Logistic", not pnl.Logistic.\n\nintegration_rate must be in [0, 1]; values outside that range raise a validation error at construction time.\n\ntermination_threshold only triggers repeated execution when the owning Composition\'s execute_until_finished=True; otherwise the mechanism always runs exactly once per trial regardless of the threshold value.'
TOOL_PARAMETERS = { 'properties': { 'clip': { 'description': 'Two-element [min, max] array that clamps '
                                           'output values elementwise. First element '
                                           'must be strictly less than second.',
                            'items': {'type': 'number'},
                            'maxItems': 2,
                            'minItems': 2,
                            'type': 'array'},
                  'default_variable': { 'description': 'Input shape as a 2D '
                                                       'list-of-lists, one inner list '
                                                       'per input port (e.g., '
                                                       '[[0,0,0]] for one 3-element '
                                                       'port). MUTUALLY EXCLUSIVE with '
                                                       'input_shapes — providing both '
                                                       'raises a shape conflict error. '
                                                       'Use this only when you need '
                                                       'multiple input ports or exact '
                                                       'initial values.',
                                        'items': { 'items': {'type': 'number'},
                                                   'type': 'array'},
                                        'type': 'array'},
                  'function': { 'description': 'Name of the transfer function to apply '
                                               "as a string: 'Linear' (default), "
                                               "'Logistic', 'ReLU', 'Tanh', 'SoftMax', "
                                               "'Gaussian', etc.",
                                'type': 'string'},
                  'initial_value': { 'description': 'Starting value for '
                                                    'integrator_function when '
                                                    'integrator_mode=true. Must match '
                                                    "the shape of the mechanism's "
                                                    'variable.',
                                     'items': {'type': 'number'},
                                     'type': 'array'},
                  'input_shapes': { 'description': 'Size of a single input port as an '
                                                   'integer (e.g., 5 creates one port '
                                                   'with 5 elements). MUTUALLY '
                                                   'EXCLUSIVE with default_variable — '
                                                   'providing both raises a shape '
                                                   'conflict error. Prefer this over '
                                                   'default_variable when you only '
                                                   'need to set port size.',
                                    'type': 'integer'},
                  'integration_rate': { 'description': 'Rate of integration when '
                                                       'integrator_mode=true; must be '
                                                       'in [0, 1]. Higher values '
                                                       'converge faster toward the '
                                                       'current input. Default: 0.5.',
                                        'maximum': 1,
                                        'minimum': 0,
                                        'type': 'number'},
                  'integrator_function': { 'description': 'Name of the '
                                                          'IntegratorFunction used '
                                                          'when integrator_mode=true. '
                                                          'Default: '
                                                          "'AdaptiveIntegrator'.",
                                           'type': 'string'},
                  'integrator_mode': { 'description': 'When true, input is first '
                                                      'integrated via '
                                                      'integrator_function before the '
                                                      'primary transfer function, '
                                                      'enabling temporal dynamics. '
                                                      'Default: false.',
                                       'type': 'boolean'},
                  'name': { 'description': 'Name for the mechanism. Auto-assigned if '
                                           'omitted.',
                            'type': 'string'},
                  'noise': { 'description': 'Scalar added to the output (when '
                                            'integrator_mode=False) or forwarded as '
                                            'noise to integrator_function (when '
                                            'integrator_mode=True). Default: 0.0.',
                             'type': 'number'},
                  'on_resume_integrator_mode': { 'description': 'Value used by '
                                                                'integrator_function '
                                                                'when integration '
                                                                'resumes after being '
                                                                'paused. Default: '
                                                                "'CURRENT_VALUE'.",
                                                 'enum': [ 'CURRENT_VALUE',
                                                           'LAST_INTEGRATED_VALUE',
                                                           'RESET'],
                                                 'type': 'string'},
                  'output_ports': { 'description': 'Output port specifiers. Default '
                                                   "['RESULTS'] yields one port per "
                                                   "input port. Use ['COMBINE'] to "
                                                   'Hadamard-sum all outputs into a '
                                                   'single 1D array.',
                                    'items': {'type': 'string'},
                                    'type': 'array'},
                  'termination_comparison_op': { 'description': 'Comparator applied '
                                                                'between '
                                                                'termination_measure_value '
                                                                'and '
                                                                'termination_threshold. '
                                                                "Default: '<='.",
                                                 'enum': [ '<',
                                                           '<=',
                                                           '>',
                                                           '>=',
                                                           '==',
                                                           '!='],
                                                 'type': 'string'},
                  'termination_threshold': { 'description': 'If set, execution repeats '
                                                            'until termination_measure '
                                                            'meets this value. Only '
                                                            'active when the owning '
                                                            'Composition has '
                                                            'execute_until_finished=True. '
                                                            'Default: null (run once).',
                                             'type': 'number'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = 'MOST COMMON BUG — double-nested args: the tool receives a single `args` dict whose contents are passed as PNL constructor kwargs. Call as `args={"name": "foo", "input_shapes": 5}`. Never nest: `args={"args": {"name": "foo"}}` — that passes the literal string "args" as a constructor kwarg and raises ComponentError: Illegal argument \'args\'.\n\ninput_shapes and default_variable are mutually exclusive: passing both causes a shape conflict error regardless of values. Use input_shapes (integer) for simple single-port sizing; use default_variable (2D list) only when you need multiple ports or specific initial values.\n\ndefault_variable must be 2D: [[0, 0, 0]] for one 3-element port, not [0, 0, 0].\n\nfunction must be a string name, not a Python object: pass "Logistic", not pnl.Logistic.\n\nintegration_rate must be in [0, 1]; values outside that range raise a validation error at construction time.\n\ntermination_threshold only triggers repeated execution when the owning Composition\'s execute_until_finished=True; otherwise the mechanism always runs exactly once per trial regardless of the threshold value.'


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
        'Call this tool to create a TransferMechanism — a processing node that applies a transfer function (default: Linear) to its input, optionally with temporal integration, noise injection, and output clipping.'
        return _impl(args or {})
