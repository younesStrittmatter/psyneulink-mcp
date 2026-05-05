"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = 'd237659aafe1d1d528f4cfd612150e58413ad8f844aad193b6093fe7f083c640'
__pnl_qualname__ = 'psyneulink.Time'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_time'
TOOL_DESCRIPTION = 'Call this tool to construct a Time snapshot representing a specific point in a PsyNeuLink scheduler\'s execution hierarchy, expressed as integer counts at each TimeScale level (life, run, trial, pass, time-step). Use it when you need to inspect, compare, or set scheduler time state — for example, to record when a condition becomes active or to check a mechanism\'s last execution time. The result is a Time object whose attributes mirror the TimeScale hierarchy.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "absolute_enabled": {\n      "default": false,\n      "description": "Set to true to enable wall-clock absolute time tracking. When false (default), the absolute, absolute_interval, and absolute_time_unit_scale parameters are ignored.",\n      "type": "boolean"\n    },\n    "consideration_set_execution": {\n      "default": 0,\n      "description": "Count at the TIME_STEP (CONSIDERATION_SET_EXECUTION) level \\u2014 the finest-grained TimeScale.",\n      "type": "integer"\n    },\n    "environment_sequence": {\n      "default": 0,\n      "description": "Count at the RUN (ENVIRONMENT_SEQUENCE) level.",\n      "type": "integer"\n    },\n    "environment_state_update": {\n      "default": 0,\n      "description": "Count at the TRIAL (ENVIRONMENT_STATE_UPDATE) level.",\n      "type": "integer"\n    },\n    "life": {\n      "default": 0,\n      "description": "Count at the LIFE level \\u2014 the coarsest TimeScale.",\n      "type": "integer"\n    },\n    "pass_": {\n      "default": 0,\n      "description": "Count at the PASS level.",\n      "type": "integer"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\nThe `absolute`, `absolute_interval`, and `absolute_time_unit_scale` parameters require `pint.Quantity` objects and a `TimeScale` enum value respectively — these cannot be passed as plain JSON and are therefore omitted from the schema. Agents needing absolute time support should leave those at their defaults (0ms, 1ms, TimeScale.CONSIDERATION_SET_EXECUTION) and only set `absolute_enabled=True`. The parameter name `pass_` has a trailing underscore because `pass` is a Python reserved keyword; pass it exactly as `pass_`. In most modeling workflows you will read Time objects from scheduler state rather than constructing them directly.'
TOOL_PARAMETERS = { 'properties': { 'absolute_enabled': { 'default': False,
                                        'description': 'Set to true to enable '
                                                       'wall-clock absolute time '
                                                       'tracking. When false '
                                                       '(default), the absolute, '
                                                       'absolute_interval, and '
                                                       'absolute_time_unit_scale '
                                                       'parameters are ignored.',
                                        'type': 'boolean'},
                  'consideration_set_execution': { 'default': 0,
                                                   'description': 'Count at the '
                                                                  'TIME_STEP '
                                                                  '(CONSIDERATION_SET_EXECUTION) '
                                                                  'level — the '
                                                                  'finest-grained '
                                                                  'TimeScale.',
                                                   'type': 'integer'},
                  'environment_sequence': { 'default': 0,
                                            'description': 'Count at the RUN '
                                                           '(ENVIRONMENT_SEQUENCE) '
                                                           'level.',
                                            'type': 'integer'},
                  'environment_state_update': { 'default': 0,
                                                'description': 'Count at the TRIAL '
                                                               '(ENVIRONMENT_STATE_UPDATE) '
                                                               'level.',
                                                'type': 'integer'},
                  'life': { 'default': 0,
                            'description': 'Count at the LIFE level — the coarsest '
                                           'TimeScale.',
                            'type': 'integer'},
                  'pass_': { 'default': 0,
                             'description': 'Count at the PASS level.',
                             'type': 'integer'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = 'The `absolute`, `absolute_interval`, and `absolute_time_unit_scale` parameters require `pint.Quantity` objects and a `TimeScale` enum value respectively — these cannot be passed as plain JSON and are therefore omitted from the schema. Agents needing absolute time support should leave those at their defaults (0ms, 1ms, TimeScale.CONSIDERATION_SET_EXECUTION) and only set `absolute_enabled=True`. The parameter name `pass_` has a trailing underscore because `pass` is a Python reserved keyword; pass it exactly as `pass_`. In most modeling workflows you will read Time objects from scheduler state rather than constructing them directly.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.Time
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
    def create_time(args: dict[str, Any] | None = None) -> Any:
        "Call this tool to construct a Time snapshot representing a specific point in a PsyNeuLink scheduler's execution hierarchy, expressed as integer counts at each TimeScale level (life, run, trial, pass, time-step)."
        return _impl(args or {})
