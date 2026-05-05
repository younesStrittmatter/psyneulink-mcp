"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = 'db6a18a34e15a88302a2d08760465ae7bc04477da2a67f39145a6833f11cc8ef'
__pnl_qualname__ = 'psyneulink.PredictionErrorDeltaFunction'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_prediction_error_delta_function'
TOOL_DESCRIPTION = 'Call this tool when you need to compute temporal difference (TD) prediction error signals — used in reinforcement learning models where you want δ(t) = r(t) + γ·sample(t) − sample(t−1) across a time series. Returns a 1D array of delta values with the same length as the input arrays (delta[0] is always 0 since there is no prior sample).\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "default_variable": {\n      "description": "A 2-element list of equal-length numeric arrays: [[sample_t0, sample_t1, ...], [reward_t0, reward_t1, ...]]. variable[0] is the predicted value (sample) time series; variable[1] is the reward time series. Both inner arrays must have the same length.",\n      "items": {\n        "items": {\n          "type": "number"\n        },\n        "type": "array"\n      },\n      "maxItems": 2,\n      "minItems": 2,\n      "type": "array"\n    },\n    "gamma": {\n      "default": 1,\n      "description": "Discount factor for future predicted values. Typically in [0, 1] for standard TD learning (0 = no future discounting, 1 = no discounting). Default is 1.0.",\n      "type": "number"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\n- `default_variable` must be a 2D structure with exactly 2 rows of equal length; mismatched lengths raise a FunctionError.\n- delta[0] is always 0.0 — the formula requires a prior sample(t−1), which does not exist at t=0.\n- gamma defaults to 1.0 (no discounting); for typical TD learning you likely want a value like 0.95.\n- The returned array has the same shape as each input row (1D, length T).\n- This class only defines the function; to use it standalone call it via its `.function()` method or pass it as the `function` argument to a PsyNeuLink Mechanism.'
TOOL_PARAMETERS = { 'properties': { 'default_variable': { 'description': 'A 2-element list of '
                                                       'equal-length numeric arrays: '
                                                       '[[sample_t0, sample_t1, ...], '
                                                       '[reward_t0, reward_t1, ...]]. '
                                                       'variable[0] is the predicted '
                                                       'value (sample) time series; '
                                                       'variable[1] is the reward time '
                                                       'series. Both inner arrays must '
                                                       'have the same length.',
                                        'items': { 'items': {'type': 'number'},
                                                   'type': 'array'},
                                        'maxItems': 2,
                                        'minItems': 2,
                                        'type': 'array'},
                  'gamma': { 'default': 1,
                             'description': 'Discount factor for future predicted '
                                            'values. Typically in [0, 1] for standard '
                                            'TD learning (0 = no future discounting, 1 '
                                            '= no discounting). Default is 1.0.',
                             'type': 'number'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = '- `default_variable` must be a 2D structure with exactly 2 rows of equal length; mismatched lengths raise a FunctionError.\n- delta[0] is always 0.0 — the formula requires a prior sample(t−1), which does not exist at t=0.\n- gamma defaults to 1.0 (no discounting); for typical TD learning you likely want a value like 0.95.\n- The returned array has the same shape as each input row (1D, length T).\n- This class only defines the function; to use it standalone call it via its `.function()` method or pass it as the `function` argument to a PsyNeuLink Mechanism.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.PredictionErrorDeltaFunction
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
    def create_prediction_error_delta_function(args: dict[str, Any] | None = None) -> Any:
        'Call this tool when you need to compute temporal difference (TD) prediction error signals — used in reinforcement learning models where you want δ(t) = r(t) + γ·sample(t) − sample(t−1) across a time series.'
        return _impl(args or {})
