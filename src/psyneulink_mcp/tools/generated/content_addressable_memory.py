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
TOOL_DESCRIPTION = 'Call this tool to create a `ContentAddressableMemory` function instance for content-based storage and retrieval of multi-field memory entries. Use it when building an `EpisodicMemoryMechanism` or any component that needs associative memory: each execution retrieves the closest-matching entry (by cosine distance) then stores the input. Returns a `ContentAddressableMemory` object ready to pass as the `function` argument of an `EpisodicMemoryMechanism`.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "default_variable": {\n      "description": "Template for memory entry shape \\u2014 a list of 1d arrays defining the number and size of fields (e.g. [[0,0,0],[0,0]] for two fields of size 3 and 2). Overridden if initializer is provided.",\n      "items": {\n        "type": "array"\n      },\n      "type": "array"\n    },\n    "distance_field_weights": {\n      "description": "Per-field weights for distance computation. Length must equal the number of fields. Fields with weight 0 are ignored (useful for label-only fields). Uniform weights treat the concatenated entry as one vector. Default: [1] (uniform).",\n      "items": {\n        "type": "number"\n      },\n      "type": "array"\n    },\n    "duplicate_entries_allowed": {\n      "description": "Controls duplicate handling. false (default): skip duplicates; true: accumulate duplicates; \'OVERWRITE\': replace matching entry in place.",\n      "oneOf": [\n        {\n          "type": "boolean"\n        },\n        {\n          "enum": [\n            "OVERWRITE"\n          ],\n          "type": "string"\n        }\n      ]\n    },\n    "duplicate_threshold": {\n      "description": "Distance below which two entries are considered duplicates. Default ~0 (exact match only). Increase to treat near-identical entries as duplicates.",\n      "type": "number"\n    },\n    "equidistant_entries_select": {\n      "description": "Which entry to retrieve when multiple entries are equidistant from the cue. Default \'RANDOM\'.",\n      "enum": [\n        "RANDOM",\n        "OLDEST",\n        "NEWEST"\n      ],\n      "type": "string"\n    },\n    "initializer": {\n      "description": "Initial memory entries \\u2014 a list of entries, each a list of 1d arrays (fields). All entries must have the same number of fields with matching per-field shapes.",\n      "items": {\n        "items": {\n          "type": "array"\n        },\n        "type": "array"\n      },\n      "type": "array"\n    },\n    "max_entries": {\n      "description": "Maximum entries in memory; oldest entry is deleted when this limit is exceeded. Default 1000.",\n      "minimum": 1,\n      "type": "integer"\n    },\n    "noise": {\n      "description": "Additive noise applied to input before storage. Default 0.0.",\n      "type": "number"\n    },\n    "rate": {\n      "description": "Multiplicative scale applied to input before storage (variable * rate + noise). Default 1.0.",\n      "type": "number"\n    },\n    "retrieval_prob": {\n      "description": "Probability of retrieving an entry on each execution. Default 1.0. Set to 0 for store-only.",\n      "maximum": 1,\n      "minimum": 0,\n      "type": "number"\n    },\n    "seed": {\n      "description": "Random seed for probabilistic retrieval/storage and RANDOM equidistant selection.",\n      "type": "integer"\n    },\n    "storage_prob": {\n      "description": "Probability of storing the input on each execution. Default 1.0. Set to 0 for retrieve-only.",\n      "maximum": 1,\n      "minimum": 0,\n      "type": "number"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\n**Do NOT pass `name`** — `ContentAddressableMemory.__init__()` does not accept a `name` argument; passing it raises TypeError. Name assignment is handled by the owning Mechanism.\n\n**Do NOT pass `distance_function` or `selection_function` as strings** — these parameters require actual PNL object instances (e.g. `Distance(metric=COSINE)`, `OneHot(mode=MIN_VAL)`), not string representations. Passing a string causes a `BeartypeCallHintParamViolation`. Omit both parameters to use the defaults (cosine distance + OneHot min), or obtain a live PNL function object via a separate tool call before passing it here.\n\nEach execution both retrieves AND stores: retrieval happens first, then storage. If memory is empty on the first call, a zero-valued array of the entry shape is returned.\n\nSetting all `distance_field_weights` entries to 0 suppresses retrieval entirely (equivalent to `retrieval_prob=0`). Only fields with non-zero weights are considered when evaluating duplicates.\n\n`initializer` entries bypass `storage_prob` — they are always stored regardless of the probability setting.'
TOOL_PARAMETERS = { 'properties': { 'default_variable': { 'description': 'Template for memory entry '
                                                       'shape — a list of 1d arrays '
                                                       'defining the number and size '
                                                       'of fields (e.g. '
                                                       '[[0,0,0],[0,0]] for two fields '
                                                       'of size 3 and 2). Overridden '
                                                       'if initializer is provided.',
                                        'items': {'type': 'array'},
                                        'type': 'array'},
                  'distance_field_weights': { 'description': 'Per-field weights for '
                                                             'distance computation. '
                                                             'Length must equal the '
                                                             'number of fields. Fields '
                                                             'with weight 0 are '
                                                             'ignored (useful for '
                                                             'label-only fields). '
                                                             'Uniform weights treat '
                                                             'the concatenated entry '
                                                             'as one vector. Default: '
                                                             '[1] (uniform).',
                                              'items': {'type': 'number'},
                                              'type': 'array'},
                  'duplicate_entries_allowed': { 'description': 'Controls duplicate '
                                                                'handling. false '
                                                                '(default): skip '
                                                                'duplicates; true: '
                                                                'accumulate '
                                                                'duplicates; '
                                                                "'OVERWRITE': replace "
                                                                'matching entry in '
                                                                'place.',
                                                 'oneOf': [ {'type': 'boolean'},
                                                            { 'enum': ['OVERWRITE'],
                                                              'type': 'string'}]},
                  'duplicate_threshold': { 'description': 'Distance below which two '
                                                          'entries are considered '
                                                          'duplicates. Default ~0 '
                                                          '(exact match only). '
                                                          'Increase to treat '
                                                          'near-identical entries as '
                                                          'duplicates.',
                                           'type': 'number'},
                  'equidistant_entries_select': { 'description': 'Which entry to '
                                                                 'retrieve when '
                                                                 'multiple entries are '
                                                                 'equidistant from the '
                                                                 'cue. Default '
                                                                 "'RANDOM'.",
                                                  'enum': [ 'RANDOM',
                                                            'OLDEST',
                                                            'NEWEST'],
                                                  'type': 'string'},
                  'initializer': { 'description': 'Initial memory entries — a list of '
                                                  'entries, each a list of 1d arrays '
                                                  '(fields). All entries must have the '
                                                  'same number of fields with matching '
                                                  'per-field shapes.',
                                   'items': { 'items': {'type': 'array'},
                                              'type': 'array'},
                                   'type': 'array'},
                  'max_entries': { 'description': 'Maximum entries in memory; oldest '
                                                  'entry is deleted when this limit is '
                                                  'exceeded. Default 1000.',
                                   'minimum': 1,
                                   'type': 'integer'},
                  'noise': { 'description': 'Additive noise applied to input before '
                                            'storage. Default 0.0.',
                             'type': 'number'},
                  'rate': { 'description': 'Multiplicative scale applied to input '
                                           'before storage (variable * rate + noise). '
                                           'Default 1.0.',
                            'type': 'number'},
                  'retrieval_prob': { 'description': 'Probability of retrieving an '
                                                     'entry on each execution. Default '
                                                     '1.0. Set to 0 for store-only.',
                                      'maximum': 1,
                                      'minimum': 0,
                                      'type': 'number'},
                  'seed': { 'description': 'Random seed for probabilistic '
                                           'retrieval/storage and RANDOM equidistant '
                                           'selection.',
                            'type': 'integer'},
                  'storage_prob': { 'description': 'Probability of storing the input '
                                                   'on each execution. Default 1.0. '
                                                   'Set to 0 for retrieve-only.',
                                    'maximum': 1,
                                    'minimum': 0,
                                    'type': 'number'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = '**Do NOT pass `name`** — `ContentAddressableMemory.__init__()` does not accept a `name` argument; passing it raises TypeError. Name assignment is handled by the owning Mechanism.\n\n**Do NOT pass `distance_function` or `selection_function` as strings** — these parameters require actual PNL object instances (e.g. `Distance(metric=COSINE)`, `OneHot(mode=MIN_VAL)`), not string representations. Passing a string causes a `BeartypeCallHintParamViolation`. Omit both parameters to use the defaults (cosine distance + OneHot min), or obtain a live PNL function object via a separate tool call before passing it here.\n\nEach execution both retrieves AND stores: retrieval happens first, then storage. If memory is empty on the first call, a zero-valued array of the entry shape is returned.\n\nSetting all `distance_field_weights` entries to 0 suppresses retrieval entirely (equivalent to `retrieval_prob=0`). Only fields with non-zero weights are considered when evaluating duplicates.\n\n`initializer` entries bypass `storage_prob` — they are always stored regardless of the probability setting.'


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
        'Call this tool to create a `ContentAddressableMemory` function instance for content-based storage and retrieval of multi-field memory entries.'
        return _impl(args or {})
