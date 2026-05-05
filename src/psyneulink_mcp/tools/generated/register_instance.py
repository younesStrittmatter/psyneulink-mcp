"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '3f01e1fae37a46320d51fadb9af19e3fcdb91a9c04d6d5e2f8ed31ba3ec8c30c'
__pnl_qualname__ = 'psyneulink.library.components.mechanisms.processing.transfer.recurrenttransfermechanism.register_instance'
__pnl_kind__ = 'function'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'register_instance'
TOOL_DESCRIPTION = 'Call this tool only in advanced scenarios where you need to manually register a PsyNeuLink component instance into an existing registry dict with explicit naming control. It handles auto-naming (when name is None), deduplication of colliding names by appending numeric suffixes, and updates instanceDict and instanceCount in the registry. The tool does not return a value; its effect is the mutation of the registry in place and global_registry.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "base_class": {\n      "description": "The base class name used for registry categorization.",\n      "type": "string"\n    },\n    "entry": {\n      "description": "The PsyNeuLink component instance to register. Must have a writable `.name` attribute.",\n      "type": "object"\n    },\n    "name": {\n      "description": "Desired name for the instance. Pass null to trigger auto-naming using the pattern \'__pnl_<sub_dict>-N\'.",\n      "type": "string"\n    },\n    "registry": {\n      "description": "The registry dict (e.g., the mechanism or projection registry) that contains the sub_dict entry.",\n      "type": "object"\n    },\n    "sub_dict": {\n      "description": "The key within the registry dict under which this instance should be filed (typically the class name string).",\n      "type": "string"\n    }\n  },\n  "required": [\n    "entry",\n    "name",\n    "base_class",\n    "registry",\n    "sub_dict"\n  ],\n  "type": "object"\n}\n\nNotes:\nThis is a low-level internal utility. Agents should almost never call it directly — PsyNeuLink components self-register during instantiation. Calling it manually risks double-registration, corrupted instanceCounts, or name collisions. Names starting with \'__pnl_\' are reserved; passing one that does not match the auto-name prefix will raise an AssertionError. If `name` is already taken, the function appends \'-N\' suffixes in a loop until a unique name is found; the resulting suffix may not match the existing count if the user previously injected a numerically-suffixed name manually.'
TOOL_PARAMETERS = { 'properties': { 'base_class': { 'description': 'The base class name used for '
                                                 'registry categorization.',
                                  'type': 'string'},
                  'entry': { 'description': 'The PsyNeuLink component instance to '
                                            'register. Must have a writable `.name` '
                                            'attribute.',
                             'type': 'object'},
                  'name': { 'description': 'Desired name for the instance. Pass null '
                                           'to trigger auto-naming using the pattern '
                                           "'__pnl_<sub_dict>-N'.",
                            'type': 'string'},
                  'registry': { 'description': 'The registry dict (e.g., the mechanism '
                                               'or projection registry) that contains '
                                               'the sub_dict entry.',
                                'type': 'object'},
                  'sub_dict': { 'description': 'The key within the registry dict under '
                                               'which this instance should be filed '
                                               '(typically the class name string).',
                                'type': 'string'}},
  'required': ['entry', 'name', 'base_class', 'registry', 'sub_dict'],
  'type': 'object'}
TOOL_NOTES = "This is a low-level internal utility. Agents should almost never call it directly — PsyNeuLink components self-register during instantiation. Calling it manually risks double-registration, corrupted instanceCounts, or name collisions. Names starting with '__pnl_' are reserved; passing one that does not match the auto-name prefix will raise an AssertionError. If `name` is already taken, the function appends '-N' suffixes in a loop until a unique name is found; the resulting suffix may not match the existing count if the user previously injected a numerically-suffixed name manually."


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.register_instance
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
    def register_instance(args: dict[str, Any] | None = None) -> Any:
        'Call this tool only in advanced scenarios where you need to manually register a PsyNeuLink component instance into an existing registry dict with explicit naming control.'
        return _impl(args or {})
