"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '8164e02fa55420005bdd5212790408547248dfb9114d4201766cb46dcc6a51a3'
__pnl_qualname__ = 'psyneulink.GammaDist'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_gamma_dist'
TOOL_DESCRIPTION = 'Call this tool when you need a PsyNeuLink function that samples from a gamma distribution — for example, to model reaction-time variability, inter-spike intervals, or any non-negative skewed noise source. The tool instantiates a GammaDist object whose `function()` call returns a single float drawn from numpy.random.gamma(dist_shape, scale).\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "dist_shape": {\n      "default": 1,\n      "description": "Shape parameter (k) of the gamma distribution. Must be > 0. Acts as the ADDITIVE modulatory parameter.",\n      "type": "number"\n    },\n    "name": {\n      "description": "Optional name for the GammaDist instance.",\n      "type": "string"\n    },\n    "scale": {\n      "default": 1,\n      "description": "Scale parameter (theta) of the gamma distribution. Must be > 0. Acts as the MULTIPLICATIVE modulatory parameter.",\n      "type": "number"\n    },\n    "seed": {\n      "description": "Seed for the internal numpy RandomState. Omit for non-deterministic sampling.",\n      "type": "integer"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\nnumpy.random.gamma uses the (shape, scale) parameterization — mean = dist_shape * scale, variance = dist_shape * scale^2. Both scale and dist_shape must be strictly greater than zero; passing zero or negative values will raise an error at call time. The random state is internal; pass `seed` for reproducibility. `params`, `owner`, and `prefs` are PsyNeuLink-internal wiring arguments not needed for standalone use.'
TOOL_PARAMETERS = { 'properties': { 'dist_shape': { 'default': 1,
                                  'description': 'Shape parameter (k) of the gamma '
                                                 'distribution. Must be > 0. Acts as '
                                                 'the ADDITIVE modulatory parameter.',
                                  'type': 'number'},
                  'name': { 'description': 'Optional name for the GammaDist instance.',
                            'type': 'string'},
                  'scale': { 'default': 1,
                             'description': 'Scale parameter (theta) of the gamma '
                                            'distribution. Must be > 0. Acts as the '
                                            'MULTIPLICATIVE modulatory parameter.',
                             'type': 'number'},
                  'seed': { 'description': 'Seed for the internal numpy RandomState. '
                                           'Omit for non-deterministic sampling.',
                            'type': 'integer'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = 'numpy.random.gamma uses the (shape, scale) parameterization — mean = dist_shape * scale, variance = dist_shape * scale^2. Both scale and dist_shape must be strictly greater than zero; passing zero or negative values will raise an error at call time. The random state is internal; pass `seed` for reproducibility. `params`, `owner`, and `prefs` are PsyNeuLink-internal wiring arguments not needed for standalone use.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.GammaDist
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
    def create_gamma_dist(args: dict[str, Any] | None = None) -> Any:
        'Call this tool when you need a PsyNeuLink function that samples from a gamma distribution — for example, to model reaction-time variability, inter-spike intervals, or any non-negative skewed noise source.'
        return _impl(args or {})
