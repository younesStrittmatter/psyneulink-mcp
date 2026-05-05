"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool
from psyneulink_mcp import method_helpers

__source_sha256__ = '5cb76dab7edb156a6b9dfc7c43c5733932d7154f14247cccccf19c1cc5246e38'
__pnl_qualname__ = 'psyneulink.Composition.add_linear_processing_pathway'
__pnl_kind__ = 'method'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'add_linear_processing_pathway'
TOOL_DESCRIPTION = 'Call this tool after creating a Composition to wire a feed-forward chain of nodes into it. Pass an ordered list of node handle strings — the tool auto-creates MappingProjections between consecutive pairs and returns the resulting Pathway. Use this (not add_node repeated calls) whenever you want a linear processing pipeline; use add_linear_learning_pathway instead if you need trainable weights.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "composition": {\n      "description": "Handle string of the target Composition, as returned by create_composition.",\n      "type": "string"\n    },\n    "default_projection_matrix": {\n      "description": "Optional matrix spec (e.g. \'IDENTITY_MATRIX\', \'FULL_CONNECTIVITY_MATRIX\') or a numeric matrix expressed as a JSON-encoded 2-D array string to use for any auto-created MappingProjection whose matrix was not explicitly specified. Overrides the MappingProjection default. Omit to use PsyNeuLink defaults.",\n      "type": "string"\n    },\n    "name": {\n      "description": "Optional name for the returned Pathway object. Overrides any name carried by a Pathway object passed as pathway.",\n      "type": "string"\n    },\n    "pathway": {\n      "description": "Ordered sequence of node handles (strings) defining the feed-forward chain. Elements are node handle strings or, when explicit projection control is needed, alternating node / projection specs. Auto-created MappingProjections connect each consecutive pair when no explicit projection is interleaved.",\n      "items": {\n        "description": "Handle string of a node (Mechanism or nested Composition) already registered in the server, or a special projection keyword between two node entries.",\n        "type": "string"\n      },\n      "minItems": 1,\n      "type": "array"\n    }\n  },\n  "required": [\n    "composition",\n    "pathway"\n  ],\n  "type": "object"\n}\n\nNotes:\n- If the exact same pathway (nodes + projections) already exists in the Composition, the existing Pathway is returned with a warning rather than a duplicate being created.\n- ControlMechanisms that have monitor_for_control set, and ObjectiveMechanisms that project to a ControlMechanism, are silently removed from the projection-wiring step; no new MappingProjections are added to them even if they appear in pathway.\n- If a (Pathway, LearningFunction) 2-tuple is passed as pathway, the LearningFunction is silently ignored; use add_linear_learning_pathway for trainable pathways.\n- Nodes do not need to be pre-added via add_node; add_linear_processing_pathway calls add_nodes internally for each entry.\n- default_projection_matrix only applies to projections that are auto-created (i.e., not explicitly interleaved in pathway); an explicit projection spec in pathway takes precedence.\n- The runtime resolves each node handle string to a live PsyNeuLink object before dispatch, so every string in pathway must correspond to a handle already known to the server.'
TOOL_PARAMETERS = { 'properties': { 'composition': { 'description': 'Handle string of the target '
                                                  'Composition, as returned by '
                                                  'create_composition.',
                                   'type': 'string'},
                  'default_projection_matrix': { 'description': 'Optional matrix spec '
                                                                '(e.g. '
                                                                "'IDENTITY_MATRIX', "
                                                                "'FULL_CONNECTIVITY_MATRIX') "
                                                                'or a numeric matrix '
                                                                'expressed as a '
                                                                'JSON-encoded 2-D '
                                                                'array string to use '
                                                                'for any auto-created '
                                                                'MappingProjection '
                                                                'whose matrix was not '
                                                                'explicitly specified. '
                                                                'Overrides the '
                                                                'MappingProjection '
                                                                'default. Omit to use '
                                                                'PsyNeuLink defaults.',
                                                 'type': 'string'},
                  'name': { 'description': 'Optional name for the returned Pathway '
                                           'object. Overrides any name carried by a '
                                           'Pathway object passed as pathway.',
                            'type': 'string'},
                  'pathway': { 'description': 'Ordered sequence of node handles '
                                              '(strings) defining the feed-forward '
                                              'chain. Elements are node handle strings '
                                              'or, when explicit projection control is '
                                              'needed, alternating node / projection '
                                              'specs. Auto-created MappingProjections '
                                              'connect each consecutive pair when no '
                                              'explicit projection is interleaved.',
                               'items': { 'description': 'Handle string of a node '
                                                         '(Mechanism or nested '
                                                         'Composition) already '
                                                         'registered in the server, or '
                                                         'a special projection keyword '
                                                         'between two node entries.',
                                          'type': 'string'},
                               'minItems': 1,
                               'type': 'array'}},
  'required': ['composition', 'pathway'],
  'type': 'object'}
TOOL_NOTES = '- If the exact same pathway (nodes + projections) already exists in the Composition, the existing Pathway is returned with a warning rather than a duplicate being created.\n- ControlMechanisms that have monitor_for_control set, and ObjectiveMechanisms that project to a ControlMechanism, are silently removed from the projection-wiring step; no new MappingProjections are added to them even if they appear in pathway.\n- If a (Pathway, LearningFunction) 2-tuple is passed as pathway, the LearningFunction is silently ignored; use add_linear_learning_pathway for trainable pathways.\n- Nodes do not need to be pre-added via add_node; add_linear_processing_pathway calls add_nodes internally for each entry.\n- default_projection_matrix only applies to projections that are auto-created (i.e., not explicitly interleaved in pathway); an explicit projection spec in pathway takes precedence.\n- The runtime resolves each node handle string to a live PsyNeuLink object before dispatch, so every string in pathway must correspond to a handle already known to the server.'


def _impl(kwargs: dict[str, Any]) -> Any:
    cls = pnl.Composition
    return method_helpers.call_method_tool(
        owner_cls=cls,
        method_name='add_linear_processing_pathway',
        kwargs=kwargs,
        tool_name=TOOL_NAME,
    )


def register(mcp: Any) -> None:
    @captured_tool(mcp, layer="generated", name=TOOL_NAME, description=TOOL_DESCRIPTION)
    def add_linear_processing_pathway(args: dict[str, Any] | None = None) -> Any:
        'Call this tool after creating a Composition to wire a feed-forward chain of nodes into it.'
        return _impl(args or {})
