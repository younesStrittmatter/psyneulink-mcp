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
TOOL_DESCRIPTION = 'Call this tool to create a PsyNeuLink TransferMechanism — a processing node that applies a transfer function (e.g., Linear, Logistic, ReLU) to its input, optionally with temporal integration via a leaky integrator. Returns a TransferMechanism handle that can be added to a Composition. Use this when you need a neuron-like unit that transforms activation values, with or without temporal dynamics. All parameters must be passed as direct top-level keyword arguments — never wrap them inside an "args" key.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "clip": {\n      "description": "Two-element [min, max] bounds applied elementwise to the output after the transfer function. Omit or null for no clipping.",\n      "items": {\n        "type": "number"\n      },\n      "maxItems": 2,\n      "minItems": 2,\n      "type": "array"\n    },\n    "default_variable": {\n      "description": "Input template as a 2D list-of-lists, e.g. [[0, 0, 0]] for a single 3-element input port. MUTUALLY EXCLUSIVE with input_shapes \\u2014 do not pass both. Use input_shapes instead when you only need to specify size.",\n      "items": {\n        "items": {\n          "type": "number"\n        },\n        "type": "array"\n      },\n      "type": "array"\n    },\n    "function": {\n      "description": "Name of the transfer function to apply. Common values: \'Linear\' (default), \'Logistic\', \'ReLU\', \'Tanh\', \'SoftMax\'. Must be a TransferFunction or SelectionFunction name string.",\n      "type": "string"\n    },\n    "initial_value": {\n      "description": "Starting value for the integrator when integrator_mode=True. Must be a 2D list with the same shape as default_variable.",\n      "items": {\n        "items": {\n          "type": "number"\n        },\n        "type": "array"\n      },\n      "type": "array"\n    },\n    "input_shapes": {\n      "description": "Shorthand to set input size: integer N creates one input port of size N. MUTUALLY EXCLUSIVE with default_variable \\u2014 do not pass both.",\n      "type": "integer"\n    },\n    "integration_rate": {\n      "description": "Rate of integration in [0, 1] when integrator_mode=True. Higher values integrate faster (0.5 = equal blend). Default 0.5.",\n      "type": "number"\n    },\n    "integrator_mode": {\n      "description": "If true, input is integrated via integrator_function before the transfer function is applied, enabling temporal/leaky-integration dynamics. Default false.",\n      "type": "boolean"\n    },\n    "name": {\n      "description": "Identifier for this mechanism within a Composition.",\n      "type": "string"\n    },\n    "noise": {\n      "description": "Scalar added to the function output (or forwarded to the integrator when integrator_mode=True). Default 0.0.",\n      "type": "number"\n    },\n    "on_resume_integrator_mode": {\n      "description": "How to seed the integrator when resuming integrator_mode=True. Default \'CURRENT_VALUE\'.",\n      "enum": [\n        "CURRENT_VALUE",\n        "LAST_INTEGRATED_VALUE",\n        "RESET"\n      ],\n      "type": "string"\n    },\n    "output_ports": {\n      "description": "Output port specifications. Default [\'RESULTS\'] generates one port per input port. Include \'COMBINE\' for an elementwise-sum port across all value items.",\n      "items": {\n        "type": "string"\n      },\n      "type": "array"\n    },\n    "termination_comparison_op": {\n      "description": "Comparison operator for termination: compares termination_measure_value against termination_threshold. Default \'<=\'.",\n      "enum": [\n        "<",\n        "<=",\n        ">",\n        ">=",\n        "==",\n        "!="\n      ],\n      "type": "string"\n    },\n    "termination_threshold": {\n      "description": "If set (with execute_until_finished=True on the Composition run), execution repeats until termination_measure_value satisfies this threshold. Default null (single-pass).",\n      "type": "number"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\nCRITICAL — do NOT nest arguments inside an \'args\' key. All parameters must be passed as flat top-level keyword arguments. Passing {"args": {"name": "foo", ...}} is wrong and causes "Illegal argument in constructor: \'args\'".\n\nCRITICAL — input_shapes and default_variable are mutually exclusive. Passing both causes ComponentError ("input_shapes and default_variable conflict"). Use input_shapes=N (integer) as the simple shorthand. Use default_variable only when you need multiple input ports or an exact initial value template.\n\ndefault_variable must be a 2D list (list of lists). For a single input port of size 3: [[0, 0, 0]]. A 1D list [[0]] has shape (1,1) — only a single scalar element.\n\nfunction must be a string name (\'Linear\', \'Logistic\', \'ReLU\', etc.), not a dict or object.\n\nintegration_rate must be a float in [0, 1]; values outside this range are rejected by PNL.\n\ntermination_threshold only has an effect when execute_until_finished=True is passed to the Composition.run() call; without it, the mechanism always runs exactly once per trial.'
TOOL_PARAMETERS = { 'properties': { 'clip': { 'description': 'Two-element [min, max] bounds applied '
                                           'elementwise to the output after the '
                                           'transfer function. Omit or null for no '
                                           'clipping.',
                            'items': {'type': 'number'},
                            'maxItems': 2,
                            'minItems': 2,
                            'type': 'array'},
                  'default_variable': { 'description': 'Input template as a 2D '
                                                       'list-of-lists, e.g. [[0, 0, '
                                                       '0]] for a single 3-element '
                                                       'input port. MUTUALLY EXCLUSIVE '
                                                       'with input_shapes — do not '
                                                       'pass both. Use input_shapes '
                                                       'instead when you only need to '
                                                       'specify size.',
                                        'items': { 'items': {'type': 'number'},
                                                   'type': 'array'},
                                        'type': 'array'},
                  'function': { 'description': 'Name of the transfer function to '
                                               "apply. Common values: 'Linear' "
                                               "(default), 'Logistic', 'ReLU', 'Tanh', "
                                               "'SoftMax'. Must be a TransferFunction "
                                               'or SelectionFunction name string.',
                                'type': 'string'},
                  'initial_value': { 'description': 'Starting value for the integrator '
                                                    'when integrator_mode=True. Must '
                                                    'be a 2D list with the same shape '
                                                    'as default_variable.',
                                     'items': { 'items': {'type': 'number'},
                                                'type': 'array'},
                                     'type': 'array'},
                  'input_shapes': { 'description': 'Shorthand to set input size: '
                                                   'integer N creates one input port '
                                                   'of size N. MUTUALLY EXCLUSIVE with '
                                                   'default_variable — do not pass '
                                                   'both.',
                                    'type': 'integer'},
                  'integration_rate': { 'description': 'Rate of integration in [0, 1] '
                                                       'when integrator_mode=True. '
                                                       'Higher values integrate faster '
                                                       '(0.5 = equal blend). Default '
                                                       '0.5.',
                                        'type': 'number'},
                  'integrator_mode': { 'description': 'If true, input is integrated '
                                                      'via integrator_function before '
                                                      'the transfer function is '
                                                      'applied, enabling '
                                                      'temporal/leaky-integration '
                                                      'dynamics. Default false.',
                                       'type': 'boolean'},
                  'name': { 'description': 'Identifier for this mechanism within a '
                                           'Composition.',
                            'type': 'string'},
                  'noise': { 'description': 'Scalar added to the function output (or '
                                            'forwarded to the integrator when '
                                            'integrator_mode=True). Default 0.0.',
                             'type': 'number'},
                  'on_resume_integrator_mode': { 'description': 'How to seed the '
                                                                'integrator when '
                                                                'resuming '
                                                                'integrator_mode=True. '
                                                                'Default '
                                                                "'CURRENT_VALUE'.",
                                                 'enum': [ 'CURRENT_VALUE',
                                                           'LAST_INTEGRATED_VALUE',
                                                           'RESET'],
                                                 'type': 'string'},
                  'output_ports': { 'description': 'Output port specifications. '
                                                   "Default ['RESULTS'] generates one "
                                                   'port per input port. Include '
                                                   "'COMBINE' for an elementwise-sum "
                                                   'port across all value items.',
                                    'items': {'type': 'string'},
                                    'type': 'array'},
                  'termination_comparison_op': { 'description': 'Comparison operator '
                                                                'for termination: '
                                                                'compares '
                                                                'termination_measure_value '
                                                                'against '
                                                                'termination_threshold. '
                                                                "Default '<='.",
                                                 'enum': [ '<',
                                                           '<=',
                                                           '>',
                                                           '>=',
                                                           '==',
                                                           '!='],
                                                 'type': 'string'},
                  'termination_threshold': { 'description': 'If set (with '
                                                            'execute_until_finished=True '
                                                            'on the Composition run), '
                                                            'execution repeats until '
                                                            'termination_measure_value '
                                                            'satisfies this threshold. '
                                                            'Default null '
                                                            '(single-pass).',
                                             'type': 'number'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = 'CRITICAL — do NOT nest arguments inside an \'args\' key. All parameters must be passed as flat top-level keyword arguments. Passing {"args": {"name": "foo", ...}} is wrong and causes "Illegal argument in constructor: \'args\'".\n\nCRITICAL — input_shapes and default_variable are mutually exclusive. Passing both causes ComponentError ("input_shapes and default_variable conflict"). Use input_shapes=N (integer) as the simple shorthand. Use default_variable only when you need multiple input ports or an exact initial value template.\n\ndefault_variable must be a 2D list (list of lists). For a single input port of size 3: [[0, 0, 0]]. A 1D list [[0]] has shape (1,1) — only a single scalar element.\n\nfunction must be a string name (\'Linear\', \'Logistic\', \'ReLU\', etc.), not a dict or object.\n\nintegration_rate must be a float in [0, 1]; values outside this range are rejected by PNL.\n\ntermination_threshold only has an effect when execute_until_finished=True is passed to the Composition.run() call; without it, the mechanism always runs exactly once per trial.'


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
        'Call this tool to create a PsyNeuLink TransferMechanism — a processing node that applies a transfer function (e.g., Linear, Logistic, ReLU) to its input, optionally with temporal integration via a leaky integrator.'
        return _impl(args or {})
