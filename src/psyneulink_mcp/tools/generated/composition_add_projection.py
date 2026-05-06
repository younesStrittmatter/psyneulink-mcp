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
TOOL_DESCRIPTION = 'Call this to wire two nodes in a Composition with a directed MappingProjection. Use it whenever you need to connect a sender Mechanism/OutputPort to a receiver Mechanism/InputPort — the runtime automatically adds both nodes to the composition first, so you do NOT need to call `add_node` beforehand. Returns the projection handle on success; retrying with the same sender/receiver is safe (duplicate projections are silently treated as no-op success).\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "composition": {\n      "description": "Handle string of the Composition (returned by create_composition) to add the projection to.",\n      "type": "string"\n    },\n    "default_matrix": {\n      "description": "Matrix keyword for the default MappingProjection when no projection object is given. Accepted PNL keywords: FULL_CONNECTIVITY_MATRIX (works for any sender/receiver size combination), IDENTITY_MATRIX (requires sender output size == receiver input size exactly \\u2014 raises FunctionError if sizes differ), HOLLOW_MATRIX, RANDOM_CONNECTIVITY_MATRIX. Omit to use the MappingProjection default. Use FULL_CONNECTIVITY_MATRIX whenever sender and receiver sizes may differ.",\n      "type": "string"\n    },\n    "feedback": {\n      "default": false,\n      "description": "If true, always designates the projection as a feedback projection to break a cycle. If false (default), the projection is never designated as feedback even if PNL would do so by default.",\n      "type": "boolean"\n    },\n    "name": {\n      "description": "Optional name for the new projection.",\n      "type": "string"\n    },\n    "receiver": {\n      "description": "Handle string OR name of the receiving Mechanism, nested Composition, or InputPort. Must be a single string \\u2014 NEVER pass a list or array here; passing [\'port_name\', \'handle\'] causes an UnboundLocalError. To target a specific InputPort, pass its handle directly.",\n      "type": "string"\n    },\n    "sender": {\n      "description": "Handle string OR name of the sending Mechanism, nested Composition, or OutputPort. Must be a single string \\u2014 NEVER pass a list or array here; passing [\'port_name\', \'handle\'] causes an UnboundLocalError. To target a specific OutputPort, pass its handle directly.",\n      "type": "string"\n    }\n  },\n  "required": [\n    "composition",\n    "sender",\n    "receiver"\n  ],\n  "type": "object"\n}\n\nNotes:\nCRITICAL — sender and receiver must each be a single string (handle or name), never a list or array. Passing a list such as ["FIELD_1_INPUT", "h_697a82aa7d63"] or ["h_abc", "RETRIEVED_FIELD_1"] causes `UnboundLocalError: cannot access local variable \'receiver_ports\'/\'sender_ports\'` inside PNL\'s _check_for_existing_projections. To target a specific InputPort or OutputPort by name, retrieve its handle first (e.g., via get_mechanism_input_ports), then pass that single handle string here.\n\nIDENTITY_MATRIX requires sender output dimensionality == receiver input dimensionality exactly. Passing it between nodes of different sizes (e.g., sender=25 units, receiver=20 units) raises FunctionError. Prefer FULL_CONNECTIVITY_MATRIX when sizes differ — it handles any combination of sender/receiver dimensions.\n\nThe runtime helper translates both `matrix` and `default_matrix` kwarg names to PNL\'s `default_matrix` parameter to avoid a PNL parameter-port bug; always pass `default_matrix` in schema usage.\n\nDuplicateProjectionError is caught by the runtime and treated as no-op success — retrying add_projection for an already-wired pair is safe.'
TOOL_PARAMETERS = { 'properties': { 'composition': { 'description': 'Handle string of the Composition '
                                                  '(returned by create_composition) to '
                                                  'add the projection to.',
                                   'type': 'string'},
                  'default_matrix': { 'description': 'Matrix keyword for the default '
                                                     'MappingProjection when no '
                                                     'projection object is given. '
                                                     'Accepted PNL keywords: '
                                                     'FULL_CONNECTIVITY_MATRIX (works '
                                                     'for any sender/receiver size '
                                                     'combination), IDENTITY_MATRIX '
                                                     '(requires sender output size == '
                                                     'receiver input size exactly — '
                                                     'raises FunctionError if sizes '
                                                     'differ), HOLLOW_MATRIX, '
                                                     'RANDOM_CONNECTIVITY_MATRIX. Omit '
                                                     'to use the MappingProjection '
                                                     'default. Use '
                                                     'FULL_CONNECTIVITY_MATRIX '
                                                     'whenever sender and receiver '
                                                     'sizes may differ.',
                                      'type': 'string'},
                  'feedback': { 'default': False,
                                'description': 'If true, always designates the '
                                               'projection as a feedback projection to '
                                               'break a cycle. If false (default), the '
                                               'projection is never designated as '
                                               'feedback even if PNL would do so by '
                                               'default.',
                                'type': 'boolean'},
                  'name': { 'description': 'Optional name for the new projection.',
                            'type': 'string'},
                  'receiver': { 'description': 'Handle string OR name of the receiving '
                                               'Mechanism, nested Composition, or '
                                               'InputPort. Must be a single string — '
                                               'NEVER pass a list or array here; '
                                               "passing ['port_name', 'handle'] causes "
                                               'an UnboundLocalError. To target a '
                                               'specific InputPort, pass its handle '
                                               'directly.',
                                'type': 'string'},
                  'sender': { 'description': 'Handle string OR name of the sending '
                                             'Mechanism, nested Composition, or '
                                             'OutputPort. Must be a single string — '
                                             'NEVER pass a list or array here; passing '
                                             "['port_name', 'handle'] causes an "
                                             'UnboundLocalError. To target a specific '
                                             'OutputPort, pass its handle directly.',
                              'type': 'string'}},
  'required': ['composition', 'sender', 'receiver'],
  'type': 'object'}
TOOL_NOTES = 'CRITICAL — sender and receiver must each be a single string (handle or name), never a list or array. Passing a list such as ["FIELD_1_INPUT", "h_697a82aa7d63"] or ["h_abc", "RETRIEVED_FIELD_1"] causes `UnboundLocalError: cannot access local variable \'receiver_ports\'/\'sender_ports\'` inside PNL\'s _check_for_existing_projections. To target a specific InputPort or OutputPort by name, retrieve its handle first (e.g., via get_mechanism_input_ports), then pass that single handle string here.\n\nIDENTITY_MATRIX requires sender output dimensionality == receiver input dimensionality exactly. Passing it between nodes of different sizes (e.g., sender=25 units, receiver=20 units) raises FunctionError. Prefer FULL_CONNECTIVITY_MATRIX when sizes differ — it handles any combination of sender/receiver dimensions.\n\nThe runtime helper translates both `matrix` and `default_matrix` kwarg names to PNL\'s `default_matrix` parameter to avoid a PNL parameter-port bug; always pass `default_matrix` in schema usage.\n\nDuplicateProjectionError is caught by the runtime and treated as no-op success — retrying add_projection for an already-wired pair is safe.'


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
        'Call this to wire two nodes in a Composition with a directed MappingProjection.'
        return _impl(args or {})
