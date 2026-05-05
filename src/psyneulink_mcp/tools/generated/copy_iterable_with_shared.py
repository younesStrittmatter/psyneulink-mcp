"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = 'ad547fc93305631fdc6ce172eb0f1a21c76cd0918abb63948405b80f99801b07'
__pnl_qualname__ = 'psyneulink.copy_iterable_with_shared'
__pnl_kind__ = 'function'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'copy_iterable_with_shared'
TOOL_DESCRIPTION = 'Call this tool to perform a selective deep-copy of a nested iterable (dict, list, tuple, set, or numpy object array) where objects belonging to specified types are kept as shared references instead of being deep-copied. Use it when you need a structurally independent copy of a container hierarchy but want certain object types (e.g., PsyNeuLink Components) to remain aliased across the original and the copy. Returns the same container type as the input with values either deep-copied or shared according to shared_types.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "memo": {\n      "additionalProperties": true,\n      "description": "Optional memoization dict passed through to copy.deepcopy to prevent duplicate copies of the same object. Leave unset in most cases.",\n      "type": "object"\n    },\n    "obj": {\n      "description": "The iterable to copy. Must be a dict, list, tuple, set, deque, or numpy object array. Raises TypeError for all other types.",\n      "type": "object"\n    },\n    "shared_types": {\n      "description": "Fully-qualified name of a single Python type (e.g. \'psyneulink.Component\') whose instances should be shared (not deep-copied). To pass multiple types, use a comma-separated string and note that the host must resolve these to actual type objects. Defaults to NoneType, meaning nothing is shared and all values are deep-copied.",\n      "type": "string"\n    }\n  },\n  "required": [\n    "obj"\n  ],\n  "type": "object"\n}\n\nNotes:\nThis is a low-level internal utility; most agents will never need to call it directly — prefer higher-level PsyNeuLink copy or clone operations. The function raises TypeError (not a graceful error) if obj is not one of the supported iterable types. shared_types defaults to type(None) (NoneType), which means in practice nothing is shared and every value is deep-copied — pass the actual type(s) you want shared or the default gives no sharing benefit. namedtuple and WeakKeyDictionary/WeakValueDictionary/WeakSet are supported but the copy preserves the concrete subclass. For numpy arrays, only dtype==object arrays are handled recursively; numeric arrays are not supported and will raise TypeError.'
TOOL_PARAMETERS = { 'properties': { 'memo': { 'additionalProperties': True,
                            'description': 'Optional memoization dict passed through '
                                           'to copy.deepcopy to prevent duplicate '
                                           'copies of the same object. Leave unset in '
                                           'most cases.',
                            'type': 'object'},
                  'obj': { 'description': 'The iterable to copy. Must be a dict, list, '
                                          'tuple, set, deque, or numpy object array. '
                                          'Raises TypeError for all other types.',
                           'type': 'object'},
                  'shared_types': { 'description': 'Fully-qualified name of a single '
                                                   'Python type (e.g. '
                                                   "'psyneulink.Component') whose "
                                                   'instances should be shared (not '
                                                   'deep-copied). To pass multiple '
                                                   'types, use a comma-separated '
                                                   'string and note that the host must '
                                                   'resolve these to actual type '
                                                   'objects. Defaults to NoneType, '
                                                   'meaning nothing is shared and all '
                                                   'values are deep-copied.',
                                    'type': 'string'}},
  'required': ['obj'],
  'type': 'object'}
TOOL_NOTES = 'This is a low-level internal utility; most agents will never need to call it directly — prefer higher-level PsyNeuLink copy or clone operations. The function raises TypeError (not a graceful error) if obj is not one of the supported iterable types. shared_types defaults to type(None) (NoneType), which means in practice nothing is shared and every value is deep-copied — pass the actual type(s) you want shared or the default gives no sharing benefit. namedtuple and WeakKeyDictionary/WeakValueDictionary/WeakSet are supported but the copy preserves the concrete subclass. For numpy arrays, only dtype==object arrays are handled recursively; numeric arrays are not supported and will raise TypeError.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.copy_iterable_with_shared
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
    def copy_iterable_with_shared(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to perform a selective deep-copy of a nested iterable (dict, list, tuple, set, or numpy object array) where objects belonging to specified types are kept as shared references instead of being deep-copied.'
        return _impl(args or {})
