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
TOOL_DESCRIPTION = 'Call this tool to instantiate a ContentAddressableMemory function — a content-addressable store that, on each call, retrieves the stored entry most similar to the input cue (using cosine distance by default), then stores the cue. Use it when building episodic memory components that need similarity-based retrieval with configurable field weighting, duplicate control, and probabilistic storage/retrieval. Returns the retrieved entry as a 2D array of fields (zeros if memory is empty or retrieval is suppressed).\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "default_variable": {\n      "description": "Template specifying entry shape: a list of fields, each a list/array of any length. Sets field count and shapes without adding any entries. Overridden by initializer if both are given. Example: [[0,0,0],[0,0]] creates entries with two fields of lengths 3 and 2.",\n      "items": {\n        "items": {\n          "type": "number"\n        },\n        "type": "array"\n      },\n      "type": "array"\n    },\n    "distance_field_weights": {\n      "description": "Per-field weights for distance computation. Length must equal number of fields. Fields with weight 0 or null are excluded from retrieval distance (useful for label-only fields). If all weights are identical, distance is computed over the full concatenated entry. Example: [1, 0] retrieves based only on field 0.",\n      "items": {\n        "type": "number"\n      },\n      "type": "array"\n    },\n    "duplicate_entries_allowed": {\n      "default": false,\n      "description": "Controls duplicate handling. false (default): skip storing duplicates. true: allow accumulation of duplicates. \'OVERWRITE\': replace the duplicate entry with the new one.",\n      "oneOf": [\n        {\n          "type": "boolean"\n        },\n        {\n          "enum": [\n            "OVERWRITE"\n          ],\n          "type": "string"\n        }\n      ]\n    },\n    "duplicate_threshold": {\n      "default": 0,\n      "description": "Distance below which two entries are considered duplicates (per distance_function). Default is approximately 0 (exact match only).",\n      "minimum": 0,\n      "type": "number"\n    },\n    "equidistant_entries_select": {\n      "default": "RANDOM",\n      "description": "Which entry to retrieve when two or more are equidistant from the cue. Default \'RANDOM\'.",\n      "enum": [\n        "RANDOM",\n        "OLDEST",\n        "NEWEST"\n      ],\n      "type": "string"\n    },\n    "initializer": {\n      "description": "Pre-populate memory with entries. Provide a list of entries, each a list of fields (matching the shape implied by default_variable if given). Example: [[[1,2],[3,4]],[[5,6],[7,8]]] initializes two entries each with two 2-element fields.",\n      "items": {\n        "items": {\n          "items": {\n            "type": "number"\n          },\n          "type": "array"\n        },\n        "type": "array"\n      },\n      "type": "array"\n    },\n    "max_entries": {\n      "default": 1000,\n      "description": "Maximum number of entries in memory. When exceeded, the oldest entry is deleted. Default 1000.",\n      "minimum": 1,\n      "type": "integer"\n    },\n    "noise": {\n      "default": 0,\n      "description": "Additive noise applied to the input before storage: stored_value = input * rate + noise. Default 0.0.",\n      "type": "number"\n    },\n    "rate": {\n      "default": 1,\n      "description": "Multiplicative factor applied to the input before storage: stored_value = input * rate + noise. Default 1.0 (no scaling).",\n      "type": "number"\n    },\n    "retrieval_prob": {\n      "default": 1,\n      "description": "Probability [0,1] of retrieving an entry on each call. Default 1.0 (always retrieve).",\n      "maximum": 1,\n      "minimum": 0,\n      "type": "number"\n    },\n    "seed": {\n      "description": "Random seed for reproducible stochastic behavior (retrieval_prob, storage_prob, equidistant RANDOM selection).",\n      "type": "integer"\n    },\n    "storage_prob": {\n      "default": 1,\n      "description": "Probability [0,1] of storing the input on each call. Default 1.0 (always store). Does not apply to initializer entries.",\n      "maximum": 1,\n      "minimum": 0,\n      "type": "number"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\nCRITICAL: Do NOT pass `name` — ContentAddressableMemory.__init__() does not accept a `name` argument (confirmed by two runtime errors). Do NOT pass `distance_function` or `selection_function` as strings; these parameters require actual PsyNeuLink object instances (e.g., Distance, OneHot), which cannot be serialized as JSON. Omit them to use the defaults (cosine distance, OneHot MIN_VAL selection). The `default_variable` sets entry shape only; use `initializer` to pre-populate memory with entries. Fields set to weight 0 in `distance_field_weights` are ignored in distance calculation AND in duplicate detection. `duplicate_entries_allowed` accepts boolean false/true or the exact string "OVERWRITE".'
TOOL_PARAMETERS = { 'properties': { 'default_variable': { 'description': 'Template specifying entry '
                                                       'shape: a list of fields, each '
                                                       'a list/array of any length. '
                                                       'Sets field count and shapes '
                                                       'without adding any entries. '
                                                       'Overridden by initializer if '
                                                       'both are given. Example: '
                                                       '[[0,0,0],[0,0]] creates '
                                                       'entries with two fields of '
                                                       'lengths 3 and 2.',
                                        'items': { 'items': {'type': 'number'},
                                                   'type': 'array'},
                                        'type': 'array'},
                  'distance_field_weights': { 'description': 'Per-field weights for '
                                                             'distance computation. '
                                                             'Length must equal number '
                                                             'of fields. Fields with '
                                                             'weight 0 or null are '
                                                             'excluded from retrieval '
                                                             'distance (useful for '
                                                             'label-only fields). If '
                                                             'all weights are '
                                                             'identical, distance is '
                                                             'computed over the full '
                                                             'concatenated entry. '
                                                             'Example: [1, 0] '
                                                             'retrieves based only on '
                                                             'field 0.',
                                              'items': {'type': 'number'},
                                              'type': 'array'},
                  'duplicate_entries_allowed': { 'default': False,
                                                 'description': 'Controls duplicate '
                                                                'handling. false '
                                                                '(default): skip '
                                                                'storing duplicates. '
                                                                'true: allow '
                                                                'accumulation of '
                                                                'duplicates. '
                                                                "'OVERWRITE': replace "
                                                                'the duplicate entry '
                                                                'with the new one.',
                                                 'oneOf': [ {'type': 'boolean'},
                                                            { 'enum': ['OVERWRITE'],
                                                              'type': 'string'}]},
                  'duplicate_threshold': { 'default': 0,
                                           'description': 'Distance below which two '
                                                          'entries are considered '
                                                          'duplicates (per '
                                                          'distance_function). Default '
                                                          'is approximately 0 (exact '
                                                          'match only).',
                                           'minimum': 0,
                                           'type': 'number'},
                  'equidistant_entries_select': { 'default': 'RANDOM',
                                                  'description': 'Which entry to '
                                                                 'retrieve when two or '
                                                                 'more are equidistant '
                                                                 'from the cue. '
                                                                 "Default 'RANDOM'.",
                                                  'enum': [ 'RANDOM',
                                                            'OLDEST',
                                                            'NEWEST'],
                                                  'type': 'string'},
                  'initializer': { 'description': 'Pre-populate memory with entries. '
                                                  'Provide a list of entries, each a '
                                                  'list of fields (matching the shape '
                                                  'implied by default_variable if '
                                                  'given). Example: '
                                                  '[[[1,2],[3,4]],[[5,6],[7,8]]] '
                                                  'initializes two entries each with '
                                                  'two 2-element fields.',
                                   'items': { 'items': { 'items': {'type': 'number'},
                                                         'type': 'array'},
                                              'type': 'array'},
                                   'type': 'array'},
                  'max_entries': { 'default': 1000,
                                   'description': 'Maximum number of entries in '
                                                  'memory. When exceeded, the oldest '
                                                  'entry is deleted. Default 1000.',
                                   'minimum': 1,
                                   'type': 'integer'},
                  'noise': { 'default': 0,
                             'description': 'Additive noise applied to the input '
                                            'before storage: stored_value = input * '
                                            'rate + noise. Default 0.0.',
                             'type': 'number'},
                  'rate': { 'default': 1,
                            'description': 'Multiplicative factor applied to the input '
                                           'before storage: stored_value = input * '
                                           'rate + noise. Default 1.0 (no scaling).',
                            'type': 'number'},
                  'retrieval_prob': { 'default': 1,
                                      'description': 'Probability [0,1] of retrieving '
                                                     'an entry on each call. Default '
                                                     '1.0 (always retrieve).',
                                      'maximum': 1,
                                      'minimum': 0,
                                      'type': 'number'},
                  'seed': { 'description': 'Random seed for reproducible stochastic '
                                           'behavior (retrieval_prob, storage_prob, '
                                           'equidistant RANDOM selection).',
                            'type': 'integer'},
                  'storage_prob': { 'default': 1,
                                    'description': 'Probability [0,1] of storing the '
                                                   'input on each call. Default 1.0 '
                                                   '(always store). Does not apply to '
                                                   'initializer entries.',
                                    'maximum': 1,
                                    'minimum': 0,
                                    'type': 'number'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = 'CRITICAL: Do NOT pass `name` — ContentAddressableMemory.__init__() does not accept a `name` argument (confirmed by two runtime errors). Do NOT pass `distance_function` or `selection_function` as strings; these parameters require actual PsyNeuLink object instances (e.g., Distance, OneHot), which cannot be serialized as JSON. Omit them to use the defaults (cosine distance, OneHot MIN_VAL selection). The `default_variable` sets entry shape only; use `initializer` to pre-populate memory with entries. Fields set to weight 0 in `distance_field_weights` are ignored in distance calculation AND in duplicate detection. `duplicate_entries_allowed` accepts boolean false/true or the exact string "OVERWRITE".'


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
        'Call this tool to instantiate a ContentAddressableMemory function — a content-addressable store that, on each call, retrieves the stored entry most similar to the input cue (using cosine distance by default), then stores the cue.'
        return _impl(args or {})
