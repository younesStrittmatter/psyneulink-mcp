"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '80ce5d275b0bf7ada4b219d43478ad569e94fd7f6bf215c76928821ab45d97a3'
__pnl_qualname__ = 'psyneulink.FunctionOutputType'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_function_output_type'
TOOL_DESCRIPTION = 'Call this tool to obtain a FunctionOutputType enum member when a PsyNeuLink function requires an explicit output dimensionality specification (e.g., forcing a result to be a 0-D scalar, 1-D vector, or 2-D array). Returns the IntEnum member corresponding to the given integer value (0=NP_0D_ARRAY, 1=NP_1D_ARRAY, 2=NP_2D_ARRAY, 3=DEFAULT).\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "value": {\n      "default": 3,\n      "description": "Integer selecting the output type: 0=NP_0D_ARRAY (scalar), 1=NP_1D_ARRAY (vector), 2=NP_2D_ARRAY (matrix), 3=DEFAULT (let the function decide).",\n      "enum": [\n        0,\n        1,\n        2,\n        3\n      ],\n      "type": "integer"\n    }\n  },\n  "required": [\n    "value"\n  ],\n  "type": "object"\n}\n\nNotes:\nFunctionOutputType is an IntEnum, so its constructor accepts a single positional integer; pass it as `value`. DEFAULT (3) means the function\'s own output-shape logic is used and is the safe choice when you are unsure. Only override with NP_0D/1D/2D_ARRAY when a downstream consumer requires a specific array dimensionality.'
TOOL_PARAMETERS = { 'properties': { 'value': { 'default': 3,
                             'description': 'Integer selecting the output type: '
                                            '0=NP_0D_ARRAY (scalar), 1=NP_1D_ARRAY '
                                            '(vector), 2=NP_2D_ARRAY (matrix), '
                                            '3=DEFAULT (let the function decide).',
                             'enum': [0, 1, 2, 3],
                             'type': 'integer'}},
  'required': ['value'],
  'type': 'object'}
TOOL_NOTES = "FunctionOutputType is an IntEnum, so its constructor accepts a single positional integer; pass it as `value`. DEFAULT (3) means the function's own output-shape logic is used and is the safe choice when you are unsure. Only override with NP_0D/1D/2D_ARRAY when a downstream consumer requires a specific array dimensionality."


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.FunctionOutputType
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
    def create_function_output_type(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to obtain a FunctionOutputType enum member when a PsyNeuLink function requires an explicit output dimensionality specification (e.g., forcing a result to be a 0-D scalar, 1-D vector, or 2-D array).'
        return _impl(args or {})
