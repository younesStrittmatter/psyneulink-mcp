"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool
from psyneulink_mcp import method_helpers

__source_sha256__ = 'aad2ff2a37448a28269446f0126429a6a923fd87b61604ed75b102fac2cd1d54'
__pnl_qualname__ = 'psyneulink.Composition.add_node'
__pnl_kind__ = 'method'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'add_node'
TOOL_DESCRIPTION = 'Call this tool to add a Mechanism or nested Composition as a node to an existing Composition. Use it whenever you\'ve created a mechanism and need to register it in the Composition before wiring projections or running. Re-adding a node that already exists is a silent no-op, so this can be called defensively without first checking membership.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "composition": {\n      "description": "Handle string for the target Composition, as returned by create_composition.",\n      "type": "string"\n    },\n    "node": {\n      "description": "Handle string for the Mechanism or nested Composition to add.",\n      "type": "string"\n    },\n    "required_roles": {\n      "description": "One or more NodeRole names (e.g. \'INPUT\', \'OUTPUT\', \'TERMINAL\', \'INTERNAL\') to assign in addition to roles inferred by graph analysis. Omit if you want PsyNeuLink to determine roles automatically.",\n      "oneOf": [\n        {\n          "type": "string"\n        },\n        {\n          "items": {\n            "type": "string"\n          },\n          "type": "array"\n        }\n      ]\n    }\n  },\n  "required": [\n    "composition",\n    "node"\n  ],\n  "type": "object"\n}\n\nNotes:\nA node that is already present in the Composition is silently skipped — no error is raised. If NodeRole.INTERNAL is included in required_roles, every input_port on the node has internal_only set to True, which means it will not receive external inputs. NodeRole strings must match PsyNeuLink\'s NodeRole enum names exactly (case-sensitive). A Composition cannot be added to itself; that raises CompositionError.'
TOOL_PARAMETERS = { 'properties': { 'composition': { 'description': 'Handle string for the target '
                                                  'Composition, as returned by '
                                                  'create_composition.',
                                   'type': 'string'},
                  'node': { 'description': 'Handle string for the Mechanism or nested '
                                           'Composition to add.',
                            'type': 'string'},
                  'required_roles': { 'description': 'One or more NodeRole names (e.g. '
                                                     "'INPUT', 'OUTPUT', 'TERMINAL', "
                                                     "'INTERNAL') to assign in "
                                                     'addition to roles inferred by '
                                                     'graph analysis. Omit if you want '
                                                     'PsyNeuLink to determine roles '
                                                     'automatically.',
                                      'oneOf': [ {'type': 'string'},
                                                 { 'items': {'type': 'string'},
                                                   'type': 'array'}]}},
  'required': ['composition', 'node'],
  'type': 'object'}
TOOL_NOTES = "A node that is already present in the Composition is silently skipped — no error is raised. If NodeRole.INTERNAL is included in required_roles, every input_port on the node has internal_only set to True, which means it will not receive external inputs. NodeRole strings must match PsyNeuLink's NodeRole enum names exactly (case-sensitive). A Composition cannot be added to itself; that raises CompositionError."


def _impl(kwargs: dict[str, Any]) -> Any:
    cls = pnl.Composition
    return method_helpers.call_method_tool(
        owner_cls=cls,
        method_name='add_node',
        kwargs=kwargs,
        tool_name=TOOL_NAME,
    )


def register(mcp: Any) -> None:
    @captured_tool(mcp, layer="generated", name=TOOL_NAME, description=TOOL_DESCRIPTION)
    def add_node(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to add a Mechanism or nested Composition as a node to an existing Composition.'
        return _impl(args or {})
