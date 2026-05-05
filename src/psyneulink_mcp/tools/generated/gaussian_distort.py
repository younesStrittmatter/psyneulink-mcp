"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = 'ea7431e6ca9f8461a43cf8344fa478888a473136acfef6814e42861740f78fcb'
__pnl_qualname__ = 'psyneulink.GaussianDistort'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_gaussian_distort'
TOOL_DESCRIPTION = 'Call this tool to add stochastic Gaussian noise to an input signal — it draws a random sample from a Gaussian distribution centered at each input element (shifted by bias), then scales and offsets the result. Use this when you want a noisy or jittered version of an input array, not a deterministic transform. Do NOT use this if you want the Gaussian probability density value at the input; use `Gaussian` for that.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "bias": {\n      "default": 0,\n      "description": "Value added to each element of the input before drawing the sample (shifts the distribution mean).",\n      "type": "number"\n    },\n    "default_variable": {\n      "description": "Template for the input value(s) that will serve as the mean of the Gaussian distribution. Can be a number or array.",\n      "oneOf": [\n        {\n          "type": "number"\n        },\n        {\n          "items": {\n            "type": "number"\n          },\n          "type": "array"\n        }\n      ]\n    },\n    "name": {\n      "description": "Optional name for the function instance.",\n      "type": "string"\n    },\n    "offset": {\n      "default": 0,\n      "description": "Value added to each sample after scale is applied.",\n      "type": "number"\n    },\n    "scale": {\n      "default": 1,\n      "description": "Multiplier applied to each drawn sample.",\n      "type": "number"\n    },\n    "seed": {\n      "description": "Seed for the random number generator. Set for reproducibility; omit for non-deterministic sampling.",\n      "type": "integer"\n    },\n    "variance": {\n      "default": 1,\n      "description": "Controls the width of the Gaussian distribution. NOTE: despite the name, this value is passed as the standard deviation to numpy\'s normal(), not as the variance.",\n      "type": "number"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\nCritical naming mismatch: the `variance` parameter is passed directly to numpy.random.normal() as its `scale` argument, which numpy defines as the **standard deviation**, not the variance. So `variance=2.0` produces samples spread with σ=2, not σ²=2. The output formula is: scale * N(variable + bias, variance) + offset. Each call produces a new random sample — calling the same function twice with the same input gives different results unless `seed` is fixed. For the deterministic Gaussian PDF transform, use `Gaussian` instead.'
TOOL_PARAMETERS = { 'properties': { 'bias': { 'default': 0,
                            'description': 'Value added to each element of the input '
                                           'before drawing the sample (shifts the '
                                           'distribution mean).',
                            'type': 'number'},
                  'default_variable': { 'description': 'Template for the input '
                                                       'value(s) that will serve as '
                                                       'the mean of the Gaussian '
                                                       'distribution. Can be a number '
                                                       'or array.',
                                        'oneOf': [ {'type': 'number'},
                                                   { 'items': {'type': 'number'},
                                                     'type': 'array'}]},
                  'name': { 'description': 'Optional name for the function instance.',
                            'type': 'string'},
                  'offset': { 'default': 0,
                              'description': 'Value added to each sample after scale '
                                             'is applied.',
                              'type': 'number'},
                  'scale': { 'default': 1,
                             'description': 'Multiplier applied to each drawn sample.',
                             'type': 'number'},
                  'seed': { 'description': 'Seed for the random number generator. Set '
                                           'for reproducibility; omit for '
                                           'non-deterministic sampling.',
                            'type': 'integer'},
                  'variance': { 'default': 1,
                                'description': 'Controls the width of the Gaussian '
                                               'distribution. NOTE: despite the name, '
                                               'this value is passed as the standard '
                                               "deviation to numpy's normal(), not as "
                                               'the variance.',
                                'type': 'number'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = 'Critical naming mismatch: the `variance` parameter is passed directly to numpy.random.normal() as its `scale` argument, which numpy defines as the **standard deviation**, not the variance. So `variance=2.0` produces samples spread with σ=2, not σ²=2. The output formula is: scale * N(variable + bias, variance) + offset. Each call produces a new random sample — calling the same function twice with the same input gives different results unless `seed` is fixed. For the deterministic Gaussian PDF transform, use `Gaussian` instead.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.GaussianDistort
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
    def create_gaussian_distort(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to add stochastic Gaussian noise to an input signal — it draws a random sample from a Gaussian distribution centered at each input element (shifted by bias), then scales and offsets the result.'
        return _impl(args or {})
