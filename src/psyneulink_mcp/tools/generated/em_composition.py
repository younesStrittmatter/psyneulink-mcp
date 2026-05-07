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
TOOL_DESCRIPTION = 'Construct an EMComposition — a differentiable episodic memory module that subclasses AutodiffComposition. Use it when the model needs content-addressable retrieval over a fixed-size memory matrix (key fields used for similarity matching, optional value fields stored alongside), with optional learnable field weights and softmax-based retrieval. Returns a Composition handle that can be run, learned, or nested inside another Composition. Properties exposed beyond Composition/AutodiffComposition include `memory`, `memory_capacity`, `field_names`, `field_weights`, `query_input_nodes`, `value_input_nodes`, `match_nodes`, `retrieved_nodes`, and `storage_node`.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "concatenate_queries": {\n      "default": false,\n      "description": "If true, concatenate all key fields into a single vector before matching. Auto-disabled (with warning) unless there is more than one key, all key weights are equal, AND `normalize_memories` is true. Incompatible with learning of field weights.",\n      "type": "boolean"\n    },\n    "enable_learning": {\n      "default": true,\n      "description": "Enables learning of field weights. Must be False if `use_gating_for_weighting=true` (otherwise `learn()` will raise). Has no effect when there is only one key, or when `concatenate_queries=true`.",\n      "type": "boolean"\n    },\n    "field_names": {\n      "description": "Names for each field. Length must equal number of fields in memory_template. Key fields are named `<name> [QUERY]`, value fields `<name> [VALUE]`.",\n      "items": {\n        "type": "string"\n      },\n      "type": "array"\n    },\n    "field_weights": {\n      "description": "Per-field retrieval weight. A field with weight `null` (None) is treated as a VALUE field (stored/retrieved but not used for matching); any non-null number makes the field a KEY. All non-null weights must be >= 0. Default treats every field as a key with weight 1 except the last, which becomes a value. Length must equal number of fields, or be a single scalar.",\n      "items": {\n        "type": [\n          "number",\n          "null"\n        ]\n      },\n      "type": "array"\n    },\n    "fields": {\n      "additionalProperties": true,\n      "description": "Dict mapping field name -> [field_weight, learn_field_weight, target_field] or {field_weight, learn_field_weight, target_field}. If specified, `field_names`, `field_weights`, `learn_field_weights`, and `target_fields` MUST NOT be specified (raises an error / warning). Number of entries must equal the number of fields in `memory_template`.",\n      "type": "object"\n    },\n    "learn_field_weights": {\n      "description": "Whether `field_weights` are learnable. Bool to apply uniformly, or list (length = number of fields) of bool / numeric per-field learning rates / None. Numeric entries override `learning_rate` for that field. For value fields (weight=null) this is forced to False.",\n      "oneOf": [\n        {\n          "type": "boolean"\n        },\n        {\n          "items": {\n            "type": [\n              "boolean",\n              "number",\n              "null"\n            ]\n          },\n          "type": "array"\n        }\n      ]\n    },\n    "learning_rate": {\n      "description": "Default learning rate for field-weight projections not individually specified in `learn_field_weights`. Default 0.001 (inherited from AutodiffComposition). Dict form is NOT supported \\u2014 use `learn_field_weights` for per-field rates.",\n      "type": "number"\n    },\n    "memory_capacity": {\n      "description": "Number of entries the memory holds. If `memory_template` is a 3D array with N entries, `memory_capacity` must be >= N (extra slots get filled by `memory_fill`). Defaults to 1000.",\n      "type": "integer"\n    },\n    "memory_decay_rate": {\n      "default": "AUTO",\n      "description": "Per-step decay applied to all memory entries before a new write. A number in [0, 1], or the keyword \'AUTO\' to use 1/memory_capacity (the default). Use 0 to disable decay.",\n      "oneOf": [\n        {\n          "type": "number"\n        },\n        {\n          "enum": [\n            "AUTO"\n          ],\n          "type": "string"\n        },\n        {\n          "type": "null"\n        }\n      ]\n    },\n    "memory_fill": {\n      "default": 0,\n      "description": "Scalar value used to fill empty memory slots (where `memory_template` is zero). Must be a single number \\u2014 see notes about random-range fill.",\n      "type": "number"\n    },\n    "memory_template": {\n      "description": "Shape of an entry in memory. 2D form `[[field0_values...], [field1_values...], ...]` specifies a single template entry that is replicated across `memory_capacity` slots; field vectors may have DIFFERENT lengths. 3D form `[[[..],[..]], [[..],[..]], ...]` specifies multiple full entries (all entries must share the same per-field shape). Any non-zero values in the template are kept verbatim; zero entries are overwritten with `memory_fill`. Default `[[0],[0]]` = 2 scalar fields.",\n      "items": {\n        "items": {},\n        "type": "array"\n      },\n      "type": "array"\n    },\n    "name": {\n      "default": "EM_Composition",\n      "description": "Name of the composition.",\n      "type": "string"\n    },\n    "normalize_field_weights": {\n      "default": true,\n      "description": "If true, weights are normalized across keys so they sum to 1; if false, used as absolute weights.",\n      "type": "boolean"\n    },\n    "normalize_memories": {\n      "default": true,\n      "description": "If true, queries and stored keys are L2-normalized before computing dot-product similarity (i.e., cosine similarity). Required for `concatenate_queries=true`.",\n      "type": "boolean"\n    },\n    "purge_by_field_weights": {\n      "default": false,\n      "description": "If true, weight per-field norms by `field_weights` when picking the slot to overwrite on storage.",\n      "type": "boolean"\n    },\n    "seed": {\n      "description": "Seed for the random number generator (used for memory_fill ranges, probabilistic storage, etc.).",\n      "type": "integer"\n    },\n    "softmax_choice": {\n      "default": "WEIGHTED_AVG",\n      "description": "How softmax over distances is consumed for retrieval. Only WEIGHTED_AVG is compatible with learning \\u2014 ARG_MAX/PROBABILISTIC raise an error if `learn()` is called.",\n      "enum": [\n        "WEIGHTED_AVG",\n        "ARG_MAX",\n        "PROBABILISTIC"\n      ],\n      "type": "string"\n    },\n    "softmax_gain": {\n      "default": 1,\n      "description": "Inverse temperature for softmax over match scores. Number, or the keyword strings \'ADAPTIVE\' or \'CONTROL\'. With \'CONTROL\', a ControlMechanism adapts the gain at runtime.",\n      "oneOf": [\n        {\n          "type": "number"\n        },\n        {\n          "enum": [\n            "ADAPTIVE",\n            "CONTROL"\n          ],\n          "type": "string"\n        }\n      ]\n    },\n    "softmax_threshold": {\n      "default": 0.001,\n      "description": "Mask threshold below which softmax inputs are zeroed. Must be > 0 if not null.",\n      "type": [\n        "number",\n        "null"\n      ]\n    },\n    "storage_prob": {\n      "default": 1,\n      "description": "Probability per execution that the current input is written to memory. Must be in [0, 1].",\n      "type": "number"\n    },\n    "store_on_optimization": {\n      "default": "FIRST",\n      "description": "Which optimization step(s) trigger storage during learning.",\n      "enum": [\n        "FIRST",\n        "LAST",\n        "ALL"\n      ],\n      "type": "string"\n    },\n    "target_fields": {\n      "description": "List of bools, one per field, marking which retrieved fields receive an error signal during learning. Defaults to all True. Mutually exclusive with the `fields` dict argument.",\n      "items": {\n        "type": "boolean"\n      },\n      "type": "array"\n    },\n    "use_gating_for_weighting": {\n      "default": false,\n      "description": "If true, use a GatingMechanism to apply field weights instead of multiplying inputs. Forces `enable_learning=false` (otherwise `learn()` raises).",\n      "type": "boolean"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\nmemory_fill gotcha (recent feedback, GitHub issue #40): PsyNeuLink\'s validator accepts ONLY a Python scalar (int/float) or a 2-element TUPLE `(low, high)` for random-range fill — a Python list of length 2 is rejected with `must be a float, int or len tuple of ints and/or floats`. JSON arrays deserialize to lists, so the random-range form cannot be expressed through this schema; pass a single scalar instead (e.g. `memory_fill: 0.0001`). If true random initialization is needed, set `memory_template` directly with the desired noise pre-baked into its values.\n\nmemory_template shape rules: in 2D form, fields may have different vector lengths (e.g. one field of length 20 and another of length 25 is valid — that\'s a single template entry with two heterogeneously-sized fields). In 3D form, ALL entries must share the same per-field shape. A 3D template with `len(memory_template) > memory_capacity` raises an error.\n\n`fields` vs `field_names`/`field_weights`/`learn_field_weights`/`target_fields`: pick one or the other — combining them raises an error or warning.\n\nfield_weights semantics: `null` (None) marks a VALUE field (no matching, only stored/retrieved). Non-null = KEY. All-zero or all-None weights produce warnings/errors. Default when more than one field is present makes the LAST field a value and all others keys with weight 1.\n\nDefault `field_weights=(1, 0)` from the docstring is misleading — the actual default in `_parse_fields` is `[1, 1, ..., None]` (last field becomes a value field).\n\nLearning constraints: `concatenate_queries=true` is incompatible with learning of field weights and `infer_backpropagation_learning_pathways` will raise. ARG_MAX / PROBABILISTIC `softmax_choice` raise on `learn()`. `use_gating_for_weighting=true` + `enable_learning=true` raise on `learn()`.\n\n`memory_decay_rate=AUTO` resolves to `1 / memory_capacity` at construction.\n\nInitializing all-zero key fields with `normalize_memories=true` triggers a divide-by-zero warning — provide a non-zero `memory_fill` (or non-zero values in the template) to avoid it.\n\nThe returned EMComposition can be nested in another Composition only when `use_storage_node=true` (the default).'
TOOL_PARAMETERS = { 'properties': { 'concatenate_queries': { 'default': False,
                                           'description': 'If true, concatenate all '
                                                          'key fields into a single '
                                                          'vector before matching. '
                                                          'Auto-disabled (with '
                                                          'warning) unless there is '
                                                          'more than one key, all key '
                                                          'weights are equal, AND '
                                                          '`normalize_memories` is '
                                                          'true. Incompatible with '
                                                          'learning of field weights.',
                                           'type': 'boolean'},
                  'enable_learning': { 'default': True,
                                       'description': 'Enables learning of field '
                                                      'weights. Must be False if '
                                                      '`use_gating_for_weighting=true` '
                                                      '(otherwise `learn()` will '
                                                      'raise). Has no effect when '
                                                      'there is only one key, or when '
                                                      '`concatenate_queries=true`.',
                                       'type': 'boolean'},
                  'field_names': { 'description': 'Names for each field. Length must '
                                                  'equal number of fields in '
                                                  'memory_template. Key fields are '
                                                  'named `<name> [QUERY]`, value '
                                                  'fields `<name> [VALUE]`.',
                                   'items': {'type': 'string'},
                                   'type': 'array'},
                  'field_weights': { 'description': 'Per-field retrieval weight. A '
                                                    'field with weight `null` (None) '
                                                    'is treated as a VALUE field '
                                                    '(stored/retrieved but not used '
                                                    'for matching); any non-null '
                                                    'number makes the field a KEY. All '
                                                    'non-null weights must be >= 0. '
                                                    'Default treats every field as a '
                                                    'key with weight 1 except the '
                                                    'last, which becomes a value. '
                                                    'Length must equal number of '
                                                    'fields, or be a single scalar.',
                                     'items': {'type': ['number', 'null']},
                                     'type': 'array'},
                  'fields': { 'additionalProperties': True,
                              'description': 'Dict mapping field name -> '
                                             '[field_weight, learn_field_weight, '
                                             'target_field] or {field_weight, '
                                             'learn_field_weight, target_field}. If '
                                             'specified, `field_names`, '
                                             '`field_weights`, `learn_field_weights`, '
                                             'and `target_fields` MUST NOT be '
                                             'specified (raises an error / warning). '
                                             'Number of entries must equal the number '
                                             'of fields in `memory_template`.',
                              'type': 'object'},
                  'learn_field_weights': { 'description': 'Whether `field_weights` are '
                                                          'learnable. Bool to apply '
                                                          'uniformly, or list (length '
                                                          '= number of fields) of bool '
                                                          '/ numeric per-field '
                                                          'learning rates / None. '
                                                          'Numeric entries override '
                                                          '`learning_rate` for that '
                                                          'field. For value fields '
                                                          '(weight=null) this is '
                                                          'forced to False.',
                                           'oneOf': [ {'type': 'boolean'},
                                                      { 'items': { 'type': [ 'boolean',
                                                                             'number',
                                                                             'null']},
                                                        'type': 'array'}]},
                  'learning_rate': { 'description': 'Default learning rate for '
                                                    'field-weight projections not '
                                                    'individually specified in '
                                                    '`learn_field_weights`. Default '
                                                    '0.001 (inherited from '
                                                    'AutodiffComposition). Dict form '
                                                    'is NOT supported — use '
                                                    '`learn_field_weights` for '
                                                    'per-field rates.',
                                     'type': 'number'},
                  'memory_capacity': { 'description': 'Number of entries the memory '
                                                      'holds. If `memory_template` is '
                                                      'a 3D array with N entries, '
                                                      '`memory_capacity` must be >= N '
                                                      '(extra slots get filled by '
                                                      '`memory_fill`). Defaults to '
                                                      '1000.',
                                       'type': 'integer'},
                  'memory_decay_rate': { 'default': 'AUTO',
                                         'description': 'Per-step decay applied to all '
                                                        'memory entries before a new '
                                                        'write. A number in [0, 1], or '
                                                        "the keyword 'AUTO' to use "
                                                        '1/memory_capacity (the '
                                                        'default). Use 0 to disable '
                                                        'decay.',
                                         'oneOf': [ {'type': 'number'},
                                                    { 'enum': ['AUTO'],
                                                      'type': 'string'},
                                                    {'type': 'null'}]},
                  'memory_fill': { 'default': 0,
                                   'description': 'Scalar value used to fill empty '
                                                  'memory slots (where '
                                                  '`memory_template` is zero). Must be '
                                                  'a single number — see notes about '
                                                  'random-range fill.',
                                   'type': 'number'},
                  'memory_template': { 'description': 'Shape of an entry in memory. 2D '
                                                      'form `[[field0_values...], '
                                                      '[field1_values...], ...]` '
                                                      'specifies a single template '
                                                      'entry that is replicated across '
                                                      '`memory_capacity` slots; field '
                                                      'vectors may have DIFFERENT '
                                                      'lengths. 3D form `[[[..],[..]], '
                                                      '[[..],[..]], ...]` specifies '
                                                      'multiple full entries (all '
                                                      'entries must share the same '
                                                      'per-field shape). Any non-zero '
                                                      'values in the template are kept '
                                                      'verbatim; zero entries are '
                                                      'overwritten with `memory_fill`. '
                                                      'Default `[[0],[0]]` = 2 scalar '
                                                      'fields.',
                                       'items': {'items': {}, 'type': 'array'},
                                       'type': 'array'},
                  'name': { 'default': 'EM_Composition',
                            'description': 'Name of the composition.',
                            'type': 'string'},
                  'normalize_field_weights': { 'default': True,
                                               'description': 'If true, weights are '
                                                              'normalized across keys '
                                                              'so they sum to 1; if '
                                                              'false, used as absolute '
                                                              'weights.',
                                               'type': 'boolean'},
                  'normalize_memories': { 'default': True,
                                          'description': 'If true, queries and stored '
                                                         'keys are L2-normalized '
                                                         'before computing dot-product '
                                                         'similarity (i.e., cosine '
                                                         'similarity). Required for '
                                                         '`concatenate_queries=true`.',
                                          'type': 'boolean'},
                  'purge_by_field_weights': { 'default': False,
                                              'description': 'If true, weight '
                                                             'per-field norms by '
                                                             '`field_weights` when '
                                                             'picking the slot to '
                                                             'overwrite on storage.',
                                              'type': 'boolean'},
                  'seed': { 'description': 'Seed for the random number generator (used '
                                           'for memory_fill ranges, probabilistic '
                                           'storage, etc.).',
                            'type': 'integer'},
                  'softmax_choice': { 'default': 'WEIGHTED_AVG',
                                      'description': 'How softmax over distances is '
                                                     'consumed for retrieval. Only '
                                                     'WEIGHTED_AVG is compatible with '
                                                     'learning — ARG_MAX/PROBABILISTIC '
                                                     'raise an error if `learn()` is '
                                                     'called.',
                                      'enum': [ 'WEIGHTED_AVG',
                                                'ARG_MAX',
                                                'PROBABILISTIC'],
                                      'type': 'string'},
                  'softmax_gain': { 'default': 1,
                                    'description': 'Inverse temperature for softmax '
                                                   'over match scores. Number, or the '
                                                   "keyword strings 'ADAPTIVE' or "
                                                   "'CONTROL'. With 'CONTROL', a "
                                                   'ControlMechanism adapts the gain '
                                                   'at runtime.',
                                    'oneOf': [ {'type': 'number'},
                                               { 'enum': ['ADAPTIVE', 'CONTROL'],
                                                 'type': 'string'}]},
                  'softmax_threshold': { 'default': 0.001,
                                         'description': 'Mask threshold below which '
                                                        'softmax inputs are zeroed. '
                                                        'Must be > 0 if not null.',
                                         'type': ['number', 'null']},
                  'storage_prob': { 'default': 1,
                                    'description': 'Probability per execution that the '
                                                   'current input is written to '
                                                   'memory. Must be in [0, 1].',
                                    'type': 'number'},
                  'store_on_optimization': { 'default': 'FIRST',
                                             'description': 'Which optimization '
                                                            'step(s) trigger storage '
                                                            'during learning.',
                                             'enum': ['FIRST', 'LAST', 'ALL'],
                                             'type': 'string'},
                  'target_fields': { 'description': 'List of bools, one per field, '
                                                    'marking which retrieved fields '
                                                    'receive an error signal during '
                                                    'learning. Defaults to all True. '
                                                    'Mutually exclusive with the '
                                                    '`fields` dict argument.',
                                     'items': {'type': 'boolean'},
                                     'type': 'array'},
                  'use_gating_for_weighting': { 'default': False,
                                                'description': 'If true, use a '
                                                               'GatingMechanism to '
                                                               'apply field weights '
                                                               'instead of multiplying '
                                                               'inputs. Forces '
                                                               '`enable_learning=false` '
                                                               '(otherwise `learn()` '
                                                               'raises).',
                                                'type': 'boolean'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = "memory_fill gotcha (recent feedback, GitHub issue #40): PsyNeuLink's validator accepts ONLY a Python scalar (int/float) or a 2-element TUPLE `(low, high)` for random-range fill — a Python list of length 2 is rejected with `must be a float, int or len tuple of ints and/or floats`. JSON arrays deserialize to lists, so the random-range form cannot be expressed through this schema; pass a single scalar instead (e.g. `memory_fill: 0.0001`). If true random initialization is needed, set `memory_template` directly with the desired noise pre-baked into its values.\n\nmemory_template shape rules: in 2D form, fields may have different vector lengths (e.g. one field of length 20 and another of length 25 is valid — that's a single template entry with two heterogeneously-sized fields). In 3D form, ALL entries must share the same per-field shape. A 3D template with `len(memory_template) > memory_capacity` raises an error.\n\n`fields` vs `field_names`/`field_weights`/`learn_field_weights`/`target_fields`: pick one or the other — combining them raises an error or warning.\n\nfield_weights semantics: `null` (None) marks a VALUE field (no matching, only stored/retrieved). Non-null = KEY. All-zero or all-None weights produce warnings/errors. Default when more than one field is present makes the LAST field a value and all others keys with weight 1.\n\nDefault `field_weights=(1, 0)` from the docstring is misleading — the actual default in `_parse_fields` is `[1, 1, ..., None]` (last field becomes a value field).\n\nLearning constraints: `concatenate_queries=true` is incompatible with learning of field weights and `infer_backpropagation_learning_pathways` will raise. ARG_MAX / PROBABILISTIC `softmax_choice` raise on `learn()`. `use_gating_for_weighting=true` + `enable_learning=true` raise on `learn()`.\n\n`memory_decay_rate=AUTO` resolves to `1 / memory_capacity` at construction.\n\nInitializing all-zero key fields with `normalize_memories=true` triggers a divide-by-zero warning — provide a non-zero `memory_fill` (or non-zero values in the template) to avoid it.\n\nThe returned EMComposition can be nested in another Composition only when `use_storage_node=true` (the default)."


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
        'Construct an EMComposition — a differentiable episodic memory module that subclasses AutodiffComposition.'
        return _impl(args or {})
