"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = 'f37629a4f89a229a917432a8e35ec36250b03247a1fa73c8ff53d0909b6bbcc0'
__pnl_qualname__ = 'psyneulink.Dropout'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_dropout'
TOOL_DESCRIPTION = 'Use this tool to create a Dropout function for regularizing neural network learning in PsyNeuLink. Call it when attaching a dropout transfer function to a mechanism that participates in learning — it randomly zeros elements with probability `p` during learning passes (scaling survivors by 1/(1-p)), and acts as a pure identity during inference/evaluation. Returns a configured Dropout function object ready to be assigned as a mechanism\'s `function`.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "default_variable": {\n      "description": "Template array defining the shape/dimensionality of inputs this function will process. Required when the function is used standalone; optional when assigned to a mechanism (which supplies its own variable).",\n      "items": {\n        "type": "number"\n      },\n      "type": "array"\n    },\n    "name": {\n      "description": "Optional name for the Dropout function instance. If omitted, a default name is assigned by FunctionRegistry.",\n      "type": "string"\n    },\n    "p": {\n      "default": 0.5,\n      "description": "Dropout probability \\u2014 each element of the input is independently zeroed with this probability during learning. 0.0 disables dropout (identity); 1.0 zeros everything.",\n      "maximum": 1,\n      "minimum": 0,\n      "type": "number"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\nDropout is ONLY active when the execution context is in LEARNING_MODE (i.e., during backprop/training passes). In all other run modes — including standard forward evaluation — it behaves as an exact identity, returning variable unchanged without any scaling. The inverse scaling factor 1/(1-p) is applied to surviving (non-zeroed) elements during learning, matching PyTorch\'s default dropout behavior. The `derivative` method returns the scalar 1.0 unconditionally (not element-wise 0/1 based on the mask), so gradient computations through this function are approximate. Do not pass `params` or `owner` from the agent — those are wired by the host template.'
TOOL_PARAMETERS = { 'properties': { 'default_variable': { 'description': 'Template array defining the '
                                                       'shape/dimensionality of inputs '
                                                       'this function will process. '
                                                       'Required when the function is '
                                                       'used standalone; optional when '
                                                       'assigned to a mechanism (which '
                                                       'supplies its own variable).',
                                        'items': {'type': 'number'},
                                        'type': 'array'},
                  'name': { 'description': 'Optional name for the Dropout function '
                                           'instance. If omitted, a default name is '
                                           'assigned by FunctionRegistry.',
                            'type': 'string'},
                  'p': { 'default': 0.5,
                         'description': 'Dropout probability — each element of the '
                                        'input is independently zeroed with this '
                                        'probability during learning. 0.0 disables '
                                        'dropout (identity); 1.0 zeros everything.',
                         'maximum': 1,
                         'minimum': 0,
                         'type': 'number'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = "Dropout is ONLY active when the execution context is in LEARNING_MODE (i.e., during backprop/training passes). In all other run modes — including standard forward evaluation — it behaves as an exact identity, returning variable unchanged without any scaling. The inverse scaling factor 1/(1-p) is applied to surviving (non-zeroed) elements during learning, matching PyTorch's default dropout behavior. The `derivative` method returns the scalar 1.0 unconditionally (not element-wise 0/1 based on the mask), so gradient computations through this function are approximate. Do not pass `params` or `owner` from the agent — those are wired by the host template."


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.Dropout
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
    def create_dropout(args: dict[str, Any] | None = None) -> Any:
        'Use this tool to create a Dropout function for regularizing neural network learning in PsyNeuLink.'
        return _impl(args or {})
