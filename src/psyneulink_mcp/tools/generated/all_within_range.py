"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = 'df30e8e22f77df356f0a762e2afbce0c9755d6b31ff17b64caf9105a98b7cec2'
__pnl_qualname__ = 'psyneulink.all_within_range'
__pnl_kind__ = 'function'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'all_within_range'
TOOL_DESCRIPTION = 'Call this tool to check whether a numeric value or array is not entirely outside a given range. Returns True unless all elements are below min or all elements are above max — useful for a loose boundary check on PsyNeuLink parameter values before passing them to a mechanism or function. The result is a boolean.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "max": {\n      "description": "Upper bound. Pass null to skip the upper-bound check.",\n      "oneOf": [\n        {\n          "type": "number"\n        },\n        {\n          "type": "null"\n        }\n      ]\n    },\n    "min": {\n      "description": "Lower bound. Pass null to skip the lower-bound check.",\n      "oneOf": [\n        {\n          "type": "number"\n        },\n        {\n          "type": "null"\n        }\n      ]\n    },\n    "x": {\n      "description": "The numeric value or array (including nested arrays) to test against the bounds.",\n      "oneOf": [\n        {\n          "type": "number"\n        },\n        {\n          "type": "array"\n        }\n      ]\n    }\n  },\n  "required": [\n    "x",\n    "min",\n    "max"\n  ],\n  "type": "object"\n}\n\nNotes:\nSemantics are NOT "every element is within [min, max]". The function returns False only when ALL elements are below min OR all elements are above max. A mixed array like [0.5, 1.5] with min=1 returns True (not all below 1), even though 0.5 < 1. Use this for loose range checks, not strict per-element validation. Nested arrays are handled recursively. Both min and max accept None (null) to disable that bound.'
TOOL_PARAMETERS = { 'properties': { 'max': { 'description': 'Upper bound. Pass null to skip the '
                                          'upper-bound check.',
                           'oneOf': [{'type': 'number'}, {'type': 'null'}]},
                  'min': { 'description': 'Lower bound. Pass null to skip the '
                                          'lower-bound check.',
                           'oneOf': [{'type': 'number'}, {'type': 'null'}]},
                  'x': { 'description': 'The numeric value or array (including nested '
                                        'arrays) to test against the bounds.',
                         'oneOf': [{'type': 'number'}, {'type': 'array'}]}},
  'required': ['x', 'min', 'max'],
  'type': 'object'}
TOOL_NOTES = 'Semantics are NOT "every element is within [min, max]". The function returns False only when ALL elements are below min OR all elements are above max. A mixed array like [0.5, 1.5] with min=1 returns True (not all below 1), even though 0.5 < 1. Use this for loose range checks, not strict per-element validation. Nested arrays are handled recursively. Both min and max accept None (null) to disable that bound.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.all_within_range
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
    def all_within_range(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to check whether a numeric value or array is not entirely outside a given range.'
        return _impl(args or {})
