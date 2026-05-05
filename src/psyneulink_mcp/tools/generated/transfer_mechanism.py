"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '6272239673b3bb6083202e3f9fee4ae09942dc4a63a9358153f2b78075ea5043'
__pnl_qualname__ = 'psyneulink.TransferMechanism'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_transfer_mechanism'
TOOL_DESCRIPTION = 'Call this tool to create a TransferMechanism — a processing node that applies a transfer function (Linear, Logistic, ReLU, etc.) to its inputs, optionally with leaky integration over time. Use it whenever you need an input layer, hidden layer, or output layer in a Composition. Returns an object handle to pass to composition tools (e.g., add_node, add_projection).\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "clip": {\n      "description": "[min, max] hard bounds applied element-wise to the output. min must be strictly less than max.",\n      "items": {\n        "type": "number"\n      },\n      "maxItems": 2,\n      "minItems": 2,\n      "type": "array"\n    },\n    "function": {\n      "description": "Name of the transfer function applied to input after optional integration. Must be a string from the allowed list \\u2014 the tool resolves it to the corresponding PsyNeuLink class. Do NOT omit quotes; do NOT pass a Python class object.",\n      "enum": [\n        "Linear",\n        "Logistic",\n        "ReLU",\n        "Tanh",\n        "Gaussian",\n        "SoftMax"\n      ],\n      "type": "string"\n    },\n    "initial_value": {\n      "description": "Starting value for the integrator when integrator_mode=true. Must match the shape of the input variable.",\n      "type": "number"\n    },\n    "input_shapes": {\n      "description": "Size of the input vector (e.g. 3 for a 3-unit layer). Equivalent to setting default_variable to a zero array of that length.",\n      "type": "integer"\n    },\n    "integration_rate": {\n      "default": 0.5,\n      "description": "Rate of integration when integrator_mode=true. Must be in [0, 1]; 1.0 means no memory of prior input, 0.0 means no update.",\n      "type": "number"\n    },\n    "integrator_mode": {\n      "default": false,\n      "description": "If true, input is first passed through integrator_function (default AdaptiveIntegrator) before the transfer function, enabling temporal dynamics / leaky integration.",\n      "type": "boolean"\n    },\n    "name": {\n      "description": "Unique name for this mechanism within the Composition.",\n      "type": "string"\n    },\n    "noise": {\n      "default": 0,\n      "description": "Scalar offset added to the output on each execution. For stochastic noise use a DistributionFunction via a separate tool and reference its handle.",\n      "type": "number"\n    },\n    "on_resume_integrator_mode": {\n      "default": "CURRENT_VALUE",\n      "description": "How to seed the integrator when switching back to integrator_mode=true. CURRENT_VALUE uses the mechanism\'s current output; LAST_INTEGRATED_VALUE uses the integrator\'s previous state; RESET reinitializes to initial_value.",\n      "enum": [\n        "CURRENT_VALUE",\n        "LAST_INTEGRATED_VALUE",\n        "RESET"\n      ],\n      "type": "string"\n    },\n    "output_ports": {\n      "description": "List of output port names. Default (\'RESULTS\') generates one RESULT port per InputPort. Pass [\'COMBINE\'] to produce the Hadamard sum of all output items as a single port.",\n      "items": {\n        "type": "string"\n      },\n      "type": "array"\n    },\n    "termination_comparison_op": {\n      "default": "<=",\n      "description": "Comparison operator applied between termination_measure_value and termination_threshold to decide whether execution is finished.",\n      "enum": [\n        "<",\n        "<=",\n        ">",\n        ">=",\n        "==",\n        "!="\n      ],\n      "type": "string"\n    },\n    "termination_threshold": {\n      "description": "If set, execution repeats (up to max_passes) until termination_measure_value satisfies this threshold. Only meaningful when execute_until_finished=True on the enclosing Composition run.",\n      "type": "number"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\nCRITICAL (from feedback 2026-05-05): The previous error "TypeError: issubclass() arg 1 must be a class" was caused by passing function=\'Linear\' as a bare string directly to psyneulink.TransferMechanism. PsyNeuLink\'s _validate_params calls issubclass(transfer_function_class, Function), which raises TypeError when the value is a string rather than a class. The tool implementation MUST resolve the function string to its psyneulink class object (e.g., psyneulink.Linear) before forwarding kwargs to the constructor.\n\nOther caveats:\n- integration_rate is validated in [0, 1]; values outside this range raise TransferError at construction time.\n- clip validation requires both elements to be numeric scalars and clip[0] < clip[1]; construction fails otherwise.\n- initial_value must match the shape of default_variable/input; mismatches raise TransferError.\n- When integrator_mode=False (default), initial_value, integration_rate, and on_resume_integrator_mode have no effect during execution.\n- If input_shapes is an integer N, the mechanism has a single N-dimensional input port; if it is a list of integers, multiple input ports are created, each with one RESULT output port.\n- noise specified as a float cannot later be changed to a list/array, and vice versa.'
TOOL_PARAMETERS = { 'properties': { 'clip': { 'description': '[min, max] hard bounds applied '
                                           'element-wise to the output. min must be '
                                           'strictly less than max.',
                            'items': {'type': 'number'},
                            'maxItems': 2,
                            'minItems': 2,
                            'type': 'array'},
                  'function': { 'description': 'Name of the transfer function applied '
                                               'to input after optional integration. '
                                               'Must be a string from the allowed list '
                                               '— the tool resolves it to the '
                                               'corresponding PsyNeuLink class. Do NOT '
                                               'omit quotes; do NOT pass a Python '
                                               'class object.',
                                'enum': [ 'Linear',
                                          'Logistic',
                                          'ReLU',
                                          'Tanh',
                                          'Gaussian',
                                          'SoftMax'],
                                'type': 'string'},
                  'initial_value': { 'description': 'Starting value for the integrator '
                                                    'when integrator_mode=true. Must '
                                                    'match the shape of the input '
                                                    'variable.',
                                     'type': 'number'},
                  'input_shapes': { 'description': 'Size of the input vector (e.g. 3 '
                                                   'for a 3-unit layer). Equivalent to '
                                                   'setting default_variable to a zero '
                                                   'array of that length.',
                                    'type': 'integer'},
                  'integration_rate': { 'default': 0.5,
                                        'description': 'Rate of integration when '
                                                       'integrator_mode=true. Must be '
                                                       'in [0, 1]; 1.0 means no memory '
                                                       'of prior input, 0.0 means no '
                                                       'update.',
                                        'type': 'number'},
                  'integrator_mode': { 'default': False,
                                       'description': 'If true, input is first passed '
                                                      'through integrator_function '
                                                      '(default AdaptiveIntegrator) '
                                                      'before the transfer function, '
                                                      'enabling temporal dynamics / '
                                                      'leaky integration.',
                                       'type': 'boolean'},
                  'name': { 'description': 'Unique name for this mechanism within the '
                                           'Composition.',
                            'type': 'string'},
                  'noise': { 'default': 0,
                             'description': 'Scalar offset added to the output on each '
                                            'execution. For stochastic noise use a '
                                            'DistributionFunction via a separate tool '
                                            'and reference its handle.',
                             'type': 'number'},
                  'on_resume_integrator_mode': { 'default': 'CURRENT_VALUE',
                                                 'description': 'How to seed the '
                                                                'integrator when '
                                                                'switching back to '
                                                                'integrator_mode=true. '
                                                                'CURRENT_VALUE uses '
                                                                "the mechanism's "
                                                                'current output; '
                                                                'LAST_INTEGRATED_VALUE '
                                                                "uses the integrator's "
                                                                'previous state; RESET '
                                                                'reinitializes to '
                                                                'initial_value.',
                                                 'enum': [ 'CURRENT_VALUE',
                                                           'LAST_INTEGRATED_VALUE',
                                                           'RESET'],
                                                 'type': 'string'},
                  'output_ports': { 'description': 'List of output port names. Default '
                                                   "('RESULTS') generates one RESULT "
                                                   'port per InputPort. Pass '
                                                   "['COMBINE'] to produce the "
                                                   'Hadamard sum of all output items '
                                                   'as a single port.',
                                    'items': {'type': 'string'},
                                    'type': 'array'},
                  'termination_comparison_op': { 'default': '<=',
                                                 'description': 'Comparison operator '
                                                                'applied between '
                                                                'termination_measure_value '
                                                                'and '
                                                                'termination_threshold '
                                                                'to decide whether '
                                                                'execution is '
                                                                'finished.',
                                                 'enum': [ '<',
                                                           '<=',
                                                           '>',
                                                           '>=',
                                                           '==',
                                                           '!='],
                                                 'type': 'string'},
                  'termination_threshold': { 'description': 'If set, execution repeats '
                                                            '(up to max_passes) until '
                                                            'termination_measure_value '
                                                            'satisfies this threshold. '
                                                            'Only meaningful when '
                                                            'execute_until_finished=True '
                                                            'on the enclosing '
                                                            'Composition run.',
                                             'type': 'number'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = 'CRITICAL (from feedback 2026-05-05): The previous error "TypeError: issubclass() arg 1 must be a class" was caused by passing function=\'Linear\' as a bare string directly to psyneulink.TransferMechanism. PsyNeuLink\'s _validate_params calls issubclass(transfer_function_class, Function), which raises TypeError when the value is a string rather than a class. The tool implementation MUST resolve the function string to its psyneulink class object (e.g., psyneulink.Linear) before forwarding kwargs to the constructor.\n\nOther caveats:\n- integration_rate is validated in [0, 1]; values outside this range raise TransferError at construction time.\n- clip validation requires both elements to be numeric scalars and clip[0] < clip[1]; construction fails otherwise.\n- initial_value must match the shape of default_variable/input; mismatches raise TransferError.\n- When integrator_mode=False (default), initial_value, integration_rate, and on_resume_integrator_mode have no effect during execution.\n- If input_shapes is an integer N, the mechanism has a single N-dimensional input port; if it is a list of integers, multiple input ports are created, each with one RESULT output port.\n- noise specified as a float cannot later be changed to a list/array, and vice versa.'


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
        'Call this tool to create a TransferMechanism — a processing node that applies a transfer function (Linear, Logistic, ReLU, etc.) to its inputs, optionally with leaky integration over time.'
        return _impl(args or {})
