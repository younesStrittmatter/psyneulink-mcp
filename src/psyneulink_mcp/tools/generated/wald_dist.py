"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '34c28b30fea634b84dc1c5f88269a30d970d7c1935e2d5ca1a75296394249575'
__pnl_qualname__ = 'psyneulink.WaldDist'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_wald_dist'
TOOL_DESCRIPTION = 'Call this tool to create a WaldDist (inverse Gaussian distribution) function for use as a noise or sampling source in a PsyNeuLink model. Use it when you need stochastic variability drawn from a Wald distribution — for example, to model reaction-time-like processes or positively-skewed random noise. Returns a configured WaldDist instance that produces a single scalar float sample on each call.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "mean": {\n      "default": 1,\n      "description": "Mean of the Wald distribution. Must be greater than or equal to zero. Acts as the ADDITIVE modulatory parameter.",\n      "type": "number"\n    },\n    "scale": {\n      "default": 1,\n      "description": "Scale (dispersion) parameter of the Wald distribution. Must be strictly greater than zero. Acts as the MULTIPLICATIVE modulatory parameter.",\n      "type": "number"\n    },\n    "seed": {\n      "description": "Integer seed for the internal numpy RandomState. Omit for a non-reproducible draw; supply a fixed integer for reproducibility.",\n      "type": "integer"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\nBoth `scale` and `mean` default to 1.0 if omitted. `scale` must be strictly > 0; `mean` must be >= 0 — numpy.random.wald will raise a ValueError otherwise. The function draws one scalar sample per call (not an array), so do not pass an array-valued `variable`. `seed` is not exposed in the docstring\'s primary argument list but is accepted by the constructor; include it when reproducibility is needed.'
TOOL_PARAMETERS = { 'properties': { 'mean': { 'default': 1,
                            'description': 'Mean of the Wald distribution. Must be '
                                           'greater than or equal to zero. Acts as the '
                                           'ADDITIVE modulatory parameter.',
                            'type': 'number'},
                  'scale': { 'default': 1,
                             'description': 'Scale (dispersion) parameter of the Wald '
                                            'distribution. Must be strictly greater '
                                            'than zero. Acts as the MULTIPLICATIVE '
                                            'modulatory parameter.',
                             'type': 'number'},
                  'seed': { 'description': 'Integer seed for the internal numpy '
                                           'RandomState. Omit for a non-reproducible '
                                           'draw; supply a fixed integer for '
                                           'reproducibility.',
                            'type': 'integer'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = "Both `scale` and `mean` default to 1.0 if omitted. `scale` must be strictly > 0; `mean` must be >= 0 — numpy.random.wald will raise a ValueError otherwise. The function draws one scalar sample per call (not an array), so do not pass an array-valued `variable`. `seed` is not exposed in the docstring's primary argument list but is accepted by the constructor; include it when reproducibility is needed."


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.WaldDist
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
    def create_wald_dist(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to create a WaldDist (inverse Gaussian distribution) function for use as a noise or sampling source in a PsyNeuLink model.'
        return _impl(args or {})
