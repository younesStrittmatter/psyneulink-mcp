"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = 'c096890e15fa9e6841e8ccbedbf0901e87b0c84720be05b644ea107c35b32fb3'
__pnl_qualname__ = 'psyneulink.Logistic'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_logistic'
TOOL_DESCRIPTION = 'Call this tool to instantiate a Logistic (sigmoid) transfer function for use as a PsyNeuLink Mechanism\'s function. Returns a Logistic object that maps input through scale * 1/(1 + e^(-gain*(variable + bias - x_0))) + offset, producing outputs in (0, 1) by default. Use this when you need a standard sigmoid activation, a gain-controlled squashing function, or a differentiable transfer function for backpropagation-based learning.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "bias": {\n      "default": 0,\n      "description": "Horizontal shift added to variable before gain is applied. Equivalent to x_0 but with opposite sign (ML convention). Default 0.0.",\n      "type": "number"\n    },\n    "default_variable": {\n      "description": "Template for the input value; sets the expected shape. Accepts a number or list of numbers.",\n      "oneOf": [\n        {\n          "type": "number"\n        },\n        {\n          "items": {\n            "type": "number"\n          },\n          "type": "array"\n        }\n      ]\n    },\n    "gain": {\n      "default": 1,\n      "description": "Slope/steepness of the sigmoid (k in standard logistic form). Multiplies (variable + bias - x_0) before exponentiation. Default 1.0.",\n      "type": "number"\n    },\n    "name": {\n      "description": "Optional string name for the Function instance.",\n      "type": "string"\n    },\n    "offset": {\n      "default": 0,\n      "description": "Constant added to the scaled output; translates the function vertically but is NOT modulated by gain. Default 0.0.",\n      "type": "number"\n    },\n    "scale": {\n      "default": 1,\n      "description": "Multiplier applied to the sigmoid output before adding offset (L in standard logistic form). Stretches the output range from (0,1) to (0, scale). Default 1.0.",\n      "type": "number"\n    },\n    "x_0": {\n      "default": 0,\n      "description": "Horizontal shift subtracted from variable before gain is applied (standard logistic convention). Equivalent to -bias. Default 0.0.",\n      "type": "number"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\nbias and x_0 have identical effects with opposite signs — do not set both non-zero unless you intend to combine them (net shift = bias - x_0). The unscaled output range is (0, 1); scale stretches it to (0, scale) and offset translates it, so the effective range becomes (offset, scale + offset). The derivative method operates on the *output* value (not the input), consistent with how BackPropagation LearningFunction uses it. params, owner, and prefs are framework-level arguments rarely needed by agents; omit them unless integrating into a larger PNL Component hierarchy.'
TOOL_PARAMETERS = { 'properties': { 'bias': { 'default': 0,
                            'description': 'Horizontal shift added to variable before '
                                           'gain is applied. Equivalent to x_0 but '
                                           'with opposite sign (ML convention). '
                                           'Default 0.0.',
                            'type': 'number'},
                  'default_variable': { 'description': 'Template for the input value; '
                                                       'sets the expected shape. '
                                                       'Accepts a number or list of '
                                                       'numbers.',
                                        'oneOf': [ {'type': 'number'},
                                                   { 'items': {'type': 'number'},
                                                     'type': 'array'}]},
                  'gain': { 'default': 1,
                            'description': 'Slope/steepness of the sigmoid (k in '
                                           'standard logistic form). Multiplies '
                                           '(variable + bias - x_0) before '
                                           'exponentiation. Default 1.0.',
                            'type': 'number'},
                  'name': { 'description': 'Optional string name for the Function '
                                           'instance.',
                            'type': 'string'},
                  'offset': { 'default': 0,
                              'description': 'Constant added to the scaled output; '
                                             'translates the function vertically but '
                                             'is NOT modulated by gain. Default 0.0.',
                              'type': 'number'},
                  'scale': { 'default': 1,
                             'description': 'Multiplier applied to the sigmoid output '
                                            'before adding offset (L in standard '
                                            'logistic form). Stretches the output '
                                            'range from (0,1) to (0, scale). Default '
                                            '1.0.',
                             'type': 'number'},
                  'x_0': { 'default': 0,
                           'description': 'Horizontal shift subtracted from variable '
                                          'before gain is applied (standard logistic '
                                          'convention). Equivalent to -bias. Default '
                                          '0.0.',
                           'type': 'number'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = 'bias and x_0 have identical effects with opposite signs — do not set both non-zero unless you intend to combine them (net shift = bias - x_0). The unscaled output range is (0, 1); scale stretches it to (0, scale) and offset translates it, so the effective range becomes (offset, scale + offset). The derivative method operates on the *output* value (not the input), consistent with how BackPropagation LearningFunction uses it. params, owner, and prefs are framework-level arguments rarely needed by agents; omit them unless integrating into a larger PNL Component hierarchy.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.Logistic
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
    def create_logistic(args: dict[str, Any] | None = None) -> Any:
        "Call this tool to instantiate a Logistic (sigmoid) transfer function for use as a PsyNeuLink Mechanism's function."
        return _impl(args or {})
