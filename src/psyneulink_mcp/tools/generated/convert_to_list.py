"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '119156007a51c6d52e8bb9dc4c25cfe21b47e56bfe0d3cc54df61d95924dbf30'
__pnl_qualname__ = 'psyneulink.convert_to_list'
__pnl_kind__ = 'function'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'convert_to_list'
TOOL_DESCRIPTION = 'Call this tool when you need to normalize a value of unknown type into a Python list before passing it to a PsyNeuLink function that expects a list. Returns None when given None; always returns a list otherwise. Useful for coercing scalars, tuples, sets, or numpy arrays into a uniform list form.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "l": {\n      "description": "The value to convert to a list. Accepts null, a scalar (string, number, boolean), an array (list or tuple), or an object (dict). Null is passed through as null.",\n      "oneOf": [\n        {\n          "type": "string"\n        },\n        {\n          "type": "number"\n        },\n        {\n          "type": "boolean"\n        },\n        {\n          "type": "array"\n        },\n        {\n          "type": "object"\n        },\n        {\n          "type": "null"\n        }\n      ]\n    }\n  },\n  "required": [\n    "l"\n  ],\n  "type": "object"\n}\n\nNotes:\nReturns None (not an empty list) when l is None — callers that need an empty list must handle this case explicitly. Dicts are wrapped in a single-element list containing the dict object (the dict-to-list-of-tuples branch is commented out in the source). Sets are converted to lists but with no guaranteed ordering. A zero-dimensional numpy array (ndim == 0) is treated as a scalar and wrapped in a list rather than converted element-wise.'
TOOL_PARAMETERS = { 'properties': { 'l': { 'description': 'The value to convert to a list. Accepts null, '
                                        'a scalar (string, number, boolean), an array '
                                        '(list or tuple), or an object (dict). Null is '
                                        'passed through as null.',
                         'oneOf': [ {'type': 'string'},
                                    {'type': 'number'},
                                    {'type': 'boolean'},
                                    {'type': 'array'},
                                    {'type': 'object'},
                                    {'type': 'null'}]}},
  'required': ['l'],
  'type': 'object'}
TOOL_NOTES = 'Returns None (not an empty list) when l is None — callers that need an empty list must handle this case explicitly. Dicts are wrapped in a single-element list containing the dict object (the dict-to-list-of-tuples branch is commented out in the source). Sets are converted to lists but with no guaranteed ordering. A zero-dimensional numpy array (ndim == 0) is treated as a scalar and wrapped in a list rather than converted element-wise.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.convert_to_list
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
    def convert_to_list(args: dict[str, Any] | None = None) -> Any:
        'Call this tool when you need to normalize a value of unknown type into a Python list before passing it to a PsyNeuLink function that expects a list.'
        return _impl(args or {})
