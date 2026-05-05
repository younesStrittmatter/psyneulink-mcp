"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = 'd23c4e0e0df8466cdceca3a19b1d95ab397f08e7591d38f8f7a886983bc3310a'
__pnl_qualname__ = 'psyneulink.is_pref'
__pnl_kind__ = 'function'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'is_pref'
TOOL_DESCRIPTION = 'Call this tool to validate whether a given value is a recognized PsyNeuLink preference identifier before passing it to preference-related APIs. Returns True if the value is a member of BasePreferenceSetPrefs, False otherwise.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "pref": {\n      "description": "The preference identifier to validate \\u2014 typically a preference name string or enum member from BasePreferenceSetPrefs (e.g., \'reportOutputPref\', \'verbosePref\', \'paramValidationPref\').",\n      "type": "string"\n    }\n  },\n  "required": [\n    "pref"\n  ],\n  "type": "object"\n}\n\nNotes:\nThe check is a membership test against BasePreferenceSetPrefs, which is a fixed set defined at import time. Passing an arbitrary string not in that set returns False without raising an exception. If you are unsure what valid preference names look like, inspect BasePreferenceSetPrefs directly rather than guessing.'
TOOL_PARAMETERS = { 'properties': { 'pref': { 'description': 'The preference identifier to validate — '
                                           'typically a preference name string or enum '
                                           'member from BasePreferenceSetPrefs (e.g., '
                                           "'reportOutputPref', 'verbosePref', "
                                           "'paramValidationPref').",
                            'type': 'string'}},
  'required': ['pref'],
  'type': 'object'}
TOOL_NOTES = 'The check is a membership test against BasePreferenceSetPrefs, which is a fixed set defined at import time. Passing an arbitrary string not in that set returns False without raising an exception. If you are unsure what valid preference names look like, inspect BasePreferenceSetPrefs directly rather than guessing.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.is_pref
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
    def is_pref(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to validate whether a given value is a recognized PsyNeuLink preference identifier before passing it to preference-related APIs.'
        return _impl(args or {})
