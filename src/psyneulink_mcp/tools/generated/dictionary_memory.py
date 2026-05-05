"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '92fa5d92296af6e01375db76a3d5466b2864d382cf90cb80f56c12545942a1cf'
__pnl_qualname__ = 'psyneulink.DictionaryMemory'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_dictionary_memory'
TOOL_DESCRIPTION = 'Use this tool to instantiate a DictionaryMemory function — a configurable associative memory that stores key-value pairs and retrieves them by similarity. Call it when building a mechanism that needs content-addressable memory: the function retrieves the best-matching stored entry (by key similarity), then stores the new key-value pair, and returns the previously retrieved entry. Returns a 2d array [[retrieved_key], [retrieved_value]], or zeros if memory is empty or retrieval is suppressed by probability.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "default_variable": {\n      "description": "Template for key and value entries: a 2-item list [[key_template], [value_template]]. Sets expected key and value lengths. Keys must all be the same length across all entries.",\n      "items": {\n        "items": {\n          "type": "number"\n        },\n        "type": "array"\n      },\n      "type": "array"\n    },\n    "distance_function": {\n      "description": "Name or specification of the function used to compare a query key against stored keys during retrieval. Default is Distance with COSINE metric. Must return a scalar per comparison.",\n      "type": "string"\n    },\n    "duplicate_keys": {\n      "default": false,\n      "description": "Controls behavior when storing a key that already exists in memory. False (default): skip storage and return existing entry. True: allow multiple entries with the same key. \'overwrite\': replace the existing entry\'s value.",\n      "oneOf": [\n        {\n          "type": "boolean"\n        },\n        {\n          "enum": [\n            "overwrite"\n          ],\n          "type": "string"\n        }\n      ]\n    },\n    "equidistant_keys_select": {\n      "default": "random",\n      "description": "Tiebreaking policy when two or more stored keys are equidistant from the query key. \'random\' picks one at random, \'oldest\' picks the first stored, \'newest\' picks the most recently stored. Default \'random\'.",\n      "enum": [\n        "random",\n        "oldest",\n        "newest"\n      ],\n      "type": "string"\n    },\n    "initializer": {\n      "description": "Initial memory contents as a list of key-value pairs: [[[key1],[value1]], [[key2],[value2]], ...]. All keys must be 1d arrays of the same length. Default None (empty memory).",\n      "items": {\n        "items": {\n          "items": {\n            "type": "number"\n          },\n          "type": "array"\n        },\n        "type": "array"\n      },\n      "type": "array"\n    },\n    "max_entries": {\n      "description": "Maximum number of entries retained in memory. When exceeded, the oldest entry is deleted. Default None uses an internal limit of 1000.",\n      "minimum": 1,\n      "type": "integer"\n    },\n    "name": {\n      "description": "Name for this DictionaryMemory instance. Auto-assigned from FunctionRegistry if omitted.",\n      "type": "string"\n    },\n    "noise": {\n      "default": 0,\n      "description": "Additive noise applied to the key before storage (key * rate + noise). Does not affect the value. Default 0.0.",\n      "oneOf": [\n        {\n          "type": "number"\n        },\n        {\n          "items": {\n            "type": "number"\n          },\n          "type": "array"\n        }\n      ]\n    },\n    "params": {\n      "description": "Optional parameter dictionary to override constructor arguments. Keys are parameter names, values override the corresponding arguments.",\n      "type": "object"\n    },\n    "rate": {\n      "default": 1,\n      "description": "Multiplicative scaling applied to the key before storage (key * rate). Does not affect retrieval or the stored value. Default 1.0 (no scaling).",\n      "oneOf": [\n        {\n          "type": "number"\n        },\n        {\n          "items": {\n            "type": "number"\n          },\n          "type": "array"\n        }\n      ]\n    },\n    "retrieval_prob": {\n      "default": 1,\n      "description": "Probability in [0, 1] of retrieving a matching entry on each call. Default 1.0 (always retrieve). When retrieval is skipped, returns a zero-valued array.",\n      "maximum": 1,\n      "minimum": 0,\n      "type": "number"\n    },\n    "selection_function": {\n      "description": "Name or specification of the function that selects which entry to retrieve from the list of distances. Default is OneHot with MIN_VAL mode (selects the closest entry).",\n      "type": "string"\n    },\n    "storage_prob": {\n      "default": 1,\n      "description": "Probability in [0, 1] of storing the input key-value pair on each call. Default 1.0 (always store).",\n      "maximum": 1,\n      "minimum": 0,\n      "type": "number"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\nExecution order matters: retrieval happens BEFORE storage on every call, so the returned value is the previously best-matching entry, not the entry just stored. If memory is empty or retrieval is probabilistically skipped, a zero-valued array of the correct shape is returned — not None or an error.\n\nnoise and rate are applied to the KEY only before storing, not to the value. The formula is: stored_key = key * rate + noise.\n\nduplicate_keys=False (default) silently skips storage when an identical key already exists; it does NOT raise an error. If you need idempotent writes, use \'overwrite\'.\n\nmax_entries defaults to None in the constructor but the internal default is 1000; always specify explicitly for bounded-memory use cases.\n\ninitializer must be a 3d structure [[[key],[value]], ...] — a flat list of two arrays [[key],[value]] is interpreted as a single entry, not two entries.\n\ndistance_function and selection_function accept PsyNeuLink Function instances or callables, not plain strings — the string fields above are for naming/reference only; pass actual Function objects when constructing programmatically.\n\nWhen duplicate_keys transitions from True to False after entries are already stored, retrieval of a key with duplicates will issue a warning and return zeros.'
TOOL_PARAMETERS = { 'properties': { 'default_variable': { 'description': 'Template for key and value '
                                                       'entries: a 2-item list '
                                                       '[[key_template], '
                                                       '[value_template]]. Sets '
                                                       'expected key and value '
                                                       'lengths. Keys must all be the '
                                                       'same length across all '
                                                       'entries.',
                                        'items': { 'items': {'type': 'number'},
                                                   'type': 'array'},
                                        'type': 'array'},
                  'distance_function': { 'description': 'Name or specification of the '
                                                        'function used to compare a '
                                                        'query key against stored keys '
                                                        'during retrieval. Default is '
                                                        'Distance with COSINE metric. '
                                                        'Must return a scalar per '
                                                        'comparison.',
                                         'type': 'string'},
                  'duplicate_keys': { 'default': False,
                                      'description': 'Controls behavior when storing a '
                                                     'key that already exists in '
                                                     'memory. False (default): skip '
                                                     'storage and return existing '
                                                     'entry. True: allow multiple '
                                                     'entries with the same key. '
                                                     "'overwrite': replace the "
                                                     "existing entry's value.",
                                      'oneOf': [ {'type': 'boolean'},
                                                 { 'enum': ['overwrite'],
                                                   'type': 'string'}]},
                  'equidistant_keys_select': { 'default': 'random',
                                               'description': 'Tiebreaking policy when '
                                                              'two or more stored keys '
                                                              'are equidistant from '
                                                              "the query key. 'random' "
                                                              'picks one at random, '
                                                              "'oldest' picks the "
                                                              "first stored, 'newest' "
                                                              'picks the most recently '
                                                              'stored. Default '
                                                              "'random'.",
                                               'enum': ['random', 'oldest', 'newest'],
                                               'type': 'string'},
                  'initializer': { 'description': 'Initial memory contents as a list '
                                                  'of key-value pairs: '
                                                  '[[[key1],[value1]], '
                                                  '[[key2],[value2]], ...]. All keys '
                                                  'must be 1d arrays of the same '
                                                  'length. Default None (empty '
                                                  'memory).',
                                   'items': { 'items': { 'items': {'type': 'number'},
                                                         'type': 'array'},
                                              'type': 'array'},
                                   'type': 'array'},
                  'max_entries': { 'description': 'Maximum number of entries retained '
                                                  'in memory. When exceeded, the '
                                                  'oldest entry is deleted. Default '
                                                  'None uses an internal limit of '
                                                  '1000.',
                                   'minimum': 1,
                                   'type': 'integer'},
                  'name': { 'description': 'Name for this DictionaryMemory instance. '
                                           'Auto-assigned from FunctionRegistry if '
                                           'omitted.',
                            'type': 'string'},
                  'noise': { 'default': 0,
                             'description': 'Additive noise applied to the key before '
                                            'storage (key * rate + noise). Does not '
                                            'affect the value. Default 0.0.',
                             'oneOf': [ {'type': 'number'},
                                        { 'items': {'type': 'number'},
                                          'type': 'array'}]},
                  'params': { 'description': 'Optional parameter dictionary to '
                                             'override constructor arguments. Keys are '
                                             'parameter names, values override the '
                                             'corresponding arguments.',
                              'type': 'object'},
                  'rate': { 'default': 1,
                            'description': 'Multiplicative scaling applied to the key '
                                           'before storage (key * rate). Does not '
                                           'affect retrieval or the stored value. '
                                           'Default 1.0 (no scaling).',
                            'oneOf': [ {'type': 'number'},
                                       {'items': {'type': 'number'}, 'type': 'array'}]},
                  'retrieval_prob': { 'default': 1,
                                      'description': 'Probability in [0, 1] of '
                                                     'retrieving a matching entry on '
                                                     'each call. Default 1.0 (always '
                                                     'retrieve). When retrieval is '
                                                     'skipped, returns a zero-valued '
                                                     'array.',
                                      'maximum': 1,
                                      'minimum': 0,
                                      'type': 'number'},
                  'selection_function': { 'description': 'Name or specification of the '
                                                         'function that selects which '
                                                         'entry to retrieve from the '
                                                         'list of distances. Default '
                                                         'is OneHot with MIN_VAL mode '
                                                         '(selects the closest entry).',
                                          'type': 'string'},
                  'storage_prob': { 'default': 1,
                                    'description': 'Probability in [0, 1] of storing '
                                                   'the input key-value pair on each '
                                                   'call. Default 1.0 (always store).',
                                    'maximum': 1,
                                    'minimum': 0,
                                    'type': 'number'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = "Execution order matters: retrieval happens BEFORE storage on every call, so the returned value is the previously best-matching entry, not the entry just stored. If memory is empty or retrieval is probabilistically skipped, a zero-valued array of the correct shape is returned — not None or an error.\n\nnoise and rate are applied to the KEY only before storing, not to the value. The formula is: stored_key = key * rate + noise.\n\nduplicate_keys=False (default) silently skips storage when an identical key already exists; it does NOT raise an error. If you need idempotent writes, use 'overwrite'.\n\nmax_entries defaults to None in the constructor but the internal default is 1000; always specify explicitly for bounded-memory use cases.\n\ninitializer must be a 3d structure [[[key],[value]], ...] — a flat list of two arrays [[key],[value]] is interpreted as a single entry, not two entries.\n\ndistance_function and selection_function accept PsyNeuLink Function instances or callables, not plain strings — the string fields above are for naming/reference only; pass actual Function objects when constructing programmatically.\n\nWhen duplicate_keys transitions from True to False after entries are already stored, retrieval of a key with duplicates will issue a warning and return zeros."


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.DictionaryMemory
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
    def create_dictionary_memory(args: dict[str, Any] | None = None) -> Any:
        'Use this tool to instantiate a DictionaryMemory function — a configurable associative memory that stores key-value pairs and retrieves them by similarity.'
        return _impl(args or {})
