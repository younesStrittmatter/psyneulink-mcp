"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = 'db91912c173d7b4074cc6c8cf7260cb4b6e2ccfc14be9c06447bab46e578974a'
__pnl_qualname__ = 'psyneulink.convert_to_np_array'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'convert_to_np_array'
TOOL_DESCRIPTION = 'Call this tool when you need to normalize a Python value (scalar, list, nested list, or existing array) into a NumPy ndarray before passing it to a PsyNeuLink component that expects array input. Optionally enforce a minimum dimensionality of 1 or 2. Returns a NumPy ndarray of the appropriate shape.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "dimension": {\n      "description": "Minimum number of dimensions for the output array. Pass 1 to ensure at least 1-D, 2 to ensure at least 2-D, or omit (null) to leave dimensionality as-is after array creation.",\n      "enum": [\n        1,\n        2\n      ],\n      "type": "integer"\n    },\n    "value": {\n      "description": "The item to convert \\u2014 scalar, list, nested list, or existing ndarray. Ragged (non-uniform) nested lists are handled automatically.",\n      "items": {},\n      "type": "array"\n    }\n  },\n  "required": [\n    "value"\n  ],\n  "type": "object"\n}\n\nNotes:\n- `dimension` only accepts 1, 2, or null (omitted); any other integer raises UtilitiesError.\n- Ragged inputs (lists of sub-arrays with unequal lengths) are stored as object-dtype arrays when `dimension=2`; the 2-D reshape step is intentionally skipped in that case to avoid data loss.\n- `value` is typed as `array` in the schema for agent convenience, but scalars and nested structures are also accepted by the underlying Python function — if you need to pass a bare scalar, wrap it in a single-element list.\n- The function uses `safe_create_np_array` internally, which handles torch tensors as well as plain Python objects; the returned array may be a torch tensor if the input was one.'
TOOL_PARAMETERS = { 'properties': { 'dimension': { 'description': 'Minimum number of dimensions for the '
                                                'output array. Pass 1 to ensure at '
                                                'least 1-D, 2 to ensure at least 2-D, '
                                                'or omit (null) to leave '
                                                'dimensionality as-is after array '
                                                'creation.',
                                 'enum': [1, 2],
                                 'type': 'integer'},
                  'value': { 'description': 'The item to convert — scalar, list, '
                                            'nested list, or existing ndarray. Ragged '
                                            '(non-uniform) nested lists are handled '
                                            'automatically.',
                             'items': {},
                             'type': 'array'}},
  'required': ['value'],
  'type': 'object'}
TOOL_NOTES = '- `dimension` only accepts 1, 2, or null (omitted); any other integer raises UtilitiesError.\n- Ragged inputs (lists of sub-arrays with unequal lengths) are stored as object-dtype arrays when `dimension=2`; the 2-D reshape step is intentionally skipped in that case to avoid data loss.\n- `value` is typed as `array` in the schema for agent convenience, but scalars and nested structures are also accepted by the underlying Python function — if you need to pass a bare scalar, wrap it in a single-element list.\n- The function uses `safe_create_np_array` internally, which handles torch tensors as well as plain Python objects; the returned array may be a torch tensor if the input was one.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.convert_to_np_array
    resolved = handles.resolve_in(kwargs)
    result = target(**resolved)
    try:
        json.dumps(result)
    except (TypeError, ValueError):
        return handles.register_handle(result)
    return result


def register(mcp: Any) -> None:
    @captured_tool(mcp, layer="generated", name=TOOL_NAME, description=TOOL_DESCRIPTION)
    def convert_to_np_array(args: dict[str, Any] | None = None) -> Any:
        'Call this tool when you need to normalize a Python value (scalar, list, nested list, or existing array) into a NumPy ndarray before passing it to a PsyNeuLink component that expects array input.'
        return _impl(args or {})
