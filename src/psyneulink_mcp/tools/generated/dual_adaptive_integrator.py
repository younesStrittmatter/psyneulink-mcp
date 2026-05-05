"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '05c0450033ed076eca460ac933998be5fc3343818509ec94c9bef9e615f01845'
__pnl_qualname__ = 'psyneulink.DualAdaptiveIntegrator'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_dual_adaptive_integrator'
TOOL_DESCRIPTION = 'Call this tool to create a DualAdaptiveIntegrator function that models utility integration over two time scales (fast/short and slow/long), as used in the Aston-Jones & Cohen (2005) locus coeruleus model. Each call instantiates the integrator with the given EWMA rates, logistic gains/biases, and combination operation; the result is a stateful function that, when executed, returns a scalar or array combining short-term and long-term exponentially-weighted averages of its input through logistic transforms.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "default_variable": {\n      "description": "Initial input value(s) used to set the shape of the integrator\'s variable. Scalar or 1d array.",\n      "type": [\n        "number",\n        "array"\n      ]\n    },\n    "initial_long_term_avg": {\n      "default": 0,\n      "description": "Starting value for the long-term EWMA accumulator (previous_long_term_avg).",\n      "type": "number"\n    },\n    "initial_short_term_avg": {\n      "default": 0,\n      "description": "Starting value for the short-term EWMA accumulator (previous_short_term_avg).",\n      "type": "number"\n    },\n    "long_term_bias": {\n      "default": 0,\n      "description": "Bias parameter for the logistic function applied to long_term_avg.",\n      "type": "number"\n    },\n    "long_term_gain": {\n      "default": 1,\n      "description": "Gain parameter for the logistic function applied to long_term_avg.",\n      "type": "number"\n    },\n    "long_term_rate": {\n      "default": 0.1,\n      "description": "EWMA smoothing factor for the long-term average; lower values produce slower integration. Must be in [0, 1].",\n      "type": "number"\n    },\n    "name": {\n      "description": "Optional name for this function instance; auto-assigned by FunctionRegistry if omitted.",\n      "type": "string"\n    },\n    "offset": {\n      "default": 0,\n      "description": "Constant added to the combined integral after each function call. Scalar applies to all elements; array must match variable length (Hadamard addition).",\n      "type": [\n        "number",\n        "array"\n      ]\n    },\n    "operation": {\n      "default": "PRODUCT",\n      "description": "How to combine the two logistic terms. PRODUCT=(1-short)*long; SUM=(1-short)+long; S_MINUS_L=(1-short)-long; L_MINUS_S=long-(1-short).",\n      "enum": [\n        "PRODUCT",\n        "SUM",\n        "S_MINUS_L",\n        "L_MINUS_S"\n      ],\n      "type": "string"\n    },\n    "short_term_bias": {\n      "default": 0,\n      "description": "Bias parameter for the logistic function applied to short_term_avg.",\n      "type": "number"\n    },\n    "short_term_gain": {\n      "default": 1,\n      "description": "Gain parameter for the logistic function applied to short_term_avg.",\n      "type": "number"\n    },\n    "short_term_rate": {\n      "default": 0.9,\n      "description": "EWMA smoothing factor for the short-term average; higher values track input more closely. Must be in [0, 1].",\n      "type": "number"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\n- The actual default for short_term_rate in the Parameters class is 0.9, and long_term_rate is 0.1 — NOT 1.0 as stated in the docstring constructor signature. The constructor accepts None and defers to these class defaults.\n- The short-term logistic is computed as (1 - logistic(short_term_avg)) while the long-term logistic is logistic(long_term_avg); their asymmetry is intentional per the Aston-Jones model.\n- Both rates must be in [0, 1]; passing values outside this range raises FunctionError.\n- operation must be one of the four string constants PRODUCT, SUM, S_MINUS_L, L_MINUS_S; any other value raises FunctionError.\n- The `initializer` parameter is accepted by the constructor but has no visible effect on short/long term avgs — use initial_short_term_avg and initial_long_term_avg instead.\n- State (previous_short_term_avg, previous_long_term_avg) is updated in-place on each execution call; to reset, call .reset(short, long) on the instantiated object.'
TOOL_PARAMETERS = { 'properties': { 'default_variable': { 'description': 'Initial input value(s) used to '
                                                       'set the shape of the '
                                                       "integrator's variable. Scalar "
                                                       'or 1d array.',
                                        'type': ['number', 'array']},
                  'initial_long_term_avg': { 'default': 0,
                                             'description': 'Starting value for the '
                                                            'long-term EWMA '
                                                            'accumulator '
                                                            '(previous_long_term_avg).',
                                             'type': 'number'},
                  'initial_short_term_avg': { 'default': 0,
                                              'description': 'Starting value for the '
                                                             'short-term EWMA '
                                                             'accumulator '
                                                             '(previous_short_term_avg).',
                                              'type': 'number'},
                  'long_term_bias': { 'default': 0,
                                      'description': 'Bias parameter for the logistic '
                                                     'function applied to '
                                                     'long_term_avg.',
                                      'type': 'number'},
                  'long_term_gain': { 'default': 1,
                                      'description': 'Gain parameter for the logistic '
                                                     'function applied to '
                                                     'long_term_avg.',
                                      'type': 'number'},
                  'long_term_rate': { 'default': 0.1,
                                      'description': 'EWMA smoothing factor for the '
                                                     'long-term average; lower values '
                                                     'produce slower integration. Must '
                                                     'be in [0, 1].',
                                      'type': 'number'},
                  'name': { 'description': 'Optional name for this function instance; '
                                           'auto-assigned by FunctionRegistry if '
                                           'omitted.',
                            'type': 'string'},
                  'offset': { 'default': 0,
                              'description': 'Constant added to the combined integral '
                                             'after each function call. Scalar applies '
                                             'to all elements; array must match '
                                             'variable length (Hadamard addition).',
                              'type': ['number', 'array']},
                  'operation': { 'default': 'PRODUCT',
                                 'description': 'How to combine the two logistic '
                                                'terms. PRODUCT=(1-short)*long; '
                                                'SUM=(1-short)+long; '
                                                'S_MINUS_L=(1-short)-long; '
                                                'L_MINUS_S=long-(1-short).',
                                 'enum': ['PRODUCT', 'SUM', 'S_MINUS_L', 'L_MINUS_S'],
                                 'type': 'string'},
                  'short_term_bias': { 'default': 0,
                                       'description': 'Bias parameter for the logistic '
                                                      'function applied to '
                                                      'short_term_avg.',
                                       'type': 'number'},
                  'short_term_gain': { 'default': 1,
                                       'description': 'Gain parameter for the logistic '
                                                      'function applied to '
                                                      'short_term_avg.',
                                       'type': 'number'},
                  'short_term_rate': { 'default': 0.9,
                                       'description': 'EWMA smoothing factor for the '
                                                      'short-term average; higher '
                                                      'values track input more '
                                                      'closely. Must be in [0, 1].',
                                       'type': 'number'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = '- The actual default for short_term_rate in the Parameters class is 0.9, and long_term_rate is 0.1 — NOT 1.0 as stated in the docstring constructor signature. The constructor accepts None and defers to these class defaults.\n- The short-term logistic is computed as (1 - logistic(short_term_avg)) while the long-term logistic is logistic(long_term_avg); their asymmetry is intentional per the Aston-Jones model.\n- Both rates must be in [0, 1]; passing values outside this range raises FunctionError.\n- operation must be one of the four string constants PRODUCT, SUM, S_MINUS_L, L_MINUS_S; any other value raises FunctionError.\n- The `initializer` parameter is accepted by the constructor but has no visible effect on short/long term avgs — use initial_short_term_avg and initial_long_term_avg instead.\n- State (previous_short_term_avg, previous_long_term_avg) is updated in-place on each execution call; to reset, call .reset(short, long) on the instantiated object.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.DualAdaptiveIntegrator
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
    def create_dual_adaptive_integrator(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to create a DualAdaptiveIntegrator function that models utility integration over two time scales (fast/short and slow/long), as used in the Aston-Jones & Cohen (2005) locus coeruleus model.'
        return _impl(args or {})
