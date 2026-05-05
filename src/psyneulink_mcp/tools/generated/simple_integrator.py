"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = 'd768d04ad1e0362a1fb8a1586f9f0058b0a773a1a05f837b0447d232c244a9a5'
__pnl_qualname__ = 'psyneulink.SimpleIntegrator'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_simple_integrator'
TOOL_DESCRIPTION = 'Call this tool to instantiate a SimpleIntegrator function that accumulates a running sum via `previous_value + rate * variable + noise + offset`. Use it when you need a basic leaky or non-leaky accumulator as the function of a Mechanism or standalone — for example, to model a simple running total, evidence accumulation without decay, or a manually-scaled integrator. The result is a PsyNeuLink Function object assignable to a Mechanism\'s `function` parameter.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "default_variable": {\n      "description": "Template for the value to be integrated. Scalar or list/array; if array, each element is integrated independently.",\n      "oneOf": [\n        {\n          "type": "number"\n        },\n        {\n          "items": {\n            "type": "number"\n          },\n          "type": "array"\n        }\n      ]\n    },\n    "initializer": {\n      "default": 0,\n      "description": "Starting value(s) for integration; sets previous_value before the first execution. Default 0.0. Must match variable length if given as an array.",\n      "oneOf": [\n        {\n          "type": "number"\n        },\n        {\n          "items": {\n            "type": "number"\n          },\n          "type": "array"\n        }\n      ]\n    },\n    "name": {\n      "description": "Optional name for the Function instance. Auto-assigned by FunctionRegistry if omitted.",\n      "type": "string"\n    },\n    "noise": {\n      "default": 0,\n      "description": "Random value added to the integral on each call. Default 0.0. Can be a float (applied uniformly) or array matching variable length.",\n      "oneOf": [\n        {\n          "type": "number"\n        },\n        {\n          "items": {\n            "type": "number"\n          },\n          "type": "array"\n        }\n      ]\n    },\n    "offset": {\n      "default": 0,\n      "description": "Constant value added to the integral on each call (ADDITIVE_PARAM for modulation). Default 0.0. Can be a float or array matching variable length.",\n      "oneOf": [\n        {\n          "type": "number"\n        },\n        {\n          "items": {\n            "type": "number"\n          },\n          "type": "array"\n        }\n      ]\n    },\n    "rate": {\n      "default": 1,\n      "description": "Multiplicative scaling applied to the incoming variable before accumulation. Default 1.0 (no scaling). Must match the length of variable if given as an array.",\n      "oneOf": [\n        {\n          "type": "number"\n        },\n        {\n          "items": {\n            "type": "number"\n          },\n          "type": "array"\n        }\n      ]\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\nSimpleIntegrator is stateful: it retains `previous_value` across calls, so repeated execution accumulates. If you need a fresh start, reinitialize or set a new `initializer`. Unlike AdaptiveIntegrator, there is no `smoothing_factor` — rate multiplies the *input*, not the complement of a decay term, so rate=1.0 gives pure summation with no decay. Array inputs are integrated element-wise; all array parameters (rate, noise, offset, initializer) must share the same length as variable. `params` and `owner` are advanced PNL internals; omit them unless integrating into a Mechanism manually.'
TOOL_PARAMETERS = { 'properties': { 'default_variable': { 'description': 'Template for the value to be '
                                                       'integrated. Scalar or '
                                                       'list/array; if array, each '
                                                       'element is integrated '
                                                       'independently.',
                                        'oneOf': [ {'type': 'number'},
                                                   { 'items': {'type': 'number'},
                                                     'type': 'array'}]},
                  'initializer': { 'default': 0,
                                   'description': 'Starting value(s) for integration; '
                                                  'sets previous_value before the '
                                                  'first execution. Default 0.0. Must '
                                                  'match variable length if given as '
                                                  'an array.',
                                   'oneOf': [ {'type': 'number'},
                                              { 'items': {'type': 'number'},
                                                'type': 'array'}]},
                  'name': { 'description': 'Optional name for the Function instance. '
                                           'Auto-assigned by FunctionRegistry if '
                                           'omitted.',
                            'type': 'string'},
                  'noise': { 'default': 0,
                             'description': 'Random value added to the integral on '
                                            'each call. Default 0.0. Can be a float '
                                            '(applied uniformly) or array matching '
                                            'variable length.',
                             'oneOf': [ {'type': 'number'},
                                        { 'items': {'type': 'number'},
                                          'type': 'array'}]},
                  'offset': { 'default': 0,
                              'description': 'Constant value added to the integral on '
                                             'each call (ADDITIVE_PARAM for '
                                             'modulation). Default 0.0. Can be a float '
                                             'or array matching variable length.',
                              'oneOf': [ {'type': 'number'},
                                         { 'items': {'type': 'number'},
                                           'type': 'array'}]},
                  'rate': { 'default': 1,
                            'description': 'Multiplicative scaling applied to the '
                                           'incoming variable before accumulation. '
                                           'Default 1.0 (no scaling). Must match the '
                                           'length of variable if given as an array.',
                            'oneOf': [ {'type': 'number'},
                                       { 'items': {'type': 'number'},
                                         'type': 'array'}]}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = 'SimpleIntegrator is stateful: it retains `previous_value` across calls, so repeated execution accumulates. If you need a fresh start, reinitialize or set a new `initializer`. Unlike AdaptiveIntegrator, there is no `smoothing_factor` — rate multiplies the *input*, not the complement of a decay term, so rate=1.0 gives pure summation with no decay. Array inputs are integrated element-wise; all array parameters (rate, noise, offset, initializer) must share the same length as variable. `params` and `owner` are advanced PNL internals; omit them unless integrating into a Mechanism manually.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.SimpleIntegrator
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
    def create_simple_integrator(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to instantiate a SimpleIntegrator function that accumulates a running sum via `previous_value + rate * variable + noise + offset`.'
        return _impl(args or {})
