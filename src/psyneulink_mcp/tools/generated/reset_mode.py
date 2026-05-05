"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '68b027d8505910ade5f98c93015784932811e0976132972b60acf91c93d22688'
__pnl_qualname__ = 'psyneulink.ResetMode'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_reset_mode'
TOOL_DESCRIPTION = 'Call this tool to obtain a ResetMode enum member when you need to pass a reset mode to a PsyNeuLink component\'s reset_params method. Returns the enum member corresponding to the chosen reset scope: current-values-only, instance-defaults-only, or all-to-class-defaults.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "value": {\n      "description": "Which reset scope to select: 0 = CURRENT_TO_INSTANCE_DEFAULTS (reset current values to instance defaults), 1 = INSTANCE_TO_CLASS (reset instance defaults to class defaults), 2 = ALL_TO_CLASS_DEFAULTS (reset both current values and instance defaults to class defaults).",\n      "enum": [\n        0,\n        1,\n        2\n      ],\n      "type": "integer"\n    }\n  },\n  "required": [\n    "value"\n  ],\n  "type": "object"\n}\n\nNotes:\nResetMode is an Enum; the template instantiates it as ResetMode(value=...). Python Enum __new__ accepts the value positionally or as the keyword `value`, so passing value=0/1/2 works. The resulting object is only useful as an argument to reset_params — do not pass it anywhere else. ALL_TO_CLASS_DEFAULTS (2) is the most destructive: it wipes both current and instance-level customizations back to class defaults.'
TOOL_PARAMETERS = { 'properties': { 'value': { 'description': 'Which reset scope to select: 0 = '
                                            'CURRENT_TO_INSTANCE_DEFAULTS (reset '
                                            'current values to instance defaults), 1 = '
                                            'INSTANCE_TO_CLASS (reset instance '
                                            'defaults to class defaults), 2 = '
                                            'ALL_TO_CLASS_DEFAULTS (reset both current '
                                            'values and instance defaults to class '
                                            'defaults).',
                             'enum': [0, 1, 2],
                             'type': 'integer'}},
  'required': ['value'],
  'type': 'object'}
TOOL_NOTES = 'ResetMode is an Enum; the template instantiates it as ResetMode(value=...). Python Enum __new__ accepts the value positionally or as the keyword `value`, so passing value=0/1/2 works. The resulting object is only useful as an argument to reset_params — do not pass it anywhere else. ALL_TO_CLASS_DEFAULTS (2) is the most destructive: it wipes both current and instance-level customizations back to class defaults.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.ResetMode
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
    def create_reset_mode(args: dict[str, Any] | None = None) -> Any:
        "Call this tool to obtain a ResetMode enum member when you need to pass a reset mode to a PsyNeuLink component's reset_params method."
        return _impl(args or {})
