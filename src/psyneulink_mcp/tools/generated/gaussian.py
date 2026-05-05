"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = 'b9486534d1ab0a3330566ed277eee6bf996f02e3823408c72fd2a069f09215e5'
__pnl_qualname__ = 'psyneulink.Gaussian'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_gaussian'
TOOL_DESCRIPTION = 'Call this tool to create a Gaussian transfer function that maps input values to their Gaussian probability density function (PDF) values. Use it when building a PsyNeuLink mechanism or composition that needs a bell-curve-shaped activation function — e.g., radial basis function units, tuning curves, or any model where output should peak at a preferred input value and decay with distance. The result is a `psyneulink.Gaussian` instance whose `function` method returns `scale * exp(-(x-bias)^2 / (2*sigma^2)) / sqrt(2*pi*sigma) + offset` for each element of the input array.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "bias": {\n      "default": 0,\n      "description": "Value subtracted from each input element before applying the Gaussian transform, effectively shifting the peak of the bell curve. Default is 0.0.",\n      "type": "number"\n    },\n    "default_variable": {\n      "description": "Template for the input \\u2014 a number or list of numbers that sets the shape/dimensionality of the variable. Defines the mean input around which the Gaussian is evaluated.",\n      "oneOf": [\n        {\n          "type": "number"\n        },\n        {\n          "items": {\n            "type": "number"\n          },\n          "type": "array"\n        }\n      ]\n    },\n    "name": {\n      "description": "Optional string name for this function instance. If omitted, PsyNeuLink assigns a default name via FunctionRegistry.",\n      "type": "string"\n    },\n    "offset": {\n      "default": 0,\n      "description": "Additive constant applied to the output after scale is applied. Shifts the entire output up or down. Default is 0.0.",\n      "type": "number"\n    },\n    "scale": {\n      "default": 1,\n      "description": "Multiplicative factor applied to the Gaussian output before adding offset. Controls the amplitude of the bell curve. Default is 1.0.",\n      "type": "number"\n    },\n    "standard_deviation": {\n      "default": 1,\n      "description": "Width (sigma) of the Gaussian bell curve. Larger values produce a wider, flatter curve. Default is 1.0.",\n      "type": "number"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\nCRITICAL: This function returns the deterministic PDF value at the input point — it is NOT a stochastic sampler. If you want to add Gaussian noise to a signal (i.e., randomly sample from a Gaussian distribution centered on the input), use `GaussianDistort` instead. The output for a unit-normal (sigma=1, bias=0, scale=1, offset=0) input of 0.0 is ~0.3989 (the peak of the standard normal PDF), not 1.0. The `bias` parameter shifts the peak location: peak occurs at `variable == bias`. Unscaled output values are always in (0, 1/sqrt(2*pi*sigma)] — apply `scale` and `offset` to fit your model\'s expected activation range.'
TOOL_PARAMETERS = { 'properties': { 'bias': { 'default': 0,
                            'description': 'Value subtracted from each input element '
                                           'before applying the Gaussian transform, '
                                           'effectively shifting the peak of the bell '
                                           'curve. Default is 0.0.',
                            'type': 'number'},
                  'default_variable': { 'description': 'Template for the input — a '
                                                       'number or list of numbers that '
                                                       'sets the shape/dimensionality '
                                                       'of the variable. Defines the '
                                                       'mean input around which the '
                                                       'Gaussian is evaluated.',
                                        'oneOf': [ {'type': 'number'},
                                                   { 'items': {'type': 'number'},
                                                     'type': 'array'}]},
                  'name': { 'description': 'Optional string name for this function '
                                           'instance. If omitted, PsyNeuLink assigns a '
                                           'default name via FunctionRegistry.',
                            'type': 'string'},
                  'offset': { 'default': 0,
                              'description': 'Additive constant applied to the output '
                                             'after scale is applied. Shifts the '
                                             'entire output up or down. Default is '
                                             '0.0.',
                              'type': 'number'},
                  'scale': { 'default': 1,
                             'description': 'Multiplicative factor applied to the '
                                            'Gaussian output before adding offset. '
                                            'Controls the amplitude of the bell curve. '
                                            'Default is 1.0.',
                             'type': 'number'},
                  'standard_deviation': { 'default': 1,
                                          'description': 'Width (sigma) of the '
                                                         'Gaussian bell curve. Larger '
                                                         'values produce a wider, '
                                                         'flatter curve. Default is '
                                                         '1.0.',
                                          'type': 'number'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = "CRITICAL: This function returns the deterministic PDF value at the input point — it is NOT a stochastic sampler. If you want to add Gaussian noise to a signal (i.e., randomly sample from a Gaussian distribution centered on the input), use `GaussianDistort` instead. The output for a unit-normal (sigma=1, bias=0, scale=1, offset=0) input of 0.0 is ~0.3989 (the peak of the standard normal PDF), not 1.0. The `bias` parameter shifts the peak location: peak occurs at `variable == bias`. Unscaled output values are always in (0, 1/sqrt(2*pi*sigma)] — apply `scale` and `offset` to fit your model's expected activation range."


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.Gaussian
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
    def create_gaussian(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to create a Gaussian transfer function that maps input values to their Gaussian probability density function (PDF) values.'
        return _impl(args or {})
