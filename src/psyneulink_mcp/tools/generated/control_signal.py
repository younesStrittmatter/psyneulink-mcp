"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '0bc862ff3a863375820c3c163834e13f28873e2fadfb861d9f5a6a907ae9d27f'
__pnl_qualname__ = 'psyneulink.ControlSignal'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_control_signal'
TOOL_DESCRIPTION = 'Call this tool to create a ControlSignal that a ControlMechanism uses to modulate a parameter of another Mechanism. Use it when you need to configure how a controller regulates a specific parameter — including setting the range of control values to sample (allocation_samples), which cost components to apply (intensity, adjustment, duration), and the functions that compute each cost. The result is a ControlSignal object that can be passed in the `control_signals` argument of a ControlMechanism, or in a `(parameter_name, ControlMechanism)` tuple shorthand.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "adjustment_cost_function": {\n      "description": "Function used to compute adjustment_cost from the change in intensity since last execution. Any TransferFunction name. Pass None to permanently disable. Default: Linear.",\n      "type": "string"\n    },\n    "allocation_samples": {\n      "description": "Discrete values the owner ControlMechanism will sample when searching for an optimal control_allocation. Provide as a list of numbers (e.g., [0.0, 0.5, 1.0]). Can also be specified as a SampleSpec string. Default samples from 0.1 to 1 in steps of 0.1.",\n      "items": {\n        "type": "number"\n      },\n      "type": "array"\n    },\n    "combine_costs_function": {\n      "description": "Function used to combine all enabled cost components into a single cost scalar. Must accept an array and return a scalar. Default: Reduce(operation=SUM).",\n      "type": "string"\n    },\n    "control": {\n      "description": "List of ControlProjection specifications \\u2014 the parameters this ControlSignal should modulate. Each item is typically a (parameter_name, Mechanism) tuple expressed as a string, or a Mechanism parameter path.",\n      "items": {\n        "type": "string"\n      },\n      "type": "array"\n    },\n    "cost_options": {\n      "description": "Which cost components to enable. Each element corresponds to a CostFunctions flag: INTENSITY (cost of current intensity), ADJUSTMENT (cost of change in intensity), DURATION (cumulative cost integral). Pass as list of strings. Default enables INTENSITY only.",\n      "items": {\n        "enum": [\n          "INTENSITY",\n          "ADJUSTMENT",\n          "DURATION",\n          "DEFAULTS",\n          "NONE",\n          "ALL"\n        ],\n        "type": "string"\n      },\n      "type": "array"\n    },\n    "default_allocation": {\n      "description": "Template and default value for the allocation (control variable). Must match the shape of each item in allocation_samples. Defaults to defaultControlAllocation (1.0).",\n      "type": "number"\n    },\n    "duration_cost_function": {\n      "description": "IntegratorFunction used to accumulate duration_cost over time. Any IntegratorFunction name. Pass None to permanently disable. Default: SimpleIntegrator.",\n      "type": "string"\n    },\n    "intensity_cost_function": {\n      "description": "Function used to compute intensity_cost from the current intensity. Any TransferFunction name (e.g., \'Exponential\', \'Linear\'). Pass None to permanently disable intensity cost. Default: Exponential.",\n      "type": "string"\n    },\n    "modulation": {\n      "description": "How the ControlSignal modulates its target parameter. Common values: \'MULTIPLICATIVE\', \'ADDITIVE\', \'OVERRIDE\'. Defaults to the ControlMechanism\'s modulation type.",\n      "type": "string"\n    },\n    "name": {\n      "description": "Name for the ControlSignal. Useful for identifying it in logs and output.",\n      "type": "string"\n    },\n    "transfer_function": {\n      "description": "The transfer function used inside TransferWithCosts to convert allocation to intensity. Specify as a PsyNeuLink function name string (e.g., \'Linear\', \'Logistic\'). Do NOT use the \'function\' argument \\u2014 it is reserved for TransferWithCosts and cannot be overridden.",\n      "type": "string"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\n- The `function` argument is NOT exposed: ControlSignal always uses TransferWithCosts internally and raises TypeError if you try to pass a different function. To customize the transfer behavior, use `transfer_function` instead.\n- `cost_options` maps to the CostFunctions flags enum; passing strings like "INTENSITY" requires the host template to convert them — verify the adapter handles this conversion.\n- `allocation_samples` drives the ControlMechanism\'s grid search. Too many samples make EVC control expensive; too few reduce optimization resolution. Default SampleSpec(0.1, 1, 0.1) gives 10 values.\n- `adjustment_cost` and `reconfiguration_cost` on the owning ControlMechanism are distinct concepts — `adjustment_cost` is per-signal, `reconfiguration_cost` is mechanism-level.\n- ControlSignal is almost never instantiated standalone. It is normally passed as part of the `control_signals` argument to a ControlMechanism (e.g., OptimizationControlMechanism or AGTControlMechanism).\n- The deprecated `modulates` argument is an alias for `control`; use `control` instead.\n- `default_allocation` must be a scalar when `allocation_samples` contains scalars; shape must match each sample.'
TOOL_PARAMETERS = { 'properties': { 'adjustment_cost_function': { 'description': 'Function used to '
                                                               'compute '
                                                               'adjustment_cost from '
                                                               'the change in '
                                                               'intensity since last '
                                                               'execution. Any '
                                                               'TransferFunction name. '
                                                               'Pass None to '
                                                               'permanently disable. '
                                                               'Default: Linear.',
                                                'type': 'string'},
                  'allocation_samples': { 'description': 'Discrete values the owner '
                                                         'ControlMechanism will sample '
                                                         'when searching for an '
                                                         'optimal control_allocation. '
                                                         'Provide as a list of numbers '
                                                         '(e.g., [0.0, 0.5, 1.0]). Can '
                                                         'also be specified as a '
                                                         'SampleSpec string. Default '
                                                         'samples from 0.1 to 1 in '
                                                         'steps of 0.1.',
                                          'items': {'type': 'number'},
                                          'type': 'array'},
                  'combine_costs_function': { 'description': 'Function used to combine '
                                                             'all enabled cost '
                                                             'components into a single '
                                                             'cost scalar. Must accept '
                                                             'an array and return a '
                                                             'scalar. Default: '
                                                             'Reduce(operation=SUM).',
                                              'type': 'string'},
                  'control': { 'description': 'List of ControlProjection '
                                              'specifications — the parameters this '
                                              'ControlSignal should modulate. Each '
                                              'item is typically a (parameter_name, '
                                              'Mechanism) tuple expressed as a string, '
                                              'or a Mechanism parameter path.',
                               'items': {'type': 'string'},
                               'type': 'array'},
                  'cost_options': { 'description': 'Which cost components to enable. '
                                                   'Each element corresponds to a '
                                                   'CostFunctions flag: INTENSITY '
                                                   '(cost of current intensity), '
                                                   'ADJUSTMENT (cost of change in '
                                                   'intensity), DURATION (cumulative '
                                                   'cost integral). Pass as list of '
                                                   'strings. Default enables INTENSITY '
                                                   'only.',
                                    'items': { 'enum': [ 'INTENSITY',
                                                         'ADJUSTMENT',
                                                         'DURATION',
                                                         'DEFAULTS',
                                                         'NONE',
                                                         'ALL'],
                                               'type': 'string'},
                                    'type': 'array'},
                  'default_allocation': { 'description': 'Template and default value '
                                                         'for the allocation (control '
                                                         'variable). Must match the '
                                                         'shape of each item in '
                                                         'allocation_samples. Defaults '
                                                         'to defaultControlAllocation '
                                                         '(1.0).',
                                          'type': 'number'},
                  'duration_cost_function': { 'description': 'IntegratorFunction used '
                                                             'to accumulate '
                                                             'duration_cost over time. '
                                                             'Any IntegratorFunction '
                                                             'name. Pass None to '
                                                             'permanently disable. '
                                                             'Default: '
                                                             'SimpleIntegrator.',
                                              'type': 'string'},
                  'intensity_cost_function': { 'description': 'Function used to '
                                                              'compute intensity_cost '
                                                              'from the current '
                                                              'intensity. Any '
                                                              'TransferFunction name '
                                                              "(e.g., 'Exponential', "
                                                              "'Linear'). Pass None to "
                                                              'permanently disable '
                                                              'intensity cost. '
                                                              'Default: Exponential.',
                                               'type': 'string'},
                  'modulation': { 'description': 'How the ControlSignal modulates its '
                                                 'target parameter. Common values: '
                                                 "'MULTIPLICATIVE', 'ADDITIVE', "
                                                 "'OVERRIDE'. Defaults to the "
                                                 "ControlMechanism's modulation type.",
                                  'type': 'string'},
                  'name': { 'description': 'Name for the ControlSignal. Useful for '
                                           'identifying it in logs and output.',
                            'type': 'string'},
                  'transfer_function': { 'description': 'The transfer function used '
                                                        'inside TransferWithCosts to '
                                                        'convert allocation to '
                                                        'intensity. Specify as a '
                                                        'PsyNeuLink function name '
                                                        "string (e.g., 'Linear', "
                                                        "'Logistic'). Do NOT use the "
                                                        "'function' argument — it is "
                                                        'reserved for '
                                                        'TransferWithCosts and cannot '
                                                        'be overridden.',
                                         'type': 'string'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = '- The `function` argument is NOT exposed: ControlSignal always uses TransferWithCosts internally and raises TypeError if you try to pass a different function. To customize the transfer behavior, use `transfer_function` instead.\n- `cost_options` maps to the CostFunctions flags enum; passing strings like "INTENSITY" requires the host template to convert them — verify the adapter handles this conversion.\n- `allocation_samples` drives the ControlMechanism\'s grid search. Too many samples make EVC control expensive; too few reduce optimization resolution. Default SampleSpec(0.1, 1, 0.1) gives 10 values.\n- `adjustment_cost` and `reconfiguration_cost` on the owning ControlMechanism are distinct concepts — `adjustment_cost` is per-signal, `reconfiguration_cost` is mechanism-level.\n- ControlSignal is almost never instantiated standalone. It is normally passed as part of the `control_signals` argument to a ControlMechanism (e.g., OptimizationControlMechanism or AGTControlMechanism).\n- The deprecated `modulates` argument is an alias for `control`; use `control` instead.\n- `default_allocation` must be a scalar when `allocation_samples` contains scalars; shape must match each sample.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.ControlSignal
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
    def create_control_signal(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to create a ControlSignal that a ControlMechanism uses to modulate a parameter of another Mechanism.'
        return _impl(args or {})
