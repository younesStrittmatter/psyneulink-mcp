"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = 'a290a17b0eabd2f9d6ad22d740d0927886f464703fc28b0fc9dfda9ed61a7d52'
__pnl_qualname__ = 'psyneulink.Normalize'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_normalize'
TOOL_DESCRIPTION = 'Call this tool to create a PsyNeuLink Normalize function that L2-normalizes an array (divides each value by the Euclidean norm of the vector). Use it when you need unit-vector outputs from a mechanism or want to scale activations so their magnitude is 1. Returns a Normalize Function object suitable for assigning to a mechanism\'s `function` parameter.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "default_variable": {\n      "description": "Template array defining the shape and default value to be normalized. For 2D inputs, provide a nested array.",\n      "items": {\n        "type": "number"\n      },\n      "type": "array"\n    },\n    "eps": {\n      "default": 1e-12,\n      "description": "Small positive constant for numerical stability. The denominator is clamped to this value when the L2 norm is near zero, preventing division by zero.",\n      "type": "number"\n    },\n    "name": {\n      "description": "Optional name for this Normalize function instance.",\n      "type": "string"\n    },\n    "per_item": {\n      "default": true,\n      "description": "For 2D variables (batch inputs), if true each row is normalized independently; if false the entire 2D array is normalized as a single vector.",\n      "type": "boolean"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\nThe normalization formula is x / max(‖x‖₂, eps). When the input norm is at or below eps the output magnitude is not 1 — the vector is scaled by 1/eps instead, which for the default eps=1e-12 produces very large values; callers should ensure inputs are not near-zero. The `per_item=True` default only activates for inputs with ndim > 1; 1D inputs are always normalized as a single vector regardless of this flag. `params`, `owner`, and `prefs` are advanced PsyNeuLink internals rarely needed by agents and are omitted from the schema.'
TOOL_PARAMETERS = { 'properties': { 'default_variable': { 'description': 'Template array defining the '
                                                       'shape and default value to be '
                                                       'normalized. For 2D inputs, '
                                                       'provide a nested array.',
                                        'items': {'type': 'number'},
                                        'type': 'array'},
                  'eps': { 'default': 1e-12,
                           'description': 'Small positive constant for numerical '
                                          'stability. The denominator is clamped to '
                                          'this value when the L2 norm is near zero, '
                                          'preventing division by zero.',
                           'type': 'number'},
                  'name': { 'description': 'Optional name for this Normalize function '
                                           'instance.',
                            'type': 'string'},
                  'per_item': { 'default': True,
                                'description': 'For 2D variables (batch inputs), if '
                                               'true each row is normalized '
                                               'independently; if false the entire 2D '
                                               'array is normalized as a single '
                                               'vector.',
                                'type': 'boolean'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = 'The normalization formula is x / max(‖x‖₂, eps). When the input norm is at or below eps the output magnitude is not 1 — the vector is scaled by 1/eps instead, which for the default eps=1e-12 produces very large values; callers should ensure inputs are not near-zero. The `per_item=True` default only activates for inputs with ndim > 1; 1D inputs are always normalized as a single vector regardless of this flag. `params`, `owner`, and `prefs` are advanced PsyNeuLink internals rarely needed by agents and are omitted from the schema.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.Normalize
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
    def create_normalize(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to create a PsyNeuLink Normalize function that L2-normalizes an array (divides each value by the Euclidean norm of the vector).'
        return _impl(args or {})
