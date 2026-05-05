"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '7463c1d7c413165c63b3c9f3b43dc740d3a9ac2fce202f936ae7dd93624c6c9c'
__pnl_qualname__ = 'psyneulink.get_class_attributes'
__pnl_kind__ = 'function'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'get_class_attributes'
TOOL_DESCRIPTION = 'Call this tool to inspect the non-trivial attributes of a PsyNeuLink class — it filters out all standard Python object attributes and returns only the class-specific members. Use it when you need to discover what parameters, defaults, or methods a PsyNeuLink class exposes beyond the base Python object. Returns a list of (name, value) tuples.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "cls": {\n      "description": "Fully-qualified or short name of the PsyNeuLink class to inspect (e.g. \\"TransferMechanism\\" or \\"psyneulink.TransferMechanism\\"). The host resolves this string to the actual class before calling the function.",\n      "type": "string"\n    }\n  },\n  "required": [\n    "cls"\n  ],\n  "type": "object"\n}\n\nNotes:\nThe function filters by comparing against `dir(object)`, so any attribute that happens to share a name with a built-in object attribute will be silently excluded. Return value is a list of (name, value) tuples — values may include unbound methods, class-level defaults, Parameters objects, or arbitrary Python objects, so consumers should handle heterogeneous types. Passing an instance instead of a class is not supported; always pass the class itself.'
TOOL_PARAMETERS = { 'properties': { 'cls': { 'description': 'Fully-qualified or short name of the '
                                          'PsyNeuLink class to inspect (e.g. '
                                          '"TransferMechanism" or '
                                          '"psyneulink.TransferMechanism"). The host '
                                          'resolves this string to the actual class '
                                          'before calling the function.',
                           'type': 'string'}},
  'required': ['cls'],
  'type': 'object'}
TOOL_NOTES = 'The function filters by comparing against `dir(object)`, so any attribute that happens to share a name with a built-in object attribute will be silently excluded. Return value is a list of (name, value) tuples — values may include unbound methods, class-level defaults, Parameters objects, or arbitrary Python objects, so consumers should handle heterogeneous types. Passing an instance instead of a class is not supported; always pass the class itself.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.get_class_attributes
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
    def get_class_attributes(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to inspect the non-trivial attributes of a PsyNeuLink class — it filters out all standard Python object attributes and returns only the class-specific members.'
        return _impl(args or {})
