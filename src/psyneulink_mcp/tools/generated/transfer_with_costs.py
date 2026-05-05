"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '80154ee5b97c97dce16644c4f4193f3b9c5183fc3c2f237c6f3ec577d72b3079'
__pnl_qualname__ = 'psyneulink.TransferWithCosts'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_transfer_with_costs'
TOOL_DESCRIPTION = 'Use this tool to construct a TransferWithCosts function — a TransferFunction wrapper that applies a primary transfer transform (e.g., Linear, Logistic) to its input and optionally computes up to three cost signals (intensity, adjustment, duration) whose weighted sum is stored as combined_costs. Call this when you need a ControlSignal\'s function to track and penalize its output magnitude, rate of change, or cumulative activation, particularly when building cost-aware control loops in PsyNeuLink compositions.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "adjustment_cost_fct": {\n      "description": "Name of the TransferFunction class used to compute adjustment_cost from the absolute change in intensity between successive calls. Default: \'Linear\'.",\n      "type": "string"\n    },\n    "combine_costs_fct": {\n      "description": "Name of the function used to aggregate all enabled cost signals into combined_costs. Default: \'LinearCombination\' (element-wise sum). Must accept an array of cost values and return a scalar.",\n      "type": "string"\n    },\n    "default_variable": {\n      "description": "Initial shape and value of the input array. Determines the dimensionality of the function. Mutually exclusive with input_shapes if lengths disagree.",\n      "items": {\n        "type": "number"\n      },\n      "type": "array"\n    },\n    "duration_cost_fct": {\n      "description": "Name of the IntegratorFunction class used to compute duration_cost as a running integral of intensity. Default: \'SimpleIntegrator\'. Only accumulates during executions where DURATION is enabled.",\n      "type": "string"\n    },\n    "enabled_cost_functions": {\n      "description": "Which cost functions to execute on each call. \'INTENSITY\' penalizes output magnitude (via Exponential by default), \'ADJUSTMENT\' penalizes change in output (via Linear), \'DURATION\' penalizes cumulative output (via SimpleIntegrator). Default is CostFunctions.INTENSITY (i.e., only intensity cost is active).",\n      "oneOf": [\n        {\n          "enum": [\n            "NONE",\n            "INTENSITY",\n            "ADJUSTMENT",\n            "DURATION",\n            "ALL",\n            "DEFAULTS"\n          ],\n          "type": "string"\n        },\n        {\n          "items": {\n            "enum": [\n              "NONE",\n              "INTENSITY",\n              "ADJUSTMENT",\n              "DURATION",\n              "ALL",\n              "DEFAULTS"\n            ],\n            "type": "string"\n          },\n          "type": "array"\n        }\n      ]\n    },\n    "input_shapes": {\n      "description": "Length of the input array; zeros are used as default values. Alternative to default_variable \\u2014 do not specify both with mismatched sizes.",\n      "type": "integer"\n    },\n    "intensity_cost_fct": {\n      "description": "Name of the TransferFunction class used to compute intensity_cost from current intensity. Default: \'Exponential\'. Can be any function that takes and returns a scalar.",\n      "type": "string"\n    },\n    "name": {\n      "description": "Optional name for this function instance.",\n      "type": "string"\n    },\n    "transfer_fct": {\n      "description": "Name of the primary TransferFunction class applied to variable to produce the returned intensity. Defaults to \'Linear\'. Common options: \'Linear\', \'Logistic\', \'ReLU\', \'Exponential\', \'SoftMax\'.",\n      "type": "string"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\n- The default value for enabled_cost_functions is CostFunctions.DEFAULTS which resolves to CostFunctions.INTENSITY — so intensity cost IS active out of the box even if you pass no arguments.\n- Cost values (intensity_cost, adjustment_cost, duration_cost, combined_costs) are None until their respective cost function has been enabled at least once; they retain their last computed value even when disabled.\n- The function returns only the intensity (result of transfer_fct) — costs are side-effects stored as attributes, not part of the return value.\n- When assigned as the function of a ControlSignal, the cost function modulatory parameters (e.g., INTENSITY_COST_FCT_MULTIPLICATIVE_PARAM) become available for modulation by ModulatorySignals — this is the primary use case.\n- enabled_cost_functions is a bitmask (CostFunctions enum); passing a list of strings is supported by the constructor. Passing "NONE" explicitly disables all costs.\n- adjustment_cost measures |intensity_t - intensity_{t-1}|; the very first call has no history, so adjustment is computed against the initial variable default.\n- duration_cost is a cumulative integral — it only accumulates during time steps where DURATION is enabled, not across all time steps regardless of enable/disable cycling.\n- combine_costs_fct cannot be disabled (toggling it raises FunctionError); it always runs if any cost is enabled.\n- Function name strings (e.g., \'Linear\', \'Exponential\') must correspond to PsyNeuLink function classes importable from psyneulink; the host template resolves these names to class instances.'
TOOL_PARAMETERS = { 'properties': { 'adjustment_cost_fct': { 'description': 'Name of the '
                                                          'TransferFunction class used '
                                                          'to compute adjustment_cost '
                                                          'from the absolute change in '
                                                          'intensity between '
                                                          'successive calls. Default: '
                                                          "'Linear'.",
                                           'type': 'string'},
                  'combine_costs_fct': { 'description': 'Name of the function used to '
                                                        'aggregate all enabled cost '
                                                        'signals into combined_costs. '
                                                        "Default: 'LinearCombination' "
                                                        '(element-wise sum). Must '
                                                        'accept an array of cost '
                                                        'values and return a scalar.',
                                         'type': 'string'},
                  'default_variable': { 'description': 'Initial shape and value of the '
                                                       'input array. Determines the '
                                                       'dimensionality of the '
                                                       'function. Mutually exclusive '
                                                       'with input_shapes if lengths '
                                                       'disagree.',
                                        'items': {'type': 'number'},
                                        'type': 'array'},
                  'duration_cost_fct': { 'description': 'Name of the '
                                                        'IntegratorFunction class used '
                                                        'to compute duration_cost as a '
                                                        'running integral of '
                                                        'intensity. Default: '
                                                        "'SimpleIntegrator'. Only "
                                                        'accumulates during executions '
                                                        'where DURATION is enabled.',
                                         'type': 'string'},
                  'enabled_cost_functions': { 'description': 'Which cost functions to '
                                                             'execute on each call. '
                                                             "'INTENSITY' penalizes "
                                                             'output magnitude (via '
                                                             'Exponential by default), '
                                                             "'ADJUSTMENT' penalizes "
                                                             'change in output (via '
                                                             "Linear), 'DURATION' "
                                                             'penalizes cumulative '
                                                             'output (via '
                                                             'SimpleIntegrator). '
                                                             'Default is '
                                                             'CostFunctions.INTENSITY '
                                                             '(i.e., only intensity '
                                                             'cost is active).',
                                              'oneOf': [ { 'enum': [ 'NONE',
                                                                     'INTENSITY',
                                                                     'ADJUSTMENT',
                                                                     'DURATION',
                                                                     'ALL',
                                                                     'DEFAULTS'],
                                                           'type': 'string'},
                                                         { 'items': { 'enum': [ 'NONE',
                                                                                'INTENSITY',
                                                                                'ADJUSTMENT',
                                                                                'DURATION',
                                                                                'ALL',
                                                                                'DEFAULTS'],
                                                                      'type': 'string'},
                                                           'type': 'array'}]},
                  'input_shapes': { 'description': 'Length of the input array; zeros '
                                                   'are used as default values. '
                                                   'Alternative to default_variable — '
                                                   'do not specify both with '
                                                   'mismatched sizes.',
                                    'type': 'integer'},
                  'intensity_cost_fct': { 'description': 'Name of the TransferFunction '
                                                         'class used to compute '
                                                         'intensity_cost from current '
                                                         'intensity. Default: '
                                                         "'Exponential'. Can be any "
                                                         'function that takes and '
                                                         'returns a scalar.',
                                          'type': 'string'},
                  'name': { 'description': 'Optional name for this function instance.',
                            'type': 'string'},
                  'transfer_fct': { 'description': 'Name of the primary '
                                                   'TransferFunction class applied to '
                                                   'variable to produce the returned '
                                                   "intensity. Defaults to 'Linear'. "
                                                   "Common options: 'Linear', "
                                                   "'Logistic', 'ReLU', 'Exponential', "
                                                   "'SoftMax'.",
                                    'type': 'string'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = '- The default value for enabled_cost_functions is CostFunctions.DEFAULTS which resolves to CostFunctions.INTENSITY — so intensity cost IS active out of the box even if you pass no arguments.\n- Cost values (intensity_cost, adjustment_cost, duration_cost, combined_costs) are None until their respective cost function has been enabled at least once; they retain their last computed value even when disabled.\n- The function returns only the intensity (result of transfer_fct) — costs are side-effects stored as attributes, not part of the return value.\n- When assigned as the function of a ControlSignal, the cost function modulatory parameters (e.g., INTENSITY_COST_FCT_MULTIPLICATIVE_PARAM) become available for modulation by ModulatorySignals — this is the primary use case.\n- enabled_cost_functions is a bitmask (CostFunctions enum); passing a list of strings is supported by the constructor. Passing "NONE" explicitly disables all costs.\n- adjustment_cost measures |intensity_t - intensity_{t-1}|; the very first call has no history, so adjustment is computed against the initial variable default.\n- duration_cost is a cumulative integral — it only accumulates during time steps where DURATION is enabled, not across all time steps regardless of enable/disable cycling.\n- combine_costs_fct cannot be disabled (toggling it raises FunctionError); it always runs if any cost is enabled.\n- Function name strings (e.g., \'Linear\', \'Exponential\') must correspond to PsyNeuLink function classes importable from psyneulink; the host template resolves these names to class instances.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.TransferWithCosts
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
    def create_transfer_with_costs(args: dict[str, Any] | None = None) -> Any:
        'Use this tool to construct a TransferWithCosts function — a TransferFunction wrapper that applies a primary transfer transform (e.g., Linear, Logistic) to its input and optionally computes up to three cost signals (intensity, adjustment, duration) whose weighted sum is stored as combined_costs.'
        return _impl(args or {})
