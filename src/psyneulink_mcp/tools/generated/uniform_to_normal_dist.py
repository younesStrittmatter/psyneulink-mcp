"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '00c34c8be4e1152c81860691c853799691b0a9f58c10ef6871275542b10673ca'
__pnl_qualname__ = 'psyneulink.UniformToNormalDist'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_uniform_to_normal_dist'
TOOL_DESCRIPTION = 'Call this tool to create a UniformToNormalDist function that generates random samples from a normal distribution via a uniform-to-normal conversion (MATLAB-compatible). Use it when you need a normally-distributed random draw and want behavior that matches MATLAB\'s randn — the output is a scalar float sampled from N(mean, standard_deviation²).\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "mean": {\n      "default": 0,\n      "description": "Center of the normal distribution. Acts as the additive modulatory parameter.",\n      "type": "number"\n    },\n    "name": {\n      "description": "Optional name for this function instance.",\n      "type": "string"\n    },\n    "params": {\n      "additionalProperties": true,\n      "description": "Optional parameter dictionary to override mean or standard_deviation. Keys are PNL parameter keywords.",\n      "type": "object"\n    },\n    "seed": {\n      "description": "Optional integer seed for the internal numpy RandomState, enabling reproducible samples.",\n      "type": "integer"\n    },\n    "standard_deviation": {\n      "default": 1,\n      "description": "Standard deviation of the normal distribution. Must be > 0. Acts as the multiplicative modulatory parameter.",\n      "type": "number"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\nRequires SciPy (scipy.special.erfinv) at runtime — will raise ImportError if SciPy is not installed. The conversion uses np.random.rand internally, not np.random.randn, so results are statistically equivalent to a standard normal draw but differ in the exact random-number stream; this is intentional for MATLAB parity. standard_deviation must be positive; passing 0 or negative values will produce nonsensical output without an explicit error from PNL. Each call draws exactly one scalar sample. If used as a component function (owner set), the seed/random_state is managed by PNL\'s context system.'
TOOL_PARAMETERS = { 'properties': { 'mean': { 'default': 0,
                            'description': 'Center of the normal distribution. Acts as '
                                           'the additive modulatory parameter.',
                            'type': 'number'},
                  'name': { 'description': 'Optional name for this function instance.',
                            'type': 'string'},
                  'params': { 'additionalProperties': True,
                              'description': 'Optional parameter dictionary to '
                                             'override mean or standard_deviation. '
                                             'Keys are PNL parameter keywords.',
                              'type': 'object'},
                  'seed': { 'description': 'Optional integer seed for the internal '
                                           'numpy RandomState, enabling reproducible '
                                           'samples.',
                            'type': 'integer'},
                  'standard_deviation': { 'default': 1,
                                          'description': 'Standard deviation of the '
                                                         'normal distribution. Must be '
                                                         '> 0. Acts as the '
                                                         'multiplicative modulatory '
                                                         'parameter.',
                                          'type': 'number'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = "Requires SciPy (scipy.special.erfinv) at runtime — will raise ImportError if SciPy is not installed. The conversion uses np.random.rand internally, not np.random.randn, so results are statistically equivalent to a standard normal draw but differ in the exact random-number stream; this is intentional for MATLAB parity. standard_deviation must be positive; passing 0 or negative values will produce nonsensical output without an explicit error from PNL. Each call draws exactly one scalar sample. If used as a component function (owner set), the seed/random_state is managed by PNL's context system."


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.UniformToNormalDist
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
    def create_uniform_to_normal_dist(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to create a UniformToNormalDist function that generates random samples from a normal distribution via a uniform-to-normal conversion (MATLAB-compatible).'
        return _impl(args or {})
