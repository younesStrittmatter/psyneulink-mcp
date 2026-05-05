"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '1341f0b795006a851bea818be61460fa42686205be5853687d3b27ddf17579a7'
__pnl_qualname__ = 'psyneulink.NormalDist'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_normal_dist'
TOOL_DESCRIPTION = 'Use this tool to create a NormalDist function that samples from a Gaussian distribution, then assign it as the `function` parameter of a Mechanism (e.g., TransferMechanism) when you need stochastic normal noise or random normal outputs. The result is a configured NormalDist object; calling it returns a single float drawn from N(mean, standard_deviation).\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "mean": {\n      "default": 0,\n      "description": "Center of the normal distribution (additive modulatory parameter).",\n      "type": "number"\n    },\n    "name": {\n      "description": "Optional name for this function instance.",\n      "type": "string"\n    },\n    "params": {\n      "additionalProperties": true,\n      "description": "Optional parameter dictionary overriding constructor arguments (ParameterPort-style).",\n      "type": "object"\n    },\n    "seed": {\n      "description": "Optional seed for the internal random state, for reproducibility.",\n      "type": "integer"\n    },\n    "standard_deviation": {\n      "default": 1,\n      "description": "Spread of the distribution; must be >= 0.0. If 0.0, always returns mean.",\n      "type": "number"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\nstandard_deviation must be > 0 at runtime (validated); passing 0.0 is technically allowed and returns mean, but negative values raise FunctionError. The modulatory aliases are MULTIPLICATIVE_PARAM → standard_deviation and ADDITIVE_PARAM → mean, so ControlSignals targeting those aliases will scale/shift the distribution. Each call to the function draws one scalar float — not a vector. The internal random_state is derived from seed; omitting seed gives a non-reproducible sequence.'
TOOL_PARAMETERS = { 'properties': { 'mean': { 'default': 0,
                            'description': 'Center of the normal distribution '
                                           '(additive modulatory parameter).',
                            'type': 'number'},
                  'name': { 'description': 'Optional name for this function instance.',
                            'type': 'string'},
                  'params': { 'additionalProperties': True,
                              'description': 'Optional parameter dictionary overriding '
                                             'constructor arguments '
                                             '(ParameterPort-style).',
                              'type': 'object'},
                  'seed': { 'description': 'Optional seed for the internal random '
                                           'state, for reproducibility.',
                            'type': 'integer'},
                  'standard_deviation': { 'default': 1,
                                          'description': 'Spread of the distribution; '
                                                         'must be >= 0.0. If 0.0, '
                                                         'always returns mean.',
                                          'type': 'number'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = 'standard_deviation must be > 0 at runtime (validated); passing 0.0 is technically allowed and returns mean, but negative values raise FunctionError. The modulatory aliases are MULTIPLICATIVE_PARAM → standard_deviation and ADDITIVE_PARAM → mean, so ControlSignals targeting those aliases will scale/shift the distribution. Each call to the function draws one scalar float — not a vector. The internal random_state is derived from seed; omitting seed gives a non-reproducible sequence.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.NormalDist
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
    def create_normal_dist(args: dict[str, Any] | None = None) -> Any:
        'Use this tool to create a NormalDist function that samples from a Gaussian distribution, then assign it as the `function` parameter of a Mechanism (e.g., TransferMechanism) when you need stochastic normal noise or random normal outputs.'
        return _impl(args or {})
