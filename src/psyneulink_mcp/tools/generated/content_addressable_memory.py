"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = 'db04cfd18ea6780395553755968c3a748e5a7f609c4979fbe92263fbb25e2aa6'
__pnl_qualname__ = 'psyneulink.library.components.mechanisms.processing.integrator.episodicmemorymechanism.ContentAddressableMemory'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_content_addressable_memory'
TOOL_DESCRIPTION = 'Call this tool to instantiate a ContentAddressableMemory function that stores and retrieves multi-field entries by content similarity. On each invocation it retrieves the closest-matching entry from its internal memory bank (cosine distance by default), then stores the input with probability storage_prob; returns the retrieved 2d array of fields, or a zero-valued array if memory is empty or retrieval is skipped. Use this when you need a key-value or episodic memory store where retrieval is driven by similarity rather than exact lookup.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "default_variable": {\n      "description": "Template for entry shape \\u2014 a list of fields, each a 1d list of numbers. E.g. [[0,0],[0,0,0]] creates a 2-field memory with field lengths 2 and 3. Overridden by initializer if both are provided.",\n      "items": {\n        "items": {\n          "type": "number"\n        },\n        "type": "array"\n      },\n      "type": "array"\n    },\n    "distance_field_weights": {\n      "description": "Per-field weights for distance computation. Length must equal the number of fields. Weight 0 marks a field as a label (excluded from distance). If all weights are identical, full-vector distance is used; otherwise field-wise weighted average. If all weights are 0, no retrieval occurs.",\n      "items": {\n        "type": "number"\n      },\n      "type": "array"\n    },\n    "duplicate_entries_allowed": {\n      "default": false,\n      "description": "Controls duplicate handling: false = skip storing duplicates (default), true = allow accumulation, \'OVERWRITE\' = replace matching entry. Duplicates are identified by distance_threshold.",\n      "oneOf": [\n        {\n          "type": "boolean"\n        },\n        {\n          "enum": [\n            "OVERWRITE"\n          ],\n          "type": "string"\n        }\n      ]\n    },\n    "duplicate_threshold": {\n      "default": 0,\n      "description": "Distance below which two entries are considered duplicates. Default 0 means exact matches only.",\n      "type": "number"\n    },\n    "equidistant_entries_select": {\n      "default": "RANDOM",\n      "description": "Which entry to return when multiple entries are equidistant from the cue.",\n      "enum": [\n        "RANDOM",\n        "OLDEST",\n        "NEWEST"\n      ],\n      "type": "string"\n    },\n    "initializer": {\n      "description": "Initial memory contents: a list of entries, each entry a list of 1d numeric fields. E.g. [[[1,2],[3,4]], [[5,6],[7,8]]]. Determines entry shape and overrides default_variable. All entries must have the same number of fields with matching field lengths.",\n      "items": {\n        "items": {\n          "items": {\n            "type": "number"\n          },\n          "type": "array"\n        },\n        "type": "array"\n      },\n      "type": "array"\n    },\n    "max_entries": {\n      "default": 1000,\n      "description": "Maximum number of entries in memory. When exceeded, the oldest entry is deleted.",\n      "type": "integer"\n    },\n    "noise": {\n      "default": 0,\n      "description": "Additive noise applied to the input before storage: stored_value = input * rate + noise.",\n      "type": "number"\n    },\n    "rate": {\n      "default": 1,\n      "description": "Multiplicative scaling applied to the input before storage: stored_value = input * rate + noise.",\n      "type": "number"\n    },\n    "retrieval_prob": {\n      "default": 1,\n      "description": "Probability [0,1] of performing a retrieval on each call. When skipped, returns a zero-valued array.",\n      "maximum": 1,\n      "minimum": 0,\n      "type": "number"\n    },\n    "seed": {\n      "description": "Random seed for reproducible probabilistic retrieval/storage decisions and equidistant tie-breaking.",\n      "type": "integer"\n    },\n    "storage_prob": {\n      "default": 1,\n      "description": "Probability [0,1] of storing the input in memory on each call. Does not affect initializer entries, which are always stored.",\n      "maximum": 1,\n      "minimum": 0,\n      "type": "number"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\nCRITICAL — do NOT pass `name`: ContentAddressableMemory.__init__() does not accept a `name` argument; passing it raises TypeError. If you need to label this function, store the reference under a variable name in your code instead.\n\nCRITICAL — do NOT pass `distance_function` or `selection_function` as strings: these parameters require actual PsyNeuLink object instances (e.g. Distance(metric=COSINE)), not string representations. Passing a string like \'Distance(metric=COSINE)\' raises BeartypeCallHintParamViolation. Omit these parameters to use the defaults (cosine distance + OneHot MIN_VAL selection).\n\nRetrieval uses cosine distance by default, where lower distance = closer match. On the very first call with no initializer and empty memory, retrieval returns a zero-valued array of the shape defined by default_variable, and the input is stored.\n\ndistance_field_weights length must match the number of fields in each entry; mismatches raise an error. Fields with weight None or 0 are treated as labels and excluded from distance computation — only fields with non-zero weights determine duplicate detection as well.\n\nrate and noise are applied only before storage, not during retrieval.'
TOOL_PARAMETERS = { 'properties': { 'default_variable': { 'description': 'Template for entry shape — a '
                                                       'list of fields, each a 1d list '
                                                       'of numbers. E.g. '
                                                       '[[0,0],[0,0,0]] creates a '
                                                       '2-field memory with field '
                                                       'lengths 2 and 3. Overridden by '
                                                       'initializer if both are '
                                                       'provided.',
                                        'items': { 'items': {'type': 'number'},
                                                   'type': 'array'},
                                        'type': 'array'},
                  'distance_field_weights': { 'description': 'Per-field weights for '
                                                             'distance computation. '
                                                             'Length must equal the '
                                                             'number of fields. Weight '
                                                             '0 marks a field as a '
                                                             'label (excluded from '
                                                             'distance). If all '
                                                             'weights are identical, '
                                                             'full-vector distance is '
                                                             'used; otherwise '
                                                             'field-wise weighted '
                                                             'average. If all weights '
                                                             'are 0, no retrieval '
                                                             'occurs.',
                                              'items': {'type': 'number'},
                                              'type': 'array'},
                  'duplicate_entries_allowed': { 'default': False,
                                                 'description': 'Controls duplicate '
                                                                'handling: false = '
                                                                'skip storing '
                                                                'duplicates (default), '
                                                                'true = allow '
                                                                'accumulation, '
                                                                "'OVERWRITE' = replace "
                                                                'matching entry. '
                                                                'Duplicates are '
                                                                'identified by '
                                                                'distance_threshold.',
                                                 'oneOf': [ {'type': 'boolean'},
                                                            { 'enum': ['OVERWRITE'],
                                                              'type': 'string'}]},
                  'duplicate_threshold': { 'default': 0,
                                           'description': 'Distance below which two '
                                                          'entries are considered '
                                                          'duplicates. Default 0 means '
                                                          'exact matches only.',
                                           'type': 'number'},
                  'equidistant_entries_select': { 'default': 'RANDOM',
                                                  'description': 'Which entry to '
                                                                 'return when multiple '
                                                                 'entries are '
                                                                 'equidistant from the '
                                                                 'cue.',
                                                  'enum': [ 'RANDOM',
                                                            'OLDEST',
                                                            'NEWEST'],
                                                  'type': 'string'},
                  'initializer': { 'description': 'Initial memory contents: a list of '
                                                  'entries, each entry a list of 1d '
                                                  'numeric fields. E.g. '
                                                  '[[[1,2],[3,4]], [[5,6],[7,8]]]. '
                                                  'Determines entry shape and '
                                                  'overrides default_variable. All '
                                                  'entries must have the same number '
                                                  'of fields with matching field '
                                                  'lengths.',
                                   'items': { 'items': { 'items': {'type': 'number'},
                                                         'type': 'array'},
                                              'type': 'array'},
                                   'type': 'array'},
                  'max_entries': { 'default': 1000,
                                   'description': 'Maximum number of entries in '
                                                  'memory. When exceeded, the oldest '
                                                  'entry is deleted.',
                                   'type': 'integer'},
                  'noise': { 'default': 0,
                             'description': 'Additive noise applied to the input '
                                            'before storage: stored_value = input * '
                                            'rate + noise.',
                             'type': 'number'},
                  'rate': { 'default': 1,
                            'description': 'Multiplicative scaling applied to the '
                                           'input before storage: stored_value = input '
                                           '* rate + noise.',
                            'type': 'number'},
                  'retrieval_prob': { 'default': 1,
                                      'description': 'Probability [0,1] of performing '
                                                     'a retrieval on each call. When '
                                                     'skipped, returns a zero-valued '
                                                     'array.',
                                      'maximum': 1,
                                      'minimum': 0,
                                      'type': 'number'},
                  'seed': { 'description': 'Random seed for reproducible probabilistic '
                                           'retrieval/storage decisions and '
                                           'equidistant tie-breaking.',
                            'type': 'integer'},
                  'storage_prob': { 'default': 1,
                                    'description': 'Probability [0,1] of storing the '
                                                   'input in memory on each call. Does '
                                                   'not affect initializer entries, '
                                                   'which are always stored.',
                                    'maximum': 1,
                                    'minimum': 0,
                                    'type': 'number'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = "CRITICAL — do NOT pass `name`: ContentAddressableMemory.__init__() does not accept a `name` argument; passing it raises TypeError. If you need to label this function, store the reference under a variable name in your code instead.\n\nCRITICAL — do NOT pass `distance_function` or `selection_function` as strings: these parameters require actual PsyNeuLink object instances (e.g. Distance(metric=COSINE)), not string representations. Passing a string like 'Distance(metric=COSINE)' raises BeartypeCallHintParamViolation. Omit these parameters to use the defaults (cosine distance + OneHot MIN_VAL selection).\n\nRetrieval uses cosine distance by default, where lower distance = closer match. On the very first call with no initializer and empty memory, retrieval returns a zero-valued array of the shape defined by default_variable, and the input is stored.\n\ndistance_field_weights length must match the number of fields in each entry; mismatches raise an error. Fields with weight None or 0 are treated as labels and excluded from distance computation — only fields with non-zero weights determine duplicate detection as well.\n\nrate and noise are applied only before storage, not during retrieval."


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.ContentAddressableMemory
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
    def create_content_addressable_memory(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to instantiate a ContentAddressableMemory function that stores and retrieves multi-field entries by content similarity.'
        return _impl(args or {})
