"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = 'f8b1be652d86225a3ea7629c57af81ef0b5202ce81358c3a5959d59a704e585b'
__pnl_qualname__ = 'psyneulink.core.components.functions.nonstateful.learningfunctions.namedtuple'
__pnl_kind__ = 'function'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'namedtuple'
TOOL_DESCRIPTION = 'Call this tool when you need to define a new named-tuple class (a lightweight, immutable record type) for use in PsyNeuLink learning-function contexts — e.g., to package a set of related values (weights, errors, learning signals) into a structured, field-accessible container. Returns a new class (a tuple subclass) whose instances expose fields both by name and by positional index.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "defaults": {\n      "default": null,\n      "description": "Default values for the rightmost N fields. Length must not exceed the number of fields. Omit to require all fields at instantiation time.",\n      "items": {},\n      "type": "array"\n    },\n    "field_names": {\n      "description": "Names for each positional field of the new tuple class.",\n      "oneOf": [\n        {\n          "description": "Ordered list of field name strings (e.g., [\'weight\', \'error\', \'delta\']).",\n          "items": {\n            "type": "string"\n          },\n          "type": "array"\n        },\n        {\n          "description": "Space- or comma-separated field names as a single string (e.g., \'weight error delta\').",\n          "type": "string"\n        }\n      ]\n    },\n    "module": {\n      "default": null,\n      "description": "Override the __module__ attribute of the generated class (affects pickling). If omitted, Python infers the caller\'s module automatically.",\n      "type": "string"\n    },\n    "rename": {\n      "default": false,\n      "description": "If true, invalid or duplicate field names are silently replaced with positional names (_0, _1, \\u2026) instead of raising an error.",\n      "type": "boolean"\n    },\n    "typename": {\n      "description": "Name of the new tuple subclass (e.g., \'LearningSignal\'). Must be a valid Python identifier.",\n      "type": "string"\n    }\n  },\n  "required": [\n    "typename",\n    "field_names"\n  ],\n  "type": "object"\n}\n\nNotes:\nThis is Python\'s standard collections.namedtuple — it creates and returns a *class*, not an instance. Agents that want a concrete record must then instantiate the returned class. `defaults` covers only the *rightmost* fields: passing 2 defaults for 4 fields means the first 2 fields are still required. Field names must be valid Python identifiers and cannot start with an underscore (unless `rename=True`). Duplicate field names always raise ValueError regardless of `rename`. The `module` parameter is rarely needed but matters for cross-process pickling.'
TOOL_PARAMETERS = { 'properties': { 'defaults': { 'default': None,
                                'description': 'Default values for the rightmost N '
                                               'fields. Length must not exceed the '
                                               'number of fields. Omit to require all '
                                               'fields at instantiation time.',
                                'items': {},
                                'type': 'array'},
                  'field_names': { 'description': 'Names for each positional field of '
                                                  'the new tuple class.',
                                   'oneOf': [ { 'description': 'Ordered list of field '
                                                               'name strings (e.g., '
                                                               "['weight', 'error', "
                                                               "'delta']).",
                                                'items': {'type': 'string'},
                                                'type': 'array'},
                                              { 'description': 'Space- or '
                                                               'comma-separated field '
                                                               'names as a single '
                                                               "string (e.g., 'weight "
                                                               "error delta').",
                                                'type': 'string'}]},
                  'module': { 'default': None,
                              'description': 'Override the __module__ attribute of the '
                                             'generated class (affects pickling). If '
                                             "omitted, Python infers the caller's "
                                             'module automatically.',
                              'type': 'string'},
                  'rename': { 'default': False,
                              'description': 'If true, invalid or duplicate field '
                                             'names are silently replaced with '
                                             'positional names (_0, _1, …) instead of '
                                             'raising an error.',
                              'type': 'boolean'},
                  'typename': { 'description': 'Name of the new tuple subclass (e.g., '
                                               "'LearningSignal'). Must be a valid "
                                               'Python identifier.',
                                'type': 'string'}},
  'required': ['typename', 'field_names'],
  'type': 'object'}
TOOL_NOTES = "This is Python's standard collections.namedtuple — it creates and returns a *class*, not an instance. Agents that want a concrete record must then instantiate the returned class. `defaults` covers only the *rightmost* fields: passing 2 defaults for 4 fields means the first 2 fields are still required. Field names must be valid Python identifiers and cannot start with an underscore (unless `rename=True`). Duplicate field names always raise ValueError regardless of `rename`. The `module` parameter is rarely needed but matters for cross-process pickling."


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.namedtuple
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
    def namedtuple(args: dict[str, Any] | None = None) -> Any:
        'Call this tool when you need to define a new named-tuple class (a lightweight, immutable record type) for use in PsyNeuLink learning-function contexts — e.g., to package a set of related values (weights, errors, learning signals) into a structured, field-accessible container.'
        return _impl(args or {})
