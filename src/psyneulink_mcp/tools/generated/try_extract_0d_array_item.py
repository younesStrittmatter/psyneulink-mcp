"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '92c37b007eda359f0dad8ae030ca2868e69e6343331a9228ae756b0935935cfb'
__pnl_qualname__ = 'psyneulink.core.components.functions.stateful.integratorfunctions.try_extract_0d_array_item'
__pnl_kind__ = 'function'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'try_extract_0d_array_item'
TOOL_DESCRIPTION = 'Call this tool to unwrap a 0-dimensional numpy ndarray into a plain Python scalar. Use it when a PsyNeuLink computation returns a result that may be a 0-d ndarray and you need a bare number or value to pass to downstream logic. Returns the scalar item if input is 0-d ndarray, otherwise returns the input unchanged.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "arr": {\n      "description": "The value to inspect and potentially unwrap. If it is a 0-dimensional numpy ndarray, its scalar item is returned; any other type or shape is returned as-is.",\n      "type": "object"\n    }\n  },\n  "required": [\n    "arr"\n  ],\n  "type": "object"\n}\n\nNotes:\nThe parameter type is declared as \'object\' because JSON Schema has no native ndarray type; pass whatever value you have — non-ndarray inputs (including plain numbers or lists) are returned unchanged due to the AttributeError catch. If arr is a multi-dimensional ndarray (ndim > 0), it is returned unmodified. The function never raises.'
TOOL_PARAMETERS = { 'properties': { 'arr': { 'description': 'The value to inspect and potentially '
                                          'unwrap. If it is a 0-dimensional numpy '
                                          'ndarray, its scalar item is returned; any '
                                          'other type or shape is returned as-is.',
                           'type': 'object'}},
  'required': ['arr'],
  'type': 'object'}
TOOL_NOTES = "The parameter type is declared as 'object' because JSON Schema has no native ndarray type; pass whatever value you have — non-ndarray inputs (including plain numbers or lists) are returned unchanged due to the AttributeError catch. If arr is a multi-dimensional ndarray (ndim > 0), it is returned unmodified. The function never raises."


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.try_extract_0d_array_item
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
    def try_extract_0d_array_item(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to unwrap a 0-dimensional numpy ndarray into a plain Python scalar.'
        return _impl(args or {})
