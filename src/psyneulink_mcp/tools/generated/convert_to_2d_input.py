"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '1af344c4d7b9e2dafa883a4816235205c19888be7664f711d5f84aabb19fa2f5'
__pnl_qualname__ = 'psyneulink.convert_to_2d_input'
__pnl_kind__ = 'function'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'convert_to_2d_input'
TOOL_DESCRIPTION = 'Call this tool when you need to normalize an array-like value (scalar, 1D list/array, or 2D list/array) into a canonical 2D format — a list of 1D numpy arrays — before passing input to a Leabra mechanism. Returns a list of numpy arrays regardless of whether the input was a scalar, flat list, or nested list.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "array_like": {\n      "description": "The value to convert. Accepts a scalar number, a 1D list/array of numbers, or a 2D list/array (list of lists). Values of 3D or higher will trigger a warning and may not convert correctly.",\n      "oneOf": [\n        {\n          "type": "number"\n        },\n        {\n          "items": {\n            "type": "number"\n          },\n          "type": "array"\n        },\n        {\n          "items": {\n            "items": {\n              "type": "number"\n            },\n            "type": "array"\n          },\n          "type": "array"\n        }\n      ]\n    }\n  },\n  "required": [\n    "array_like"\n  ],\n  "type": "object"\n}\n\nNotes:\n- A scalar input `n` becomes `[np.array([n])]`.\n- A 1D input `[a, b, c]` becomes `[np.array([a, b, c])]`.\n- A 2D input `[[a, b], [c, d]]` becomes `[np.array([a, b]), np.array([c, d])]`.\n- Inputs of 3D or higher print a warning to stdout but still attempt conversion; results may be incorrect.\n- If `array_like` is not a number, list, or np.ndarray (e.g., a plain dict or string), the function returns `None` silently — no error is raised.'
TOOL_PARAMETERS = { 'properties': { 'array_like': { 'description': 'The value to convert. Accepts a '
                                                 'scalar number, a 1D list/array of '
                                                 'numbers, or a 2D list/array (list of '
                                                 'lists). Values of 3D or higher will '
                                                 'trigger a warning and may not '
                                                 'convert correctly.',
                                  'oneOf': [ {'type': 'number'},
                                             { 'items': {'type': 'number'},
                                               'type': 'array'},
                                             { 'items': { 'items': {'type': 'number'},
                                                          'type': 'array'},
                                               'type': 'array'}]}},
  'required': ['array_like'],
  'type': 'object'}
TOOL_NOTES = '- A scalar input `n` becomes `[np.array([n])]`.\n- A 1D input `[a, b, c]` becomes `[np.array([a, b, c])]`.\n- A 2D input `[[a, b], [c, d]]` becomes `[np.array([a, b]), np.array([c, d])]`.\n- Inputs of 3D or higher print a warning to stdout but still attempt conversion; results may be incorrect.\n- If `array_like` is not a number, list, or np.ndarray (e.g., a plain dict or string), the function returns `None` silently — no error is raised.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.convert_to_2d_input
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
    def convert_to_2d_input(args: dict[str, Any] | None = None) -> Any:
        'Call this tool when you need to normalize an array-like value (scalar, 1D list/array, or 2D list/array) into a canonical 2D format — a list of 1D numpy arrays — before passing input to a Leabra mechanism.'
        return _impl(args or {})
