"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '2c169459628c4c38173fc6328abde5f582a9eb5deb4554c6dd83c0d8d7a8709d'
__pnl_qualname__ = 'psyneulink.core.components.mechanisms.modulatory.learning.learningmechanism.Enum'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_enum'
TOOL_DESCRIPTION = 'Call this tool to dynamically create a new enumeration type with named constant members. Returns a new Enum subclass whose members are accessible by attribute, value, or name lookup. Use this when you need a named set of constants for PsyNeuLink configuration, parameter flags, or mode selectors.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "module": {\n      "description": "Module name to assign to __module__ on the new class. Optional.",\n      "type": "string"\n    },\n    "names": {\n      "description": "Member names as a whitespace- or comma-separated string (e.g. \'RED GREEN BLUE\'), a JSON array of strings, a JSON object mapping names to values, or a JSON array of [name, value] pairs.",\n      "type": "string"\n    },\n    "new_class_name": {\n      "description": "Name for the new Enum class (e.g. \'Color\', \'Mode\'). Positional-only in the underlying signature.",\n      "type": "string"\n    },\n    "qualname": {\n      "description": "Qualified name to assign to __qualname__. Optional.",\n      "type": "string"\n    },\n    "start": {\n      "default": 1,\n      "description": "Starting integer value for auto-numbered members when names is a plain string or list of strings. Defaults to 1.",\n      "type": "integer"\n    }\n  },\n  "required": [\n    "new_class_name",\n    "names"\n  ],\n  "type": "object"\n}\n\nNotes:\nThis is Python\'s stdlib enum.Enum imported via the PsyNeuLink learning mechanism module — it is the generic functional-API constructor, not a PsyNeuLink-specific class. new_class_name is positional-only in the real Python signature; passing it as a keyword argument will raise TypeError in Python versions that enforce positional-only parameters. The `type` mixin parameter (for subclassing int, str, etc.) is intentionally omitted from the schema because it expects a Python type object which cannot be serialised as JSON. If auto-numbered values are not desired, pass names as a JSON object mapping each name to its integer value.'
TOOL_PARAMETERS = { 'properties': { 'module': { 'description': 'Module name to assign to __module__ on '
                                             'the new class. Optional.',
                              'type': 'string'},
                  'names': { 'description': 'Member names as a whitespace- or '
                                            "comma-separated string (e.g. 'RED GREEN "
                                            "BLUE'), a JSON array of strings, a JSON "
                                            'object mapping names to values, or a JSON '
                                            'array of [name, value] pairs.',
                             'type': 'string'},
                  'new_class_name': { 'description': 'Name for the new Enum class '
                                                     "(e.g. 'Color', 'Mode'). "
                                                     'Positional-only in the '
                                                     'underlying signature.',
                                      'type': 'string'},
                  'qualname': { 'description': 'Qualified name to assign to '
                                               '__qualname__. Optional.',
                                'type': 'string'},
                  'start': { 'default': 1,
                             'description': 'Starting integer value for auto-numbered '
                                            'members when names is a plain string or '
                                            'list of strings. Defaults to 1.',
                             'type': 'integer'}},
  'required': ['new_class_name', 'names'],
  'type': 'object'}
TOOL_NOTES = "This is Python's stdlib enum.Enum imported via the PsyNeuLink learning mechanism module — it is the generic functional-API constructor, not a PsyNeuLink-specific class. new_class_name is positional-only in the real Python signature; passing it as a keyword argument will raise TypeError in Python versions that enforce positional-only parameters. The `type` mixin parameter (for subclassing int, str, etc.) is intentionally omitted from the schema because it expects a Python type object which cannot be serialised as JSON. If auto-numbered values are not desired, pass names as a JSON object mapping each name to its integer value."


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.Enum
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
    def create_enum(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to dynamically create a new enumeration type with named constant members.'
        return _impl(args or {})
