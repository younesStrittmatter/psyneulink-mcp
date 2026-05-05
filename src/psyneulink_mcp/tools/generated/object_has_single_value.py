"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = 'af636684a5531fe65c237b8071d0ce925c6a6d14ee0c308781b00ebf7eede00e'
__pnl_qualname__ = 'psyneulink.object_has_single_value'
__pnl_kind__ = 'function'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'object_has_single_value'
TOOL_DESCRIPTION = 'Call this tool to check whether a value, array, or nested structure contains exactly one scalar element regardless of its shape or nesting. Returns True if all dimensions have size ≤ 1 (e.g., a scalar, a 1-element list, or a shape-(1,1,1) array), False otherwise. Useful for validating inputs before passing them to PsyNeuLink components that require singleton values.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "obj": {\n      "description": "The value to test. Can be a scalar, list, nested list, or numpy array. Will be cast to a numpy array internally before checking.",\n      "type": [\n        "number",\n        "boolean",\n        "array"\n      ]\n    }\n  },\n  "required": [\n    "obj"\n  ],\n  "type": "object"\n}\n\nNotes:\nAny input is coerced to a numpy array via `np.asarray` before shape inspection, so scalars and nested lists are handled transparently. A shape-() zero-dimensional array (bare scalar) has no dimensions to iterate and returns True. An empty array (shape containing 0) also returns True since no dimension exceeds 1 — pass only non-empty inputs if that edge case matters.'
TOOL_PARAMETERS = { 'properties': { 'obj': { 'description': 'The value to test. Can be a scalar, list, '
                                          'nested list, or numpy array. Will be cast '
                                          'to a numpy array internally before '
                                          'checking.',
                           'type': ['number', 'boolean', 'array']}},
  'required': ['obj'],
  'type': 'object'}
TOOL_NOTES = 'Any input is coerced to a numpy array via `np.asarray` before shape inspection, so scalars and nested lists are handled transparently. A shape-() zero-dimensional array (bare scalar) has no dimensions to iterate and returns True. An empty array (shape containing 0) also returns True since no dimension exceeds 1 — pass only non-empty inputs if that edge case matters.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.object_has_single_value
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
    def object_has_single_value(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to check whether a value, array, or nested structure contains exactly one scalar element regardless of its shape or nesting.'
        return _impl(args or {})
