"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool
from psyneulink_mcp import method_helpers

__source_sha256__ = 'dc3bbe2f71177e42f99915b3467f41b4424d010ba1ac5ba673d5f26056651322'
__pnl_qualname__ = 'psyneulink.Composition.add_projection'
__pnl_kind__ = 'method'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'add_projection'
TOOL_DESCRIPTION = 'Call this tool to wire two nodes in a Composition with a directed projection. Use it after nodes exist in the composition — but you do NOT need to call add_node first, because the runtime defensively adds sender and receiver automatically. Returns a handle string for the created Projection, or None if a duplicate already existed (retrying is safe: DuplicateProjectionError is treated as success).\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "composition": {\n      "description": "Handle string for the target Composition, as returned by create_composition.",\n      "type": "string"\n    },\n    "default_matrix": {\n      "description": "Matrix for the default MappingProjection when no projection is specified. Pass a PNL keyword string (e.g. \'IDENTITY_MATRIX\', \'FULL_CONNECTIVITY_MATRIX\', \'HOLLOW_MATRIX\', \'RANDOM_CONNECTIVITY_MATRIX\') or omit to use the MappingProjection default. The runtime also accepts the alias \'matrix\' and translates it here.",\n      "type": "string"\n    },\n    "feedback": {\n      "default": false,\n      "description": "If true, the projection is always designated as a feedback projection and used to break cycles. If false (default), it is never designated as feedback even if it forms a loop.",\n      "type": "boolean"\n    },\n    "name": {\n      "description": "Optional name for the new Projection.",\n      "type": "string"\n    },\n    "projection": {\n      "description": "Optional handle string for an existing Projection object to add. If omitted, a default MappingProjection is created between sender and receiver.",\n      "type": "string"\n    },\n    "receiver": {\n      "description": "Handle string for the receiving Mechanism, Composition, or InputPort. The runtime adds this node to the composition if not already present.",\n      "type": "string"\n    },\n    "sender": {\n      "description": "Handle string for the sending Mechanism, Composition, or OutputPort. The runtime adds this node to the composition if not already present.",\n      "type": "string"\n    }\n  },\n  "required": [\n    "composition",\n    "sender",\n    "receiver"\n  ],\n  "type": "object"\n}\n\nNotes:\n- You do NOT need to call add_node before add_projection — the runtime pre-adds sender and receiver to avoid CompositionError: \'... not (yet) in it\'.\n- DuplicateProjectionError is silently treated as success; retrying the same add_projection call is safe.\n- Use default_matrix (not matrix) for the weight matrix kwarg. Both names are accepted by the runtime and translated to PNL\'s default_matrix, but the canonical name is default_matrix.\n- Supported matrix keyword strings: \'IDENTITY_MATRIX\', \'FULL_CONNECTIVITY_MATRIX\', \'HOLLOW_MATRIX\', \'RANDOM_CONNECTIVITY_MATRIX\'. For numeric matrices, pass a 2-D array as a JSON array of arrays.\n- If sender and receiver already have a projection between them inside the composition, the existing projection is returned and no new one is created.\n- The projection parameter and default_matrix parameter are mutually informing: if projection is omitted, default_matrix controls the weight matrix of the auto-created MappingProjection.\n- is_learning_projection and allow_duplicates are internal PNL parameters; do not pass them.'
TOOL_PARAMETERS = { 'properties': { 'composition': { 'description': 'Handle string for the target '
                                                  'Composition, as returned by '
                                                  'create_composition.',
                                   'type': 'string'},
                  'default_matrix': { 'description': 'Matrix for the default '
                                                     'MappingProjection when no '
                                                     'projection is specified. Pass a '
                                                     'PNL keyword string (e.g. '
                                                     "'IDENTITY_MATRIX', "
                                                     "'FULL_CONNECTIVITY_MATRIX', "
                                                     "'HOLLOW_MATRIX', "
                                                     "'RANDOM_CONNECTIVITY_MATRIX') or "
                                                     'omit to use the '
                                                     'MappingProjection default. The '
                                                     'runtime also accepts the alias '
                                                     "'matrix' and translates it here.",
                                      'type': 'string'},
                  'feedback': { 'default': False,
                                'description': 'If true, the projection is always '
                                               'designated as a feedback projection '
                                               'and used to break cycles. If false '
                                               '(default), it is never designated as '
                                               'feedback even if it forms a loop.',
                                'type': 'boolean'},
                  'name': { 'description': 'Optional name for the new Projection.',
                            'type': 'string'},
                  'projection': { 'description': 'Optional handle string for an '
                                                 'existing Projection object to add. '
                                                 'If omitted, a default '
                                                 'MappingProjection is created between '
                                                 'sender and receiver.',
                                  'type': 'string'},
                  'receiver': { 'description': 'Handle string for the receiving '
                                               'Mechanism, Composition, or InputPort. '
                                               'The runtime adds this node to the '
                                               'composition if not already present.',
                                'type': 'string'},
                  'sender': { 'description': 'Handle string for the sending Mechanism, '
                                             'Composition, or OutputPort. The runtime '
                                             'adds this node to the composition if not '
                                             'already present.',
                              'type': 'string'}},
  'required': ['composition', 'sender', 'receiver'],
  'type': 'object'}
TOOL_NOTES = "- You do NOT need to call add_node before add_projection — the runtime pre-adds sender and receiver to avoid CompositionError: '... not (yet) in it'.\n- DuplicateProjectionError is silently treated as success; retrying the same add_projection call is safe.\n- Use default_matrix (not matrix) for the weight matrix kwarg. Both names are accepted by the runtime and translated to PNL's default_matrix, but the canonical name is default_matrix.\n- Supported matrix keyword strings: 'IDENTITY_MATRIX', 'FULL_CONNECTIVITY_MATRIX', 'HOLLOW_MATRIX', 'RANDOM_CONNECTIVITY_MATRIX'. For numeric matrices, pass a 2-D array as a JSON array of arrays.\n- If sender and receiver already have a projection between them inside the composition, the existing projection is returned and no new one is created.\n- The projection parameter and default_matrix parameter are mutually informing: if projection is omitted, default_matrix controls the weight matrix of the auto-created MappingProjection.\n- is_learning_projection and allow_duplicates are internal PNL parameters; do not pass them."


def _impl(kwargs: dict[str, Any]) -> Any:
    cls = pnl.Composition
    return method_helpers.call_method_tool(
        owner_cls=cls,
        method_name='add_projection',
        kwargs=kwargs,
        tool_name=TOOL_NAME,
    )


def register(mcp: Any) -> None:
    @captured_tool(mcp, layer="generated", name=TOOL_NAME, description=TOOL_DESCRIPTION)
    def add_projection(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to wire two nodes in a Composition with a directed projection.'
        return _impl(args or {})
