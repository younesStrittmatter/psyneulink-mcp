"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '32fe8c2360eee0e798cf82d9ad8a653f43903a507ac6e3871319c4a86f542d3f'
__pnl_qualname__ = 'psyneulink.MemoryFunction'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_memory_function'
TOOL_DESCRIPTION = 'Use this tool to instantiate a `psyneulink.MemoryFunction` — the abstract base class for stateful memory functions whose output depends on stored previous values. Call it when you need to reference or subclass the MemoryFunction type directly; in most modeling cases you will want a concrete subclass (e.g. `DictionaryMemory`, `ContentAddressableMemory`) instead. Returns a MemoryFunction instance configured with the given initialization, rate, and noise parameters.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "default_variable": {\n      "description": "Template for the input variable. Accepts a number, list, or array. Sets the shape expectation for all subsequent calls.",\n      "oneOf": [\n        {\n          "type": "number"\n        },\n        {\n          "items": {\n            "type": "number"\n          },\n          "type": "array"\n        }\n      ]\n    },\n    "initializer": {\n      "description": "Initial value for `previous_value`. If a float or single-element array, applied to every element. If a list or array, must match the length of `default_variable`.",\n      "oneOf": [\n        {\n          "type": "number"\n        },\n        {\n          "items": {\n            "type": "number"\n          },\n          "type": "array"\n        }\n      ]\n    },\n    "name": {\n      "description": "Name for this function instance. If omitted, FunctionRegistry assigns a default.",\n      "type": "string"\n    },\n    "noise": {\n      "default": 0,\n      "description": "Random offset added on each call. Float or array of floats produce a fixed offset; pass a PsyNeuLink DistributionFunction name/spec to get per-execution random noise.",\n      "oneOf": [\n        {\n          "type": "number"\n        },\n        {\n          "items": {\n            "type": "number"\n          },\n          "type": "array"\n        }\n      ]\n    },\n    "params": {\n      "additionalProperties": true,\n      "description": "Optional parameter dictionary (ParameterPort-style). Values here override constructor arguments.",\n      "type": "object"\n    },\n    "rate": {\n      "default": 1,\n      "description": "Scaling parameter applied each call in a subclass-dependent manner. Float applies uniformly; array applies elementwise and must match `default_variable` length.",\n      "oneOf": [\n        {\n          "type": "number"\n        },\n        {\n          "items": {\n            "type": "number"\n          },\n          "type": "array"\n        }\n      ]\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\n`MemoryFunction` is an abstract base class; direct instantiation is possible but usually not the right choice — prefer a concrete subclass such as `DictionaryMemory` or `ContentAddressableMemory`. The `_update_default_variable` override silently initializes `previous_value` to a zero array shaped like `default_variable` whenever `initializer` has not been explicitly set by the user, so changing `default_variable` after construction resets state. `noise` only generates a `ParameterPort` (and thus becomes truly stateful/randomizable at runtime) if its value is entirely numeric at construction time — passing a function object suppresses the port. The `owner` and `prefs` arguments are Component-level wiring and are rarely needed when constructing a function standalone.'
TOOL_PARAMETERS = { 'properties': { 'default_variable': { 'description': 'Template for the input '
                                                       'variable. Accepts a number, '
                                                       'list, or array. Sets the shape '
                                                       'expectation for all subsequent '
                                                       'calls.',
                                        'oneOf': [ {'type': 'number'},
                                                   { 'items': {'type': 'number'},
                                                     'type': 'array'}]},
                  'initializer': { 'description': 'Initial value for `previous_value`. '
                                                  'If a float or single-element array, '
                                                  'applied to every element. If a list '
                                                  'or array, must match the length of '
                                                  '`default_variable`.',
                                   'oneOf': [ {'type': 'number'},
                                              { 'items': {'type': 'number'},
                                                'type': 'array'}]},
                  'name': { 'description': 'Name for this function instance. If '
                                           'omitted, FunctionRegistry assigns a '
                                           'default.',
                            'type': 'string'},
                  'noise': { 'default': 0,
                             'description': 'Random offset added on each call. Float '
                                            'or array of floats produce a fixed '
                                            'offset; pass a PsyNeuLink '
                                            'DistributionFunction name/spec to get '
                                            'per-execution random noise.',
                             'oneOf': [ {'type': 'number'},
                                        { 'items': {'type': 'number'},
                                          'type': 'array'}]},
                  'params': { 'additionalProperties': True,
                              'description': 'Optional parameter dictionary '
                                             '(ParameterPort-style). Values here '
                                             'override constructor arguments.',
                              'type': 'object'},
                  'rate': { 'default': 1,
                            'description': 'Scaling parameter applied each call in a '
                                           'subclass-dependent manner. Float applies '
                                           'uniformly; array applies elementwise and '
                                           'must match `default_variable` length.',
                            'oneOf': [ {'type': 'number'},
                                       { 'items': {'type': 'number'},
                                         'type': 'array'}]}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = '`MemoryFunction` is an abstract base class; direct instantiation is possible but usually not the right choice — prefer a concrete subclass such as `DictionaryMemory` or `ContentAddressableMemory`. The `_update_default_variable` override silently initializes `previous_value` to a zero array shaped like `default_variable` whenever `initializer` has not been explicitly set by the user, so changing `default_variable` after construction resets state. `noise` only generates a `ParameterPort` (and thus becomes truly stateful/randomizable at runtime) if its value is entirely numeric at construction time — passing a function object suppresses the port. The `owner` and `prefs` arguments are Component-level wiring and are rarely needed when constructing a function standalone.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.MemoryFunction
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
    def create_memory_function(args: dict[str, Any] | None = None) -> Any:
        'Use this tool to instantiate a `psyneulink.MemoryFunction` — the abstract base class for stateful memory functions whose output depends on stored previous values.'
        return _impl(args or {})
