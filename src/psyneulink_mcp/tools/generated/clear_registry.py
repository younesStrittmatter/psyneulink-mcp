"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '9f23c54971d6ff0199f98c23e626a5d9e9b06c9cb3d93fd0bdc9651b86a6721d'
__pnl_qualname__ = 'psyneulink.clear_registry'
__pnl_kind__ = 'function'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'clear_registry'
TOOL_DESCRIPTION = 'Call this tool to reset PsyNeuLink\'s component registry before a test or fresh modeling session, removing all named instances while preserving category structure. Use it when you need to guarantee that subsequently created components receive predictable default names (e.g., "TransferMechanism-0") without collision from earlier creations. Returns None; side effect is that all registered instances are purged from the specified registry (or all primary registries if none is given).\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "registry": {\n      "description": "A specific PsyNeuLink registry dict to clear. If omitted, all primary registries are cleared. Passing a registry object is rarely needed outside of targeted test teardown.",\n      "type": "object"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\nCalling this outside of testing is dangerous: it allows new components to be created with the same PsyNeuLink name as existing ones in the same Python namespace, breaking name-based lookups. Omitting `registry` clears ALL primary registries at once. The function does not return anything useful — it operates purely by side effect. The `registry` parameter expects a live registry dict object, not a string name; there is no string-based lookup.'
TOOL_PARAMETERS = { 'properties': { 'registry': { 'description': 'A specific PsyNeuLink registry dict to '
                                               'clear. If omitted, all primary '
                                               'registries are cleared. Passing a '
                                               'registry object is rarely needed '
                                               'outside of targeted test teardown.',
                                'type': 'object'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = 'Calling this outside of testing is dangerous: it allows new components to be created with the same PsyNeuLink name as existing ones in the same Python namespace, breaking name-based lookups. Omitting `registry` clears ALL primary registries at once. The function does not return anything useful — it operates purely by side effect. The `registry` parameter expects a live registry dict object, not a string name; there is no string-based lookup.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.clear_registry
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
    def clear_registry(args: dict[str, Any] | None = None) -> Any:
        "Call this tool to reset PsyNeuLink's component registry before a test or fresh modeling session, removing all named instances while preserving category structure."
        return _impl(args or {})
