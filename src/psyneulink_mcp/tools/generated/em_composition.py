"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '65224806554d464da08e3c3efa6bf4b0bf06e96f4e49529e95b4658a468bcda9'
__pnl_qualname__ = 'psyneulink.EMComposition'
__pnl_kind__ = 'class'
__pnl_parents__ = ['AutodiffComposition',
 'Composition',
 'Composition_Base',
 'ShellClass',
 'Component',
 'MDFSerializable']
__pnl_parent_sha256s__ = {'AutodiffComposition': '216b828fe306c49eaec2babb8733dbbd63d515f752a42e1ec5082020b1b6b939',
 'Component': 'b878afca9fca90ac1a952605ca8d39a37f25ebebf1411a7f545b9c48a3eaeec3',
 'Composition': '82e486b9b09ff0cde5e71602e6f5b2d26ee05fc304b26675dbbf2c8dd497f0cd',
 'Composition_Base': '2d408586b92821739232ac4056a9f2f4b67dea27d505539eafa784d173037624',
 'MDFSerializable': 'caad6059e8ef158be1269a23127f13da3733824c3585f9b4d6e3a63de82f65da',
 'ShellClass': 'adc23754ebeb0c55bdde1324622b33a509116703503508ee7e7de181a8afeee6'}
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_em_composition'
TOOL_DESCRIPTION = 'Build a differentiable, learnable episodic memory module (subclass of `AutodiffComposition`) where retrieval is a softmax over field-weighted dot-product (or 1-L0) similarities between input keys and stored entries, and storage replaces the weakest memory row at each execution step. Use this when you need content-addressable memory with multi-field keys/values, optional concatenation of keys, learnable field weights via backprop, and a storage probability — beyond what `AutodiffComposition`/`Composition` provide. Returns an EMComposition handle whose own nodes (query_input_nodes, value_input_nodes, retrieved_nodes, softmax_node, storage_node) are auto-built; treat the result as a single Composition Node when nesting.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "concatenate_queries": {\n      "default": false,\n      "description": "If true, concatenate all key inputs into a single vector before matching (one match_node total). Silently downgraded to false (with warning) unless num_keys>1, all key weights are equal, AND normalize_memories=true. Incompatible with learning of field weights.",\n      "type": "boolean"\n    },\n    "enable_learning": {\n      "default": true,\n      "description": "Wire backprop pathways for retrieved_nodes (subject to target_fields). Requires use_gating_for_weighting=False and softmax_choice=\'WEIGHTED_AVG\' at learn() time, otherwise raises. Has no effect when concatenate_queries is true or there is only one key.",\n      "type": "boolean"\n    },\n    "field_names": {\n      "default": null,\n      "description": "Names for each field, in memory_template order. Length must equal num_fields. Ignored (with warning) if `fields` is provided.",\n      "items": {\n        "type": "string"\n      },\n      "type": [\n        "array",\n        "null"\n      ]\n    },\n    "field_weights": {\n      "default": null,\n      "description": "Per-field weight: positive number = KEY field with that contribution to matching; null = VALUE field (stored/retrieved, not matched). Length must equal num_fields, or 1 (broadcast). Cannot be all-null. Ignored (with warning) if `fields` is provided.",\n      "items": {\n        "type": [\n          "number",\n          "null"\n        ]\n      },\n      "type": [\n        "array",\n        "null"\n      ]\n    },\n    "fields": {\n      "additionalProperties": {\n        "oneOf": [\n          {\n            "description": "[field_weight (number or null for value field), learn_field_weight (bool|number|null), target_field (bool)]",\n            "maxItems": 3,\n            "minItems": 3,\n            "type": "array"\n          },\n          {\n            "properties": {\n              "field_weight": {\n                "description": "null marks the field as a VALUE field (stored/retrieved but not used for matching); a positive number marks it as a KEY field with that weight.",\n                "type": [\n                  "number",\n                  "null"\n                ]\n              },\n              "learn_field_weight": {\n                "description": "false to disable learning for this field, true/null for default learning_rate, or a numeric per-field learning rate. Ignored for value fields."\n              },\n              "target_field": {\n                "description": "Whether to construct a learning pathway terminating at this field\'s retrieved_node.",\n                "type": "boolean"\n              }\n            },\n            "required": [\n              "field_weight",\n              "learn_field_weight",\n              "target_field"\n            ],\n            "type": "object"\n          }\n        ]\n      },\n      "default": null,\n      "description": "Per-field config keyed by field name. EACH value MUST be either (a) a 3-element array [field_weight, learn_field_weight, target_field], or (b) an object containing ALL three keys \'field_weight\', \'learn_field_weight\', \'target_field\' (lowercase). Partial dicts raise KeyError. When `fields` is given, do NOT also pass field_names/field_weights/learn_field_weights/target_fields \\u2014 they are silently overridden and warn.",\n      "type": [\n        "object",\n        "null"\n      ]\n    },\n    "learn_field_weights": {\n      "default": false,\n      "description": "Whether/how to learn each field\'s weight. bool applies to all keys; list (length num_fields) gives per-field bool or numeric learning rate. Forced False for value fields. Ignored (with warning) if `fields` is provided.",\n      "oneOf": [\n        {\n          "type": "boolean"\n        },\n        {\n          "items": {\n            "type": [\n              "boolean",\n              "number",\n              "null"\n            ]\n          },\n          "type": "array"\n        }\n      ]\n    },\n    "learning_rate": {\n      "default": 0.01,\n      "description": "Default learning rate applied to any field weight whose learn_field_weights entry is True/None. Dict form is NOT supported by EMComposition (raises EMCompositionError) \\u2014 use `fields` or `learn_field_weights` for per-field rates.",\n      "oneOf": [\n        {\n          "type": "number"\n        },\n        {\n          "type": "boolean"\n        }\n      ]\n    },\n    "memory_capacity": {\n      "default": null,\n      "description": "Number of entries the memory can hold. Required if memory_template is a 2-tuple or a single-entry 2D template; otherwise defaults to 1000 or to len(memory_template) for 3D templates.",\n      "minimum": 1,\n      "type": [\n        "integer",\n        "null"\n      ]\n    },\n    "memory_decay_rate": {\n      "default": "AUTO",\n      "description": "Multiplicative decay applied to existing memories before each new write. Numeric in [0,1] (0 = no decay), or \'AUTO\' which sets it to 1/memory_capacity.",\n      "oneOf": [\n        {\n          "maximum": 1,\n          "minimum": 0,\n          "type": "number"\n        },\n        {\n          "enum": [\n            "AUTO"\n          ],\n          "type": "string"\n        }\n      ]\n    },\n    "memory_fill": {\n      "default": 0,\n      "description": "Value used to populate empty slots: scalar (constant fill) or a 2-element [low, high] tuple (uniform random fill). Important when normalize_memories=True \\u2014 a field of all zeros causes a divide-by-zero warning at construction and NaN matches at runtime.",\n      "oneOf": [\n        {\n          "type": "number"\n        },\n        {\n          "items": {\n            "type": "number"\n          },\n          "maxItems": 2,\n          "minItems": 2,\n          "type": "array"\n        }\n      ]\n    },\n    "memory_template": {\n      "default": [\n        [\n          0\n        ],\n        [\n          0\n        ]\n      ],\n      "description": "Shape/content of an entry. (1) 2-tuple (num_fields, field_len) or 3-tuple (num_entries, num_fields, field_len) of ints \\u2014 shape only, contents come from memory_fill. (2) 2D list/array \\u2014 a single entry template, replicated memory_capacity times. (3) 3D list/array \\u2014 explicit per-entry contents (rows are entries, columns are fields). Fields may have different lengths only when given via list/array, not via tuple-of-ints.",\n      "oneOf": [\n        {\n          "items": {\n            "type": "integer"\n          },\n          "maxItems": 3,\n          "minItems": 2,\n          "type": "array"\n        },\n        {\n          "items": {\n            "items": {\n              "type": "number"\n            },\n            "type": "array"\n          },\n          "type": "array"\n        },\n        {\n          "items": {\n            "items": {\n              "items": {\n                "type": "number"\n              },\n              "type": "array"\n            },\n            "type": "array"\n          },\n          "type": "array"\n        }\n      ]\n    },\n    "name": {\n      "default": "EM_Composition",\n      "description": "Name of the EMComposition instance.",\n      "type": "string"\n    },\n    "normalize_field_weights": {\n      "default": true,\n      "description": "If true, key field_weights are renormalized to sum to 1; if false, used as absolute weights.",\n      "type": "boolean"\n    },\n    "normalize_memories": {\n      "default": true,\n      "description": "If true, queries and stored keys are L2-normalized before dot-product (cosine similarity). Required by concatenate_queries.",\n      "type": "boolean"\n    },\n    "purge_by_field_weights": {\n      "default": false,\n      "description": "If true, the row chosen for replacement on storage is the weakest after multiplying field norms by field_weights (so unweighted/value fields don\'t influence which slot is overwritten).",\n      "type": "boolean"\n    },\n    "seed": {\n      "default": null,\n      "description": "Seed for the random_state used by storage_prob and random memory_fill.",\n      "type": [\n        "integer",\n        "null"\n      ]\n    },\n    "softmax_choice": {\n      "default": "WEIGHTED_AVG",\n      "description": "How softmax output is used for retrieval. WEIGHTED_AVG = standard softmax-weighted average over entries (the only choice compatible with learning). ARG_MAX = pick the single best-matching entry (internally rewritten to ARG_MAX_INDICATOR). NOTE: \'PROBABILISTIC\' appears in the docstring but is BROKEN in the current PNL build \\u2014 it is forwarded raw to OneHot.mode which only accepts {\'PROB\',\'PROB_INDICATOR\',...}, so it raises a Beartype error at construction. Do not use it.",\n      "enum": [\n        "WEIGHTED_AVG",\n        "ARG_MAX"\n      ],\n      "type": "string"\n    },\n    "softmax_gain": {\n      "default": 1,\n      "description": "Inverse-temperature for the retrieval softmax. Numeric scalar OR the keyword \'ADAPTIVE\' (entropy-weighted) OR \'CONTROL\' (constructs a SOFTMAX GAIN CONTROL node that adapts gain at runtime; this also forces softmax_gain to be non-modulable).",\n      "oneOf": [\n        {\n          "type": "number"\n        },\n        {\n          "enum": [\n            "ADAPTIVE",\n            "CONTROL"\n          ],\n          "type": "string"\n        }\n      ]\n    },\n    "softmax_threshold": {\n      "default": 0.001,\n      "description": "Mask cutoff: values below this are zeroed before softmax. Must be > 0 if not null.",\n      "type": [\n        "number",\n        "null"\n      ]\n    },\n    "storage_prob": {\n      "default": 1,\n      "description": "Per-execution probability that the current input is written into memory. 0 disables storage; 1 always stores.",\n      "maximum": 1,\n      "minimum": 0,\n      "type": "number"\n    },\n    "store_on_optimization": {\n      "default": "FIRST",\n      "description": "Which optimization step(s) inside a learning trial actually store an entry.",\n      "enum": [\n        "FIRST",\n        "LAST",\n        "ALL"\n      ],\n      "type": "string"\n    },\n    "target_fields": {\n      "default": null,\n      "description": "Per-field bool: which retrieved fields should receive an error signal during learning. Length must equal num_fields. Ignored (with warning) if `fields` is provided.",\n      "items": {\n        "type": "boolean"\n      },\n      "type": [\n        "array",\n        "null"\n      ]\n    },\n    "use_gating_for_weighting": {\n      "default": false,\n      "description": "If true, weight match outputs via output gating (GatingMechanism) instead of multiplicative ProcessingMechanisms; in that case no weighted_match_nodes are built and field weights cannot be learned (must combine with enable_learning=False).",\n      "type": "boolean"\n    },\n    "use_storage_node": {\n      "default": true,\n      "description": "If true (recommended/default), an EMStorageMechanism handles writes. If false, storage runs as a Composition method instead \\u2014 debug only, and prevents the EMComposition from being imported into another Composition via import_composition.",\n      "type": "boolean"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\nFEEDBACK-DRIVEN GOTCHAS:\n\n1. softmax_choice=\'PROBABILISTIC\' is documented but BROKEN in the current PNL build: EMComposition forwards the raw string to SoftMax → OneHot.mode, whose Literal only accepts {\'deterministic\',\'PROB\',\'PROB_INDICATOR\',\'arg_max\',...,\'MIN_ABS_INDICATOR\'}. Result: BeartypeCallHintParamViolation at construction. The schema therefore exposes only WEIGHTED_AVG and ARG_MAX. If the caller wants categorical sampling, omit softmax_choice and either (a) post-sample externally from the softmax output, or (b) wait for an upstream PNL fix. ARG_MAX is rewritten internally to ARG_MAX_INDICATOR.\n\n2. `fields` dict entries must be COMPLETE: either a 3-tuple/list [field_weight, learn_field_weight, target_field] or an object with ALL three lowercase keys \'field_weight\', \'learn_field_weight\', \'target_field\'. Passing only a subset (e.g. {\'field_weight\': 1.0}) raises KeyError because _parse_fields_dict indexes the constants directly. Mark value fields with field_weight=null (None), not 0 — 0 means "key field currently weighted to zero; ignored at retrieval but still a key".\n\n3. `fields` and the legacy args (field_names/field_weights/learn_field_weights/target_fields) are mutually exclusive in spirit; passing both warns and the legacy args are dropped.\n\nOTHER GOTCHAS:\n\n- field_weights default if not given and num_fields>1: all keys with weight 1 except the LAST field, which becomes a value (None). Single-field default is [1].\n- memory_template tuple form: 2-tuple = (num_fields, field_len) and needs memory_capacity; 3-tuple\'s first element MUST equal memory_capacity if both given.\n- memory_fill must avoid all-zero key fields when normalize_memories=True — the constructor warns and runtime will divide by zero.\n- learning_rate as a dict raises EMCompositionError; per-field rates go in `fields` or `learn_field_weights`.\n- enable_learning is silently neutralized (with a runtime warning at learn()) when concatenate_queries is true or num_keys==1.\n- use_gating_for_weighting=True is incompatible with enable_learning=True at learn() time (raises).\n- After construction, add_node/add_projection from outside raise — EMComposition is treated as immutable post-build; nest it as-is.\n- Returned object is a Composition; query_input_nodes / value_input_nodes / retrieved_nodes / softmax_node / storage_node are auto-named with [QUERY]/[VALUE]/[RETRIEVED] suffixes (or KEY_n_INPUT / VALUE_n_INPUT if field_names not provided).'
TOOL_PARAMETERS = { 'properties': { 'concatenate_queries': { 'default': False,
                                           'description': 'If true, concatenate all '
                                                          'key inputs into a single '
                                                          'vector before matching (one '
                                                          'match_node total). Silently '
                                                          'downgraded to false (with '
                                                          'warning) unless num_keys>1, '
                                                          'all key weights are equal, '
                                                          'AND '
                                                          'normalize_memories=true. '
                                                          'Incompatible with learning '
                                                          'of field weights.',
                                           'type': 'boolean'},
                  'enable_learning': { 'default': True,
                                       'description': 'Wire backprop pathways for '
                                                      'retrieved_nodes (subject to '
                                                      'target_fields). Requires '
                                                      'use_gating_for_weighting=False '
                                                      'and '
                                                      "softmax_choice='WEIGHTED_AVG' "
                                                      'at learn() time, otherwise '
                                                      'raises. Has no effect when '
                                                      'concatenate_queries is true or '
                                                      'there is only one key.',
                                       'type': 'boolean'},
                  'field_names': { 'default': None,
                                   'description': 'Names for each field, in '
                                                  'memory_template order. Length must '
                                                  'equal num_fields. Ignored (with '
                                                  'warning) if `fields` is provided.',
                                   'items': {'type': 'string'},
                                   'type': ['array', 'null']},
                  'field_weights': { 'default': None,
                                     'description': 'Per-field weight: positive number '
                                                    '= KEY field with that '
                                                    'contribution to matching; null = '
                                                    'VALUE field (stored/retrieved, '
                                                    'not matched). Length must equal '
                                                    'num_fields, or 1 (broadcast). '
                                                    'Cannot be all-null. Ignored (with '
                                                    'warning) if `fields` is provided.',
                                     'items': {'type': ['number', 'null']},
                                     'type': ['array', 'null']},
                  'fields': { 'additionalProperties': { 'oneOf': [ { 'description': '[field_weight '
                                                                                    '(number '
                                                                                    'or '
                                                                                    'null '
                                                                                    'for '
                                                                                    'value '
                                                                                    'field), '
                                                                                    'learn_field_weight '
                                                                                    '(bool|number|null), '
                                                                                    'target_field '
                                                                                    '(bool)]',
                                                                     'maxItems': 3,
                                                                     'minItems': 3,
                                                                     'type': 'array'},
                                                                   { 'properties': { 'field_weight': { 'description': 'null '
                                                                                                                      'marks '
                                                                                                                      'the '
                                                                                                                      'field '
                                                                                                                      'as '
                                                                                                                      'a '
                                                                                                                      'VALUE '
                                                                                                                      'field '
                                                                                                                      '(stored/retrieved '
                                                                                                                      'but '
                                                                                                                      'not '
                                                                                                                      'used '
                                                                                                                      'for '
                                                                                                                      'matching); '
                                                                                                                      'a '
                                                                                                                      'positive '
                                                                                                                      'number '
                                                                                                                      'marks '
                                                                                                                      'it '
                                                                                                                      'as '
                                                                                                                      'a '
                                                                                                                      'KEY '
                                                                                                                      'field '
                                                                                                                      'with '
                                                                                                                      'that '
                                                                                                                      'weight.',
                                                                                                       'type': [ 'number',
                                                                                                                 'null']},
                                                                                     'learn_field_weight': { 'description': 'false '
                                                                                                                            'to '
                                                                                                                            'disable '
                                                                                                                            'learning '
                                                                                                                            'for '
                                                                                                                            'this '
                                                                                                                            'field, '
                                                                                                                            'true/null '
                                                                                                                            'for '
                                                                                                                            'default '
                                                                                                                            'learning_rate, '
                                                                                                                            'or '
                                                                                                                            'a '
                                                                                                                            'numeric '
                                                                                                                            'per-field '
                                                                                                                            'learning '
                                                                                                                            'rate. '
                                                                                                                            'Ignored '
                                                                                                                            'for '
                                                                                                                            'value '
                                                                                                                            'fields.'},
                                                                                     'target_field': { 'description': 'Whether '
                                                                                                                      'to '
                                                                                                                      'construct '
                                                                                                                      'a '
                                                                                                                      'learning '
                                                                                                                      'pathway '
                                                                                                                      'terminating '
                                                                                                                      'at '
                                                                                                                      'this '
                                                                                                                      "field's "
                                                                                                                      'retrieved_node.',
                                                                                                       'type': 'boolean'}},
                                                                     'required': [ 'field_weight',
                                                                                   'learn_field_weight',
                                                                                   'target_field'],
                                                                     'type': 'object'}]},
                              'default': None,
                              'description': 'Per-field config keyed by field name. '
                                             'EACH value MUST be either (a) a '
                                             '3-element array [field_weight, '
                                             'learn_field_weight, target_field], or '
                                             '(b) an object containing ALL three keys '
                                             "'field_weight', 'learn_field_weight', "
                                             "'target_field' (lowercase). Partial "
                                             'dicts raise KeyError. When `fields` is '
                                             'given, do NOT also pass '
                                             'field_names/field_weights/learn_field_weights/target_fields '
                                             '— they are silently overridden and warn.',
                              'type': ['object', 'null']},
                  'learn_field_weights': { 'default': False,
                                           'description': 'Whether/how to learn each '
                                                          "field's weight. bool "
                                                          'applies to all keys; list '
                                                          '(length num_fields) gives '
                                                          'per-field bool or numeric '
                                                          'learning rate. Forced False '
                                                          'for value fields. Ignored '
                                                          '(with warning) if `fields` '
                                                          'is provided.',
                                           'oneOf': [ {'type': 'boolean'},
                                                      { 'items': { 'type': [ 'boolean',
                                                                             'number',
                                                                             'null']},
                                                        'type': 'array'}]},
                  'learning_rate': { 'default': 0.01,
                                     'description': 'Default learning rate applied to '
                                                    'any field weight whose '
                                                    'learn_field_weights entry is '
                                                    'True/None. Dict form is NOT '
                                                    'supported by EMComposition '
                                                    '(raises EMCompositionError) — use '
                                                    '`fields` or `learn_field_weights` '
                                                    'for per-field rates.',
                                     'oneOf': [ {'type': 'number'},
                                                {'type': 'boolean'}]},
                  'memory_capacity': { 'default': None,
                                       'description': 'Number of entries the memory '
                                                      'can hold. Required if '
                                                      'memory_template is a 2-tuple or '
                                                      'a single-entry 2D template; '
                                                      'otherwise defaults to 1000 or '
                                                      'to len(memory_template) for 3D '
                                                      'templates.',
                                       'minimum': 1,
                                       'type': ['integer', 'null']},
                  'memory_decay_rate': { 'default': 'AUTO',
                                         'description': 'Multiplicative decay applied '
                                                        'to existing memories before '
                                                        'each new write. Numeric in '
                                                        '[0,1] (0 = no decay), or '
                                                        "'AUTO' which sets it to "
                                                        '1/memory_capacity.',
                                         'oneOf': [ { 'maximum': 1,
                                                      'minimum': 0,
                                                      'type': 'number'},
                                                    { 'enum': ['AUTO'],
                                                      'type': 'string'}]},
                  'memory_fill': { 'default': 0,
                                   'description': 'Value used to populate empty slots: '
                                                  'scalar (constant fill) or a '
                                                  '2-element [low, high] tuple '
                                                  '(uniform random fill). Important '
                                                  'when normalize_memories=True — a '
                                                  'field of all zeros causes a '
                                                  'divide-by-zero warning at '
                                                  'construction and NaN matches at '
                                                  'runtime.',
                                   'oneOf': [ {'type': 'number'},
                                              { 'items': {'type': 'number'},
                                                'maxItems': 2,
                                                'minItems': 2,
                                                'type': 'array'}]},
                  'memory_template': { 'default': [[0], [0]],
                                       'description': 'Shape/content of an entry. (1) '
                                                      '2-tuple (num_fields, field_len) '
                                                      'or 3-tuple (num_entries, '
                                                      'num_fields, field_len) of ints '
                                                      '— shape only, contents come '
                                                      'from memory_fill. (2) 2D '
                                                      'list/array — a single entry '
                                                      'template, replicated '
                                                      'memory_capacity times. (3) 3D '
                                                      'list/array — explicit per-entry '
                                                      'contents (rows are entries, '
                                                      'columns are fields). Fields may '
                                                      'have different lengths only '
                                                      'when given via list/array, not '
                                                      'via tuple-of-ints.',
                                       'oneOf': [ { 'items': {'type': 'integer'},
                                                    'maxItems': 3,
                                                    'minItems': 2,
                                                    'type': 'array'},
                                                  { 'items': { 'items': { 'type': 'number'},
                                                               'type': 'array'},
                                                    'type': 'array'},
                                                  { 'items': { 'items': { 'items': { 'type': 'number'},
                                                                          'type': 'array'},
                                                               'type': 'array'},
                                                    'type': 'array'}]},
                  'name': { 'default': 'EM_Composition',
                            'description': 'Name of the EMComposition instance.',
                            'type': 'string'},
                  'normalize_field_weights': { 'default': True,
                                               'description': 'If true, key '
                                                              'field_weights are '
                                                              'renormalized to sum to '
                                                              '1; if false, used as '
                                                              'absolute weights.',
                                               'type': 'boolean'},
                  'normalize_memories': { 'default': True,
                                          'description': 'If true, queries and stored '
                                                         'keys are L2-normalized '
                                                         'before dot-product (cosine '
                                                         'similarity). Required by '
                                                         'concatenate_queries.',
                                          'type': 'boolean'},
                  'purge_by_field_weights': { 'default': False,
                                              'description': 'If true, the row chosen '
                                                             'for replacement on '
                                                             'storage is the weakest '
                                                             'after multiplying field '
                                                             'norms by field_weights '
                                                             '(so unweighted/value '
                                                             "fields don't influence "
                                                             'which slot is '
                                                             'overwritten).',
                                              'type': 'boolean'},
                  'seed': { 'default': None,
                            'description': 'Seed for the random_state used by '
                                           'storage_prob and random memory_fill.',
                            'type': ['integer', 'null']},
                  'softmax_choice': { 'default': 'WEIGHTED_AVG',
                                      'description': 'How softmax output is used for '
                                                     'retrieval. WEIGHTED_AVG = '
                                                     'standard softmax-weighted '
                                                     'average over entries (the only '
                                                     'choice compatible with '
                                                     'learning). ARG_MAX = pick the '
                                                     'single best-matching entry '
                                                     '(internally rewritten to '
                                                     'ARG_MAX_INDICATOR). NOTE: '
                                                     "'PROBABILISTIC' appears in the "
                                                     'docstring but is BROKEN in the '
                                                     'current PNL build — it is '
                                                     'forwarded raw to OneHot.mode '
                                                     'which only accepts '
                                                     "{'PROB','PROB_INDICATOR',...}, "
                                                     'so it raises a Beartype error at '
                                                     'construction. Do not use it.',
                                      'enum': ['WEIGHTED_AVG', 'ARG_MAX'],
                                      'type': 'string'},
                  'softmax_gain': { 'default': 1,
                                    'description': 'Inverse-temperature for the '
                                                   'retrieval softmax. Numeric scalar '
                                                   "OR the keyword 'ADAPTIVE' "
                                                   "(entropy-weighted) OR 'CONTROL' "
                                                   '(constructs a SOFTMAX GAIN CONTROL '
                                                   'node that adapts gain at runtime; '
                                                   'this also forces softmax_gain to '
                                                   'be non-modulable).',
                                    'oneOf': [ {'type': 'number'},
                                               { 'enum': ['ADAPTIVE', 'CONTROL'],
                                                 'type': 'string'}]},
                  'softmax_threshold': { 'default': 0.001,
                                         'description': 'Mask cutoff: values below '
                                                        'this are zeroed before '
                                                        'softmax. Must be > 0 if not '
                                                        'null.',
                                         'type': ['number', 'null']},
                  'storage_prob': { 'default': 1,
                                    'description': 'Per-execution probability that the '
                                                   'current input is written into '
                                                   'memory. 0 disables storage; 1 '
                                                   'always stores.',
                                    'maximum': 1,
                                    'minimum': 0,
                                    'type': 'number'},
                  'store_on_optimization': { 'default': 'FIRST',
                                             'description': 'Which optimization '
                                                            'step(s) inside a learning '
                                                            'trial actually store an '
                                                            'entry.',
                                             'enum': ['FIRST', 'LAST', 'ALL'],
                                             'type': 'string'},
                  'target_fields': { 'default': None,
                                     'description': 'Per-field bool: which retrieved '
                                                    'fields should receive an error '
                                                    'signal during learning. Length '
                                                    'must equal num_fields. Ignored '
                                                    '(with warning) if `fields` is '
                                                    'provided.',
                                     'items': {'type': 'boolean'},
                                     'type': ['array', 'null']},
                  'use_gating_for_weighting': { 'default': False,
                                                'description': 'If true, weight match '
                                                               'outputs via output '
                                                               'gating '
                                                               '(GatingMechanism) '
                                                               'instead of '
                                                               'multiplicative '
                                                               'ProcessingMechanisms; '
                                                               'in that case no '
                                                               'weighted_match_nodes '
                                                               'are built and field '
                                                               'weights cannot be '
                                                               'learned (must combine '
                                                               'with '
                                                               'enable_learning=False).',
                                                'type': 'boolean'},
                  'use_storage_node': { 'default': True,
                                        'description': 'If true (recommended/default), '
                                                       'an EMStorageMechanism handles '
                                                       'writes. If false, storage runs '
                                                       'as a Composition method '
                                                       'instead — debug only, and '
                                                       'prevents the EMComposition '
                                                       'from being imported into '
                                                       'another Composition via '
                                                       'import_composition.',
                                        'type': 'boolean'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = 'FEEDBACK-DRIVEN GOTCHAS:\n\n1. softmax_choice=\'PROBABILISTIC\' is documented but BROKEN in the current PNL build: EMComposition forwards the raw string to SoftMax → OneHot.mode, whose Literal only accepts {\'deterministic\',\'PROB\',\'PROB_INDICATOR\',\'arg_max\',...,\'MIN_ABS_INDICATOR\'}. Result: BeartypeCallHintParamViolation at construction. The schema therefore exposes only WEIGHTED_AVG and ARG_MAX. If the caller wants categorical sampling, omit softmax_choice and either (a) post-sample externally from the softmax output, or (b) wait for an upstream PNL fix. ARG_MAX is rewritten internally to ARG_MAX_INDICATOR.\n\n2. `fields` dict entries must be COMPLETE: either a 3-tuple/list [field_weight, learn_field_weight, target_field] or an object with ALL three lowercase keys \'field_weight\', \'learn_field_weight\', \'target_field\'. Passing only a subset (e.g. {\'field_weight\': 1.0}) raises KeyError because _parse_fields_dict indexes the constants directly. Mark value fields with field_weight=null (None), not 0 — 0 means "key field currently weighted to zero; ignored at retrieval but still a key".\n\n3. `fields` and the legacy args (field_names/field_weights/learn_field_weights/target_fields) are mutually exclusive in spirit; passing both warns and the legacy args are dropped.\n\nOTHER GOTCHAS:\n\n- field_weights default if not given and num_fields>1: all keys with weight 1 except the LAST field, which becomes a value (None). Single-field default is [1].\n- memory_template tuple form: 2-tuple = (num_fields, field_len) and needs memory_capacity; 3-tuple\'s first element MUST equal memory_capacity if both given.\n- memory_fill must avoid all-zero key fields when normalize_memories=True — the constructor warns and runtime will divide by zero.\n- learning_rate as a dict raises EMCompositionError; per-field rates go in `fields` or `learn_field_weights`.\n- enable_learning is silently neutralized (with a runtime warning at learn()) when concatenate_queries is true or num_keys==1.\n- use_gating_for_weighting=True is incompatible with enable_learning=True at learn() time (raises).\n- After construction, add_node/add_projection from outside raise — EMComposition is treated as immutable post-build; nest it as-is.\n- Returned object is a Composition; query_input_nodes / value_input_nodes / retrieved_nodes / softmax_node / storage_node are auto-named with [QUERY]/[VALUE]/[RETRIEVED] suffixes (or KEY_n_INPUT / VALUE_n_INPUT if field_names not provided).'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.EMComposition
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
    def create_em_composition(args: dict[str, Any] | None = None) -> Any:
        'Build a differentiable, learnable episodic memory module (subclass of `AutodiffComposition`) where retrieval is a softmax over field-weighted dot-product (or 1-L0) similarities between input keys and stored entries, and storage replaces the weakest memory row at each execution step.'
        return _impl(args or {})
