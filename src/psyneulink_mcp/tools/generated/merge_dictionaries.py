"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = 'f569abdfd3468d555101264cdd4c6445603a67bbc3b70ea0d01017dbeab4d843'
__pnl_qualname__ = 'psyneulink.merge_dictionaries'
__pnl_kind__ = 'function'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'merge_dictionaries'
TOOL_DESCRIPTION = 'Call this tool when you need to merge two PsyNeuLink parameter or configuration dictionaries and want to detect key collisions. Returns a tuple of (merged_dict, had_conflicts): the merged dict combines all key-value pairs from both inputs, with shared keys resolved into union sets rather than overwriting; the boolean is True if any keys overlapped.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "a": {\n      "additionalProperties": true,\n      "description": "First dictionary to merge. Any JSON-serializable key-value pairs.",\n      "type": "object"\n    },\n    "b": {\n      "additionalProperties": true,\n      "description": "Second dictionary to merge. Any JSON-serializable key-value pairs.",\n      "type": "object"\n    }\n  },\n  "required": [\n    "a",\n    "b"\n  ],\n  "type": "object"\n}\n\nNotes:\nShared keys are NOT overwritten — their values are merged into a union set via `create_union_set`. The returned bool is True when `len(merged) < len(a) + len(b)`, i.e., when there was at least one overlapping key. If you need simple last-write-wins merging, use a plain dict update instead. Values that end up as sets may not be accepted by PsyNeuLink parameters that expect scalar types.'
TOOL_PARAMETERS = { 'properties': { 'a': { 'additionalProperties': True,
                         'description': 'First dictionary to merge. Any '
                                        'JSON-serializable key-value pairs.',
                         'type': 'object'},
                  'b': { 'additionalProperties': True,
                         'description': 'Second dictionary to merge. Any '
                                        'JSON-serializable key-value pairs.',
                         'type': 'object'}},
  'required': ['a', 'b'],
  'type': 'object'}
TOOL_NOTES = 'Shared keys are NOT overwritten — their values are merged into a union set via `create_union_set`. The returned bool is True when `len(merged) < len(a) + len(b)`, i.e., when there was at least one overlapping key. If you need simple last-write-wins merging, use a plain dict update instead. Values that end up as sets may not be accepted by PsyNeuLink parameters that expect scalar types.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.merge_dictionaries
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
    def merge_dictionaries(args: dict[str, Any] | None = None) -> Any:
        'Call this tool when you need to merge two PsyNeuLink parameter or configuration dictionaries and want to detect key collisions.'
        return _impl(args or {})
