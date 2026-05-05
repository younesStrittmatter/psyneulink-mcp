"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = 'dc39b3ba123a9efe9769016225fec0f1a27ddb9d1a7e02a71c595aee1e44ca6a'
__pnl_qualname__ = 'psyneulink.DeceleratingTimer'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_decelerating_timer'
TOOL_DESCRIPTION = 'Use this tool to create a DeceleratingTimer function that maps an input variable to an exponentially decaying (or rising) value. Call it when you need a smooth decay schedule — e.g., annealing a learning rate, reducing noise over time, or modeling fatigue — where the output starts near `initial` at variable=0 and approaches `initial * final` at variable=`duration`. Returns the transformed scalar or array value.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "default_variable": {\n      "description": "Template value (number or 1-D array) to be transformed. Sets the expected shape of inputs.",\n      "oneOf": [\n        {\n          "type": "number"\n        },\n        {\n          "items": {\n            "type": "number"\n          },\n          "type": "array"\n        }\n      ]\n    },\n    "duration": {\n      "default": 1,\n      "description": "The input value at which the output equals initial * final (+ offset). Must be > 0. Default: 1.0.",\n      "exclusiveMinimum": 0,\n      "type": "number"\n    },\n    "final": {\n      "default": 0.01,\n      "description": "Fraction of `initial` that determines the function value at variable=`duration`. Must be between 0 and 1 exclusive for a decay; can exceed 1 to produce a rising curve. Default: 0.01.",\n      "type": "number"\n    },\n    "initial": {\n      "default": 1,\n      "description": "Value of the function at variable=0 (before adding offset). Must be > 0. Default: 1.0.",\n      "exclusiveMinimum": 0,\n      "type": "number"\n    },\n    "name": {\n      "description": "Optional name for the Function instance. Auto-assigned by FunctionRegistry if omitted.",\n      "type": "string"\n    },\n    "rate": {\n      "default": 1,\n      "description": "Controls the curvature of the decay. Values > 1 decelerate faster early; values < 1 decelerate slower early. Must be > 0. Default: 1.0.",\n      "exclusiveMinimum": 0,\n      "type": "number"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\n- `direction` is computed internally as +1 when `final > initial` (rising) or -1 otherwise (decaying); you cannot set it directly.\n- The function value at variable=0 is `initial + offset` (not just `initial`); `offset` is inherited from the parent TimerFunction and defaults to 0 — if you see unexpected baseline shifts, check whether `offset` was set elsewhere.\n- `final` is a *fraction*, not an absolute target value. The target at variable=`duration` is `initial * final + offset`.\n- Passing variable values beyond `duration` extrapolates the curve; the formula remains valid but values will fall below `initial * final`.\n- `rate` in the docstring attributes section says "> 1.0" but the constructor only enforces "> 0"; values between 0 and 1 are accepted and produce sub-linear (slower initial) decay shapes.\n- `default_variable` sets the shape template; subsequent calls must match that shape.'
TOOL_PARAMETERS = { 'properties': { 'default_variable': { 'description': 'Template value (number or 1-D '
                                                       'array) to be transformed. Sets '
                                                       'the expected shape of inputs.',
                                        'oneOf': [ {'type': 'number'},
                                                   { 'items': {'type': 'number'},
                                                     'type': 'array'}]},
                  'duration': { 'default': 1,
                                'description': 'The input value at which the output '
                                               'equals initial * final (+ offset). '
                                               'Must be > 0. Default: 1.0.',
                                'exclusiveMinimum': 0,
                                'type': 'number'},
                  'final': { 'default': 0.01,
                             'description': 'Fraction of `initial` that determines the '
                                            'function value at variable=`duration`. '
                                            'Must be between 0 and 1 exclusive for a '
                                            'decay; can exceed 1 to produce a rising '
                                            'curve. Default: 0.01.',
                             'type': 'number'},
                  'initial': { 'default': 1,
                               'description': 'Value of the function at variable=0 '
                                              '(before adding offset). Must be > 0. '
                                              'Default: 1.0.',
                               'exclusiveMinimum': 0,
                               'type': 'number'},
                  'name': { 'description': 'Optional name for the Function instance. '
                                           'Auto-assigned by FunctionRegistry if '
                                           'omitted.',
                            'type': 'string'},
                  'rate': { 'default': 1,
                            'description': 'Controls the curvature of the decay. '
                                           'Values > 1 decelerate faster early; values '
                                           '< 1 decelerate slower early. Must be > 0. '
                                           'Default: 1.0.',
                            'exclusiveMinimum': 0,
                            'type': 'number'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = '- `direction` is computed internally as +1 when `final > initial` (rising) or -1 otherwise (decaying); you cannot set it directly.\n- The function value at variable=0 is `initial + offset` (not just `initial`); `offset` is inherited from the parent TimerFunction and defaults to 0 — if you see unexpected baseline shifts, check whether `offset` was set elsewhere.\n- `final` is a *fraction*, not an absolute target value. The target at variable=`duration` is `initial * final + offset`.\n- Passing variable values beyond `duration` extrapolates the curve; the formula remains valid but values will fall below `initial * final`.\n- `rate` in the docstring attributes section says "> 1.0" but the constructor only enforces "> 0"; values between 0 and 1 are accepted and produce sub-linear (slower initial) decay shapes.\n- `default_variable` sets the shape template; subsequent calls must match that shape.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.DeceleratingTimer
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
    def create_decelerating_timer(args: dict[str, Any] | None = None) -> Any:
        'Use this tool to create a DeceleratingTimer function that maps an input variable to an exponentially decaying (or rising) value.'
        return _impl(args or {})
