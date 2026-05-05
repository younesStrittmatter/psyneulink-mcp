"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '9e5ad54ea680094fd37882b0e512b2ac0fe9e57d5b682717950805734180965b'
__pnl_qualname__ = 'psyneulink.DDM'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_ddm'
TOOL_DESCRIPTION = 'Call this tool to instantiate a Drift Diffusion Model (DDM) Mechanism that simulates evidence accumulation toward a decision threshold. Use it when modeling speeded two-alternative forced-choice decisions requiring reaction time distributions and/or decision accuracy. Returns a DDM Mechanism with at minimum DECISION_VARIABLE and RESPONSE_TIME output ports; analytic mode additionally returns probability-correct and full RT distribution statistics (mean, variance, skew for correct and incorrect responses).\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "default_variable": {\n      "description": "Default input to the mechanism when none is provided at execution time. Serves as the stimulus component of the drift rate. Must resolve to a single numeric value unless input_format is ARRAY or VECTOR.",\n      "oneOf": [\n        {\n          "type": "number"\n        },\n        {\n          "items": {\n            "type": "number"\n          },\n          "type": "array"\n        }\n      ]\n    },\n    "function": {\n      "default": "DriftDiffusionAnalytical",\n      "description": "DriftDiffusionAnalytical (default): computes closed-form analytic solution per trial; returns mean RT, accuracy, and RT statistics. DriftDiffusionIntegrator: performs step-wise numerical integration; DECISION_VARIABLE is current accumulator value at each TIME_STEP, PROBABILITY outputs are unavailable.",\n      "enum": [\n        "DriftDiffusionAnalytical",\n        "DriftDiffusionIntegrator"\n      ],\n      "type": "string"\n    },\n    "input_format": {\n      "default": "SCALAR",\n      "description": "SCALAR (default): single numeric input. ARRAY or VECTOR: accepts a 2-element array [correct_stimulus, incorrect_stimulus] and adds DECISION_VARIABLE_ARRAY and SELECTED_INPUT_ARRAY output ports.",\n      "enum": [\n        "SCALAR",\n        "ARRAY",\n        "VECTOR"\n      ],\n      "type": "string"\n    },\n    "name": {\n      "description": "Name for the DDM mechanism instance.",\n      "type": "string"\n    },\n    "output_ports": {\n      "description": "List of output ports to expose. Defaults to [DECISION_VARIABLE, RESPONSE_TIME]. RT_* and PROBABILITY_* ports are only meaningful in analytic mode (DriftDiffusionAnalytical). DECISION_OUTCOME returns 1.0 if decision variable is positive, 0 otherwise.",\n      "items": {\n        "enum": [\n          "DECISION_VARIABLE",\n          "RESPONSE_TIME",\n          "DECISION_OUTCOME",\n          "PROBABILITY_UPPER_THRESHOLD",\n          "PROBABILITY_LOWER_THRESHOLD",\n          "RT_CORRECT_MEAN",\n          "RT_CORRECT_VARIANCE",\n          "RT_CORRECT_SKEW",\n          "RT_INCORRECT_MEAN",\n          "RT_INCORRECT_VARIANCE",\n          "RT_INCORRECT_SKEW"\n        ],\n        "type": "string"\n      },\n      "type": "array"\n    },\n    "seed": {\n      "description": "Random seed for reproducible stochastic results (used in analytic mode when sampling decision outcome from error rate).",\n      "type": "integer"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\nDefault DriftDiffusionAnalytical parameters: drift_rate=1.0, starting_value=0.0, threshold=1.0, noise=0.5, non_decision_time=0.200. These are set on the function object, not directly on DDM — to change them, construct DriftDiffusionAnalytical with custom values and pass it as the function argument.\n\nexecute_until_finished defaults to True: the DDM will loop internally until the decision threshold is crossed (or max_executions_before_finished is reached, set to sys.maxsize), consuming multiple TIME_STEPs per call to execute().\n\nIntegration state resets at each trial start by default (reset_stateful_function_when=AtTrialStart()). Override by passing reset_stateful_function_when as a kwarg.\n\nIn analytic mode (DriftDiffusionAnalytical), DECISION_VARIABLE is the threshold value (positive or negative) reached, not a continuous accumulator trajectory. In integration mode (DriftDiffusionIntegrator), DECISION_VARIABLE is the current accumulator position at each TIME_STEP.\n\nDECISION_VARIABLE_ARRAY and SELECTED_INPUT_ARRAY output ports are only available when input_format is ARRAY or VECTOR; requesting them with SCALAR input_format will fail.\n\ninput_format and input_ports are mutually exclusive — do not pass both.\n\nThe function parameter in this schema accepts a string class name; the underlying PNL call requires a function object instance. Pass the pre-constructed function object when custom function parameters (drift_rate, threshold, noise, non_decision_time, starting_value) are needed.'
TOOL_PARAMETERS = { 'properties': { 'default_variable': { 'description': 'Default input to the mechanism '
                                                       'when none is provided at '
                                                       'execution time. Serves as the '
                                                       'stimulus component of the '
                                                       'drift rate. Must resolve to a '
                                                       'single numeric value unless '
                                                       'input_format is ARRAY or '
                                                       'VECTOR.',
                                        'oneOf': [ {'type': 'number'},
                                                   { 'items': {'type': 'number'},
                                                     'type': 'array'}]},
                  'function': { 'default': 'DriftDiffusionAnalytical',
                                'description': 'DriftDiffusionAnalytical (default): '
                                               'computes closed-form analytic solution '
                                               'per trial; returns mean RT, accuracy, '
                                               'and RT statistics. '
                                               'DriftDiffusionIntegrator: performs '
                                               'step-wise numerical integration; '
                                               'DECISION_VARIABLE is current '
                                               'accumulator value at each TIME_STEP, '
                                               'PROBABILITY outputs are unavailable.',
                                'enum': [ 'DriftDiffusionAnalytical',
                                          'DriftDiffusionIntegrator'],
                                'type': 'string'},
                  'input_format': { 'default': 'SCALAR',
                                    'description': 'SCALAR (default): single numeric '
                                                   'input. ARRAY or VECTOR: accepts a '
                                                   '2-element array [correct_stimulus, '
                                                   'incorrect_stimulus] and adds '
                                                   'DECISION_VARIABLE_ARRAY and '
                                                   'SELECTED_INPUT_ARRAY output ports.',
                                    'enum': ['SCALAR', 'ARRAY', 'VECTOR'],
                                    'type': 'string'},
                  'name': { 'description': 'Name for the DDM mechanism instance.',
                            'type': 'string'},
                  'output_ports': { 'description': 'List of output ports to expose. '
                                                   'Defaults to [DECISION_VARIABLE, '
                                                   'RESPONSE_TIME]. RT_* and '
                                                   'PROBABILITY_* ports are only '
                                                   'meaningful in analytic mode '
                                                   '(DriftDiffusionAnalytical). '
                                                   'DECISION_OUTCOME returns 1.0 if '
                                                   'decision variable is positive, 0 '
                                                   'otherwise.',
                                    'items': { 'enum': [ 'DECISION_VARIABLE',
                                                         'RESPONSE_TIME',
                                                         'DECISION_OUTCOME',
                                                         'PROBABILITY_UPPER_THRESHOLD',
                                                         'PROBABILITY_LOWER_THRESHOLD',
                                                         'RT_CORRECT_MEAN',
                                                         'RT_CORRECT_VARIANCE',
                                                         'RT_CORRECT_SKEW',
                                                         'RT_INCORRECT_MEAN',
                                                         'RT_INCORRECT_VARIANCE',
                                                         'RT_INCORRECT_SKEW'],
                                               'type': 'string'},
                                    'type': 'array'},
                  'seed': { 'description': 'Random seed for reproducible stochastic '
                                           'results (used in analytic mode when '
                                           'sampling decision outcome from error '
                                           'rate).',
                            'type': 'integer'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = 'Default DriftDiffusionAnalytical parameters: drift_rate=1.0, starting_value=0.0, threshold=1.0, noise=0.5, non_decision_time=0.200. These are set on the function object, not directly on DDM — to change them, construct DriftDiffusionAnalytical with custom values and pass it as the function argument.\n\nexecute_until_finished defaults to True: the DDM will loop internally until the decision threshold is crossed (or max_executions_before_finished is reached, set to sys.maxsize), consuming multiple TIME_STEPs per call to execute().\n\nIntegration state resets at each trial start by default (reset_stateful_function_when=AtTrialStart()). Override by passing reset_stateful_function_when as a kwarg.\n\nIn analytic mode (DriftDiffusionAnalytical), DECISION_VARIABLE is the threshold value (positive or negative) reached, not a continuous accumulator trajectory. In integration mode (DriftDiffusionIntegrator), DECISION_VARIABLE is the current accumulator position at each TIME_STEP.\n\nDECISION_VARIABLE_ARRAY and SELECTED_INPUT_ARRAY output ports are only available when input_format is ARRAY or VECTOR; requesting them with SCALAR input_format will fail.\n\ninput_format and input_ports are mutually exclusive — do not pass both.\n\nThe function parameter in this schema accepts a string class name; the underlying PNL call requires a function object instance. Pass the pre-constructed function object when custom function parameters (drift_rate, threshold, noise, non_decision_time, starting_value) are needed.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.DDM
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
    def create_ddm(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to instantiate a Drift Diffusion Model (DDM) Mechanism that simulates evidence accumulation toward a decision threshold.'
        return _impl(args or {})
