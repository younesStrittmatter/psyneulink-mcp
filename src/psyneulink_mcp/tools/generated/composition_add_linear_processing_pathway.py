"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool
from psyneulink_mcp import method_helpers

__source_sha256__ = 'c6d5a410ed9b1d8c352ba2eeb40e1b0a04ab33bd5ff406c45c5fdefb884891e3'
__pnl_qualname__ = 'psyneulink.Composition.add_linear_processing_pathway'
__pnl_kind__ = 'method'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'add_linear_processing_pathway'
TOOL_DESCRIPTION = 'Call this tool to wire an ordered sequence of Mechanism/Composition nodes into a feed-forward processing chain within an existing Composition. It registers each node, auto-creates MappingProjections between consecutive pairs, and returns a named Pathway object. Use it whenever you want to connect two or more nodes in sequence rather than adding nodes and projections individually.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "composition": {\n      "description": "Handle string of the target Composition, as returned by create_composition.",\n      "type": "string"\n    },\n    "default_projection_matrix": {\n      "description": "Numeric weight matrix (list of lists of numbers) used for any auto-created MappingProjection that has no explicit specification. Omit to use the MappingProjection default (identity-like). Do NOT pass a string keyword such as \'FULL_CONNECTIVITY_MATRIX\' \\u2014 see notes.",\n      "items": {\n        "items": {\n          "type": "number"\n        },\n        "type": "array"\n      },\n      "type": "array"\n    },\n    "name": {\n      "description": "Optional name for the resulting Pathway object. Overrides any name carried by a Pathway object passed in pathway.",\n      "type": "string"\n    },\n    "pathway": {\n      "description": "Ordered list of node handle strings (Mechanism or nested Composition handles). Projection handle strings may be interleaved between node handles to specify explicit connectivity; any adjacent pair of node handles without an intervening Projection handle receives an auto-created MappingProjection.",\n      "items": {\n        "type": "string"\n      },\n      "type": "array"\n    }\n  },\n  "required": [\n    "composition",\n    "pathway"\n  ],\n  "type": "object"\n}\n\nNotes:\nFULL_CONNECTIVITY_MATRIX and other PNL MATRIX_KEYWORD strings must NOT be passed as the default_projection_matrix value. The runtime helper does not resolve matrix keyword strings, so they reach PNL as plain Python strings and cause CompositionError: Invalid projection … specified. Use a numeric matrix (list of lists) or omit the parameter entirely (confirmed failure: issues #19, auto-feedback 2026-05-06).\n\nControlMechanism nodes placed in the pathway will NOT receive a MappingProjection from their predecessor — ControlMechanisms can only have ControlProjections as efferents. PNL will instead wire a MappingProjection from the last non-ControlMechanism node to the successor, and emit a warning.\n\nIf a 2-item (Pathway, LearningFunction) tuple is passed as pathway, the LearningFunction is silently ignored. Use add_linear_learning_pathway instead if learning is required.\n\nDuplicate pathway detection: if the resulting pathway is identical to one already in the Composition, the existing Pathway is returned and a warning is issued — no error is raised.'
TOOL_PARAMETERS = { 'properties': { 'composition': { 'description': 'Handle string of the target '
                                                  'Composition, as returned by '
                                                  'create_composition.',
                                   'type': 'string'},
                  'default_projection_matrix': { 'description': 'Numeric weight matrix '
                                                                '(list of lists of '
                                                                'numbers) used for any '
                                                                'auto-created '
                                                                'MappingProjection '
                                                                'that has no explicit '
                                                                'specification. Omit '
                                                                'to use the '
                                                                'MappingProjection '
                                                                'default '
                                                                '(identity-like). Do '
                                                                'NOT pass a string '
                                                                'keyword such as '
                                                                "'FULL_CONNECTIVITY_MATRIX' "
                                                                '— see notes.',
                                                 'items': { 'items': {'type': 'number'},
                                                            'type': 'array'},
                                                 'type': 'array'},
                  'name': { 'description': 'Optional name for the resulting Pathway '
                                           'object. Overrides any name carried by a '
                                           'Pathway object passed in pathway.',
                            'type': 'string'},
                  'pathway': { 'description': 'Ordered list of node handle strings '
                                              '(Mechanism or nested Composition '
                                              'handles). Projection handle strings may '
                                              'be interleaved between node handles to '
                                              'specify explicit connectivity; any '
                                              'adjacent pair of node handles without '
                                              'an intervening Projection handle '
                                              'receives an auto-created '
                                              'MappingProjection.',
                               'items': {'type': 'string'},
                               'type': 'array'}},
  'required': ['composition', 'pathway'],
  'type': 'object'}
TOOL_NOTES = 'FULL_CONNECTIVITY_MATRIX and other PNL MATRIX_KEYWORD strings must NOT be passed as the default_projection_matrix value. The runtime helper does not resolve matrix keyword strings, so they reach PNL as plain Python strings and cause CompositionError: Invalid projection … specified. Use a numeric matrix (list of lists) or omit the parameter entirely (confirmed failure: issues #19, auto-feedback 2026-05-06).\n\nControlMechanism nodes placed in the pathway will NOT receive a MappingProjection from their predecessor — ControlMechanisms can only have ControlProjections as efferents. PNL will instead wire a MappingProjection from the last non-ControlMechanism node to the successor, and emit a warning.\n\nIf a 2-item (Pathway, LearningFunction) tuple is passed as pathway, the LearningFunction is silently ignored. Use add_linear_learning_pathway instead if learning is required.\n\nDuplicate pathway detection: if the resulting pathway is identical to one already in the Composition, the existing Pathway is returned and a warning is issued — no error is raised.'


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
        'Call this tool to wire an ordered sequence of Mechanism/Composition nodes into a feed-forward processing chain within an existing Composition.'
        return _impl(args or {})
