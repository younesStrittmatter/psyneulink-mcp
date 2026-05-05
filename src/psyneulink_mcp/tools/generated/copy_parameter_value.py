"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = 'f07248bb56480700d6fef9243dad2e400eca6b1bcde6d020db48999cbed1e8ac'
__pnl_qualname__ = 'psyneulink.core.components.functions.nonstateful.objectivefunctions.copy_parameter_value'
__pnl_kind__ = 'function'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'copy_parameter_value'
TOOL_DESCRIPTION = 'Call this tool when you need a safe, independent copy of a PsyNeuLink parameter value or specification (e.g., a weight matrix, port spec list, or numeric default). Unlike a raw deepcopy, it correctly treats Component references inside iterables as pointers rather than cloning them, preventing accidental shared-state bugs. The result is the copied value, or the original value unchanged if deepcopy fails due to an unpicklable type.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "shared_types": {\n      "description": "Optional list of fully-qualified Python type names (as strings) to treat as shared references rather than deep-copied instances. Defaults to (Component, ComponentsMeta) if omitted.",\n      "items": {\n        "type": "string"\n      },\n      "type": "array"\n    },\n    "value": {\n      "description": "The parameter value or spec to copy. May be a number, string, boolean, array, dict, or a nested structure. Component references inside iterables are preserved as pointers rather than cloned.",\n      "oneOf": [\n        {\n          "type": "number"\n        },\n        {\n          "type": "string"\n        },\n        {\n          "type": "boolean"\n        },\n        {\n          "type": "array"\n        },\n        {\n          "type": "object"\n        }\n      ]\n    }\n  },\n  "required": [\n    "value"\n  ],\n  "type": "object"\n}\n\nNotes:\n- The `memo` parameter is an internal deepcopy memo dict; agents should never pass it.\n- If deepcopy raises a TypeError mentioning \'pickle\', the original value is returned silently instead of raising — callers cannot distinguish a failed copy from a successful one in that case.\n- Bound methods whose `__self__` is a Component are always treated as references (not cloned), regardless of `shared_types`.\n- `shared_types` is most useful when you have custom subclasses that should behave like Component pointers but are not subclasses of Component or ComponentsMeta.'
TOOL_PARAMETERS = { 'properties': { 'shared_types': { 'description': 'Optional list of fully-qualified '
                                                   'Python type names (as strings) to '
                                                   'treat as shared references rather '
                                                   'than deep-copied instances. '
                                                   'Defaults to (Component, '
                                                   'ComponentsMeta) if omitted.',
                                    'items': {'type': 'string'},
                                    'type': 'array'},
                  'value': { 'description': 'The parameter value or spec to copy. May '
                                            'be a number, string, boolean, array, '
                                            'dict, or a nested structure. Component '
                                            'references inside iterables are preserved '
                                            'as pointers rather than cloned.',
                             'oneOf': [ {'type': 'number'},
                                        {'type': 'string'},
                                        {'type': 'boolean'},
                                        {'type': 'array'},
                                        {'type': 'object'}]}},
  'required': ['value'],
  'type': 'object'}
TOOL_NOTES = "- The `memo` parameter is an internal deepcopy memo dict; agents should never pass it.\n- If deepcopy raises a TypeError mentioning 'pickle', the original value is returned silently instead of raising — callers cannot distinguish a failed copy from a successful one in that case.\n- Bound methods whose `__self__` is a Component are always treated as references (not cloned), regardless of `shared_types`.\n- `shared_types` is most useful when you have custom subclasses that should behave like Component pointers but are not subclasses of Component or ComponentsMeta."


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.copy_parameter_value
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
    def copy_parameter_value(args: dict[str, Any] | None = None) -> Any:
        'Call this tool when you need a safe, independent copy of a PsyNeuLink parameter value or specification (e.g., a weight matrix, port spec list, or numeric default).'
        return _impl(args or {})
