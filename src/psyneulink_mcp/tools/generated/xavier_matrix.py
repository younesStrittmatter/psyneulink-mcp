"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = 'cd622c9b806be9f715f578fd3b3bcb0b4a962865c9411118307f433a21a6017a'
__pnl_qualname__ = 'psyneulink.XavierMatrix'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_xavier_matrix'
TOOL_DESCRIPTION = 'Call this tool when you need to generate a Xavier (Glorot) initialized weight matrix for use as the `matrix` parameter of a `MappingProjection`. The result is a 2D numpy array of shape (sender_size, receiver_size) sampled from either a normal or uniform distribution scaled to balance activation variance across layers. Prefer this over random or identity matrices when connecting layers with tanh or logistic activation functions.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "distribution": {\n      "default": "normal",\n      "description": "Sampling distribution for matrix elements. \'normal\' uses std=sqrt(gain/(sender+receiver)); \'uniform\' uses bound=sqrt(3*gain/(sender+receiver)).",\n      "enum": [\n        "normal",\n        "uniform"\n      ],\n      "type": "string"\n    },\n    "gain": {\n      "default": 1,\n      "description": "Scaling factor applied to the initialization variance. Use 1.0 for tanh; some frameworks recommend sqrt(2) for ReLU, though Xavier is not designed for ReLU.",\n      "type": "number"\n    },\n    "receiver_size": {\n      "description": "Number of columns in the output matrix (units in the receiving layer).",\n      "type": "integer"\n    },\n    "sender_size": {\n      "description": "Number of rows in the output matrix (units in the sending layer).",\n      "type": "integer"\n    }\n  },\n  "required": [\n    "sender_size",\n    "receiver_size"\n  ],\n  "type": "object"\n}\n\nNotes:\nThe matrix is freshly sampled on every call — repeated calls with the same arguments return different values. The returned array has shape (sender_size, receiver_size). Designed for symmetric activations (tanh, logistic); not recommended for ReLU (use He initialization instead). The variance formula uses fan_sum = sender_size + receiver_size, not the fan_in or fan_out separately.'
TOOL_PARAMETERS = { 'properties': { 'distribution': { 'default': 'normal',
                                    'description': 'Sampling distribution for matrix '
                                                   "elements. 'normal' uses "
                                                   'std=sqrt(gain/(sender+receiver)); '
                                                   "'uniform' uses "
                                                   'bound=sqrt(3*gain/(sender+receiver)).',
                                    'enum': ['normal', 'uniform'],
                                    'type': 'string'},
                  'gain': { 'default': 1,
                            'description': 'Scaling factor applied to the '
                                           'initialization variance. Use 1.0 for tanh; '
                                           'some frameworks recommend sqrt(2) for '
                                           'ReLU, though Xavier is not designed for '
                                           'ReLU.',
                            'type': 'number'},
                  'receiver_size': { 'description': 'Number of columns in the output '
                                                    'matrix (units in the receiving '
                                                    'layer).',
                                     'type': 'integer'},
                  'sender_size': { 'description': 'Number of rows in the output matrix '
                                                  '(units in the sending layer).',
                                   'type': 'integer'}},
  'required': ['sender_size', 'receiver_size'],
  'type': 'object'}
TOOL_NOTES = 'The matrix is freshly sampled on every call — repeated calls with the same arguments return different values. The returned array has shape (sender_size, receiver_size). Designed for symmetric activations (tanh, logistic); not recommended for ReLU (use He initialization instead). The variance formula uses fan_sum = sender_size + receiver_size, not the fan_in or fan_out separately.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.XavierMatrix
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
    def create_xavier_matrix(args: dict[str, Any] | None = None) -> Any:
        'Call this tool when you need to generate a Xavier (Glorot) initialized weight matrix for use as the `matrix` parameter of a `MappingProjection`.'
        return _impl(args or {})
