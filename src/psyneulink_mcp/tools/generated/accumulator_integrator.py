"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '0121c797b0dab47396d3dea7d4f01c5aeb4c81eafc3ffc81814e56831bddf56e'
__pnl_qualname__ = 'psyneulink.AccumulatorIntegrator'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_accumulator_integrator'
TOOL_DESCRIPTION = 'Call this tool to create an AccumulatorIntegrator function that accumulates a running total across time steps, ignoring its input variable entirely. Use it when you need a counter or accumulator that adds a fixed increment each step (linear with rate=1.0) or grows exponentially (rate≠1.0), computing: previous_value * rate + increment + noise. The return value is a 2D array representing the current accumulated value.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "default_variable": {\n      "description": "Template for the value shape to be accumulated; if list or array, each element is independently accumulated. NOTE: the variable is ignored during execution \\u2014 it only sets the shape.",\n      "oneOf": [\n        {\n          "type": "number"\n        },\n        {\n          "items": {\n            "type": "number"\n          },\n          "type": "array"\n        }\n      ]\n    },\n    "increment": {\n      "default": 0,\n      "description": "Amount added to previous_value each step (the ADDITIVE_PARAM). With rate=1.0, the total grows by this amount per step. Can be scalar or array matching variable shape.",\n      "oneOf": [\n        {\n          "type": "number"\n        },\n        {\n          "items": {\n            "type": "number"\n          },\n          "type": "array"\n        }\n      ]\n    },\n    "initializer": {\n      "default": 0,\n      "description": "Starting value for the accumulator (sets previous_value before first step). Defaults to 0.0. Can be scalar or array matching variable shape.",\n      "oneOf": [\n        {\n          "type": "number"\n        },\n        {\n          "items": {\n            "type": "number"\n          },\n          "type": "array"\n        }\n      ]\n    },\n    "name": {\n      "description": "Optional name for this integrator instance. If omitted, a default name is assigned by FunctionRegistry.",\n      "type": "string"\n    },\n    "noise": {\n      "default": 0,\n      "description": "Random value added each step. Can be a float (constant offset), array, or a PsyNeuLink noise Function. Must match variable shape if array.",\n      "oneOf": [\n        {\n          "type": "number"\n        },\n        {\n          "items": {\n            "type": "number"\n          },\n          "type": "array"\n        }\n      ]\n    },\n    "rate": {\n      "default": 1,\n      "description": "Multiplicative factor applied to previous_value each step. rate=1.0 gives linear accumulation; rate\\u22601.0 gives exponential growth/decay. Can be a scalar or array matching variable shape.",\n      "oneOf": [\n        {\n          "type": "number"\n        },\n        {\n          "items": {\n            "type": "number"\n          },\n          "type": "array"\n        }\n      ]\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\n- The `variable` argument passed at execution time is completely ignored — AccumulatorIntegrator never reads its input. If you need an integrator that uses both prior state and a new input signal, use LeakyCompetingIntegrator or AdaptiveIntegrator instead.\n- With default rate=1.0 and increment=0.0, every call returns 0.0 (no change). Set increment to a non-zero value to actually accumulate.\n- Return value is always a 2D array (shape [1, n]) even for scalar inputs.\n- rate is the MULTIPLICATIVE_PARAM and increment is the ADDITIVE_PARAM for modulation — both can be controlled by ModulatorySignals at runtime.\n- Array-valued rate, increment, noise, and initializer must all match the length of default_variable; mixing shapes raises an error.'
TOOL_PARAMETERS = { 'properties': { 'default_variable': { 'description': 'Template for the value shape '
                                                       'to be accumulated; if list or '
                                                       'array, each element is '
                                                       'independently accumulated. '
                                                       'NOTE: the variable is ignored '
                                                       'during execution — it only '
                                                       'sets the shape.',
                                        'oneOf': [ {'type': 'number'},
                                                   { 'items': {'type': 'number'},
                                                     'type': 'array'}]},
                  'increment': { 'default': 0,
                                 'description': 'Amount added to previous_value each '
                                                'step (the ADDITIVE_PARAM). With '
                                                'rate=1.0, the total grows by this '
                                                'amount per step. Can be scalar or '
                                                'array matching variable shape.',
                                 'oneOf': [ {'type': 'number'},
                                            { 'items': {'type': 'number'},
                                              'type': 'array'}]},
                  'initializer': { 'default': 0,
                                   'description': 'Starting value for the accumulator '
                                                  '(sets previous_value before first '
                                                  'step). Defaults to 0.0. Can be '
                                                  'scalar or array matching variable '
                                                  'shape.',
                                   'oneOf': [ {'type': 'number'},
                                              { 'items': {'type': 'number'},
                                                'type': 'array'}]},
                  'name': { 'description': 'Optional name for this integrator '
                                           'instance. If omitted, a default name is '
                                           'assigned by FunctionRegistry.',
                            'type': 'string'},
                  'noise': { 'default': 0,
                             'description': 'Random value added each step. Can be a '
                                            'float (constant offset), array, or a '
                                            'PsyNeuLink noise Function. Must match '
                                            'variable shape if array.',
                             'oneOf': [ {'type': 'number'},
                                        { 'items': {'type': 'number'},
                                          'type': 'array'}]},
                  'rate': { 'default': 1,
                            'description': 'Multiplicative factor applied to '
                                           'previous_value each step. rate=1.0 gives '
                                           'linear accumulation; rate≠1.0 gives '
                                           'exponential growth/decay. Can be a scalar '
                                           'or array matching variable shape.',
                            'oneOf': [ {'type': 'number'},
                                       { 'items': {'type': 'number'},
                                         'type': 'array'}]}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = '- The `variable` argument passed at execution time is completely ignored — AccumulatorIntegrator never reads its input. If you need an integrator that uses both prior state and a new input signal, use LeakyCompetingIntegrator or AdaptiveIntegrator instead.\n- With default rate=1.0 and increment=0.0, every call returns 0.0 (no change). Set increment to a non-zero value to actually accumulate.\n- Return value is always a 2D array (shape [1, n]) even for scalar inputs.\n- rate is the MULTIPLICATIVE_PARAM and increment is the ADDITIVE_PARAM for modulation — both can be controlled by ModulatorySignals at runtime.\n- Array-valued rate, increment, noise, and initializer must all match the length of default_variable; mixing shapes raises an error.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.AccumulatorIntegrator
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
    def create_accumulator_integrator(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to create an AccumulatorIntegrator function that accumulates a running total across time steps, ignoring its input variable entirely.'
        return _impl(args or {})
