"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '9adc62637f9bc4732731726fd54a2e7b9d14d9404a6e9758de8fb10377114a34'
__pnl_qualname__ = 'psyneulink.PreferenceLevel'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_preference_level'
TOOL_DESCRIPTION = 'Call this tool to resolve a PsyNeuLink `PreferenceLevel` enum member by its integer code — use it when you need to convert a numeric level (0–5) to its named constant (NONE, INSTANCE, SUBTYPE, TYPE, CATEGORY, COMPOSITION) before passing a preference level to another PNL tool or inspection call. Returns the enum member, which is simultaneously an integer and a named constant.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "value": {\n      "description": "Integer code of the desired preference level: NONE=0, INSTANCE=1, SUBTYPE=2, TYPE=3, CATEGORY=4, COMPOSITION=5.",\n      "enum": [\n        0,\n        1,\n        2,\n        3,\n        4,\n        5\n      ],\n      "type": "integer"\n    }\n  },\n  "required": [\n    "value"\n  ],\n  "type": "object"\n}\n\nNotes:\nPreferenceLevel is an IntEnum, so any member compares equal to its integer value and can be used anywhere an int is expected. The six levels form a strict hierarchy — higher numeric values represent broader (less specific) scopes: INSTANCE (1) is the narrowest (a single object), COMPOSITION (5) is the broadest. When PsyNeuLink resolves a preference it walks up this hierarchy, so a preference set at COMPOSITION can be overridden by one set at TYPE, SUBTYPE, or INSTANCE. NONE (0) means no preference level is assigned. You cannot instantiate this enum by name string via the tool (e.g. "INSTANCE") — pass the integer code only.'
TOOL_PARAMETERS = { 'properties': { 'value': { 'description': 'Integer code of the desired preference '
                                            'level: NONE=0, INSTANCE=1, SUBTYPE=2, '
                                            'TYPE=3, CATEGORY=4, COMPOSITION=5.',
                             'enum': [0, 1, 2, 3, 4, 5],
                             'type': 'integer'}},
  'required': ['value'],
  'type': 'object'}
TOOL_NOTES = 'PreferenceLevel is an IntEnum, so any member compares equal to its integer value and can be used anywhere an int is expected. The six levels form a strict hierarchy — higher numeric values represent broader (less specific) scopes: INSTANCE (1) is the narrowest (a single object), COMPOSITION (5) is the broadest. When PsyNeuLink resolves a preference it walks up this hierarchy, so a preference set at COMPOSITION can be overridden by one set at TYPE, SUBTYPE, or INSTANCE. NONE (0) means no preference level is assigned. You cannot instantiate this enum by name string via the tool (e.g. "INSTANCE") — pass the integer code only.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.PreferenceLevel
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
    def create_preference_level(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to resolve a PsyNeuLink `PreferenceLevel` enum member by its integer code — use it when you need to convert a numeric level (0–5) to its named constant (NONE, INSTANCE, SUBTYPE, TYPE, CATEGORY, COMPOSITION) before passing a preference level to another PNL tool or inspection call.'
        return _impl(args or {})
