"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '2eb4e76d5a3fd0f74051b099ad3da18a86d89602de3c223834550ccd2986e335'
__pnl_qualname__ = 'psyneulink.Pathway'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_pathway'
TOOL_DESCRIPTION = 'Call this tool to create a standalone Pathway template — an ordered sequence of Nodes (Mechanisms or Compositions) with optional interleaved Projections — that can later be passed to a Composition method such as add_linear_processing_pathway or add_backpropagation_learning_pathway. Returns a Pathway object whose .pathway attribute holds the specification list; once assigned to a Composition, .input, .output, .roles, and .learning_components become populated.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "name": {\n      "description": "Optional name for the Pathway. If omitted, PathwayRegistry assigns a default name following Registry_Naming conventions.",\n      "type": "string"\n    },\n    "pathway": {\n      "description": "Ordered list alternating Nodes and optional Projections: [Node, Node], [Node, Projection, Node], or [Node, Projection, Node, ...]. Each Node is a string name of an existing Mechanism or Composition. A Projection entry is a string name of an existing MappingProjection. To specify a default matrix for auto-created projections, wrap the list in a tuple with the matrix as a second element, e.g. [\'mech_a\', \'mech_b\'] \\u2014 but pass as a plain array here; use default_projection_matrix_hint in notes instead.",\n      "items": {\n        "type": "string"\n      },\n      "minItems": 1,\n      "type": "array"\n    }\n  },\n  "required": [\n    "pathway"\n  ],\n  "type": "object"\n}\n\nNotes:\n1. `default_projection_matrix` is NOT a direct constructor argument — it is commented out in the source. To supply a default projection matrix, wrap the pathway list in a tuple where the second element is the matrix, and pass that tuple as the `pathway` argument; the constructor parses the matrix out internally. 2. When created standalone (without a Composition), the Pathway is a "template": `.roles` is None, `.learning_components` is None, and `.input`/`.output` return nothing useful until the Pathway is assigned to a Composition. 3. Node and Projection entries in `pathway` must be already-constructed PsyNeuLink objects, not bare strings — the schema above simplifies for MCP transport; the host template must resolve names to live objects before passing them. 4. The `composition` kwarg is stripped internally and is not intended for agent use. 5. Any unexpected keyword arguments raise a CompositionError, so pass only `pathway` and `name`.'
TOOL_PARAMETERS = { 'properties': { 'name': { 'description': 'Optional name for the Pathway. If omitted, '
                                           'PathwayRegistry assigns a default name '
                                           'following Registry_Naming conventions.',
                            'type': 'string'},
                  'pathway': { 'description': 'Ordered list alternating Nodes and '
                                              'optional Projections: [Node, Node], '
                                              '[Node, Projection, Node], or [Node, '
                                              'Projection, Node, ...]. Each Node is a '
                                              'string name of an existing Mechanism or '
                                              'Composition. A Projection entry is a '
                                              'string name of an existing '
                                              'MappingProjection. To specify a default '
                                              'matrix for auto-created projections, '
                                              'wrap the list in a tuple with the '
                                              'matrix as a second element, e.g. '
                                              "['mech_a', 'mech_b'] — but pass as a "
                                              'plain array here; use '
                                              'default_projection_matrix_hint in notes '
                                              'instead.',
                               'items': {'type': 'string'},
                               'minItems': 1,
                               'type': 'array'}},
  'required': ['pathway'],
  'type': 'object'}
TOOL_NOTES = '1. `default_projection_matrix` is NOT a direct constructor argument — it is commented out in the source. To supply a default projection matrix, wrap the pathway list in a tuple where the second element is the matrix, and pass that tuple as the `pathway` argument; the constructor parses the matrix out internally. 2. When created standalone (without a Composition), the Pathway is a "template": `.roles` is None, `.learning_components` is None, and `.input`/`.output` return nothing useful until the Pathway is assigned to a Composition. 3. Node and Projection entries in `pathway` must be already-constructed PsyNeuLink objects, not bare strings — the schema above simplifies for MCP transport; the host template must resolve names to live objects before passing them. 4. The `composition` kwarg is stripped internally and is not intended for agent use. 5. Any unexpected keyword arguments raise a CompositionError, so pass only `pathway` and `name`.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.Pathway
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
    def create_pathway(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to create a standalone Pathway template — an ordered sequence of Nodes (Mechanisms or Compositions) with optional interleaved Projections — that can later be passed to a Composition method such as add_linear_processing_pathway or add_backpropagation_learning_pathway.'
        return _impl(args or {})
