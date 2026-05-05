"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '3a39536c71e7603c685ce75cec38d12b36174d4d0f1b2ae5a66ad3caf3c738ce'
__pnl_qualname__ = 'psyneulink.EpisodicMemoryMechanism'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_episodic_memory_mechanism'
TOOL_DESCRIPTION = 'Call this tool to create a content-addressable episodic memory component that stores multi-field memory entries and retrieves the closest match to a query by distance/similarity. The resulting mechanism has one InputPort per memory field (named FIELD_n_INPUT by default) and returns the retrieved entry\'s fields via corresponding OutputPorts. Use it when building recall-based neural models where stored episodes need to be retrieved by partial cues.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "default_variable": {\n      "description": "Template defining the field structure of memory entries. Each element defines one field; e.g. [[0,0],[0,0,0]] creates a 2-field memory with fields of length 2 and 3. Defaults to [[0,0]] (single 2-element field).",\n      "items": {\n        "items": {\n          "type": "number"\n        },\n        "type": "array"\n      },\n      "type": "array"\n    },\n    "function": {\n      "description": "MemoryFunction class name to use for storage and retrieval (e.g. \'ContentAddressableMemory\'). Defaults to ContentAddressableMemory, which retrieves entries by distance metric. Pass \'DictionaryMemory\' only for legacy compatibility.",\n      "type": "string"\n    },\n    "input_shapes": {\n      "description": "Alternative way to specify field sizes as integer(s) or list of integers instead of providing a full default_variable template.",\n      "oneOf": [\n        {\n          "type": "integer"\n        },\n        {\n          "items": {\n            "type": "integer"\n          },\n          "type": "array"\n        }\n      ]\n    },\n    "memory": {\n      "description": "Initial set of entries to pre-populate memory. Must be a 3d array (entries \\u00d7 fields \\u00d7 values) or a 2d ragged array when fields have different lengths. Each entry must match the shape defined by default_variable.",\n      "items": {\n        "items": {\n          "items": {\n            "type": "number"\n          },\n          "type": "array"\n        },\n        "type": "array"\n      },\n      "type": "array"\n    },\n    "name": {\n      "description": "Name for the mechanism instance.",\n      "type": "string"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\n- The number of InputPorts and OutputPorts is determined by the number of fields in each memory entry (i.e., length of default_variable). Plan your composition wiring accordingly before instantiation.\n- `memory` is passed as the `initializer` argument to the underlying MemoryFunction, not directly to the class; shape mismatches between `memory[0]` and `default_variable` raise an error at construction time.\n- `DictionaryMemory` as the function is legacy/deprecated; prefer the default `ContentAddressableMemory`.\n- If both `default_variable` and `memory` are provided, their entry shapes must match exactly or construction fails.\n- Default `default_variable` is `[[0,0]]`, yielding a single 2-element field and thus one InputPort and one OutputPort.\n- OutputPort values reflect the last *retrieved* entry, not the entry just stored.'
TOOL_PARAMETERS = { 'properties': { 'default_variable': { 'description': 'Template defining the field '
                                                       'structure of memory entries. '
                                                       'Each element defines one '
                                                       'field; e.g. [[0,0],[0,0,0]] '
                                                       'creates a 2-field memory with '
                                                       'fields of length 2 and 3. '
                                                       'Defaults to [[0,0]] (single '
                                                       '2-element field).',
                                        'items': { 'items': {'type': 'number'},
                                                   'type': 'array'},
                                        'type': 'array'},
                  'function': { 'description': 'MemoryFunction class name to use for '
                                               'storage and retrieval (e.g. '
                                               "'ContentAddressableMemory'). Defaults "
                                               'to ContentAddressableMemory, which '
                                               'retrieves entries by distance metric. '
                                               "Pass 'DictionaryMemory' only for "
                                               'legacy compatibility.',
                                'type': 'string'},
                  'input_shapes': { 'description': 'Alternative way to specify field '
                                                   'sizes as integer(s) or list of '
                                                   'integers instead of providing a '
                                                   'full default_variable template.',
                                    'oneOf': [ {'type': 'integer'},
                                               { 'items': {'type': 'integer'},
                                                 'type': 'array'}]},
                  'memory': { 'description': 'Initial set of entries to pre-populate '
                                             'memory. Must be a 3d array (entries × '
                                             'fields × values) or a 2d ragged array '
                                             'when fields have different lengths. Each '
                                             'entry must match the shape defined by '
                                             'default_variable.',
                              'items': { 'items': { 'items': {'type': 'number'},
                                                    'type': 'array'},
                                         'type': 'array'},
                              'type': 'array'},
                  'name': { 'description': 'Name for the mechanism instance.',
                            'type': 'string'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = '- The number of InputPorts and OutputPorts is determined by the number of fields in each memory entry (i.e., length of default_variable). Plan your composition wiring accordingly before instantiation.\n- `memory` is passed as the `initializer` argument to the underlying MemoryFunction, not directly to the class; shape mismatches between `memory[0]` and `default_variable` raise an error at construction time.\n- `DictionaryMemory` as the function is legacy/deprecated; prefer the default `ContentAddressableMemory`.\n- If both `default_variable` and `memory` are provided, their entry shapes must match exactly or construction fails.\n- Default `default_variable` is `[[0,0]]`, yielding a single 2-element field and thus one InputPort and one OutputPort.\n- OutputPort values reflect the last *retrieved* entry, not the entry just stored.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.EpisodicMemoryMechanism
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
    def create_episodic_memory_mechanism(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to create a content-addressable episodic memory component that stores multi-field memory entries and retrieves the closest match to a query by distance/similarity.'
        return _impl(args or {})
