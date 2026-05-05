"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '33754984f8bbdcc29253a52d6483213a9c9049f489e1c2525319fa92f5b67cfd'
__pnl_qualname__ = 'psyneulink.ExponentialDist'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_exponential_dist'
TOOL_DESCRIPTION = 'Use this tool to create an ExponentialDist function that samples from an exponential distribution — call it when you need a stochastic noise source, inter-arrival time generator, or any component that draws from an exponential distribution with a given scale. The result is a single float sampled via numpy.random.exponential(beta).\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "beta": {\n      "default": 1,\n      "description": "Scale parameter (mean) of the exponential distribution. Must be positive. Also serves as the MULTIPLICATIVE_PARAM for modulatory control.",\n      "type": "number"\n    },\n    "name": {\n      "description": "Optional name for this function instance.",\n      "type": "string"\n    },\n    "params": {\n      "additionalProperties": true,\n      "description": "Optional parameter dictionary to override constructor arguments at instantiation. Keys are PsyNeuLink parameter keywords.",\n      "type": "object"\n    },\n    "seed": {\n      "description": "Optional integer seed for the internal numpy RandomState, enabling reproducible sampling. Omit for non-deterministic behavior.",\n      "type": "integer"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\nbeta is the scale (mean) of the exponential distribution, not the rate (lambda). If you have a rate lambda, pass beta=1/lambda. The random_state is managed internally and derived from seed — do not pass random_state directly. beta is modulable (MULTIPLICATIVE_PARAM), so it can be controlled by a ModulatorySignal at runtime. Each call to the function draws a fresh sample; there is no batching — the output is always a scalar float.'
TOOL_PARAMETERS = { 'properties': { 'beta': { 'default': 1,
                            'description': 'Scale parameter (mean) of the exponential '
                                           'distribution. Must be positive. Also '
                                           'serves as the MULTIPLICATIVE_PARAM for '
                                           'modulatory control.',
                            'type': 'number'},
                  'name': { 'description': 'Optional name for this function instance.',
                            'type': 'string'},
                  'params': { 'additionalProperties': True,
                              'description': 'Optional parameter dictionary to '
                                             'override constructor arguments at '
                                             'instantiation. Keys are PsyNeuLink '
                                             'parameter keywords.',
                              'type': 'object'},
                  'seed': { 'description': 'Optional integer seed for the internal '
                                           'numpy RandomState, enabling reproducible '
                                           'sampling. Omit for non-deterministic '
                                           'behavior.',
                            'type': 'integer'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = 'beta is the scale (mean) of the exponential distribution, not the rate (lambda). If you have a rate lambda, pass beta=1/lambda. The random_state is managed internally and derived from seed — do not pass random_state directly. beta is modulable (MULTIPLICATIVE_PARAM), so it can be controlled by a ModulatorySignal at runtime. Each call to the function draws a fresh sample; there is no batching — the output is always a scalar float.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.ExponentialDist
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
    def create_exponential_dist(args: dict[str, Any] | None = None) -> Any:
        'Use this tool to create an ExponentialDist function that samples from an exponential distribution — call it when you need a stochastic noise source, inter-arrival time generator, or any component that draws from an exponential distribution with a given scale.'
        return _impl(args or {})
