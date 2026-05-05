"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '5cc1a1087d9a6d098233eb522e02f5995f6a2373adc7c34c60004f31d675f0b7'
__pnl_qualname__ = 'psyneulink.create_union_set'
__pnl_kind__ = 'function'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_union_set'
TOOL_DESCRIPTION = 'Call this tool when you need to merge multiple collections or scalar values into a single deduplicated set. Pass any mix of lists, sets, or individual values; the tool flattens all iterables and returns one flat set. Useful for combining overlapping node sets, parameter groups, or mixed scalar/collection inputs before passing them to a PsyNeuLink component.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "args": {\n      "description": "List of items to union into a single set. Each element may be a scalar (string, number, boolean) or an array/list \\u2014 arrays are expanded and their elements added individually. Strings are treated as scalars, not expanded character-by-character.",\n      "items": {\n        "oneOf": [\n          {\n            "type": "string"\n          },\n          {\n            "type": "number"\n          },\n          {\n            "type": "boolean"\n          },\n          {\n            "items": {\n              "oneOf": [\n                {\n                  "type": "string"\n                },\n                {\n                  "type": "number"\n                },\n                {\n                  "type": "boolean"\n                }\n              ]\n            },\n            "type": "array"\n          }\n        ]\n      },\n      "type": "array"\n    }\n  },\n  "required": [\n    "args"\n  ],\n  "type": "object"\n}\n\nNotes:\nThe function signature is `*args`, not keyword args. The host template must unpack the `args` list with `*` when calling `create_union_set(*args)`. Strings are explicitly excluded from iterable expansion — passing `"abc"` adds the string `"abc"` as one element, not `"a"`, `"b"`, `"c"`. Only one level of nesting is flattened (the function unions each top-level item\'s members, but does not recurse into nested arrays within an array element). The return value is a Python `set` — order is not preserved.'
TOOL_PARAMETERS = { 'properties': { 'args': { 'description': 'List of items to union into a single set. '
                                           'Each element may be a scalar (string, '
                                           'number, boolean) or an array/list — arrays '
                                           'are expanded and their elements added '
                                           'individually. Strings are treated as '
                                           'scalars, not expanded '
                                           'character-by-character.',
                            'items': { 'oneOf': [ {'type': 'string'},
                                                  {'type': 'number'},
                                                  {'type': 'boolean'},
                                                  { 'items': { 'oneOf': [ { 'type': 'string'},
                                                                          { 'type': 'number'},
                                                                          { 'type': 'boolean'}]},
                                                    'type': 'array'}]},
                            'type': 'array'}},
  'required': ['args'],
  'type': 'object'}
TOOL_NOTES = 'The function signature is `*args`, not keyword args. The host template must unpack the `args` list with `*` when calling `create_union_set(*args)`. Strings are explicitly excluded from iterable expansion — passing `"abc"` adds the string `"abc"` as one element, not `"a"`, `"b"`, `"c"`. Only one level of nesting is flattened (the function unions each top-level item\'s members, but does not recurse into nested arrays within an array element). The return value is a Python `set` — order is not preserved.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.create_union_set
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
    def create_union_set(args: dict[str, Any] | None = None) -> Any:
        'Call this tool when you need to merge multiple collections or scalar values into a single deduplicated set.'
        return _impl(args or {})
