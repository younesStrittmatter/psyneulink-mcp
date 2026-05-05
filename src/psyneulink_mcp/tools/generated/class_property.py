"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '97ed263b67fb66e07290fc32fd1397ea7911d33059e79ef6c0478ae91d80ee92'
__pnl_qualname__ = 'psyneulink.classProperty'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_class_property'
TOOL_DESCRIPTION = 'Call this tool only when you need to inspect or understand the classProperty descriptor type from PsyNeuLink\'s internals — it is a class-level property descriptor that binds to the owner class rather than an instance. Unlike standard Python property, classProperty.fget is called unbound on the class itself, so accessing it on either a class or instance always invokes the getter with the owner class as context. This tool is rarely useful for modeling tasks; it exists as a metaclass utility.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "doc": {\n      "description": "Docstring for the property.",\n      "type": "string"\n    },\n    "fdel": {\n      "description": "Name or string representation of the deleter function. Same limitation as fget.",\n      "type": "string"\n    },\n    "fget": {\n      "description": "Name or string representation of the getter function. NOTE: callables cannot be passed via JSON; this parameter is effectively non-functional through the MCP interface.",\n      "type": "string"\n    },\n    "fset": {\n      "description": "Name or string representation of the setter function. Same limitation as fget.",\n      "type": "string"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\nclassProperty is an internal Python descriptor utility, not a PsyNeuLink modeling primitive. It subclasses property and overrides __get__ so the getter is always invoked on the owner class (never the instance), making it useful for class-level computed attributes. Because its constructor expects callable fget/fset/fdel arguments and MCP tool calls use JSON, you cannot meaningfully instantiate classProperty through this interface — any attempt to pass function names as strings will fail at runtime. Do not call this tool expecting to create or modify class properties at runtime; it exists primarily so agents can discover and understand the descriptor pattern used throughout PsyNeuLink\'s class hierarchy.'
TOOL_PARAMETERS = { 'properties': { 'doc': { 'description': 'Docstring for the property.',
                           'type': 'string'},
                  'fdel': { 'description': 'Name or string representation of the '
                                           'deleter function. Same limitation as fget.',
                            'type': 'string'},
                  'fget': { 'description': 'Name or string representation of the '
                                           'getter function. NOTE: callables cannot be '
                                           'passed via JSON; this parameter is '
                                           'effectively non-functional through the MCP '
                                           'interface.',
                            'type': 'string'},
                  'fset': { 'description': 'Name or string representation of the '
                                           'setter function. Same limitation as fget.',
                            'type': 'string'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = "classProperty is an internal Python descriptor utility, not a PsyNeuLink modeling primitive. It subclasses property and overrides __get__ so the getter is always invoked on the owner class (never the instance), making it useful for class-level computed attributes. Because its constructor expects callable fget/fset/fdel arguments and MCP tool calls use JSON, you cannot meaningfully instantiate classProperty through this interface — any attempt to pass function names as strings will fail at runtime. Do not call this tool expecting to create or modify class properties at runtime; it exists primarily so agents can discover and understand the descriptor pattern used throughout PsyNeuLink's class hierarchy."


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.classProperty
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
    def create_class_property(args: dict[str, Any] | None = None) -> Any:
        "Call this tool only when you need to inspect or understand the classProperty descriptor type from PsyNeuLink's internals — it is a class-level property descriptor that binds to the owner class rather than an instance."
        return _impl(args or {})
