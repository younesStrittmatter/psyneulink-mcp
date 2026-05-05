"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '78a4500b8f1bb32e8868906a2ecc6fa1b6b2e2824feac491d85bedf3e85f4034'
__pnl_qualname__ = 'psyneulink.EntriesDict'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_entries_dict'
TOOL_DESCRIPTION = 'Call this tool only when you need to directly instantiate a raw log-entries container for a PsyNeuLink Log object — for example, when building or inspecting a custom Log programmatically. This is an internal data structure; in normal usage it is created automatically by Log and you should not need to call it directly. Returns an EntriesDict instance that maps attribute names to lists of LogEntry objects.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "owner": {\n      "description": "The name or reference string identifying the Log instance this EntriesDict belongs to. In typical PsyNeuLink usage, this is set automatically by the owning Log; only supply it when constructing an EntriesDict manually.",\n      "type": "string"\n    }\n  },\n  "required": [\n    "owner"\n  ],\n  "type": "object"\n}\n\nNotes:\nEntriesDict is an internal class normally instantiated by Log, not directly by user code or agents. The owner argument in the constructor expects an actual Log object (a Python reference), not a string — passing a string will likely fail at runtime unless the host system resolves it. Only non-LogEntry assignments to entries will raise a LogError; direct list assignment bypasses the append logic. Deleting entries is permanent and cannot be undone.'
TOOL_PARAMETERS = { 'properties': { 'owner': { 'description': 'The name or reference string identifying '
                                            'the Log instance this EntriesDict belongs '
                                            'to. In typical PsyNeuLink usage, this is '
                                            'set automatically by the owning Log; only '
                                            'supply it when constructing an '
                                            'EntriesDict manually.',
                             'type': 'string'}},
  'required': ['owner'],
  'type': 'object'}
TOOL_NOTES = 'EntriesDict is an internal class normally instantiated by Log, not directly by user code or agents. The owner argument in the constructor expects an actual Log object (a Python reference), not a string — passing a string will likely fail at runtime unless the host system resolves it. Only non-LogEntry assignments to entries will raise a LogError; direct list assignment bypasses the append logic. Deleting entries is permanent and cannot be undone.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.EntriesDict
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
    def create_entries_dict(args: dict[str, Any] | None = None) -> Any:
        'Call this tool only when you need to directly instantiate a raw log-entries container for a PsyNeuLink Log object — for example, when building or inspecting a custom Log programmatically.'
        return _impl(args or {})
