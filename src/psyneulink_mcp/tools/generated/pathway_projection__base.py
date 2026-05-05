"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = 'f6b0080dcf8ab1ff961b71f6d8dcdc54ff5e4dd16d8f808a478464cc735362fb'
__pnl_qualname__ = 'psyneulink.core.components.projections.pathway.mappingprojection.PathwayProjection_Base'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_pathway_projection__base'
TOOL_DESCRIPTION = 'Do NOT call this tool directly — PathwayProjection_Base is an abstract base class and cannot be instantiated. Use a concrete subclass tool instead (e.g., MappingProjection) to create a projection that routes signals from an OutputPort to an InputPort along a processing pathway.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "name": {\n      "description": "Optional name for the projection. Auto-generated as \'ClassName from <sender> to <receiver>\' if omitted.",\n      "type": "string"\n    },\n    "receiver": {\n      "description": "Name of the InputPort or Mechanism that receives the projection. If a Mechanism is specified, its primary InputPort is used.",\n      "type": "string"\n    },\n    "sender": {\n      "description": "Name of the OutputPort or Mechanism that sends the projection. If a Mechanism is specified, its primary OutputPort is used.",\n      "type": "string"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\nPathwayProjection_Base is abstract and should never be instantiated directly — calling this tool will raise an error. Use a concrete subclass such as MappingProjection instead. The parameter schema here reflects the common Projection_Base signature; the actual accepted kwargs depend on the concrete subclass. Auto-naming follows the pattern "ClassName[sender_port] from Mechanism[Port] to Mechanism[Port]" and only applies when the default name has not been overridden.'
TOOL_PARAMETERS = { 'properties': { 'name': { 'description': 'Optional name for the projection. '
                                           "Auto-generated as 'ClassName from <sender> "
                                           "to <receiver>' if omitted.",
                            'type': 'string'},
                  'receiver': { 'description': 'Name of the InputPort or Mechanism '
                                               'that receives the projection. If a '
                                               'Mechanism is specified, its primary '
                                               'InputPort is used.',
                                'type': 'string'},
                  'sender': { 'description': 'Name of the OutputPort or Mechanism that '
                                             'sends the projection. If a Mechanism is '
                                             'specified, its primary OutputPort is '
                                             'used.',
                              'type': 'string'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = 'PathwayProjection_Base is abstract and should never be instantiated directly — calling this tool will raise an error. Use a concrete subclass such as MappingProjection instead. The parameter schema here reflects the common Projection_Base signature; the actual accepted kwargs depend on the concrete subclass. Auto-naming follows the pattern "ClassName[sender_port] from Mechanism[Port] to Mechanism[Port]" and only applies when the default name has not been overridden.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.PathwayProjection_Base
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
    def create_pathway_projection__base(args: dict[str, Any] | None = None) -> Any:
        'Do NOT call this tool directly — PathwayProjection_Base is an abstract base class and cannot be instantiated.'
        return _impl(args or {})
