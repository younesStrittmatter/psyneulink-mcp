"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = 'd3a07e74e5fefdf053b043624b6a79afabf415d51f96116e0de58f432ec9d8bb'
__pnl_qualname__ = 'psyneulink.LeakyCompetingIntegrator'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_leaky_competing_integrator'
TOOL_DESCRIPTION = 'Use this tool to create a LeakyCompetingIntegrator function implementing the Leaky Competitive Accumulator (LCA) model from Usher & McClelland (2001). Call it when you need a stateful integrator that applies decay (leak) to accumulated values over time steps, suitable as the function of an LCAMechanism or standalone for modeling competitive accumulation dynamics. Returns the updated integral: previous_value + (variable - leak * previous_value) * time_step_size + noise * sqrt(time_step_size).\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "default_variable": {\n      "description": "Template for input values to integrate; if list/array, each element is independently integrated.",\n      "oneOf": [\n        {\n          "type": "number"\n        },\n        {\n          "items": {\n            "type": "number"\n          },\n          "type": "array"\n        }\n      ]\n    },\n    "initializer": {\n      "default": 0,\n      "description": "Starting value(s) for integration (previous_value at t=0). Must match length of variable if array.",\n      "oneOf": [\n        {\n          "type": "number"\n        },\n        {\n          "items": {\n            "type": "number"\n          },\n          "type": "array"\n        }\n      ]\n    },\n    "leak": {\n      "default": 1,\n      "description": "Decay rate scaling previous_value on each time step (aliased to \'rate\'). Higher values cause faster decay. Default 1.0. Use negative values to allow growth from previous state.",\n      "oneOf": [\n        {\n          "type": "number"\n        },\n        {\n          "items": {\n            "type": "number"\n          },\n          "type": "array"\n        }\n      ]\n    },\n    "name": {\n      "description": "Name for the function instance. Auto-assigned by FunctionRegistry if omitted.",\n      "type": "string"\n    },\n    "noise": {\n      "default": 0,\n      "description": "Random noise added to integral each step, scaled by sqrt(time_step_size). Can be scalar, array, or a noise-generating function.",\n      "oneOf": [\n        {\n          "type": "number"\n        },\n        {\n          "items": {\n            "type": "number"\n          },\n          "type": "array"\n        }\n      ]\n    },\n    "offset": {\n      "default": 0,\n      "description": "Constant value added to integral each step (ADDITIVE_PARAM, modulatable). Applied element-wise if array.",\n      "oneOf": [\n        {\n          "type": "number"\n        },\n        {\n          "items": {\n            "type": "number"\n          },\n          "type": "array"\n        }\n      ]\n    },\n    "time_step_size": {\n      "default": 0.1,\n      "description": "Integration time step (dt/tau). Controls timing precision and scales noise appropriately. Corresponds to dt/tau in Usher & McClelland Eq. 4.",\n      "type": "number"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\nleak is assigned to the \'rate\' parameter internally; passing \'rate\' as a kwarg also works for backward compatibility. Unlike standard IntegratorFunctions where rate*previous_value is ADDED, here it is SUBTRACTED to implement decay — so leak=1.0 (default) causes full decay each step, not amplification. The function value can only increase if leak is negative or variable is sufficiently positive. When used as the function of an LCAMechanism, variable receives the sum of external + recurrent inputs automatically. noise is scaled by sqrt(time_step_size) for proper Euler-Maruyama stochastic integration.'
TOOL_PARAMETERS = { 'properties': { 'default_variable': { 'description': 'Template for input values to '
                                                       'integrate; if list/array, each '
                                                       'element is independently '
                                                       'integrated.',
                                        'oneOf': [ {'type': 'number'},
                                                   { 'items': {'type': 'number'},
                                                     'type': 'array'}]},
                  'initializer': { 'default': 0,
                                   'description': 'Starting value(s) for integration '
                                                  '(previous_value at t=0). Must match '
                                                  'length of variable if array.',
                                   'oneOf': [ {'type': 'number'},
                                              { 'items': {'type': 'number'},
                                                'type': 'array'}]},
                  'leak': { 'default': 1,
                            'description': 'Decay rate scaling previous_value on each '
                                           "time step (aliased to 'rate'). Higher "
                                           'values cause faster decay. Default 1.0. '
                                           'Use negative values to allow growth from '
                                           'previous state.',
                            'oneOf': [ {'type': 'number'},
                                       {'items': {'type': 'number'}, 'type': 'array'}]},
                  'name': { 'description': 'Name for the function instance. '
                                           'Auto-assigned by FunctionRegistry if '
                                           'omitted.',
                            'type': 'string'},
                  'noise': { 'default': 0,
                             'description': 'Random noise added to integral each step, '
                                            'scaled by sqrt(time_step_size). Can be '
                                            'scalar, array, or a noise-generating '
                                            'function.',
                             'oneOf': [ {'type': 'number'},
                                        { 'items': {'type': 'number'},
                                          'type': 'array'}]},
                  'offset': { 'default': 0,
                              'description': 'Constant value added to integral each '
                                             'step (ADDITIVE_PARAM, modulatable). '
                                             'Applied element-wise if array.',
                              'oneOf': [ {'type': 'number'},
                                         { 'items': {'type': 'number'},
                                           'type': 'array'}]},
                  'time_step_size': { 'default': 0.1,
                                      'description': 'Integration time step (dt/tau). '
                                                     'Controls timing precision and '
                                                     'scales noise appropriately. '
                                                     'Corresponds to dt/tau in Usher & '
                                                     'McClelland Eq. 4.',
                                      'type': 'number'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = "leak is assigned to the 'rate' parameter internally; passing 'rate' as a kwarg also works for backward compatibility. Unlike standard IntegratorFunctions where rate*previous_value is ADDED, here it is SUBTRACTED to implement decay — so leak=1.0 (default) causes full decay each step, not amplification. The function value can only increase if leak is negative or variable is sufficiently positive. When used as the function of an LCAMechanism, variable receives the sum of external + recurrent inputs automatically. noise is scaled by sqrt(time_step_size) for proper Euler-Maruyama stochastic integration."


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.LeakyCompetingIntegrator
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
    def create_leaky_competing_integrator(args: dict[str, Any] | None = None) -> Any:
        'Use this tool to create a LeakyCompetingIntegrator function implementing the Leaky Competitive Accumulator (LCA) model from Usher & McClelland (2001).'
        return _impl(args or {})
