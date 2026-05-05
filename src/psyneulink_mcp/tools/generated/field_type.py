"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '694a2d39793cc1336dd7a0657dd6e34d0c13d72a3fd90dfc9c9efaaa1e4a1418'
__pnl_qualname__ = 'psyneulink.FieldType'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_field_type'
TOOL_DESCRIPTION = 'Call this tool when you need to specify whether a memory field in an EMComposition serves as a retrieval key (matched against queries) or a stored value (returned as retrieved content). Returns the corresponding FieldType enum member (KEY=0 or VALUE=1) for use in EMComposition field configuration.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "value": {\n      "description": "Numeric value of the enum member: 0 for KEY (field used for query matching/retrieval), 1 for VALUE (field returned as retrieved content).",\n      "enum": [\n        0,\n        1\n      ],\n      "type": "integer"\n    }\n  },\n  "required": [\n    "value"\n  ],\n  "type": "object"\n}\n\nNotes:\nFieldType is a two-member Enum: KEY=0 (memory fields matched against the query during retrieval) and VALUE=1 (fields fetched as output when a match is found). Enum instantiation uses positional value — `FieldType(0)` — not keyword arguments; the `value` parameter here maps to that positional call. In most EMComposition workflows you will not need to construct a FieldType directly; instead pass the string "KEY" or "VALUE" where a field_type argument is expected and PsyNeuLink will resolve it. Only call this tool if you explicitly need the enum object itself.'
TOOL_PARAMETERS = { 'properties': { 'value': { 'description': 'Numeric value of the enum member: 0 for '
                                            'KEY (field used for query '
                                            'matching/retrieval), 1 for VALUE (field '
                                            'returned as retrieved content).',
                             'enum': [0, 1],
                             'type': 'integer'}},
  'required': ['value'],
  'type': 'object'}
TOOL_NOTES = 'FieldType is a two-member Enum: KEY=0 (memory fields matched against the query during retrieval) and VALUE=1 (fields fetched as output when a match is found). Enum instantiation uses positional value — `FieldType(0)` — not keyword arguments; the `value` parameter here maps to that positional call. In most EMComposition workflows you will not need to construct a FieldType directly; instead pass the string "KEY" or "VALUE" where a field_type argument is expected and PsyNeuLink will resolve it. Only call this tool if you explicitly need the enum object itself.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.FieldType
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
    def create_field_type(args: dict[str, Any] | None = None) -> Any:
        'Call this tool when you need to specify whether a memory field in an EMComposition serves as a retrieval key (matched against queries) or a stored value (returned as retrieved content).'
        return _impl(args or {})
