"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '1a8c9d72542b2262f17336d1bb46e14fddb186a0e36574f72b5d156d97cf1396'
__pnl_qualname__ = 'psyneulink.Buffer'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_buffer'
TOOL_DESCRIPTION = 'Call this tool to create a Buffer function that maintains a sliding-window deque of recent inputs — use it when a mechanism needs short-term memory of past values (e.g., recurrent signal history, temporal context windows, delay lines). Returns the updated deque with the new input right-appended; if history is set, older entries are dropped to maintain fixed length.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "default_variable": {\n      "description": "Template for the input shape. Each call appends a value of this shape to the deque. All subsequent inputs must match this shape.",\n      "oneOf": [\n        {\n          "type": "number"\n        },\n        {\n          "items": {\n            "type": "number"\n          },\n          "type": "array"\n        }\n      ]\n    },\n    "history": {\n      "description": "Maximum number of entries in the deque (maxlen). When a new item is appended and the deque is full, the oldest entry is dropped. If omitted, the deque grows indefinitely.",\n      "minimum": 1,\n      "type": "integer"\n    },\n    "initializer": {\n      "description": "Starting contents of the deque before any inputs arrive. Defaults to an empty list. Pass a list of values matching default_variable shape to pre-populate the buffer.",\n      "oneOf": [\n        {\n          "type": "number"\n        },\n        {\n          "items": {},\n          "type": "array"\n        }\n      ]\n    },\n    "name": {\n      "description": "Name for this Buffer instance. Auto-assigned if omitted.",\n      "type": "string"\n    },\n    "noise": {\n      "default": 0,\n      "description": "Scalar added to each already-stored item on every call. Applied after rate multiplication. Default 0.0.",\n      "type": "number"\n    },\n    "params": {\n      "description": "Optional parameter dictionary overriding constructor arguments at runtime.",\n      "type": "object"\n    },\n    "rate": {\n      "default": 1,\n      "description": "Multiplicative decay applied to all already-stored items on every call. Must be in [0, 1]. Values < 1 cause exponential decay of older entries. Default 1.0 (no decay).",\n      "oneOf": [\n        {\n          "maximum": 1,\n          "minimum": 0,\n          "type": "number"\n        },\n        {\n          "items": {\n            "maximum": 1,\n            "minimum": 0,\n            "type": "number"\n          },\n          "type": "array"\n        }\n      ]\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\n- `rate` and `noise` are applied to already-stored items on *every* call — effects accumulate exponentially over repeated calls; rate=0.9 over 10 steps leaves ~0.35 of original amplitude, not 0.1.\n- Every appended item must have the same shape as the first item ever stored (either from `initializer` or the first `variable` passed in); mismatched shapes will error.\n- `history=None` means unlimited growth — set it explicitly if memory footprint matters.\n- During initialization runs (`is_initializing=True`), the function returns `variable` directly without appending to the deque, so the deque stays empty until real execution begins.\n- `initializer` defaults to `[]` (empty array), not `None`; passing `None` is treated the same as `[]`.\n- `params` and `owner`/`prefs` are rarely needed by agents; omit unless attaching to a specific Component or overriding preferences.'
TOOL_PARAMETERS = { 'properties': { 'default_variable': { 'description': 'Template for the input shape. '
                                                       'Each call appends a value of '
                                                       'this shape to the deque. All '
                                                       'subsequent inputs must match '
                                                       'this shape.',
                                        'oneOf': [ {'type': 'number'},
                                                   { 'items': {'type': 'number'},
                                                     'type': 'array'}]},
                  'history': { 'description': 'Maximum number of entries in the deque '
                                              '(maxlen). When a new item is appended '
                                              'and the deque is full, the oldest entry '
                                              'is dropped. If omitted, the deque grows '
                                              'indefinitely.',
                               'minimum': 1,
                               'type': 'integer'},
                  'initializer': { 'description': 'Starting contents of the deque '
                                                  'before any inputs arrive. Defaults '
                                                  'to an empty list. Pass a list of '
                                                  'values matching default_variable '
                                                  'shape to pre-populate the buffer.',
                                   'oneOf': [ {'type': 'number'},
                                              {'items': {}, 'type': 'array'}]},
                  'name': { 'description': 'Name for this Buffer instance. '
                                           'Auto-assigned if omitted.',
                            'type': 'string'},
                  'noise': { 'default': 0,
                             'description': 'Scalar added to each already-stored item '
                                            'on every call. Applied after rate '
                                            'multiplication. Default 0.0.',
                             'type': 'number'},
                  'params': { 'description': 'Optional parameter dictionary overriding '
                                             'constructor arguments at runtime.',
                              'type': 'object'},
                  'rate': { 'default': 1,
                            'description': 'Multiplicative decay applied to all '
                                           'already-stored items on every call. Must '
                                           'be in [0, 1]. Values < 1 cause exponential '
                                           'decay of older entries. Default 1.0 (no '
                                           'decay).',
                            'oneOf': [ {'maximum': 1, 'minimum': 0, 'type': 'number'},
                                       { 'items': { 'maximum': 1,
                                                    'minimum': 0,
                                                    'type': 'number'},
                                         'type': 'array'}]}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = '- `rate` and `noise` are applied to already-stored items on *every* call — effects accumulate exponentially over repeated calls; rate=0.9 over 10 steps leaves ~0.35 of original amplitude, not 0.1.\n- Every appended item must have the same shape as the first item ever stored (either from `initializer` or the first `variable` passed in); mismatched shapes will error.\n- `history=None` means unlimited growth — set it explicitly if memory footprint matters.\n- During initialization runs (`is_initializing=True`), the function returns `variable` directly without appending to the deque, so the deque stays empty until real execution begins.\n- `initializer` defaults to `[]` (empty array), not `None`; passing `None` is treated the same as `[]`.\n- `params` and `owner`/`prefs` are rarely needed by agents; omit unless attaching to a specific Component or overriding preferences.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.Buffer
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
    def create_buffer(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to create a Buffer function that maintains a sliding-window deque of recent inputs — use it when a mechanism needs short-term memory of past values (e.g., recurrent signal history, temporal context windows, delay lines).'
        return _impl(args or {})
