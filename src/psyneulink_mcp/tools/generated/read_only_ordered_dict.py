"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = 'd28f557bc8e68722636f1b8a49c07778adc954fa22fa567e0c63822e6a308217'
__pnl_qualname__ = 'psyneulink.ReadOnlyOrderedDict'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_read_only_ordered_dict'
TOOL_DESCRIPTION = 'Call this tool to create a read-only, insertion-ordered dictionary snapshot from an existing mapping or keyword arguments. Use it when you need an immutable key-value store that preserves key order and must not be modified after creation. The result is a ReadOnlyOrderedDict instance whose keys() method returns keys in insertion order; any attempt to write, delete, clear, or pop entries will raise a UtilitiesError.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "dict": {\n      "description": "Initial mapping to populate the dictionary. Keys and values are copied in; insertion order is preserved.",\n      "type": "object"\n    },\n    "name": {\n      "description": "Human-readable label used in UtilitiesError messages when a write is attempted. Defaults to the class name if omitted.",\n      "type": "string"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\nThis class is strictly read-only after construction: __setitem__, __delitem__, clear, pop, and popitem all raise UtilitiesError. The internal __additem__ / __deleteitem__ methods bypass the restriction but are not part of the public interface and should not be called by agents. keys() returns insertion order (via _ordered_keys), not the standard dict key view — iterating over the instance directly may not respect that order. Passing additional kwargs to __init__ is forwarded to UserDict but their insertion order in _ordered_keys is not guaranteed relative to the \'dict\' argument.'
TOOL_PARAMETERS = { 'properties': { 'dict': { 'description': 'Initial mapping to populate the '
                                           'dictionary. Keys and values are copied in; '
                                           'insertion order is preserved.',
                            'type': 'object'},
                  'name': { 'description': 'Human-readable label used in '
                                           'UtilitiesError messages when a write is '
                                           'attempted. Defaults to the class name if '
                                           'omitted.',
                            'type': 'string'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = "This class is strictly read-only after construction: __setitem__, __delitem__, clear, pop, and popitem all raise UtilitiesError. The internal __additem__ / __deleteitem__ methods bypass the restriction but are not part of the public interface and should not be called by agents. keys() returns insertion order (via _ordered_keys), not the standard dict key view — iterating over the instance directly may not respect that order. Passing additional kwargs to __init__ is forwarded to UserDict but their insertion order in _ordered_keys is not guaranteed relative to the 'dict' argument."


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.ReadOnlyOrderedDict
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
    def create_read_only_ordered_dict(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to create a read-only, insertion-ordered dictionary snapshot from an existing mapping or keyword arguments.'
        return _impl(args or {})
