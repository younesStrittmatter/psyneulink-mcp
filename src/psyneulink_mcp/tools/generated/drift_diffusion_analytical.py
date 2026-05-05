"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = 'f71856d008b4f7dedd922d7d98eea7db867caa3a2d48fdf618890a2a7b367fe1'
__pnl_qualname__ = 'psyneulink.DriftDiffusionAnalytical'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_drift_diffusion_analytical'
TOOL_DESCRIPTION = 'Call this tool to instantiate a DriftDiffusionAnalytical function that computes closed-form (Bogacz et al. 2006) solutions for the drift diffusion model. Use it when you need the analytical mean RT, error rate, and full conditional RT distribution moments (mean, variance, skew for upper/lower boundary responses) without running a simulation. The instantiated function returns an 8-element array: [mean_RT, error_rate, mean_rt_upper, var_rt_upper, skew_rt_upper, mean_rt_lower, var_rt_lower, skew_rt_lower].\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "drift_rate": {\n      "default": 1,\n      "description": "Drift rate of the DDM (attentional/baseline component). Multiplied by the stimulus input at call time to get effective drift. Acts as the MULTIPLICATIVE modulatory parameter.",\n      "type": "number"\n    },\n    "name": {\n      "description": "Optional name for the function instance. Auto-assigned by FunctionRegistry if omitted.",\n      "type": "string"\n    },\n    "noise": {\n      "default": 0.5,\n      "description": "Diffusion coefficient (standard deviation of the Gaussian noise term). Must be in [0, 1] when scalar.",\n      "type": "number"\n    },\n    "non_decision_time": {\n      "default": 0.2,\n      "description": "Non-decision time (seconds) added to the decision time to produce total RT. Must be in [0, 1] when scalar.",\n      "type": "number"\n    },\n    "shenhav_et_al_compat_mode": {\n      "default": false,\n      "description": "When true, replicates Shenhav et al. MATLAB DDM edge-case handling: floating-point overflows/underflows are suppressed, exponentials are clamped to [1e-12, 1e12], and negative decision times are floored to 0. Only set true when comparing against that MATLAB code.",\n      "type": "boolean"\n    },\n    "starting_value": {\n      "default": 0,\n      "description": "Initial value of the decision variable. Acts as the ADDITIVE modulatory parameter. Converted internally to a normalized bias: (starting_value + threshold) / (2 * threshold).",\n      "type": "number"\n    },\n    "threshold": {\n      "default": 1,\n      "description": "Decision boundary (symmetric, positive). Integration terminates when the decision variable reaches \\u00b1threshold.",\n      "type": "number"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\n- The docstring lists noise default as 0.0 but the Parameters class sets it to 0.5 — use 0.5 as the true default.\n- `default_variable` sets the shape template only; the actual stimulus drift rate is passed as the input when the function is called, and is multiplied by `drift_rate` to produce the effective drift. Do not confuse them.\n- Output index mapping: [0] mean RT, [1] error rate (p(lower boundary)), [2] mean_rt_upper, [3] var_rt_upper, [4] skew_rt_upper, [5] mean_rt_lower, [6] var_rt_lower, [7] skew_rt_lower. Error rate is relative to the upper boundary: values near 0 mean near-perfect upper-boundary accuracy.\n- `bias` is a read-only derived attribute; set `starting_value` to control it, not `bias` directly.\n- If |drift_rate * stimulus| < 1e-8, the function falls back to the zero-drift limit formula (Srivastava et al. 2016).\n- `noise` and `non_decision_time` must each be in [0, 1] when passed as scalars; array inputs must match the length of `default_variable`.'
TOOL_PARAMETERS = { 'properties': { 'drift_rate': { 'default': 1,
                                  'description': 'Drift rate of the DDM '
                                                 '(attentional/baseline component). '
                                                 'Multiplied by the stimulus input at '
                                                 'call time to get effective drift. '
                                                 'Acts as the MULTIPLICATIVE '
                                                 'modulatory parameter.',
                                  'type': 'number'},
                  'name': { 'description': 'Optional name for the function instance. '
                                           'Auto-assigned by FunctionRegistry if '
                                           'omitted.',
                            'type': 'string'},
                  'noise': { 'default': 0.5,
                             'description': 'Diffusion coefficient (standard deviation '
                                            'of the Gaussian noise term). Must be in '
                                            '[0, 1] when scalar.',
                             'type': 'number'},
                  'non_decision_time': { 'default': 0.2,
                                         'description': 'Non-decision time (seconds) '
                                                        'added to the decision time to '
                                                        'produce total RT. Must be in '
                                                        '[0, 1] when scalar.',
                                         'type': 'number'},
                  'shenhav_et_al_compat_mode': { 'default': False,
                                                 'description': 'When true, replicates '
                                                                'Shenhav et al. MATLAB '
                                                                'DDM edge-case '
                                                                'handling: '
                                                                'floating-point '
                                                                'overflows/underflows '
                                                                'are suppressed, '
                                                                'exponentials are '
                                                                'clamped to [1e-12, '
                                                                '1e12], and negative '
                                                                'decision times are '
                                                                'floored to 0. Only '
                                                                'set true when '
                                                                'comparing against '
                                                                'that MATLAB code.',
                                                 'type': 'boolean'},
                  'starting_value': { 'default': 0,
                                      'description': 'Initial value of the decision '
                                                     'variable. Acts as the ADDITIVE '
                                                     'modulatory parameter. Converted '
                                                     'internally to a normalized bias: '
                                                     '(starting_value + threshold) / '
                                                     '(2 * threshold).',
                                      'type': 'number'},
                  'threshold': { 'default': 1,
                                 'description': 'Decision boundary (symmetric, '
                                                'positive). Integration terminates '
                                                'when the decision variable reaches '
                                                '±threshold.',
                                 'type': 'number'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = '- The docstring lists noise default as 0.0 but the Parameters class sets it to 0.5 — use 0.5 as the true default.\n- `default_variable` sets the shape template only; the actual stimulus drift rate is passed as the input when the function is called, and is multiplied by `drift_rate` to produce the effective drift. Do not confuse them.\n- Output index mapping: [0] mean RT, [1] error rate (p(lower boundary)), [2] mean_rt_upper, [3] var_rt_upper, [4] skew_rt_upper, [5] mean_rt_lower, [6] var_rt_lower, [7] skew_rt_lower. Error rate is relative to the upper boundary: values near 0 mean near-perfect upper-boundary accuracy.\n- `bias` is a read-only derived attribute; set `starting_value` to control it, not `bias` directly.\n- If |drift_rate * stimulus| < 1e-8, the function falls back to the zero-drift limit formula (Srivastava et al. 2016).\n- `noise` and `non_decision_time` must each be in [0, 1] when passed as scalars; array inputs must match the length of `default_variable`.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.DriftDiffusionAnalytical
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
    def create_drift_diffusion_analytical(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to instantiate a DriftDiffusionAnalytical function that computes closed-form (Bogacz et al.'
        return _impl(args or {})
