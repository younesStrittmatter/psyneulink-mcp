"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = 'b894b3c9922e3801c6f21666ca134626314282d21ed0e53640c6f85c6f335e34'
__pnl_qualname__ = 'psyneulink.observe_value_at_keypath'
__pnl_kind__ = 'function'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'observe_value_at_keypath'
TOOL_DESCRIPTION = 'Call this tool when you want to log or observe a value change at a specific keypath in a PsyNeuLink object hierarchy — for example, during debugging to trace when and how a parameter or state variable changes. The tool prints a formatted line to stdout showing the keypath, the old value, and the new value; it returns nothing.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "keypath": {\n      "description": "The dotted key path identifying the attribute or nested property that changed (e.g. \'mechanism.parameter_ports.gain.value\').",\n      "type": "string"\n    },\n    "new_value": {\n      "description": "The new value at the keypath after the change. Pass as a string representation of the value.",\n      "type": "string"\n    },\n    "old_value": {\n      "description": "The previous value at the keypath before the change. Pass as a string representation of the value.",\n      "type": "string"\n    }\n  },\n  "required": [\n    "keypath",\n    "old_value",\n    "new_value"\n  ],\n  "type": "object"\n}\n\nNotes:\nThis function only prints to stdout and returns None — do not expect a structured return value. It is primarily a KVO (Key-Value Observing) debug helper intended to be used as an observer callback, not as a general-purpose inspection tool; prefer parameter introspection tools for read-only value queries. Values are formatted via Python str(), so complex objects will appear as their repr.'
TOOL_PARAMETERS = { 'properties': { 'keypath': { 'description': 'The dotted key path identifying the '
                                              'attribute or nested property that '
                                              'changed (e.g. '
                                              "'mechanism.parameter_ports.gain.value').",
                               'type': 'string'},
                  'new_value': { 'description': 'The new value at the keypath after '
                                                'the change. Pass as a string '
                                                'representation of the value.',
                                 'type': 'string'},
                  'old_value': { 'description': 'The previous value at the keypath '
                                                'before the change. Pass as a string '
                                                'representation of the value.',
                                 'type': 'string'}},
  'required': ['keypath', 'old_value', 'new_value'],
  'type': 'object'}
TOOL_NOTES = 'This function only prints to stdout and returns None — do not expect a structured return value. It is primarily a KVO (Key-Value Observing) debug helper intended to be used as an observer callback, not as a general-purpose inspection tool; prefer parameter introspection tools for read-only value queries. Values are formatted via Python str(), so complex objects will appear as their repr.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.observe_value_at_keypath
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
    def observe_value_at_keypath(args: dict[str, Any] | None = None) -> Any:
        'Call this tool when you want to log or observe a value change at a specific keypath in a PsyNeuLink object hierarchy — for example, during debugging to trace when and how a parameter or state variable changes.'
        return _impl(args or {})
