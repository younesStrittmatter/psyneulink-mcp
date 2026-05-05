"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '90441c3fb21404838f2ea840c25ebfe5caf7fd5035d8e045469ad8e2243f432d'
__pnl_qualname__ = 'psyneulink.library.components.mechanisms.processing.transfer.recurrenttransfermechanism.ConnectionInfo'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_connection_info'
TOOL_DESCRIPTION = 'Call this tool to create a ConnectionInfo object that tracks which Compositions a Projection-to-Port connection is active in and under what context flags. Use it when constructing or inspecting connection metadata for a RecurrentTransferMechanism or similar component — not for building network structure directly, but for querying or annotating connection membership.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "active_context": {\n      "description": "The ContextFlags value indicating the execution context under which this connection is active (e.g., \'EXECUTING\', \'INITIALIZING\'). Omit if context-independent.",\n      "type": "string"\n    },\n    "compositions": {\n      "description": "Name or identifier of the Composition(s) this connection is associated with. Pass a single composition name, a list of names, or the string \'ALL\' to indicate the connection is active in all compositions. Omit to leave unset (None).",\n      "type": "string"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\nConnectionInfo.ALL is a sentinel (True) meaning the connection is active in every Composition — passing \'ALL\' as the compositions string maps to this sentinel. The implementation converts a single composition or an iterable into a Python set; order is not preserved. active_context expects a ContextFlags enum value at runtime, but the MCP layer accepts it as a string label. This class is a SimpleNamespace subclass, so arbitrary attributes can be set, but only compositions and active_context are formally supported. Calling is_active_in_composition returns False when compositions is None, True when ALL, and membership-checks otherwise.'
TOOL_PARAMETERS = { 'properties': { 'active_context': { 'description': 'The ContextFlags value '
                                                     'indicating the execution context '
                                                     'under which this connection is '
                                                     "active (e.g., 'EXECUTING', "
                                                     "'INITIALIZING'). Omit if "
                                                     'context-independent.',
                                      'type': 'string'},
                  'compositions': { 'description': 'Name or identifier of the '
                                                   'Composition(s) this connection is '
                                                   'associated with. Pass a single '
                                                   'composition name, a list of names, '
                                                   "or the string 'ALL' to indicate "
                                                   'the connection is active in all '
                                                   'compositions. Omit to leave unset '
                                                   '(None).',
                                    'type': 'string'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = "ConnectionInfo.ALL is a sentinel (True) meaning the connection is active in every Composition — passing 'ALL' as the compositions string maps to this sentinel. The implementation converts a single composition or an iterable into a Python set; order is not preserved. active_context expects a ContextFlags enum value at runtime, but the MCP layer accepts it as a string label. This class is a SimpleNamespace subclass, so arbitrary attributes can be set, but only compositions and active_context are formally supported. Calling is_active_in_composition returns False when compositions is None, True when ALL, and membership-checks otherwise."


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.ConnectionInfo
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
    def create_connection_info(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to create a ConnectionInfo object that tracks which Compositions a Projection-to-Port connection is active in and under what context flags.'
        return _impl(args or {})
