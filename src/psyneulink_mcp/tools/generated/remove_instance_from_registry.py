"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '6383415a2d6ea500cc963ac0061bffd20a21c549d4de83a3bc943122c86e62bd'
__pnl_qualname__ = 'psyneulink.library.components.mechanisms.processing.transfer.recurrenttransfermechanism.remove_instance_from_registry'
__pnl_kind__ = 'function'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'remove_instance_from_registry'
TOOL_DESCRIPTION = 'Call this tool to deregister a specific PsyNeuLink component instance from a named registry category — decrementing the instance count and cleaning up any attached port registry. Use it when explicitly tearing down a component that was registered under a known category. Returns nothing on success; raises RegistryError if neither name nor component is supplied, or if both are supplied but disagree.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "category": {\n      "description": "The category key within the registry whose entry holds the instance (e.g. the class name string used at registration time).",\n      "type": "string"\n    },\n    "component": {\n      "description": "Direct reference to the PsyNeuLink component object to remove. Used when the name is not known; the function will look up the name from the registry. Cannot be serialized to JSON \\u2014 pass \'name\' instead whenever possible.",\n      "type": "object"\n    },\n    "name": {\n      "description": "String name of the instance to remove. Prefer this over \'component\' \\u2014 it is the only option expressible as plain JSON.",\n      "type": "string"\n    },\n    "registry": {\n      "description": "The registry dict from which the instance should be removed (e.g. a Mechanism or Projection registry).",\n      "type": "object"\n    }\n  },\n  "required": [\n    "registry",\n    "category"\n  ],\n  "type": "object"\n}\n\nNotes:\nExactly one of \'name\' or \'component\' must be provided; passing neither raises RegistryError. Passing both is allowed only if name == component.name — any mismatch also raises RegistryError. Because MCP parameters are JSON-serialized, \'component\' (a live Python object) cannot be passed from an LLM agent; always use \'name\'. The function does NOT decrement renamed_instance_counts for duplicate-indexed names (e.g. "MyMech-1", "MyMech-2") — this is an intentional implementation choice documented in the source to avoid index collisions on future registrations. The global_registry is also updated as a side-effect.'
TOOL_PARAMETERS = { 'properties': { 'category': { 'description': 'The category key within the registry '
                                               'whose entry holds the instance (e.g. '
                                               'the class name string used at '
                                               'registration time).',
                                'type': 'string'},
                  'component': { 'description': 'Direct reference to the PsyNeuLink '
                                                'component object to remove. Used when '
                                                'the name is not known; the function '
                                                'will look up the name from the '
                                                'registry. Cannot be serialized to '
                                                "JSON — pass 'name' instead whenever "
                                                'possible.',
                                 'type': 'object'},
                  'name': { 'description': 'String name of the instance to remove. '
                                           "Prefer this over 'component' — it is the "
                                           'only option expressible as plain JSON.',
                            'type': 'string'},
                  'registry': { 'description': 'The registry dict from which the '
                                               'instance should be removed (e.g. a '
                                               'Mechanism or Projection registry).',
                                'type': 'object'}},
  'required': ['registry', 'category'],
  'type': 'object'}
TOOL_NOTES = 'Exactly one of \'name\' or \'component\' must be provided; passing neither raises RegistryError. Passing both is allowed only if name == component.name — any mismatch also raises RegistryError. Because MCP parameters are JSON-serialized, \'component\' (a live Python object) cannot be passed from an LLM agent; always use \'name\'. The function does NOT decrement renamed_instance_counts for duplicate-indexed names (e.g. "MyMech-1", "MyMech-2") — this is an intentional implementation choice documented in the source to avoid index collisions on future registrations. The global_registry is also updated as a side-effect.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.remove_instance_from_registry
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
    def remove_instance_from_registry(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to deregister a specific PsyNeuLink component instance from a named registry category — decrementing the instance count and cleaning up any attached port registry.'
        return _impl(args or {})
