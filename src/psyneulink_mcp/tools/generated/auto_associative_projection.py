"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = 'fdab1fa9b24a736aa28d08d46683359daaefb9e3e2769ffaeb21d01670b4423e'
__pnl_qualname__ = 'psyneulink.AutoAssociativeProjection'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_auto_associative_projection'
TOOL_DESCRIPTION = 'Call this tool when you need to explicitly construct a self-recurrent projection on a RecurrentTransferMechanism — i.e., when you are manually wiring a mechanism\'s output back to its own input rather than letting RecurrentTransferMechanism create it automatically. The result is an AutoAssociativeProjection object whose sender and receiver both belong to the same Mechanism. Prefer letting RecurrentTransferMechanism create this implicitly unless you need to override the default matrix or function.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "matrix": {\n      "description": "Square 2D matrix used to transform sender output to receiver input. Must have equal rows and columns matching the sender\'s output size. Do NOT pass auto or hetero separately \\u2014 they should already be baked into this matrix.",\n      "items": {\n        "items": {\n          "type": "number"\n        },\n        "type": "array"\n      },\n      "type": "array"\n    },\n    "name": {\n      "description": "Optional string name for the projection.",\n      "type": "string"\n    },\n    "owner": {\n      "description": "Name of the Mechanism that owns this projection. If provided, sender and receiver default to this mechanism. Must be a Mechanism instance reference (pass as a variable name string resolved in context).",\n      "type": "string"\n    },\n    "receiver": {\n      "description": "Name/reference of the InputPort or Mechanism that is the destination of the projection\'s output. Must belong to the same Mechanism as sender.",\n      "type": "string"\n    },\n    "sender": {\n      "description": "Name/reference of the OutputPort or Mechanism that is the source of the projection\'s input. Must belong to the same Mechanism as receiver.",\n      "type": "string"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\nAutoAssociativeProjection is almost always created implicitly by RecurrentTransferMechanism — call this tool directly only when you need explicit control. The `auto` and `hetero` parameters are NOT accepted by the constructor; they must be pre-incorporated into the `matrix` argument before passing. Both sender and receiver must belong to the same Mechanism — passing ports or mechanisms from different mechanisms will raise an error. The matrix must be square (n×n where n equals the mechanism\'s output size). If `owner` is provided and sender/receiver are omitted, both default to the owner mechanism. Accessing `.matrix` on the returned projection delegates to the owner mechanism\'s matrix, so mutations via `.matrix =` affect the owning RecurrentTransferMechanism.'
TOOL_PARAMETERS = { 'properties': { 'matrix': { 'description': 'Square 2D matrix used to transform '
                                             'sender output to receiver input. Must '
                                             'have equal rows and columns matching the '
                                             "sender's output size. Do NOT pass auto "
                                             'or hetero separately — they should '
                                             'already be baked into this matrix.',
                              'items': {'items': {'type': 'number'}, 'type': 'array'},
                              'type': 'array'},
                  'name': { 'description': 'Optional string name for the projection.',
                            'type': 'string'},
                  'owner': { 'description': 'Name of the Mechanism that owns this '
                                            'projection. If provided, sender and '
                                            'receiver default to this mechanism. Must '
                                            'be a Mechanism instance reference (pass '
                                            'as a variable name string resolved in '
                                            'context).',
                             'type': 'string'},
                  'receiver': { 'description': 'Name/reference of the InputPort or '
                                               'Mechanism that is the destination of '
                                               "the projection's output. Must belong "
                                               'to the same Mechanism as sender.',
                                'type': 'string'},
                  'sender': { 'description': 'Name/reference of the OutputPort or '
                                             'Mechanism that is the source of the '
                                             "projection's input. Must belong to the "
                                             'same Mechanism as receiver.',
                              'type': 'string'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = "AutoAssociativeProjection is almost always created implicitly by RecurrentTransferMechanism — call this tool directly only when you need explicit control. The `auto` and `hetero` parameters are NOT accepted by the constructor; they must be pre-incorporated into the `matrix` argument before passing. Both sender and receiver must belong to the same Mechanism — passing ports or mechanisms from different mechanisms will raise an error. The matrix must be square (n×n where n equals the mechanism's output size). If `owner` is provided and sender/receiver are omitted, both default to the owner mechanism. Accessing `.matrix` on the returned projection delegates to the owner mechanism's matrix, so mutations via `.matrix =` affect the owning RecurrentTransferMechanism."


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.AutoAssociativeProjection
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
    def create_auto_associative_projection(args: dict[str, Any] | None = None) -> Any:
        "Call this tool when you need to explicitly construct a self-recurrent projection on a RecurrentTransferMechanism — i.e., when you are manually wiring a mechanism's output back to its own input rather than letting RecurrentTransferMechanism create it automatically."
        return _impl(args or {})
