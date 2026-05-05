"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '94398091c12cbe1cd7f258c7bb9252e8111a33235cba1b24c8a255e612e6412c'
__pnl_qualname__ = 'psyneulink.flatten_list'
__pnl_kind__ = 'function'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'flatten_list'
TOOL_DESCRIPTION = 'Call this tool when you have a list of lists and need to flatten it into a single flat list. It concatenates all sublists into one list, returning a one-dimensional array of the collected items.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "l": {\n      "description": "A list of lists to flatten. Each element must itself be an iterable; non-iterable elements will cause a TypeError.",\n      "items": {\n        "type": "array"\n      },\n      "type": "array"\n    }\n  },\n  "required": [\n    "l"\n  ],\n  "type": "object"\n}\n\nNotes:\nFlattens exactly one level deep — if sublists contain further nested lists, those inner lists are left intact. The argument name is the single letter `l` (lowercase L). Passing an empty outer list returns an empty list; passing sublists that are empty is fine. Non-iterable elements inside `l` (e.g., bare integers) will raise a TypeError.'
TOOL_PARAMETERS = { 'properties': { 'l': { 'description': 'A list of lists to flatten. Each element must '
                                        'itself be an iterable; non-iterable elements '
                                        'will cause a TypeError.',
                         'items': {'type': 'array'},
                         'type': 'array'}},
  'required': ['l'],
  'type': 'object'}
TOOL_NOTES = 'Flattens exactly one level deep — if sublists contain further nested lists, those inner lists are left intact. The argument name is the single letter `l` (lowercase L). Passing an empty outer list returns an empty list; passing sublists that are empty is fine. Non-iterable elements inside `l` (e.g., bare integers) will raise a TypeError.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.flatten_list
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
    def flatten_list(args: dict[str, Any] | None = None) -> Any:
        'Call this tool when you have a list of lists and need to flatten it into a single flat list.'
        return _impl(args or {})
