"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '945f7d52d35ade1d80654dd764ef61a3d6617a991340f64c74218bc2fd78091d'
__pnl_qualname__ = 'psyneulink.Log'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_log'
TOOL_DESCRIPTION = 'Call this tool to explicitly construct a Log object tied to a PsyNeuLink Component when you need programmatic control over which attributes are tracked from the start. Returns a Log instance whose `.entries` dict accumulates timestamped LogEntry tuples (time, context, value) as the Component executes. In practice, every Component auto-creates its own log accessible via `component.log`; use this only when you need a standalone Log or custom initialization.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "entries": {\n      "default": null,\n      "description": "Optional list of attribute keypaths (strings) to pre-register for logging. Each string must correspond to a loggable parameter, input port, output port, parameter port, or function parameter of the owner Component. If omitted, no entries are pre-registered; use set_log_conditions() afterward to activate recording.",\n      "items": {\n        "type": "string"\n      },\n      "type": "array"\n    },\n    "owner": {\n      "description": "The name or reference of the PsyNeuLink Component this Log belongs to. Must be an already-instantiated Component; the Log attaches to it and reads its parameters, ports, and functions for loggable items.",\n      "type": "string"\n    }\n  },\n  "required": [\n    "owner"\n  ],\n  "type": "object"\n}\n\nNotes:\nLog objects are automatically instantiated by Component.__init__() for every PsyNeuLink Component — you almost never need to call this tool directly; instead access `component.log` on an existing Component. The `entries` argument at construction time only pre-registers keys in the internal dict; it does NOT activate recording — you must separately call `log.set_log_conditions(items, log_condition=LogCondition.EXECUTION)` to start capturing data. LogCondition levels are OFF, EXECUTION, VALIDATION, and ALL_ASSIGNMENTS (IntEnum, combinable with |). The owner\'s actual name is aliased to VALUE internally in loggable_items/logged_items but stored under its real name in log_entries — this can cause apparent key mismatches when inspecting entries directly. `print_entries()`, `nparray()`, `nparray_dictionary()`, and `csv()` are the primary retrieval methods; they all default to ALL logged entries if no entries argument is given.'
TOOL_PARAMETERS = { 'properties': { 'entries': { 'default': None,
                               'description': 'Optional list of attribute keypaths '
                                              '(strings) to pre-register for logging. '
                                              'Each string must correspond to a '
                                              'loggable parameter, input port, output '
                                              'port, parameter port, or function '
                                              'parameter of the owner Component. If '
                                              'omitted, no entries are pre-registered; '
                                              'use set_log_conditions() afterward to '
                                              'activate recording.',
                               'items': {'type': 'string'},
                               'type': 'array'},
                  'owner': { 'description': 'The name or reference of the PsyNeuLink '
                                            'Component this Log belongs to. Must be an '
                                            'already-instantiated Component; the Log '
                                            'attaches to it and reads its parameters, '
                                            'ports, and functions for loggable items.',
                             'type': 'string'}},
  'required': ['owner'],
  'type': 'object'}
TOOL_NOTES = "Log objects are automatically instantiated by Component.__init__() for every PsyNeuLink Component — you almost never need to call this tool directly; instead access `component.log` on an existing Component. The `entries` argument at construction time only pre-registers keys in the internal dict; it does NOT activate recording — you must separately call `log.set_log_conditions(items, log_condition=LogCondition.EXECUTION)` to start capturing data. LogCondition levels are OFF, EXECUTION, VALIDATION, and ALL_ASSIGNMENTS (IntEnum, combinable with |). The owner's actual name is aliased to VALUE internally in loggable_items/logged_items but stored under its real name in log_entries — this can cause apparent key mismatches when inspecting entries directly. `print_entries()`, `nparray()`, `nparray_dictionary()`, and `csv()` are the primary retrieval methods; they all default to ALL logged entries if no entries argument is given."


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.Log
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
    def create_log(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to explicitly construct a Log object tied to a PsyNeuLink Component when you need programmatic control over which attributes are tracked from the start.'
        return _impl(args or {})
