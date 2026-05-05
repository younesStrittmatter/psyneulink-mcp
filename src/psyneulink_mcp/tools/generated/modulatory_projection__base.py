"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = 'dc4fa1ca635cd3a9989030f42fd059c9fd14eadd36774289baadbeb67ce4a85e'
__pnl_qualname__ = 'psyneulink.core.components.projections.modulatory.controlprojection.ModulatoryProjection_Base'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_modulatory_projection__base'
TOOL_DESCRIPTION = 'Do NOT call this tool directly — ModulatoryProjection_Base is an abstract base class that must never be instantiated. Use a concrete subclass instead: ControlProjection (for modulating parameters of a Mechanism) or GatingProjection (for modulating the value of an InputPort or OutputPort). This tool exists only as a documentation reference for shared attributes.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "name": {\n      "description": "Optional name for the projection. If omitted, a default name is assigned in the format \'<ModulatorySignal type> for <receiver owner Mechanism name>[<receiver port name>]\'.",\n      "type": "string"\n    },\n    "receiver": {\n      "description": "Name of the Port whose value this projection modulates.",\n      "type": "string"\n    },\n    "sender": {\n      "description": "Name of the ModulatorySignal (e.g. ControlSignal or GatingSignal) that is the source of the projection.",\n      "type": "string"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\nThis class is abstract and must never be instantiated directly — calling it will raise an error. Always use a concrete subclass: ControlProjection for parameter modulation, GatingProjection for port-value modulation. If initialization is deferred, a temporary name is assigned until the projection is fully initialized; the final name follows the pattern \'<ClassName> for <receiver.owner.name>[<receiver.name>]\'. Duplicate names are disambiguated with an indexed suffix.'
TOOL_PARAMETERS = { 'properties': { 'name': { 'description': 'Optional name for the projection. If '
                                           'omitted, a default name is assigned in the '
                                           "format '<ModulatorySignal type> for "
                                           '<receiver owner Mechanism name>[<receiver '
                                           "port name>]'.",
                            'type': 'string'},
                  'receiver': { 'description': 'Name of the Port whose value this '
                                               'projection modulates.',
                                'type': 'string'},
                  'sender': { 'description': 'Name of the ModulatorySignal (e.g. '
                                             'ControlSignal or GatingSignal) that is '
                                             'the source of the projection.',
                              'type': 'string'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = "This class is abstract and must never be instantiated directly — calling it will raise an error. Always use a concrete subclass: ControlProjection for parameter modulation, GatingProjection for port-value modulation. If initialization is deferred, a temporary name is assigned until the projection is fully initialized; the final name follows the pattern '<ClassName> for <receiver.owner.name>[<receiver.name>]'. Duplicate names are disambiguated with an indexed suffix."


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.ModulatoryProjection_Base
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
    def create_modulatory_projection__base(args: dict[str, Any] | None = None) -> Any:
        'Do NOT call this tool directly — ModulatoryProjection_Base is an abstract base class that must never be instantiated.'
        return _impl(args or {})
