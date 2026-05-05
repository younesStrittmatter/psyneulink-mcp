"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = 'db04cfd18ea6780395553755968c3a748e5a7f609c4979fbe92263fbb25e2aa6'
__pnl_qualname__ = 'psyneulink.ContentAddressableMemory'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_content_addressable_memory'
TOOL_DESCRIPTION = 'Use this tool to instantiate a ContentAddressableMemory function when you need content-based (similarity-driven) storage and retrieval of multi-field entries — for example, implementing an associative memory, episodic buffer, or key-value store within a PsyNeuLink model. Each call to the resulting function first retrieves the closest-matching entry from memory (returning a 2d array of fields), then stores the input; if memory is empty the call returns a zero-valued array matching the entry shape.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "default_variable": {\n      "description": "Template specifying the shape of memory entries \\u2014 a list of fields, each a 1d array (e.g. [[0,0],[0,0,0]] for two fields of lengths 2 and 3). Overridden if initializer is provided. Use this when you want to define the entry shape without pre-loading any entries.",\n      "items": {\n        "items": {\n          "type": "number"\n        },\n        "type": "array"\n      },\n      "type": "array"\n    },\n    "distance_field_weights": {\n      "description": "Per-field weights used when computing distance. Length must equal the number of fields in each entry. Fields with weight 0 or null are excluded from distance computation (useful for label fields). When all weights are equal, distance is computed over the full concatenated entry vector. Pattern [1, 0] creates key-value dictionary behavior where only the first field drives retrieval.",\n      "items": {\n        "type": "number"\n      },\n      "type": "array"\n    },\n    "distance_function": {\n      "description": "Specification string for the distance function used during retrieval, e.g. \'Distance(metric=COSINE)\' (default), \'Distance(metric=EUCLIDEAN)\', \'Distance(metric=CORRELATION)\'. Must return a scalar for full-entry comparisons.",\n      "type": "string"\n    },\n    "duplicate_entries_allowed": {\n      "default": false,\n      "description": "Controls duplicate storage behavior. False (default): silently skips storing entries that match an existing one within duplicate_threshold. True: allows accumulation of duplicates. \'OVERWRITE\': replaces the matching entry with the new input.",\n      "oneOf": [\n        {\n          "type": "boolean"\n        },\n        {\n          "enum": [\n            "OVERWRITE"\n          ],\n          "type": "string"\n        }\n      ]\n    },\n    "duplicate_threshold": {\n      "default": 0,\n      "description": "Distance below which two entries are considered duplicates. Default 0 (exact match only). Increase to treat near-identical entries as duplicates.",\n      "type": "number"\n    },\n    "equidistant_entries_select": {\n      "default": "RANDOM",\n      "description": "Which entry to retrieve when multiple entries are equidistant from the cue. Default \'RANDOM\'.",\n      "enum": [\n        "RANDOM",\n        "OLDEST",\n        "NEWEST"\n      ],\n      "type": "string"\n    },\n    "initializer": {\n      "description": "Pre-load memory with an array of entries. Each entry must be a list of fields matching the intended shape. Bypasses storage_prob \\u2014 entries are always stored. Overrides default_variable if both are given.",\n      "items": {\n        "items": {\n          "items": {\n            "type": "number"\n          },\n          "type": "array"\n        },\n        "type": "array"\n      },\n      "type": "array"\n    },\n    "max_entries": {\n      "default": 1000,\n      "description": "Maximum number of entries kept in memory. When exceeded, the oldest entry is deleted. Default 1000.",\n      "type": "integer"\n    },\n    "noise": {\n      "default": 0,\n      "description": "Additive noise applied to the input before storage: stored_value = input * rate + noise. Default 0.0. Does not affect retrieval.",\n      "type": "number"\n    },\n    "rate": {\n      "default": 1,\n      "description": "Multiplicative scaling applied to the input before storage: stored_value = input * rate + noise. Default 1.0 (no scaling).",\n      "type": "number"\n    },\n    "retrieval_prob": {\n      "default": 1,\n      "description": "Probability [0, 1] of retrieving an entry on each call. Default 1.0. Set to 0.0 to suppress retrieval (store-only mode).",\n      "maximum": 1,\n      "minimum": 0,\n      "type": "number"\n    },\n    "seed": {\n      "description": "Random seed for the internal numpy.RandomState used by retrieval_prob, storage_prob, and RANDOM equidistant selection.",\n      "type": "integer"\n    },\n    "selection_function": {\n      "description": "Specification string for the function that selects which entry to retrieve based on distances. Default \'OneHot(mode=MIN_VAL)\' returns the single closest entry (SINGLE selection_type). Use \'SoftMax()\' for a distance-weighted sum of all entries (WEIGHTED selection_type).",\n      "type": "string"\n    },\n    "storage_prob": {\n      "default": 1,\n      "description": "Probability [0, 1] of storing the input on each call. Default 1.0. Set to 0.0 to suppress storage (retrieve-only mode). Does NOT apply to initializer entries.",\n      "maximum": 1,\n      "minimum": 0,\n      "type": "number"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\nExecution order: retrieval always happens BEFORE storage on each call — the function returns the best match from the state of memory prior to storing the current input. On the very first call with empty memory (no initializer), a zero-valued array matching the entry shape is returned.\n\nAll entries must have the same number of fields, and corresponding fields must have identical shapes across all entries. Fields themselves must be 1d arrays; entries are at most 2d.\n\nduplicate_entries_allowed defaults to False, so attempting to store an input that is within duplicate_threshold of an existing entry is silently dropped — no error or warning is raised.\n\nmax_entries defaults to 1000 (from the Parameters class), not None as the constructor signature implies.\n\ninitializer entries bypass storage_prob entirely and are always loaded into memory regardless of that setting.\n\nIf all distance_field_weights are 0 or None, no retrieval occurs (equivalent to retrieval_prob=0).\n\nWhen using distance_field_weights with non-identical values, distances are computed field-by-field and averaged weighted by those values; with identical values (or a scalar), distances are computed over the full concatenated entry vector scaled by that value.'
TOOL_PARAMETERS = { 'properties': { 'default_variable': { 'description': 'Template specifying the shape '
                                                       'of memory entries — a list of '
                                                       'fields, each a 1d array (e.g. '
                                                       '[[0,0],[0,0,0]] for two fields '
                                                       'of lengths 2 and 3). '
                                                       'Overridden if initializer is '
                                                       'provided. Use this when you '
                                                       'want to define the entry shape '
                                                       'without pre-loading any '
                                                       'entries.',
                                        'items': { 'items': {'type': 'number'},
                                                   'type': 'array'},
                                        'type': 'array'},
                  'distance_field_weights': { 'description': 'Per-field weights used '
                                                             'when computing distance. '
                                                             'Length must equal the '
                                                             'number of fields in each '
                                                             'entry. Fields with '
                                                             'weight 0 or null are '
                                                             'excluded from distance '
                                                             'computation (useful for '
                                                             'label fields). When all '
                                                             'weights are equal, '
                                                             'distance is computed '
                                                             'over the full '
                                                             'concatenated entry '
                                                             'vector. Pattern [1, 0] '
                                                             'creates key-value '
                                                             'dictionary behavior '
                                                             'where only the first '
                                                             'field drives retrieval.',
                                              'items': {'type': 'number'},
                                              'type': 'array'},
                  'distance_function': { 'description': 'Specification string for the '
                                                        'distance function used during '
                                                        'retrieval, e.g. '
                                                        "'Distance(metric=COSINE)' "
                                                        '(default), '
                                                        "'Distance(metric=EUCLIDEAN)', "
                                                        "'Distance(metric=CORRELATION)'. "
                                                        'Must return a scalar for '
                                                        'full-entry comparisons.',
                                         'type': 'string'},
                  'duplicate_entries_allowed': { 'default': False,
                                                 'description': 'Controls duplicate '
                                                                'storage behavior. '
                                                                'False (default): '
                                                                'silently skips '
                                                                'storing entries that '
                                                                'match an existing one '
                                                                'within '
                                                                'duplicate_threshold. '
                                                                'True: allows '
                                                                'accumulation of '
                                                                'duplicates. '
                                                                "'OVERWRITE': replaces "
                                                                'the matching entry '
                                                                'with the new input.',
                                                 'oneOf': [ {'type': 'boolean'},
                                                            { 'enum': ['OVERWRITE'],
                                                              'type': 'string'}]},
                  'duplicate_threshold': { 'default': 0,
                                           'description': 'Distance below which two '
                                                          'entries are considered '
                                                          'duplicates. Default 0 '
                                                          '(exact match only). '
                                                          'Increase to treat '
                                                          'near-identical entries as '
                                                          'duplicates.',
                                           'type': 'number'},
                  'equidistant_entries_select': { 'default': 'RANDOM',
                                                  'description': 'Which entry to '
                                                                 'retrieve when '
                                                                 'multiple entries are '
                                                                 'equidistant from the '
                                                                 'cue. Default '
                                                                 "'RANDOM'.",
                                                  'enum': [ 'RANDOM',
                                                            'OLDEST',
                                                            'NEWEST'],
                                                  'type': 'string'},
                  'initializer': { 'description': 'Pre-load memory with an array of '
                                                  'entries. Each entry must be a list '
                                                  'of fields matching the intended '
                                                  'shape. Bypasses storage_prob — '
                                                  'entries are always stored. '
                                                  'Overrides default_variable if both '
                                                  'are given.',
                                   'items': { 'items': { 'items': {'type': 'number'},
                                                         'type': 'array'},
                                              'type': 'array'},
                                   'type': 'array'},
                  'max_entries': { 'default': 1000,
                                   'description': 'Maximum number of entries kept in '
                                                  'memory. When exceeded, the oldest '
                                                  'entry is deleted. Default 1000.',
                                   'type': 'integer'},
                  'noise': { 'default': 0,
                             'description': 'Additive noise applied to the input '
                                            'before storage: stored_value = input * '
                                            'rate + noise. Default 0.0. Does not '
                                            'affect retrieval.',
                             'type': 'number'},
                  'rate': { 'default': 1,
                            'description': 'Multiplicative scaling applied to the '
                                           'input before storage: stored_value = input '
                                           '* rate + noise. Default 1.0 (no scaling).',
                            'type': 'number'},
                  'retrieval_prob': { 'default': 1,
                                      'description': 'Probability [0, 1] of retrieving '
                                                     'an entry on each call. Default '
                                                     '1.0. Set to 0.0 to suppress '
                                                     'retrieval (store-only mode).',
                                      'maximum': 1,
                                      'minimum': 0,
                                      'type': 'number'},
                  'seed': { 'description': 'Random seed for the internal '
                                           'numpy.RandomState used by retrieval_prob, '
                                           'storage_prob, and RANDOM equidistant '
                                           'selection.',
                            'type': 'integer'},
                  'selection_function': { 'description': 'Specification string for the '
                                                         'function that selects which '
                                                         'entry to retrieve based on '
                                                         'distances. Default '
                                                         "'OneHot(mode=MIN_VAL)' "
                                                         'returns the single closest '
                                                         'entry (SINGLE '
                                                         'selection_type). Use '
                                                         "'SoftMax()' for a "
                                                         'distance-weighted sum of all '
                                                         'entries (WEIGHTED '
                                                         'selection_type).',
                                          'type': 'string'},
                  'storage_prob': { 'default': 1,
                                    'description': 'Probability [0, 1] of storing the '
                                                   'input on each call. Default 1.0. '
                                                   'Set to 0.0 to suppress storage '
                                                   '(retrieve-only mode). Does NOT '
                                                   'apply to initializer entries.',
                                    'maximum': 1,
                                    'minimum': 0,
                                    'type': 'number'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = 'Execution order: retrieval always happens BEFORE storage on each call — the function returns the best match from the state of memory prior to storing the current input. On the very first call with empty memory (no initializer), a zero-valued array matching the entry shape is returned.\n\nAll entries must have the same number of fields, and corresponding fields must have identical shapes across all entries. Fields themselves must be 1d arrays; entries are at most 2d.\n\nduplicate_entries_allowed defaults to False, so attempting to store an input that is within duplicate_threshold of an existing entry is silently dropped — no error or warning is raised.\n\nmax_entries defaults to 1000 (from the Parameters class), not None as the constructor signature implies.\n\ninitializer entries bypass storage_prob entirely and are always loaded into memory regardless of that setting.\n\nIf all distance_field_weights are 0 or None, no retrieval occurs (equivalent to retrieval_prob=0).\n\nWhen using distance_field_weights with non-identical values, distances are computed field-by-field and averaged weighted by those values; with identical values (or a scalar), distances are computed over the full concatenated entry vector scaled by that value.'


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
        'Use this tool to instantiate a ContentAddressableMemory function when you need content-based (similarity-driven) storage and retrieval of multi-field entries — for example, implementing an associative memory, episodic buffer, or key-value store within a PsyNeuLink model.'
        return _impl(args or {})
