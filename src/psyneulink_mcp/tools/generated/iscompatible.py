"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = 'df8eaebdc4c262666327c9580ae0d15ec7a9b2b1b8a227d9bd5b502b84693d6b'
__pnl_qualname__ = 'psyneulink.core.components.mechanisms.processing.transfermechanism.iscompatible'
__pnl_kind__ = 'function'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'iscompatible'
TOOL_DESCRIPTION = 'Call this tool to check whether a candidate value is structurally compatible with a reference value, or meets explicit type/length/numeric constraints when no reference is given. Returns True if compatible, False otherwise. Use it before passing data to PsyNeuLink parameters that require specific shapes or numeric types.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "candidate": {\n      "description": "The value to check for compatibility. Can be a number, list, nested list, or dict.",\n      "oneOf": [\n        {\n          "type": "number"\n        },\n        {\n          "type": "array"\n        },\n        {\n          "type": "object"\n        },\n        {\n          "type": "string"\n        }\n      ]\n    },\n    "length": {\n      "description": "Required length for candidate. 0 means any length is accepted. If reference is also given, this overrides reference-derived length checking. Must be non-negative.",\n      "minimum": 0,\n      "type": "integer"\n    },\n    "number": {\n      "default": true,\n      "description": "If true (default), candidate must be numeric or a list/tuple of numerics. If false, strings, lists of strings, and dicts are also accepted.",\n      "type": "boolean"\n    },\n    "reference": {\n      "description": "Optional reference value. If provided, candidate must match its type and length (unless overridden by kargs). If omitted, candidate is checked against kargs constraints.",\n      "oneOf": [\n        {\n          "type": "number"\n        },\n        {\n          "type": "array"\n        },\n        {\n          "type": "object"\n        },\n        {\n          "type": "string"\n        }\n      ]\n    }\n  },\n  "required": [\n    "candidate"\n  ],\n  "type": "object"\n}\n\nNotes:\nThe `type` kwarg (kwCompatibilityType) accepts a Python type object and cannot be serialized over JSON/MCP — omit it; the tool will default to `list` as the match type when no reference is given. When `reference` is provided, the match type is automatically derived from `type(reference)`, ignoring the `type` kwarg. Silent defaults: if `length` is omitted and reference is provided, candidate must match reference length; if both are omitted, any length is accepted. Numbers and 0-dim ndarrays short-circuit to True regardless of other constraints. Enums are treated as numbers unless `kwCompatibilityType=Enum` is explicitly set (not available via JSON). A negative `length` value triggers a warning and is silently coerced to 0.'
TOOL_PARAMETERS = { 'properties': { 'candidate': { 'description': 'The value to check for compatibility. '
                                                'Can be a number, list, nested list, '
                                                'or dict.',
                                 'oneOf': [ {'type': 'number'},
                                            {'type': 'array'},
                                            {'type': 'object'},
                                            {'type': 'string'}]},
                  'length': { 'description': 'Required length for candidate. 0 means '
                                             'any length is accepted. If reference is '
                                             'also given, this overrides '
                                             'reference-derived length checking. Must '
                                             'be non-negative.',
                              'minimum': 0,
                              'type': 'integer'},
                  'number': { 'default': True,
                              'description': 'If true (default), candidate must be '
                                             'numeric or a list/tuple of numerics. If '
                                             'false, strings, lists of strings, and '
                                             'dicts are also accepted.',
                              'type': 'boolean'},
                  'reference': { 'description': 'Optional reference value. If '
                                                'provided, candidate must match its '
                                                'type and length (unless overridden by '
                                                'kargs). If omitted, candidate is '
                                                'checked against kargs constraints.',
                                 'oneOf': [ {'type': 'number'},
                                            {'type': 'array'},
                                            {'type': 'object'},
                                            {'type': 'string'}]}},
  'required': ['candidate'],
  'type': 'object'}
TOOL_NOTES = 'The `type` kwarg (kwCompatibilityType) accepts a Python type object and cannot be serialized over JSON/MCP — omit it; the tool will default to `list` as the match type when no reference is given. When `reference` is provided, the match type is automatically derived from `type(reference)`, ignoring the `type` kwarg. Silent defaults: if `length` is omitted and reference is provided, candidate must match reference length; if both are omitted, any length is accepted. Numbers and 0-dim ndarrays short-circuit to True regardless of other constraints. Enums are treated as numbers unless `kwCompatibilityType=Enum` is explicitly set (not available via JSON). A negative `length` value triggers a warning and is silently coerced to 0.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.iscompatible
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
    def iscompatible(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to check whether a candidate value is structurally compatible with a reference value, or meets explicit type/length/numeric constraints when no reference is given.'
        return _impl(args or {})
