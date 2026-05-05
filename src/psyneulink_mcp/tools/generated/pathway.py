"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '727d502b7b4957cd561a58e74e918e070fd3a8d887455c557d122001a171f3f1'
__pnl_qualname__ = 'psyneulink.Pathway'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_pathway'
TOOL_DESCRIPTION = 'Call this tool to create a Pathway — a named, ordered sequence of Nodes (Mechanisms or Compositions) and interleaved Projections — either as a reusable template or to pass directly to a Composition\'s `add_pathway` / `add_linear_processing_pathway` call. The result is a Pathway object whose `.pathway`, `.roles`, `.input`, `.output`, and `.learning_components` attributes describe its structure once it is assigned to a Composition.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "name": {\n      "description": "Optional human-readable name for the Pathway. If omitted, PathwayRegistry assigns a default name.",\n      "type": "string"\n    },\n    "pathway": {\n      "description": "Ordered list alternating Nodes (Mechanism/Composition names or specs) and optional interleaved Projection specs. Minimal form: [node_a, node_b]. To set a default projection matrix for auto-created projections, wrap the list in a 2- or 3-item tuple: (list, matrix) or (list, matrix, LearningFunction) \\u2014 the matrix is extracted automatically.",\n      "items": {},\n      "type": "array"\n    }\n  },\n  "required": [\n    "pathway"\n  ],\n  "type": "object"\n}\n\nNotes:\n`default_projection_matrix` is NOT a constructor keyword argument despite appearing in older docstrings — it is parsed automatically when `pathway` is a tuple of the form `(list, matrix)` or `(list, matrix, learning_function)`. Passing it as a keyword will raise a CompositionError. A Pathway created outside a Composition is a *template*: `.roles`, `.learning_components`, `.input`, `.output` all return None until the Pathway is added to a Composition. The `composition` kwarg is internal and injected by the Composition at add-time; agents should never pass it.'
TOOL_PARAMETERS = { 'properties': { 'name': { 'description': 'Optional human-readable name for the '
                                           'Pathway. If omitted, PathwayRegistry '
                                           'assigns a default name.',
                            'type': 'string'},
                  'pathway': { 'description': 'Ordered list alternating Nodes '
                                              '(Mechanism/Composition names or specs) '
                                              'and optional interleaved Projection '
                                              'specs. Minimal form: [node_a, node_b]. '
                                              'To set a default projection matrix for '
                                              'auto-created projections, wrap the list '
                                              'in a 2- or 3-item tuple: (list, matrix) '
                                              'or (list, matrix, LearningFunction) — '
                                              'the matrix is extracted automatically.',
                               'items': {},
                               'type': 'array'}},
  'required': ['pathway'],
  'type': 'object'}
TOOL_NOTES = '`default_projection_matrix` is NOT a constructor keyword argument despite appearing in older docstrings — it is parsed automatically when `pathway` is a tuple of the form `(list, matrix)` or `(list, matrix, learning_function)`. Passing it as a keyword will raise a CompositionError. A Pathway created outside a Composition is a *template*: `.roles`, `.learning_components`, `.input`, `.output` all return None until the Pathway is added to a Composition. The `composition` kwarg is internal and injected by the Composition at add-time; agents should never pass it.'


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
        "Call this tool to create a Pathway — a named, ordered sequence of Nodes (Mechanisms or Compositions) and interleaved Projections — either as a reusable template or to pass directly to a Composition's `add_pathway` / `add_linear_processing_pathway` call."
        return _impl(args or {})
