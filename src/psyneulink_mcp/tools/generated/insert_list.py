"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '767aa3963dc8bbc4a62ddff3ac95be8cfaf3d2743a13b0f1400c4a0f7e24c035'
__pnl_qualname__ = 'psyneulink.insert_list'
__pnl_kind__ = 'function'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'insert_list'
TOOL_DESCRIPTION = 'Call this tool when you need to splice the elements of one list into another list at a specific index position. Returns a new list with list2\'s elements inserted into list1 starting at `position` — the elements of list2 are flattened in, not nested.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "list1": {\n      "description": "The base list to insert into. Elements can be of any type consistent with list2.",\n      "type": "array"\n    },\n    "list2": {\n      "description": "The list whose elements will be spliced into list1 at the given position.",\n      "type": "array"\n    },\n    "position": {\n      "description": "Zero-based index in list1 at which to begin inserting elements from list2. Elements at or after this index are shifted right.",\n      "type": "integer"\n    }\n  },\n  "required": [\n    "list1",\n    "position",\n    "list2"\n  ],\n  "type": "object"\n}\n\nNotes:\nThis is a splice, not a nested insert: elements of list2 are individually inserted into list1 (equivalent to list1[:position] + list2 + list1[position:]). The result length is len(list1) + len(list2). Position is not bounds-checked; out-of-range values silently clamp to the start or end (Python slice behavior).'
TOOL_PARAMETERS = { 'properties': { 'list1': { 'description': 'The base list to insert into. Elements '
                                            'can be of any type consistent with list2.',
                             'type': 'array'},
                  'list2': { 'description': 'The list whose elements will be spliced '
                                            'into list1 at the given position.',
                             'type': 'array'},
                  'position': { 'description': 'Zero-based index in list1 at which to '
                                               'begin inserting elements from list2. '
                                               'Elements at or after this index are '
                                               'shifted right.',
                                'type': 'integer'}},
  'required': ['list1', 'position', 'list2'],
  'type': 'object'}
TOOL_NOTES = 'This is a splice, not a nested insert: elements of list2 are individually inserted into list1 (equivalent to list1[:position] + list2 + list1[position:]). The result length is len(list1) + len(list2). Position is not bounds-checked; out-of-range values silently clamp to the start or end (Python slice behavior).'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.insert_list
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
    def insert_list(args: dict[str, Any] | None = None) -> Any:
        'Call this tool when you need to splice the elements of one list into another list at a specific index position.'
        return _impl(args or {})
