"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '08d20b21233c2adacbf965059f935a6b3511f664b3fc1059f14cc97038a560fc'
__pnl_qualname__ = 'psyneulink.process_registry_object_instances'
__pnl_kind__ = 'function'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'process_registry_object_instances'
TOOL_DESCRIPTION = 'Call this tool to iterate over every named instance in a PsyNeuLink registry and apply a callback to each `(name, object)` pair. Use it when you need to enumerate or bulk-process all registered PsyNeuLink objects across every category in a given registry. Returns nothing — all effects occur through the `func` callback.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "func": {\n      "description": "Fully-qualified name of the Python callable to apply to each (name, obj) pair (e.g. \'mymodule.my_callback\'). Must accept exactly two positional arguments: the instance name (str) and the instance object.",\n      "type": "string"\n    },\n    "registry": {\n      "description": "A PsyNeuLink registry dict: keys are category names, values are objects with an `instanceDict` attribute mapping instance names to objects (e.g. psyneulink.MechanismRegistry).",\n      "type": "object"\n    }\n  },\n  "required": [\n    "registry",\n    "func"\n  ],\n  "type": "object"\n}\n\nNotes:\nThis is a low-level registry traversal utility with no return value — output is entirely via side effects of `func`. The `func` parameter is a callable in the Python signature but is represented here as a string name; the host must resolve it. If `func` raises, the loop aborts mid-registry with no partial-success guarantee. The `registry` parameter is a live Python dict structure; agents cannot construct one from scratch via JSON — this tool is most useful when the registry reference is already held in the server process (e.g. passed by reference from a prior setup step).'
TOOL_PARAMETERS = { 'properties': { 'func': { 'description': 'Fully-qualified name of the Python '
                                           'callable to apply to each (name, obj) pair '
                                           "(e.g. 'mymodule.my_callback'). Must accept "
                                           'exactly two positional arguments: the '
                                           'instance name (str) and the instance '
                                           'object.',
                            'type': 'string'},
                  'registry': { 'description': 'A PsyNeuLink registry dict: keys are '
                                               'category names, values are objects '
                                               'with an `instanceDict` attribute '
                                               'mapping instance names to objects '
                                               '(e.g. psyneulink.MechanismRegistry).',
                                'type': 'object'}},
  'required': ['registry', 'func'],
  'type': 'object'}
TOOL_NOTES = 'This is a low-level registry traversal utility with no return value — output is entirely via side effects of `func`. The `func` parameter is a callable in the Python signature but is represented here as a string name; the host must resolve it. If `func` raises, the loop aborts mid-registry with no partial-success guarantee. The `registry` parameter is a live Python dict structure; agents cannot construct one from scratch via JSON — this tool is most useful when the registry reference is already held in the server process (e.g. passed by reference from a prior setup step).'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.process_registry_object_instances
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
    def process_registry_object_instances(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to iterate over every named instance in a PsyNeuLink registry and apply a callback to each `(name, object)` pair.'
        return _impl(args or {})
