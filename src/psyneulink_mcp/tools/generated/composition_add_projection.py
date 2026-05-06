"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool
from psyneulink_mcp import method_helpers

__source_sha256__ = 'c5041bab66b1c5fd5c2e1b3ac9db00b905bf0bb39f0ecfbb1f796e0426493f01'
__pnl_qualname__ = 'psyneulink.Composition.add_projection'
__pnl_kind__ = 'method'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'add_projection'
TOOL_DESCRIPTION = 'Call this to wire two nodes in a Composition with a directed projection. Use it whenever you need to connect a sender Mechanism/OutputPort to a receiver Mechanism/InputPort — the runtime automatically adds both nodes to the composition first, so you do NOT need to call add_node beforehand. Returns the projection handle on success; retrying with the same sender/receiver is safe (duplicate projections are silently treated as success).\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "composition": {\n      "description": "Handle string of the Composition (returned by create_composition) to add the projection to.",\n      "type": "string"\n    },\n    "default_matrix": {\n      "description": "Matrix for the default MappingProjection when no projection is specified. Accepts a PNL keyword string: FULL_CONNECTIVITY_MATRIX, IDENTITY_MATRIX, HOLLOW_MATRIX, RANDOM_CONNECTIVITY_MATRIX. IDENTITY_MATRIX requires sender and receiver to have the same output/input size \\u2014 use FULL_CONNECTIVITY_MATRIX when sizes differ.",\n      "type": "string"\n    },\n    "feedback": {\n      "default": false,\n      "description": "If true, the projection is always designated as a feedback projection to break a cycle. If false (default), it is never designated as feedback even if PNL would do so by default.",\n      "type": "boolean"\n    },\n    "name": {\n      "description": "Optional name for the new projection.",\n      "type": "string"\n    },\n    "receiver": {\n      "description": "Handle string of the receiving Mechanism, nested Composition, or InputPort.",\n      "type": "string"\n    },\n    "sender": {\n      "description": "Handle string of the sending Mechanism, nested Composition, or OutputPort.",\n      "type": "string"\n    }\n  },\n  "required": [\n    "composition",\n    "sender",\n    "receiver"\n  ],\n  "type": "object"\n}\n\nNotes:\nIDENTITY_MATRIX requires sender output size == receiver input size exactly; passing it between nodes of different sizes raises FunctionError (e.g., sender=25, receiver=20). Use FULL_CONNECTIVITY_MATRIX when sizes differ — it works for any sender/receiver size combination. The runtime helper resolves all handle strings to live PNL objects before dispatching, and defensively adds sender and receiver to the composition (PNL no-ops if already present). DuplicateProjectionError is caught and treated as no-op success, so retrying is safe. The underlying PNL parameter is default_matrix (not matrix); both names are accepted by the runtime but the schema advertises default_matrix.'
TOOL_PARAMETERS = { 'properties': { 'composition': { 'description': 'Handle string of the Composition '
                                                  '(returned by create_composition) to '
                                                  'add the projection to.',
                                   'type': 'string'},
                  'default_matrix': { 'description': 'Matrix for the default '
                                                     'MappingProjection when no '
                                                     'projection is specified. Accepts '
                                                     'a PNL keyword string: '
                                                     'FULL_CONNECTIVITY_MATRIX, '
                                                     'IDENTITY_MATRIX, HOLLOW_MATRIX, '
                                                     'RANDOM_CONNECTIVITY_MATRIX. '
                                                     'IDENTITY_MATRIX requires sender '
                                                     'and receiver to have the same '
                                                     'output/input size — use '
                                                     'FULL_CONNECTIVITY_MATRIX when '
                                                     'sizes differ.',
                                      'type': 'string'},
                  'feedback': { 'default': False,
                                'description': 'If true, the projection is always '
                                               'designated as a feedback projection to '
                                               'break a cycle. If false (default), it '
                                               'is never designated as feedback even '
                                               'if PNL would do so by default.',
                                'type': 'boolean'},
                  'name': { 'description': 'Optional name for the new projection.',
                            'type': 'string'},
                  'receiver': { 'description': 'Handle string of the receiving '
                                               'Mechanism, nested Composition, or '
                                               'InputPort.',
                                'type': 'string'},
                  'sender': { 'description': 'Handle string of the sending Mechanism, '
                                             'nested Composition, or OutputPort.',
                              'type': 'string'}},
  'required': ['composition', 'sender', 'receiver'],
  'type': 'object'}
TOOL_NOTES = 'IDENTITY_MATRIX requires sender output size == receiver input size exactly; passing it between nodes of different sizes raises FunctionError (e.g., sender=25, receiver=20). Use FULL_CONNECTIVITY_MATRIX when sizes differ — it works for any sender/receiver size combination. The runtime helper resolves all handle strings to live PNL objects before dispatching, and defensively adds sender and receiver to the composition (PNL no-ops if already present). DuplicateProjectionError is caught and treated as no-op success, so retrying is safe. The underlying PNL parameter is default_matrix (not matrix); both names are accepted by the runtime but the schema advertises default_matrix.'


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
        'Call this to wire two nodes in a Composition with a directed projection.'
        return _impl(args or {})
