"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool
from psyneulink_mcp import method_helpers

__source_sha256__ = 'd91c8cf053c5ad71f5f33ea28ced2754c8e6d1324ceaf21a57c5bc91e44420c8'
__pnl_qualname__ = 'psyneulink.Composition.add_pathways'
__pnl_kind__ = 'method'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'add_pathways'
TOOL_DESCRIPTION = 'Call this tool to add one or more processing or learning pathways to an existing Composition in a single operation. Use it instead of repeated `add_linear_processing_pathway` calls when you have multiple pathways to add at once, or when you want to mix processing and learning pathways. Returns a list of Pathway handle strings representing the added pathways.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "composition": {\n      "description": "Handle string of the target Composition, as returned by `create_composition`.",\n      "type": "string"\n    },\n    "pathways": {\n      "description": "One or more pathway specifications. Accepts a wide range of forms \\u2014 see notes. Most common forms: (1) a list of node handles for a single processing pathway, (2) a 2-element array [list_of_node_handles, LearningFunctionClassName] for a learning pathway, (3) a dict {\\"name\\": pathway_spec} for a named pathway, or (4) a list containing any mix of the above for multiple pathways at once.",\n      "oneOf": [\n        {\n          "description": "Single node handle \\u2014 adds a one-node processing pathway.",\n          "type": "string"\n        },\n        {\n          "description": "Either a flat list of node/projection handles (single processing pathway), a 2-element [pathway, LearningFunctionClass] tuple (learning pathway), or a list of pathway specs (multiple pathways).",\n          "items": {\n            "oneOf": [\n              {\n                "type": "string"\n              },\n              {\n                "items": {\n                  "type": "string"\n                },\n                "type": "array"\n              },\n              {\n                "type": "object"\n              }\n            ]\n          },\n          "type": "array"\n        },\n        {\n          "additionalProperties": true,\n          "description": "Dict mapping a single string name to a pathway spec \\u2014 adds a named pathway.",\n          "type": "object"\n        }\n      ]\n    }\n  },\n  "required": [\n    "composition",\n    "pathways"\n  ],\n  "type": "object"\n}\n\nNotes:\n**Pathway spec forms (JSON equivalents):**\n- Single node: `"my_transfer_mech_handle"` (string)\n- Simple processing pathway: `["node_a", "node_b", "node_c"]` (flat array of node handles)\n- Learning pathway: `[["node_a", "node_b"], "BackPropagation"]` — 2-element array where first is node list and second is a LearningFunction class name string; the runtime resolves the class name to `pnl.BackPropagation`\n- Named pathway: `{"my_pathway": ["node_a", "node_b"]}` — single-key dict\n- Multiple mixed pathways: `[["node_a", "node_b"], [["node_c", "node_d"], "Reinforcement"]]` — outer list containing any of the above\n- Set of nodes: cannot be represented directly in JSON; use a list instead\n- If `pathways` is empty or `null`, the method returns `None` silently (no error, no pathways added).\n- Projections can be interleaved between nodes in pathway lists using projection handle strings.\n- A dict with more than one key will raise `CompositionError` — always use single-key dicts.\n- Prefer `add_linear_processing_pathway` or `add_linear_learning_pathway` for a single pathway with fine-grained control; use `add_pathways` when adding several pathways in one call.'
TOOL_PARAMETERS = { 'properties': { 'composition': { 'description': 'Handle string of the target '
                                                  'Composition, as returned by '
                                                  '`create_composition`.',
                                   'type': 'string'},
                  'pathways': { 'description': 'One or more pathway specifications. '
                                               'Accepts a wide range of forms — see '
                                               'notes. Most common forms: (1) a list '
                                               'of node handles for a single '
                                               'processing pathway, (2) a 2-element '
                                               'array [list_of_node_handles, '
                                               'LearningFunctionClassName] for a '
                                               'learning pathway, (3) a dict {"name": '
                                               'pathway_spec} for a named pathway, or '
                                               '(4) a list containing any mix of the '
                                               'above for multiple pathways at once.',
                                'oneOf': [ { 'description': 'Single node handle — adds '
                                                            'a one-node processing '
                                                            'pathway.',
                                             'type': 'string'},
                                           { 'description': 'Either a flat list of '
                                                            'node/projection handles '
                                                            '(single processing '
                                                            'pathway), a 2-element '
                                                            '[pathway, '
                                                            'LearningFunctionClass] '
                                                            'tuple (learning pathway), '
                                                            'or a list of pathway '
                                                            'specs (multiple '
                                                            'pathways).',
                                             'items': { 'oneOf': [ {'type': 'string'},
                                                                   { 'items': { 'type': 'string'},
                                                                     'type': 'array'},
                                                                   {'type': 'object'}]},
                                             'type': 'array'},
                                           { 'additionalProperties': True,
                                             'description': 'Dict mapping a single '
                                                            'string name to a pathway '
                                                            'spec — adds a named '
                                                            'pathway.',
                                             'type': 'object'}]}},
  'required': ['composition', 'pathways'],
  'type': 'object'}
TOOL_NOTES = '**Pathway spec forms (JSON equivalents):**\n- Single node: `"my_transfer_mech_handle"` (string)\n- Simple processing pathway: `["node_a", "node_b", "node_c"]` (flat array of node handles)\n- Learning pathway: `[["node_a", "node_b"], "BackPropagation"]` — 2-element array where first is node list and second is a LearningFunction class name string; the runtime resolves the class name to `pnl.BackPropagation`\n- Named pathway: `{"my_pathway": ["node_a", "node_b"]}` — single-key dict\n- Multiple mixed pathways: `[["node_a", "node_b"], [["node_c", "node_d"], "Reinforcement"]]` — outer list containing any of the above\n- Set of nodes: cannot be represented directly in JSON; use a list instead\n- If `pathways` is empty or `null`, the method returns `None` silently (no error, no pathways added).\n- Projections can be interleaved between nodes in pathway lists using projection handle strings.\n- A dict with more than one key will raise `CompositionError` — always use single-key dicts.\n- Prefer `add_linear_processing_pathway` or `add_linear_learning_pathway` for a single pathway with fine-grained control; use `add_pathways` when adding several pathways in one call.'


def _impl(kwargs: dict[str, Any]) -> Any:
    cls = pnl.Composition
    return method_helpers.call_method_tool(
        owner_cls=cls,
        method_name='add_pathways',
        kwargs=kwargs,
        tool_name=TOOL_NAME,
    )


def register(mcp: Any) -> None:
    @captured_tool(mcp, layer="generated", name=TOOL_NAME, description=TOOL_DESCRIPTION)
    def add_pathways(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to add one or more processing or learning pathways to an existing Composition in a single operation.'
        return _impl(args or {})
