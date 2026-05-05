"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool
from psyneulink_mcp import method_helpers

__source_sha256__ = 'afc9c220d27af6b656d282016f64d2ced2c70accfc3f50c0e4dd205f3816c2e0'
__pnl_qualname__ = 'psyneulink.Composition.add_nodes'
__pnl_kind__ = 'method'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'add_nodes'
TOOL_DESCRIPTION = 'Call this tool to add multiple Mechanisms or sub-Compositions to an existing Composition in one batch. Prefer this over repeated `add_node` calls when you have two or more nodes ready to register. Returns nothing; side-effects the Composition\'s node graph in place.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "composition": {\n      "description": "Handle string for the target Composition, as returned by create_composition.",\n      "type": "string"\n    },\n    "nodes": {\n      "description": "Nodes to add. Each element is either a handle string for a Mechanism or Composition, or a two-element array [handle_string, role_or_roles] where role_or_roles is a NodeRole string or array of NodeRole strings (e.g. \'INPUT\', \'OUTPUT\', \'TERMINAL\'). Roles in tuple elements are merged with required_roles.",\n      "items": {\n        "oneOf": [\n          {\n            "description": "Handle string for a Mechanism or Composition.",\n            "type": "string"\n          },\n          {\n            "description": "Role-specification pair: [handle_string, NodeRole_string_or_array].",\n            "items": [\n              {\n                "type": "string"\n              },\n              {\n                "oneOf": [\n                  {\n                    "type": "string"\n                  },\n                  {\n                    "items": {\n                      "type": "string"\n                    },\n                    "type": "array"\n                  }\n                ]\n              }\n            ],\n            "maxItems": 2,\n            "minItems": 2,\n            "type": "array"\n          }\n        ]\n      },\n      "type": "array"\n    },\n    "required_roles": {\n      "description": "NodeRole(s) to assign to every node in the list (including tuple-specified nodes). Common values: \'INPUT\', \'OUTPUT\', \'TERMINAL\', \'ORIGIN\', \'SINGLETON\', \'INTERNAL\'. Optional.",\n      "oneOf": [\n        {\n          "type": "string"\n        },\n        {\n          "items": {\n            "type": "string"\n          },\n          "type": "array"\n        }\n      ]\n    }\n  },\n  "required": [\n    "composition",\n    "nodes"\n  ],\n  "type": "object"\n}\n\nNotes:\nThis is a thin loop over `add_node`; all validation and role-merging happen there. If any element of `nodes` is not a Mechanism, Composition, or a valid two-element tuple, the call raises `CompositionError` and no nodes are added (there is no transactional rollback — nodes processed before the bad element are already registered). Tuple roles and `required_roles` are additive, not mutually exclusive. `required_roles` applies to ALL nodes, including those inside tuples.'
TOOL_PARAMETERS = { 'properties': { 'composition': { 'description': 'Handle string for the target '
                                                  'Composition, as returned by '
                                                  'create_composition.',
                                   'type': 'string'},
                  'nodes': { 'description': 'Nodes to add. Each element is either a '
                                            'handle string for a Mechanism or '
                                            'Composition, or a two-element array '
                                            '[handle_string, role_or_roles] where '
                                            'role_or_roles is a NodeRole string or '
                                            "array of NodeRole strings (e.g. 'INPUT', "
                                            "'OUTPUT', 'TERMINAL'). Roles in tuple "
                                            'elements are merged with required_roles.',
                             'items': { 'oneOf': [ { 'description': 'Handle string for '
                                                                    'a Mechanism or '
                                                                    'Composition.',
                                                     'type': 'string'},
                                                   { 'description': 'Role-specification '
                                                                    'pair: '
                                                                    '[handle_string, '
                                                                    'NodeRole_string_or_array].',
                                                     'items': [ {'type': 'string'},
                                                                { 'oneOf': [ { 'type': 'string'},
                                                                             { 'items': { 'type': 'string'},
                                                                               'type': 'array'}]}],
                                                     'maxItems': 2,
                                                     'minItems': 2,
                                                     'type': 'array'}]},
                             'type': 'array'},
                  'required_roles': { 'description': 'NodeRole(s) to assign to every '
                                                     'node in the list (including '
                                                     'tuple-specified nodes). Common '
                                                     "values: 'INPUT', 'OUTPUT', "
                                                     "'TERMINAL', 'ORIGIN', "
                                                     "'SINGLETON', 'INTERNAL'. "
                                                     'Optional.',
                                      'oneOf': [ {'type': 'string'},
                                                 { 'items': {'type': 'string'},
                                                   'type': 'array'}]}},
  'required': ['composition', 'nodes'],
  'type': 'object'}
TOOL_NOTES = 'This is a thin loop over `add_node`; all validation and role-merging happen there. If any element of `nodes` is not a Mechanism, Composition, or a valid two-element tuple, the call raises `CompositionError` and no nodes are added (there is no transactional rollback — nodes processed before the bad element are already registered). Tuple roles and `required_roles` are additive, not mutually exclusive. `required_roles` applies to ALL nodes, including those inside tuples.'


def _impl(kwargs: dict[str, Any]) -> Any:
    cls = pnl.Composition
    return method_helpers.call_method_tool(
        owner_cls=cls,
        method_name='add_nodes',
        kwargs=kwargs,
        tool_name=TOOL_NAME,
    )


def register(mcp: Any) -> None:
    @captured_tool(mcp, layer="generated", name=TOOL_NAME, description=TOOL_DESCRIPTION)
    def add_nodes(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to add multiple Mechanisms or sub-Compositions to an existing Composition in one batch.'
        return _impl(args or {})
