"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '6ce9017a4a05c18cb0ad8644eb4ec85db72148f92bcfda955951ab84d198fefc'
__pnl_qualname__ = 'psyneulink.RandomMatrix'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_random_matrix'
TOOL_DESCRIPTION = 'Call this tool when you need a random weight matrix initializer for a MappingProjection, Pathway, or add_linear_processing_pathway — anywhere PsyNeuLink accepts a matrix specification. Returns a RandomMatrix object whose elements are drawn uniformly from [center - range/2, center + range/2] (approximately), usable directly as the `matrix` argument of a MappingProjection or as the default projection matrix in pathway construction.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "center": {\n      "default": 0,\n      "description": "Center of the uniform distribution from which matrix elements are drawn. Default 0.0.",\n      "type": "number"\n    },\n    "range": {\n      "default": 1,\n      "description": "Width of the uniform distribution. Elements span approximately center \\u00b1 range/2. Default 1.0.",\n      "type": "number"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\nThe internal mapping is offset = center - 0.5 and scale = range, so elements are drawn from [center - 0.5, center - 0.5 + range], not a symmetric interval around center. For a symmetric distribution centered at 0 with spread 1, the defaults (center=0.0, range=1.0) produce elements in [-0.5, 0.5]. This tool instantiates the RandomMatrix initializer object; the actual matrix is only generated when PsyNeuLink calls it with sender_size and receiver_size internally — you do not pass those here.'
TOOL_PARAMETERS = { 'properties': { 'center': { 'default': 0,
                              'description': 'Center of the uniform distribution from '
                                             'which matrix elements are drawn. Default '
                                             '0.0.',
                              'type': 'number'},
                  'range': { 'default': 1,
                             'description': 'Width of the uniform distribution. '
                                            'Elements span approximately center ± '
                                            'range/2. Default 1.0.',
                             'type': 'number'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = 'The internal mapping is offset = center - 0.5 and scale = range, so elements are drawn from [center - 0.5, center - 0.5 + range], not a symmetric interval around center. For a symmetric distribution centered at 0 with spread 1, the defaults (center=0.0, range=1.0) produce elements in [-0.5, 0.5]. This tool instantiates the RandomMatrix initializer object; the actual matrix is only generated when PsyNeuLink calls it with sender_size and receiver_size internally — you do not pass those here.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.RandomMatrix
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
    def create_random_matrix(args: dict[str, Any] | None = None) -> Any:
        'Call this tool when you need a random weight matrix initializer for a MappingProjection, Pathway, or add_linear_processing_pathway — anywhere PsyNeuLink accepts a matrix specification.'
        return _impl(args or {})
