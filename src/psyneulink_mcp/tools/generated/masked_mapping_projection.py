"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '800b29e9015b565249458d78425759226b188aa8bb02900a86c1843e916a014a'
__pnl_qualname__ = 'psyneulink.MaskedMappingProjection'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_masked_mapping_projection'
TOOL_DESCRIPTION = 'Call this tool to create a MaskedMappingProjection — a weighted connection between two Mechanisms where a mask is applied element-wise to the weight matrix on every execution. Use it instead of a plain MappingProjection whenever you need to selectively suppress, scale, or modulate specific weights dynamically (e.g., to implement gating, dropout-style masking, or attention-like reweighting). Returns a projection object that can be added to a Composition.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "mask": {\n      "description": "Mask applied to the matrix on each execution. Can be a scalar (applied uniformly) or an array/matrix with the same shape as the weight matrix. Combined with the matrix via mask_operation.",\n      "oneOf": [\n        {\n          "type": "number"\n        },\n        {\n          "type": "array"\n        }\n      ]\n    },\n    "mask_operation": {\n      "default": "multiply",\n      "description": "How the mask is combined with the matrix each execution: \'multiply\' scales weights, \'add\' shifts them, \'exponentiate\' raises matrix elements to the mask power.",\n      "enum": [\n        "add",\n        "multiply",\n        "exponentiate"\n      ],\n      "type": "string"\n    },\n    "matrix": {\n      "description": "Weight matrix for the projection. Can be a 2D list/array, or a keyword like \'IDENTITY_MATRIX\', \'FULL_CONNECTIVITY_MATRIX\'. If omitted, defaults to an identity-like matrix based on sender/receiver dimensionality.",\n      "oneOf": [\n        {\n          "items": {\n            "items": {\n              "type": "number"\n            },\n            "type": "array"\n          },\n          "type": "array"\n        },\n        {\n          "type": "string"\n        }\n      ]\n    },\n    "name": {\n      "description": "Optional name for the projection.",\n      "type": "string"\n    },\n    "receiver": {\n      "description": "Name or reference to the receiving Mechanism or InputPort.",\n      "type": "string"\n    },\n    "sender": {\n      "description": "Name or reference to the sending Mechanism or OutputPort.",\n      "type": "string"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\nThe mask is re-applied on EVERY execution — it is not a one-time initialization. This means the effective matrix seen at runtime is always `f(base_matrix, mask)`, so the stored matrix parameter is mutated each call; inspect `parameters.matrix` in context, not the base default. If mask is an array (not a scalar), its shape must exactly match the weight matrix shape or PsyNeuLink will raise a MaskedMappingProjectionError at validation time — mismatches are caught late (at first execution attempt), not at construction. The string constants \'add\', \'multiply\', \'exponentiate\' are lowercase; passing the PNL constants ADD/MULTIPLY/EXPONENTIATE also works. All MappingProjection arguments (function, params, prefs) are accepted via **kwargs but are rarely needed.'
TOOL_PARAMETERS = { 'properties': { 'mask': { 'description': 'Mask applied to the matrix on each '
                                           'execution. Can be a scalar (applied '
                                           'uniformly) or an array/matrix with the '
                                           'same shape as the weight matrix. Combined '
                                           'with the matrix via mask_operation.',
                            'oneOf': [{'type': 'number'}, {'type': 'array'}]},
                  'mask_operation': { 'default': 'multiply',
                                      'description': 'How the mask is combined with '
                                                     'the matrix each execution: '
                                                     "'multiply' scales weights, 'add' "
                                                     "shifts them, 'exponentiate' "
                                                     'raises matrix elements to the '
                                                     'mask power.',
                                      'enum': ['add', 'multiply', 'exponentiate'],
                                      'type': 'string'},
                  'matrix': { 'description': 'Weight matrix for the projection. Can be '
                                             'a 2D list/array, or a keyword like '
                                             "'IDENTITY_MATRIX', "
                                             "'FULL_CONNECTIVITY_MATRIX'. If omitted, "
                                             'defaults to an identity-like matrix '
                                             'based on sender/receiver dimensionality.',
                              'oneOf': [ { 'items': { 'items': {'type': 'number'},
                                                      'type': 'array'},
                                           'type': 'array'},
                                         {'type': 'string'}]},
                  'name': { 'description': 'Optional name for the projection.',
                            'type': 'string'},
                  'receiver': { 'description': 'Name or reference to the receiving '
                                               'Mechanism or InputPort.',
                                'type': 'string'},
                  'sender': { 'description': 'Name or reference to the sending '
                                             'Mechanism or OutputPort.',
                              'type': 'string'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = "The mask is re-applied on EVERY execution — it is not a one-time initialization. This means the effective matrix seen at runtime is always `f(base_matrix, mask)`, so the stored matrix parameter is mutated each call; inspect `parameters.matrix` in context, not the base default. If mask is an array (not a scalar), its shape must exactly match the weight matrix shape or PsyNeuLink will raise a MaskedMappingProjectionError at validation time — mismatches are caught late (at first execution attempt), not at construction. The string constants 'add', 'multiply', 'exponentiate' are lowercase; passing the PNL constants ADD/MULTIPLY/EXPONENTIATE also works. All MappingProjection arguments (function, params, prefs) are accepted via **kwargs but are rarely needed."


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.MaskedMappingProjection
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
    def create_masked_mapping_projection(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to create a MaskedMappingProjection — a weighted connection between two Mechanisms where a mask is applied element-wise to the weight matrix on every execution.'
        return _impl(args or {})
