"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '48e219345217f8fdcec3d560619f06b7bdc7e1240b317fa71dc8cf369545297c'
__pnl_qualname__ = 'psyneulink.AcceleratingTimer'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_accelerating_timer'
TOOL_DESCRIPTION = 'Call this tool to instantiate a PsyNeuLink AcceleratingTimer function, which maps a variable from `initial` (at variable=0) to `final` (at variable=duration) using a convex accelerating curve. Use it when you need a smooth, non-linear ramp-up schedule — for example, as a transfer function on a Mechanism that should start slow and accelerate. The result is a configured AcceleratingTimer object ready to be assigned to a Mechanism\'s `function` parameter.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "default_variable": {\n      "description": "Template value (scalar or 1-D array) specifying the shape of the input. Determines the shape of the output.",\n      "oneOf": [\n        {\n          "type": "number"\n        },\n        {\n          "items": {\n            "type": "number"\n          },\n          "type": "array"\n        }\n      ]\n    },\n    "duration": {\n      "default": 1,\n      "description": "The value of the input variable at which the function output equals `final`. Must be > 0. Defaults to 1.0.",\n      "type": "number"\n    },\n    "final": {\n      "default": 1,\n      "description": "Output value when variable=duration. Must be strictly greater than initial. Defaults to 1.0.",\n      "type": "number"\n    },\n    "initial": {\n      "default": 0,\n      "description": "Output value when variable=0. Must be >= 0. Defaults to 0.0.",\n      "type": "number"\n    },\n    "name": {\n      "description": "Optional string name for the function instance. A unique name is auto-assigned if omitted.",\n      "type": "string"\n    },\n    "params": {\n      "additionalProperties": true,\n      "description": "Optional parameter dictionary for overriding constructor arguments, including \'rate\' (acceleration rate, >0, default 1.0) which is not exposed as a direct constructor argument.",\n      "type": "object"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\n1. `rate` is documented in the class docstring (controls acceleration steepness, must be >0, default 1.0) but is absent from the constructor signature — it is inherited from `TimerFunction`. Pass it via the `params` dict: `params={"rate": 2.0}`.\n2. The docstring labels the default for `initial` as 1.0 in some places and 0.0 in others; the constructor default is `None` (resolved to 0.0 by the parent). Use 0.0 as the effective default.\n3. The formula evaluates to `initial` exactly at variable=0 and `final` exactly at variable=duration only when rate>0; at rate=1 the curve is still non-linear (exponential weighting), not linear.\n4. Passing variable > duration is allowed but produces extrapolated values beyond `final`.\n5. `owner` should be set when assigning directly to a Mechanism rather than constructing standalone; omit it for standalone use.'
TOOL_PARAMETERS = { 'properties': { 'default_variable': { 'description': 'Template value (scalar or 1-D '
                                                       'array) specifying the shape of '
                                                       'the input. Determines the '
                                                       'shape of the output.',
                                        'oneOf': [ {'type': 'number'},
                                                   { 'items': {'type': 'number'},
                                                     'type': 'array'}]},
                  'duration': { 'default': 1,
                                'description': 'The value of the input variable at '
                                               'which the function output equals '
                                               '`final`. Must be > 0. Defaults to 1.0.',
                                'type': 'number'},
                  'final': { 'default': 1,
                             'description': 'Output value when variable=duration. Must '
                                            'be strictly greater than initial. '
                                            'Defaults to 1.0.',
                             'type': 'number'},
                  'initial': { 'default': 0,
                               'description': 'Output value when variable=0. Must be '
                                              '>= 0. Defaults to 0.0.',
                               'type': 'number'},
                  'name': { 'description': 'Optional string name for the function '
                                           'instance. A unique name is auto-assigned '
                                           'if omitted.',
                            'type': 'string'},
                  'params': { 'additionalProperties': True,
                              'description': 'Optional parameter dictionary for '
                                             'overriding constructor arguments, '
                                             "including 'rate' (acceleration rate, >0, "
                                             'default 1.0) which is not exposed as a '
                                             'direct constructor argument.',
                              'type': 'object'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = '1. `rate` is documented in the class docstring (controls acceleration steepness, must be >0, default 1.0) but is absent from the constructor signature — it is inherited from `TimerFunction`. Pass it via the `params` dict: `params={"rate": 2.0}`.\n2. The docstring labels the default for `initial` as 1.0 in some places and 0.0 in others; the constructor default is `None` (resolved to 0.0 by the parent). Use 0.0 as the effective default.\n3. The formula evaluates to `initial` exactly at variable=0 and `final` exactly at variable=duration only when rate>0; at rate=1 the curve is still non-linear (exponential weighting), not linear.\n4. Passing variable > duration is allowed but produces extrapolated values beyond `final`.\n5. `owner` should be set when assigning directly to a Mechanism rather than constructing standalone; omit it for standalone use.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.AcceleratingTimer
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
    def create_accelerating_timer(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to instantiate a PsyNeuLink AcceleratingTimer function, which maps a variable from `initial` (at variable=0) to `final` (at variable=duration) using a convex accelerating curve.'
        return _impl(args or {})
