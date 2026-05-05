"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '4b6ead6c77a15b545934e5e0b25e18c24180ac598b57a8ffbee2c4d837ac2848'
__pnl_qualname__ = 'psyneulink.AdaptiveIntegrator'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_adaptive_integrator'
TOOL_DESCRIPTION = 'Call this tool to create an AdaptiveIntegrator function that computes an exponentially weighted moving average (EWMA) of its input: ((1-rate) * previous_value) + (rate * variable) + noise + offset. Use it when you need a leaky integrator or smoothing filter as a function for a Mechanism (e.g., IntegratorMechanism). The result is a configured AdaptiveIntegrator instance ready to assign to a Mechanism\'s function parameter.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "default_variable": {\n      "description": "Template for the value to be integrated. If a list or array, each element is independently integrated. Determines the shape of the integrator\'s input.",\n      "oneOf": [\n        {\n          "type": "number"\n        },\n        {\n          "items": {\n            "type": "number"\n          },\n          "type": "array"\n        }\n      ]\n    },\n    "initializer": {\n      "default": 0,\n      "description": "Starting value(s) for integration; sets previous_value before the first execution. If array, must match variable length.",\n      "oneOf": [\n        {\n          "type": "number"\n        },\n        {\n          "items": {\n            "type": "number"\n          },\n          "type": "array"\n        }\n      ]\n    },\n    "name": {\n      "description": "Optional name for this function instance. If omitted, FunctionRegistry assigns a default.",\n      "type": "string"\n    },\n    "noise": {\n      "default": 0,\n      "description": "Random value added to the integral on each call. Can be a float constant or an array matching variable length.",\n      "oneOf": [\n        {\n          "type": "number"\n        },\n        {\n          "items": {\n            "type": "number"\n          },\n          "type": "array"\n        }\n      ]\n    },\n    "offset": {\n      "default": 0,\n      "description": "Constant value added to the integral on each call (ADDITIVE_PARAM for modulation). Can be a float or array matching variable length.",\n      "oneOf": [\n        {\n          "type": "number"\n        },\n        {\n          "items": {\n            "type": "number"\n          },\n          "type": "array"\n        }\n      ]\n    },\n    "rate": {\n      "default": 1,\n      "description": "EWMA smoothing factor between 0.0 and 1.0 (inclusive). rate=0 means no change (input ignored), rate=1 means no memory (previous value ignored). Can be a scalar applied to all elements, or an array matching the length of variable.",\n      "oneOf": [\n        {\n          "maximum": 1,\n          "minimum": 0,\n          "type": "number"\n        },\n        {\n          "items": {\n            "maximum": 1,\n            "minimum": 0,\n            "type": "number"\n          },\n          "type": "array"\n        }\n      ]\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\nrate is the MULTIPLICATIVE_PARAM and offset is the ADDITIVE_PARAM for ModulatorySignal modulation — these can be controlled by a ControlMechanism at runtime. rate MUST be between 0.0 and 1.0 (inclusive); values outside this range raise FunctionError at instantiation. If rate is specified as an array, its length must match variable length — if variable shape is flexible (not yet bound to a Mechanism input), PNL will silently reshape variable to match rate. The integrator maintains stateful previous_value across calls within a context; initializer sets that state before the first step. noise parameter accepts a DistributionFunction for stochastic integration, but the JSON schema covers only numeric constants — pass a DistributionFunction via params dict if needed.'
TOOL_PARAMETERS = { 'properties': { 'default_variable': { 'description': 'Template for the value to be '
                                                       'integrated. If a list or '
                                                       'array, each element is '
                                                       'independently integrated. '
                                                       'Determines the shape of the '
                                                       "integrator's input.",
                                        'oneOf': [ {'type': 'number'},
                                                   { 'items': {'type': 'number'},
                                                     'type': 'array'}]},
                  'initializer': { 'default': 0,
                                   'description': 'Starting value(s) for integration; '
                                                  'sets previous_value before the '
                                                  'first execution. If array, must '
                                                  'match variable length.',
                                   'oneOf': [ {'type': 'number'},
                                              { 'items': {'type': 'number'},
                                                'type': 'array'}]},
                  'name': { 'description': 'Optional name for this function instance. '
                                           'If omitted, FunctionRegistry assigns a '
                                           'default.',
                            'type': 'string'},
                  'noise': { 'default': 0,
                             'description': 'Random value added to the integral on '
                                            'each call. Can be a float constant or an '
                                            'array matching variable length.',
                             'oneOf': [ {'type': 'number'},
                                        { 'items': {'type': 'number'},
                                          'type': 'array'}]},
                  'offset': { 'default': 0,
                              'description': 'Constant value added to the integral on '
                                             'each call (ADDITIVE_PARAM for '
                                             'modulation). Can be a float or array '
                                             'matching variable length.',
                              'oneOf': [ {'type': 'number'},
                                         { 'items': {'type': 'number'},
                                           'type': 'array'}]},
                  'rate': { 'default': 1,
                            'description': 'EWMA smoothing factor between 0.0 and 1.0 '
                                           '(inclusive). rate=0 means no change (input '
                                           'ignored), rate=1 means no memory (previous '
                                           'value ignored). Can be a scalar applied to '
                                           'all elements, or an array matching the '
                                           'length of variable.',
                            'oneOf': [ {'maximum': 1, 'minimum': 0, 'type': 'number'},
                                       { 'items': { 'maximum': 1,
                                                    'minimum': 0,
                                                    'type': 'number'},
                                         'type': 'array'}]}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = 'rate is the MULTIPLICATIVE_PARAM and offset is the ADDITIVE_PARAM for ModulatorySignal modulation — these can be controlled by a ControlMechanism at runtime. rate MUST be between 0.0 and 1.0 (inclusive); values outside this range raise FunctionError at instantiation. If rate is specified as an array, its length must match variable length — if variable shape is flexible (not yet bound to a Mechanism input), PNL will silently reshape variable to match rate. The integrator maintains stateful previous_value across calls within a context; initializer sets that state before the first step. noise parameter accepts a DistributionFunction for stochastic integration, but the JSON schema covers only numeric constants — pass a DistributionFunction via params dict if needed.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.AdaptiveIntegrator
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
    def create_adaptive_integrator(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to create an AdaptiveIntegrator function that computes an exponentially weighted moving average (EWMA) of its input: ((1-rate) * previous_value) + (rate * variable) + noise + offset.'
        return _impl(args or {})
