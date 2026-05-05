"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '61423be9907846dfafb03ade48e2a5d6823aa4bd0c7cbb01f36f26b0101f9a32'
__pnl_qualname__ = 'psyneulink.NodeRole'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_node_role'
TOOL_DESCRIPTION = 'Call this tool to retrieve a specific NodeRole enum member by name — use it when you need to pass a role constant to other PsyNeuLink calls (e.g., `required_roles` or `exclude_roles` in `add_node`, or role checks on `get_nodes_by_role`). Returns the `NodeRole` enum member corresponding to the given name string.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "name": {\n      "description": "The name of the NodeRole member to retrieve.",\n      "enum": [\n        "ORIGIN",\n        "INPUT",\n        "SINGLETON",\n        "BIAS",\n        "INTERNAL",\n        "CYCLE",\n        "FEEDBACK_SENDER",\n        "FEEDBACK_RECEIVER",\n        "CONTROL_OBJECTIVE",\n        "CONTROLLER",\n        "CONTROLLER_OBJECTIVE",\n        "LEARNING",\n        "TARGET",\n        "LEARNING_OBJECTIVE",\n        "PROBE",\n        "OUTPUT",\n        "TERMINAL"\n      ],\n      "type": "string"\n    }\n  },\n  "required": [\n    "name"\n  ],\n  "type": "object"\n}\n\nNotes:\nNodeRole is a pure enum — most roles are assigned automatically by PsyNeuLink based on graph topology and cannot (or should not) be set programmatically: ORIGIN, SINGLETON, INTERNAL, CYCLE, CONTROLLER, FEEDBACK_SENDER, FEEDBACK_RECEIVER, and TERMINAL are all read-only. Only INPUT, OUTPUT, PROBE, LEARNING, TARGET, and LEARNING_OBJECTIVE can be explicitly assigned via `required_roles`/`exclude_roles`. PROBE nodes appear in output_CIM projections but are excluded from Composition.results. BIAS nodes always co-occur with ORIGIN and never with INPUT. SINGLETON = ORIGIN + TERMINAL in the same node.'
TOOL_PARAMETERS = { 'properties': { 'name': { 'description': 'The name of the NodeRole member to '
                                           'retrieve.',
                            'enum': [ 'ORIGIN',
                                      'INPUT',
                                      'SINGLETON',
                                      'BIAS',
                                      'INTERNAL',
                                      'CYCLE',
                                      'FEEDBACK_SENDER',
                                      'FEEDBACK_RECEIVER',
                                      'CONTROL_OBJECTIVE',
                                      'CONTROLLER',
                                      'CONTROLLER_OBJECTIVE',
                                      'LEARNING',
                                      'TARGET',
                                      'LEARNING_OBJECTIVE',
                                      'PROBE',
                                      'OUTPUT',
                                      'TERMINAL'],
                            'type': 'string'}},
  'required': ['name'],
  'type': 'object'}
TOOL_NOTES = 'NodeRole is a pure enum — most roles are assigned automatically by PsyNeuLink based on graph topology and cannot (or should not) be set programmatically: ORIGIN, SINGLETON, INTERNAL, CYCLE, CONTROLLER, FEEDBACK_SENDER, FEEDBACK_RECEIVER, and TERMINAL are all read-only. Only INPUT, OUTPUT, PROBE, LEARNING, TARGET, and LEARNING_OBJECTIVE can be explicitly assigned via `required_roles`/`exclude_roles`. PROBE nodes appear in output_CIM projections but are excluded from Composition.results. BIAS nodes always co-occur with ORIGIN and never with INPUT. SINGLETON = ORIGIN + TERMINAL in the same node.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.NodeRole
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
    def create_node_role(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to retrieve a specific NodeRole enum member by name — use it when you need to pass a role constant to other PsyNeuLink calls (e.g., `required_roles` or `exclude_roles` in `add_node`, or role checks on `get_nodes_by_role`).'
        return _impl(args or {})
