"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = 'bf19a62dcaf2ade18f191fb3767557943ff2d98be9f845155f765c34e5503a61'
__pnl_qualname__ = 'psyneulink.core.components.functions.nonstateful.learningfunctions.safe_len'
__pnl_kind__ = 'function'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'safe_len'
TOOL_DESCRIPTION = 'Call this tool when you need the length of an object that may or may not support `len()` — for example, when handling a PsyNeuLink parameter that could be a scalar, None, or an array. Returns an integer: the true length if the object is sized, or `fallback` if `len()` raises a TypeError.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "arr": {\n      "description": "The object whose length to measure. Typically a list or array; scalars and None are handled gracefully via the fallback.",\n      "type": "array"\n    },\n    "fallback": {\n      "default": 1,\n      "description": "Value to return when arr does not support len(). Defaults to 1.",\n      "type": "integer"\n    }\n  },\n  "required": [\n    "arr"\n  ],\n  "type": "object"\n}\n\nNotes:\nThe default fallback is 1, not 0 — if you want 0 returned for non-sized objects (e.g., scalars), you must pass fallback=0 explicitly. Only TypeError is caught; other exceptions (e.g., from a broken __len__) will propagate.'
TOOL_PARAMETERS = { 'properties': { 'arr': { 'description': 'The object whose length to measure. '
                                          'Typically a list or array; scalars and None '
                                          'are handled gracefully via the fallback.',
                           'type': 'array'},
                  'fallback': { 'default': 1,
                                'description': 'Value to return when arr does not '
                                               'support len(). Defaults to 1.',
                                'type': 'integer'}},
  'required': ['arr'],
  'type': 'object'}
TOOL_NOTES = 'The default fallback is 1, not 0 — if you want 0 returned for non-sized objects (e.g., scalars), you must pass fallback=0 explicitly. Only TypeError is caught; other exceptions (e.g., from a broken __len__) will propagate.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.safe_len
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
    def safe_len(args: dict[str, Any] | None = None) -> Any:
        'Call this tool when you need the length of an object that may or may not support `len()` — for example, when handling a PsyNeuLink parameter that could be a scalar, None, or an array.'
        return _impl(args or {})
