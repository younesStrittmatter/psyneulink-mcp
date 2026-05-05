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
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_em_composition'
TOOL_DESCRIPTION = 'Call this tool to construct an episodic memory Composition that stores multi-field vector entries and retrieves the closest match via weighted softmax similarity over key fields. Use it when modeling content-addressable, hippocampal-style memory where the agent needs to store (key, value) pairs and later retrieve values by presenting a query key. The result is an EMComposition instance with `query_input_nodes`, `value_input_nodes`, and `retrieved_nodes` that can be embedded in a larger Composition or run standalone.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "concatenate_queries": {\n      "default": false,\n      "description": "If true, all key inputs are concatenated into a single vector before matching. Silently ignored (with a warning) if field_weights are not all equal, normalize_memories=False, or there is only one key field. Cannot be used with learning.",\n      "type": "boolean"\n    },\n    "enable_learning": {\n      "default": true,\n      "description": "Whether to enable backpropagation learning of field_weights. Requires use_gating_for_weighting=False and softmax_choice=WEIGHTED_AVG during learn(). Default true.",\n      "type": "boolean"\n    },\n    "field_names": {\n      "description": "Names for each field in memory_template, in order. Skip if using the \'fields\' dict.",\n      "items": {\n        "type": "string"\n      },\n      "type": "array"\n    },\n    "field_weights": {\n      "description": "Weight for each field. Positive values mark a field as a \'key\' used for matching; null marks it as a \'value\' (stored/retrieved but not matched). Default: all fields are keys except the last, which is a value. E.g., [1, 1, null] = two key fields, one value field.",\n      "items": {\n        "type": [\n          "number",\n          "null"\n        ]\n      },\n      "type": "array"\n    },\n    "fields": {\n      "additionalProperties": {},\n      "description": "Preferred way to configure fields. Dict mapping field name (string) to a 3-element list/tuple [field_weight, learn_field_weight, target_field] or a dict with keys \'field_weight\', \'learn_field_weight\', \'target_field\'. Using this arg replaces field_names, field_weights, learn_field_weights, and target_fields \\u2014 specifying those alongside raises a warning.",\n      "type": "object"\n    },\n    "learn_field_weights": {\n      "description": "Whether field_weights are learnable. True/False applies to all key fields; a list allows per-field control (booleans, floats for per-field learning rate, or null to use default learning_rate). Value fields are always forced to False.",\n      "oneOf": [\n        {\n          "type": "boolean"\n        },\n        {\n          "items": {\n            "type": [\n              "boolean",\n              "number",\n              "null"\n            ]\n          },\n          "type": "array"\n        }\n      ]\n    },\n    "learning_rate": {\n      "description": "Default learning rate for field_weights not given an explicit rate via learn_field_weights or fields. Applies only to learnable key fields.",\n      "type": "number"\n    },\n    "memory_capacity": {\n      "description": "Maximum number of entries the memory can hold. Defaults to 1000 if not specified. Also determines the default memory_decay_rate (AUTO = 1/memory_capacity).",\n      "type": "integer"\n    },\n    "memory_decay_rate": {\n      "default": "AUTO",\n      "description": "Rate at which stored memories decay on each storage event. AUTO (default) sets decay = 1/memory_capacity. Pass a float in [0, 1] to override, or 0 to disable decay.",\n      "oneOf": [\n        {\n          "maximum": 1,\n          "minimum": 0,\n          "type": "number"\n        },\n        {\n          "enum": [\n            "AUTO"\n          ],\n          "type": "string"\n        }\n      ]\n    },\n    "memory_fill": {\n      "description": "Value used to initialize empty memory slots. Use 0 (default) for zeros, a float for a constant, or a 2-tuple (low, high) for uniform random fill. Avoid all-zero key fields when normalize_memories=True to prevent divide-by-zero.",\n      "oneOf": [\n        {\n          "type": "number"\n        },\n        {\n          "items": {\n            "type": "number"\n          },\n          "maxItems": 2,\n          "minItems": 2,\n          "type": "array"\n        }\n      ]\n    },\n    "memory_template": {\n      "description": "Shape of a single memory entry. A 2D list/array where each inner list is one field (e.g., [[0,0,0],[0,0,0]] = 2 fields of size 3). Can also be a 3D array to pre-populate memory with specific entries, or a length-2 tuple (num_fields, field_size) for uniform fields.",\n      "items": {},\n      "type": "array"\n    },\n    "name": {\n      "default": "EM_Composition",\n      "description": "Name of the EMComposition instance.",\n      "type": "string"\n    },\n    "normalize_field_weights": {\n      "default": true,\n      "description": "If true (default), field_weights are normalized to sum to 1 across key fields before use. Set false to use raw weights as absolute contributions.",\n      "type": "boolean"\n    },\n    "normalize_memories": {\n      "default": true,\n      "description": "If true (default), both query vectors and stored memory vectors are L2-normalized before computing dot-product similarity.",\n      "type": "boolean"\n    },\n    "purge_by_field_weights": {\n      "default": false,\n      "description": "If true, field_weights are used to select which stored memory to replace when capacity is full (weakest weighted memory is purged). Default false (replaces lowest-norm memory).",\n      "type": "boolean"\n    },\n    "softmax_choice": {\n      "default": "WEIGHTED_AVG",\n      "description": "How the softmax distribution is used for retrieval. WEIGHTED_AVG (default) returns a weighted average over all memories. ARG_MAX returns the best-matching memory. PROBABILISTIC samples one memory. ARG_MAX and PROBABILISTIC cannot be used with enable_learning=True.",\n      "enum": [\n        "WEIGHTED_AVG",\n        "ARG_MAX",\n        "PROBABILISTIC"\n      ],\n      "type": "string"\n    },\n    "softmax_gain": {\n      "default": 1,\n      "description": "Inverse temperature for the softmax over match scores. A float sets a fixed gain; \'ADAPTIVE\' uses entropy-based adaptation; \'CONTROL\' adds a ControlMechanism that dynamically sets gain.",\n      "oneOf": [\n        {\n          "type": "number"\n        },\n        {\n          "enum": [\n            "ADAPTIVE",\n            "CONTROL"\n          ],\n          "type": "string"\n        }\n      ]\n    },\n    "softmax_threshold": {\n      "default": 0.001,\n      "description": "Values below this threshold in the softmax input are masked to zero before normalization. Default 0.001.",\n      "type": "number"\n    },\n    "storage_prob": {\n      "default": 1,\n      "description": "Probability [0, 1] that each execution stores the current input into memory. Default 1.0 (always store).",\n      "type": "number"\n    },\n    "store_on_optimization": {\n      "default": "FIRST",\n      "description": "During learning, which optimization step(s) trigger memory storage: FIRST (default), LAST, or ALL.",\n      "enum": [\n        "FIRST",\n        "LAST",\n        "ALL"\n      ],\n      "type": "string"\n    },\n    "target_fields": {\n      "description": "List of booleans (one per field) indicating which fields provide error signals during learning. Default: all fields are target fields. Skip if using the \'fields\' dict.",\n      "items": {\n        "type": "boolean"\n      },\n      "type": "array"\n    },\n    "use_gating_for_weighting": {\n      "default": false,\n      "description": "If true, uses GatingMechanisms (output gating) to apply field weights instead of a standard weighted input. Incompatible with enable_learning=True.",\n      "type": "boolean"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\n- The `fields` dict is the preferred single-arg way to configure all field properties at once; mixing it with field_names/field_weights/learn_field_weights/target_fields raises a warning (fields wins).\n- Default field_weights behavior when omitted: if memory_template has 1 field, weight=[1] (all keys); if >1 fields, all are keys except the last field, which is a value (weight=None).\n- memory_capacity defaults to 1000 (not None as the signature suggests) via Parameters.memory_capacity default.\n- memory_decay_rate AUTO is computed at construction as 1/memory_capacity; pass 0 to disable decay entirely.\n- Initializing memory_template with all-zero key fields will trigger a warning about divide-by-zero when normalize_memories=True. Use memory_fill=(low, high) or a nonzero scalar to avoid this.\n- concatenate_queries is silently overridden to False (with a warning) if: field weights are not all equal, normalize_memories=False, or there is only one key field.\n- ARG_MAX and PROBABILISTIC softmax_choice raise EMCompositionError if learn() is called.\n- use_gating_for_weighting=True + enable_learning=True raises EMCompositionError on learn() call.\n- Nodes and Projections cannot be added to an EMComposition after construction (raises EMCompositionError).\n- learning_rate as a dict is not supported for EMComposition (raises error); use the fields arg or learn_field_weights for per-field rates.\n- When enable_learning=True but there is only one key or concatenate_queries=True, field weight learning has no effect and enable_learning is effectively forced to False at learn() time (with a warning).'
TOOL_PARAMETERS = { 'properties': { 'concatenate_queries': { 'default': False,
                                           'description': 'If true, all key inputs are '
                                                          'concatenated into a single '
                                                          'vector before matching. '
                                                          'Silently ignored (with a '
                                                          'warning) if field_weights '
                                                          'are not all equal, '
                                                          'normalize_memories=False, '
                                                          'or there is only one key '
                                                          'field. Cannot be used with '
                                                          'learning.',
                                           'type': 'boolean'},
                  'enable_learning': { 'default': True,
                                       'description': 'Whether to enable '
                                                      'backpropagation learning of '
                                                      'field_weights. Requires '
                                                      'use_gating_for_weighting=False '
                                                      'and softmax_choice=WEIGHTED_AVG '
                                                      'during learn(). Default true.',
                                       'type': 'boolean'},
                  'field_names': { 'description': 'Names for each field in '
                                                  'memory_template, in order. Skip if '
                                                  "using the 'fields' dict.",
                                   'items': {'type': 'string'},
                                   'type': 'array'},
                  'field_weights': { 'description': 'Weight for each field. Positive '
                                                    "values mark a field as a 'key' "
                                                    'used for matching; null marks it '
                                                    "as a 'value' (stored/retrieved "
                                                    'but not matched). Default: all '
                                                    'fields are keys except the last, '
                                                    'which is a value. E.g., [1, 1, '
                                                    'null] = two key fields, one value '
                                                    'field.',
                                     'items': {'type': ['number', 'null']},
                                     'type': 'array'},
                  'fields': { 'additionalProperties': {},
                              'description': 'Preferred way to configure fields. Dict '
                                             'mapping field name (string) to a '
                                             '3-element list/tuple [field_weight, '
                                             'learn_field_weight, target_field] or a '
                                             "dict with keys 'field_weight', "
                                             "'learn_field_weight', 'target_field'. "
                                             'Using this arg replaces field_names, '
                                             'field_weights, learn_field_weights, and '
                                             'target_fields — specifying those '
                                             'alongside raises a warning.',
                              'type': 'object'},
                  'learn_field_weights': { 'description': 'Whether field_weights are '
                                                          'learnable. True/False '
                                                          'applies to all key fields; '
                                                          'a list allows per-field '
                                                          'control (booleans, floats '
                                                          'for per-field learning '
                                                          'rate, or null to use '
                                                          'default learning_rate). '
                                                          'Value fields are always '
                                                          'forced to False.',
                                           'oneOf': [ {'type': 'boolean'},
                                                      { 'items': { 'type': [ 'boolean',
                                                                             'number',
                                                                             'null']},
                                                        'type': 'array'}]},
                  'learning_rate': { 'description': 'Default learning rate for '
                                                    'field_weights not given an '
                                                    'explicit rate via '
                                                    'learn_field_weights or fields. '
                                                    'Applies only to learnable key '
                                                    'fields.',
                                     'type': 'number'},
                  'memory_capacity': { 'description': 'Maximum number of entries the '
                                                      'memory can hold. Defaults to '
                                                      '1000 if not specified. Also '
                                                      'determines the default '
                                                      'memory_decay_rate (AUTO = '
                                                      '1/memory_capacity).',
                                       'type': 'integer'},
                  'memory_decay_rate': { 'default': 'AUTO',
                                         'description': 'Rate at which stored memories '
                                                        'decay on each storage event. '
                                                        'AUTO (default) sets decay = '
                                                        '1/memory_capacity. Pass a '
                                                        'float in [0, 1] to override, '
                                                        'or 0 to disable decay.',
                                         'oneOf': [ { 'maximum': 1,
                                                      'minimum': 0,
                                                      'type': 'number'},
                                                    { 'enum': ['AUTO'],
                                                      'type': 'string'}]},
                  'memory_fill': { 'description': 'Value used to initialize empty '
                                                  'memory slots. Use 0 (default) for '
                                                  'zeros, a float for a constant, or a '
                                                  '2-tuple (low, high) for uniform '
                                                  'random fill. Avoid all-zero key '
                                                  'fields when normalize_memories=True '
                                                  'to prevent divide-by-zero.',
                                   'oneOf': [ {'type': 'number'},
                                              { 'items': {'type': 'number'},
                                                'maxItems': 2,
                                                'minItems': 2,
                                                'type': 'array'}]},
                  'memory_template': { 'description': 'Shape of a single memory entry. '
                                                      'A 2D list/array where each '
                                                      'inner list is one field (e.g., '
                                                      '[[0,0,0],[0,0,0]] = 2 fields of '
                                                      'size 3). Can also be a 3D array '
                                                      'to pre-populate memory with '
                                                      'specific entries, or a length-2 '
                                                      'tuple (num_fields, field_size) '
                                                      'for uniform fields.',
                                       'items': {},
                                       'type': 'array'},
                  'name': { 'default': 'EM_Composition',
                            'description': 'Name of the EMComposition instance.',
                            'type': 'string'},
                  'normalize_field_weights': { 'default': True,
                                               'description': 'If true (default), '
                                                              'field_weights are '
                                                              'normalized to sum to 1 '
                                                              'across key fields '
                                                              'before use. Set false '
                                                              'to use raw weights as '
                                                              'absolute contributions.',
                                               'type': 'boolean'},
                  'normalize_memories': { 'default': True,
                                          'description': 'If true (default), both '
                                                         'query vectors and stored '
                                                         'memory vectors are '
                                                         'L2-normalized before '
                                                         'computing dot-product '
                                                         'similarity.',
                                          'type': 'boolean'},
                  'purge_by_field_weights': { 'default': False,
                                              'description': 'If true, field_weights '
                                                             'are used to select which '
                                                             'stored memory to replace '
                                                             'when capacity is full '
                                                             '(weakest weighted memory '
                                                             'is purged). Default '
                                                             'false (replaces '
                                                             'lowest-norm memory).',
                                              'type': 'boolean'},
                  'softmax_choice': { 'default': 'WEIGHTED_AVG',
                                      'description': 'How the softmax distribution is '
                                                     'used for retrieval. WEIGHTED_AVG '
                                                     '(default) returns a weighted '
                                                     'average over all memories. '
                                                     'ARG_MAX returns the '
                                                     'best-matching memory. '
                                                     'PROBABILISTIC samples one '
                                                     'memory. ARG_MAX and '
                                                     'PROBABILISTIC cannot be used '
                                                     'with enable_learning=True.',
                                      'enum': [ 'WEIGHTED_AVG',
                                                'ARG_MAX',
                                                'PROBABILISTIC'],
                                      'type': 'string'},
                  'softmax_gain': { 'default': 1,
                                    'description': 'Inverse temperature for the '
                                                   'softmax over match scores. A float '
                                                   "sets a fixed gain; 'ADAPTIVE' uses "
                                                   'entropy-based adaptation; '
                                                   "'CONTROL' adds a ControlMechanism "
                                                   'that dynamically sets gain.',
                                    'oneOf': [ {'type': 'number'},
                                               { 'enum': ['ADAPTIVE', 'CONTROL'],
                                                 'type': 'string'}]},
                  'softmax_threshold': { 'default': 0.001,
                                         'description': 'Values below this threshold '
                                                        'in the softmax input are '
                                                        'masked to zero before '
                                                        'normalization. Default 0.001.',
                                         'type': 'number'},
                  'storage_prob': { 'default': 1,
                                    'description': 'Probability [0, 1] that each '
                                                   'execution stores the current input '
                                                   'into memory. Default 1.0 (always '
                                                   'store).',
                                    'type': 'number'},
                  'store_on_optimization': { 'default': 'FIRST',
                                             'description': 'During learning, which '
                                                            'optimization step(s) '
                                                            'trigger memory storage: '
                                                            'FIRST (default), LAST, or '
                                                            'ALL.',
                                             'enum': ['FIRST', 'LAST', 'ALL'],
                                             'type': 'string'},
                  'target_fields': { 'description': 'List of booleans (one per field) '
                                                    'indicating which fields provide '
                                                    'error signals during learning. '
                                                    'Default: all fields are target '
                                                    'fields. Skip if using the '
                                                    "'fields' dict.",
                                     'items': {'type': 'boolean'},
                                     'type': 'array'},
                  'use_gating_for_weighting': { 'default': False,
                                                'description': 'If true, uses '
                                                               'GatingMechanisms '
                                                               '(output gating) to '
                                                               'apply field weights '
                                                               'instead of a standard '
                                                               'weighted input. '
                                                               'Incompatible with '
                                                               'enable_learning=True.',
                                                'type': 'boolean'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = '- The `fields` dict is the preferred single-arg way to configure all field properties at once; mixing it with field_names/field_weights/learn_field_weights/target_fields raises a warning (fields wins).\n- Default field_weights behavior when omitted: if memory_template has 1 field, weight=[1] (all keys); if >1 fields, all are keys except the last field, which is a value (weight=None).\n- memory_capacity defaults to 1000 (not None as the signature suggests) via Parameters.memory_capacity default.\n- memory_decay_rate AUTO is computed at construction as 1/memory_capacity; pass 0 to disable decay entirely.\n- Initializing memory_template with all-zero key fields will trigger a warning about divide-by-zero when normalize_memories=True. Use memory_fill=(low, high) or a nonzero scalar to avoid this.\n- concatenate_queries is silently overridden to False (with a warning) if: field weights are not all equal, normalize_memories=False, or there is only one key field.\n- ARG_MAX and PROBABILISTIC softmax_choice raise EMCompositionError if learn() is called.\n- use_gating_for_weighting=True + enable_learning=True raises EMCompositionError on learn() call.\n- Nodes and Projections cannot be added to an EMComposition after construction (raises EMCompositionError).\n- learning_rate as a dict is not supported for EMComposition (raises error); use the fields arg or learn_field_weights for per-field rates.\n- When enable_learning=True but there is only one key or concatenate_queries=True, field weight learning has no effect and enable_learning is effectively forced to False at learn() time (with a warning).'


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
        'Call this tool to construct an episodic memory Composition that stores multi-field vector entries and retrieves the closest match via weighted softmax similarity over key fields.'
        return _impl(args or {})
