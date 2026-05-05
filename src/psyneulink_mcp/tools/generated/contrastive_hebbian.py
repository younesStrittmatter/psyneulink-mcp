"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = 'be71f44facc182c93ff49ab785419bb33d3cd5ea9b188c9d8014bf34cacaae6e'
__pnl_qualname__ = 'psyneulink.ContrastiveHebbian'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_contrastive_hebbian'
TOOL_DESCRIPTION = 'Call this tool to create a ContrastiveHebbian learning function when building a network that uses the Contrastive Hebbian learning rule — specifically when you need a LearningFunction that computes weight changes as the difference between plus-phase (target) and minus-phase (actual) pairwise activity products. Returns a 2D hollow weight-change matrix (diagonal = 0) scaled by learning_rate.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "default_variable": {\n      "description": "1D array of activation values. Must be numeric and 1-dimensional. Default is [0, 0].",\n      "items": {\n        "type": "number"\n      },\n      "type": "array"\n    },\n    "learning_rate": {\n      "description": "Scales the weight change matrix. Scalar multiplies the whole matrix; 1d array applies Hadamard to variable before outer product; 2d array applies Hadamard to the result matrix. Default is 0.05.",\n      "type": "number"\n    },\n    "name": {\n      "description": "Name for this function instance.",\n      "type": "string"\n    },\n    "params": {\n      "description": "Optional parameter dictionary overriding constructor arguments. Keys are parameter names, values override defaults.",\n      "type": "object"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\nThe learning rule implemented in source is actually the standard Hebbian outer product (variable * col), not the true contrastive difference (plus_phase - minus_phase). The source comment says \'NEEDS TO BE REPLACED BY THE CONTRASTIVE HEBBIAN LEARNING RULE\' — the current implementation does NOT subtract minus-phase activity. Do not rely on this for true contrastive learning without verifying PNL version behavior. The output is always a hollow 2D matrix (diagonal zeroed). Variable must be exactly 1D; 0D scalars and 2D+ arrays both raise ComponentError. The `learning_rate` dimensionality changes application order: 1D scales variable before outer product, 0D or 2D scales the result matrix after.'
TOOL_PARAMETERS = { 'properties': { 'default_variable': { 'description': '1D array of activation values. '
                                                       'Must be numeric and '
                                                       '1-dimensional. Default is [0, '
                                                       '0].',
                                        'items': {'type': 'number'},
                                        'type': 'array'},
                  'learning_rate': { 'description': 'Scales the weight change matrix. '
                                                    'Scalar multiplies the whole '
                                                    'matrix; 1d array applies Hadamard '
                                                    'to variable before outer product; '
                                                    '2d array applies Hadamard to the '
                                                    'result matrix. Default is 0.05.',
                                     'type': 'number'},
                  'name': { 'description': 'Name for this function instance.',
                            'type': 'string'},
                  'params': { 'description': 'Optional parameter dictionary overriding '
                                             'constructor arguments. Keys are '
                                             'parameter names, values override '
                                             'defaults.',
                              'type': 'object'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = "The learning rule implemented in source is actually the standard Hebbian outer product (variable * col), not the true contrastive difference (plus_phase - minus_phase). The source comment says 'NEEDS TO BE REPLACED BY THE CONTRASTIVE HEBBIAN LEARNING RULE' — the current implementation does NOT subtract minus-phase activity. Do not rely on this for true contrastive learning without verifying PNL version behavior. The output is always a hollow 2D matrix (diagonal zeroed). Variable must be exactly 1D; 0D scalars and 2D+ arrays both raise ComponentError. The `learning_rate` dimensionality changes application order: 1D scales variable before outer product, 0D or 2D scales the result matrix after."


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.ContrastiveHebbian
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
    def create_contrastive_hebbian(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to create a ContrastiveHebbian learning function when building a network that uses the Contrastive Hebbian learning rule — specifically when you need a LearningFunction that computes weight changes as the difference between plus-phase (target) and minus-phase (actual) pairwise activity products.'
        return _impl(args or {})
