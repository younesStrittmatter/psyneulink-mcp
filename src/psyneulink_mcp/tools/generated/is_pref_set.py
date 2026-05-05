"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '9d5258ad0323bbfb0b3a928969cf28dea33d7d94091aed0c575a4738b1711b88'
__pnl_qualname__ = 'psyneulink.is_pref_set'
__pnl_kind__ = 'function'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'is_pref_set'
TOOL_DESCRIPTION = 'Call this tool to validate whether a value qualifies as a valid PsyNeuLink preference set before passing it to a component or mechanism. Returns True if the value is None, a BasePreferenceSet instance, or a dict whose keys are all recognized preference names; returns False otherwise. Use it as a guard check when you are unsure whether a user-supplied or constructed preference value is acceptable.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "pref": {\n      "additionalProperties": true,\n      "description": "The value to validate as a preference set. Pass null to confirm that no preference set is fine (always returns True). Pass a dict mapping PsyNeuLink preference key names to their values to check whether all keys are recognized. Passing a Python BasePreferenceSet object is valid in-process but cannot be expressed directly via this tool; use null or dict instead.",\n      "type": [\n        "object",\n        "null"\n      ]\n    }\n  },\n  "required": [\n    "pref"\n  ],\n  "type": "object"\n}\n\nNotes:\nPassing null always returns True — it is treated as "no preference set specified." A dict is valid only if every key it contains appears in BasePreferenceSetPrefs; a single unrecognized key causes the function to return False. The function does not validate dict values, only keys. BasePreferenceSet instances return True but cannot be passed through the MCP JSON boundary; agents should use dict or null in practice.'
TOOL_PARAMETERS = { 'properties': { 'pref': { 'additionalProperties': True,
                            'description': 'The value to validate as a preference set. '
                                           'Pass null to confirm that no preference '
                                           'set is fine (always returns True). Pass a '
                                           'dict mapping PsyNeuLink preference key '
                                           'names to their values to check whether all '
                                           'keys are recognized. Passing a Python '
                                           'BasePreferenceSet object is valid '
                                           'in-process but cannot be expressed '
                                           'directly via this tool; use null or dict '
                                           'instead.',
                            'type': ['object', 'null']}},
  'required': ['pref'],
  'type': 'object'}
TOOL_NOTES = 'Passing null always returns True — it is treated as "no preference set specified." A dict is valid only if every key it contains appears in BasePreferenceSetPrefs; a single unrecognized key causes the function to return False. The function does not validate dict values, only keys. BasePreferenceSet instances return True but cannot be passed through the MCP JSON boundary; agents should use dict or null in practice.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.is_pref_set
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
    def is_pref_set(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to validate whether a value qualifies as a valid PsyNeuLink preference set before passing it to a component or mechanism.'
        return _impl(args or {})
