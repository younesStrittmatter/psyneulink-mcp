"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '7f2ee852f12b3082995747b11cf649ea748ea20255257b68a4ebfbd676bd3533'
__pnl_qualname__ = 'psyneulink.LinearTimer'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_linear_timer'
TOOL_DESCRIPTION = 'Use this tool to create a LinearTimer function that maps an input variable linearly from `initial` (at variable=0) to `final` (at variable=`duration`). Call it when you need a time-varying gain or ramp function — for example, to schedule a parameter that rises or falls at a constant rate over a trial. The function returns a scalar or array of the same shape as `variable`.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "default_variable": {\n      "description": "Template value (number or array) that defines the shape of the input. Defaults to class default if omitted.",\n      "oneOf": [\n        {\n          "type": "number"\n        },\n        {\n          "items": {\n            "type": "number"\n          },\n          "type": "array"\n        }\n      ]\n    },\n    "duration": {\n      "default": 1,\n      "description": "The value of variable at which the output equals final. Must be > 0. Default: 1.0.",\n      "type": "number"\n    },\n    "final": {\n      "default": 1,\n      "description": "Output value when variable=duration. Must be strictly greater than initial. Default: 1.0.",\n      "type": "number"\n    },\n    "initial": {\n      "default": 1,\n      "description": "Output value when variable=0. Must be >= 0. Default: 1.0.",\n      "type": "number"\n    },\n    "name": {\n      "description": "Optional name for the function instance.",\n      "type": "string"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\nThe docstring lists defaults as 1.0 for all of initial, final, and duration, but the constructor signature shows None for each (resolved at super().__init__ time). With initial=1.0 and final=1.0 the slope is zero — you almost certainly want final > initial for a meaningful ramp. The constraint final > initial is documented but not enforced at construction time in the visible source (the FIX comment suggests validation is pending). Passing initial >= final will silently produce a zero or negative-slope function. The derivative is the constant (final-initial)/duration, independent of variable. `params` and `owner` are PsyNeuLink internals that should not normally be passed by an agent; omit them.'
TOOL_PARAMETERS = { 'properties': { 'default_variable': { 'description': 'Template value (number or '
                                                       'array) that defines the shape '
                                                       'of the input. Defaults to '
                                                       'class default if omitted.',
                                        'oneOf': [ {'type': 'number'},
                                                   { 'items': {'type': 'number'},
                                                     'type': 'array'}]},
                  'duration': { 'default': 1,
                                'description': 'The value of variable at which the '
                                               'output equals final. Must be > 0. '
                                               'Default: 1.0.',
                                'type': 'number'},
                  'final': { 'default': 1,
                             'description': 'Output value when variable=duration. Must '
                                            'be strictly greater than initial. '
                                            'Default: 1.0.',
                             'type': 'number'},
                  'initial': { 'default': 1,
                               'description': 'Output value when variable=0. Must be '
                                              '>= 0. Default: 1.0.',
                               'type': 'number'},
                  'name': { 'description': 'Optional name for the function instance.',
                            'type': 'string'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = 'The docstring lists defaults as 1.0 for all of initial, final, and duration, but the constructor signature shows None for each (resolved at super().__init__ time). With initial=1.0 and final=1.0 the slope is zero — you almost certainly want final > initial for a meaningful ramp. The constraint final > initial is documented but not enforced at construction time in the visible source (the FIX comment suggests validation is pending). Passing initial >= final will silently produce a zero or negative-slope function. The derivative is the constant (final-initial)/duration, independent of variable. `params` and `owner` are PsyNeuLink internals that should not normally be passed by an agent; omit them.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.LinearTimer
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
    def create_linear_timer(args: dict[str, Any] | None = None) -> Any:
        'Use this tool to create a LinearTimer function that maps an input variable linearly from `initial` (at variable=0) to `final` (at variable=`duration`).'
        return _impl(args or {})
