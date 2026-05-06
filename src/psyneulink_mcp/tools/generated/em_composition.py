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
TOOL_DESCRIPTION = 'Call this tool to instantiate an EMComposition — a differentiable episodic memory system that stores and retrieves multi-field entries by query-key similarity matching. Returns a named EMComposition object registered in the PsyNeuLink session. Use when you need content-addressable memory with optional learnable field weights; fields with non-zero field_weights act as keys (matched during retrieval), while fields with None field_weights act as values (stored and retrieved but not matched).\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "concatenate_queries": {\n      "default": false,\n      "description": "If true, all key inputs are concatenated into a single vector before matching. Only valid when all key field_weights are equal and normalize_memories is true and there is more than one key.",\n      "type": "boolean"\n    },\n    "enable_learning": {\n      "default": true,\n      "description": "If true, field_weights can be learned via backpropagation. Requires use_gating_for_weighting=false and softmax_choice=WEIGHTED_AVG; has no effect with concatenate_queries=true or a single key field.",\n      "type": "boolean"\n    },\n    "field_names": {\n      "description": "Names for each field in the memory entry, in order. Length must match the number of fields in memory_template.",\n      "items": {\n        "type": "string"\n      },\n      "type": "array"\n    },\n    "field_weights": {\n      "description": "Weight for each field. Non-null positive values mark key fields (used for matching); null marks a value field (stored/retrieved but not matched). Default assigns weight 1 to all fields except the last, which is null (value). All-zero weights result in no retrieval.",\n      "items": {},\n      "type": "array"\n    },\n    "fields": {\n      "additionalProperties": {},\n      "description": "Dict mapping field names to their specifications as [field_weight, learn_field_weight, target_field]. When provided, replaces field_names, field_weights, learn_field_weights, and target_fields arguments \\u2014 do not specify those alongside fields.",\n      "type": "object"\n    },\n    "learn_field_weights": {\n      "default": false,\n      "description": "Whether field_weights are learnable. True/False applies to all key fields; a list allows per-field control (True, False, or a float learning rate). Value fields (null weight) are always non-learnable.",\n      "oneOf": [\n        {\n          "type": "boolean"\n        },\n        {\n          "items": {},\n          "type": "array"\n        }\n      ]\n    },\n    "learning_rate": {\n      "default": 0.01,\n      "description": "Default learning rate for field_weights not individually specified. Only applies when learn_field_weights is enabled.",\n      "type": "number"\n    },\n    "memory_capacity": {\n      "default": 1000,\n      "description": "Maximum number of entries the memory can hold. Defaults to 1000 if not specified.",\n      "type": "integer"\n    },\n    "memory_decay_rate": {\n      "default": "AUTO",\n      "description": "Rate [0.0, 1.0] at which stored memories decay each trial. Pass 0 to disable decay. Defaults to \'AUTO\', which sets rate to 1/memory_capacity.",\n      "oneOf": [\n        {\n          "maximum": 1,\n          "minimum": 0,\n          "type": "number"\n        },\n        {\n          "enum": [\n            "AUTO"\n          ],\n          "type": "string"\n        }\n      ]\n    },\n    "memory_fill": {\n      "default": 0,\n      "description": "Value used to initialize empty memory slots. Use a scalar (e.g., 0) for uniform fill, or a 2-element array [low, high] for random uniform fill in that range.",\n      "oneOf": [\n        {\n          "type": "number"\n        },\n        {\n          "items": {\n            "type": "number"\n          },\n          "maxItems": 2,\n          "minItems": 2,\n          "type": "array"\n        }\n      ]\n    },\n    "memory_template": {\n      "description": "Specifies the shape of a memory entry. Use a 2D list (array of field arrays) for a single-entry template \\u2014 e.g., [[0,0,0],[0,0,0,0,0]] for two fields of sizes 3 and 5. For homogeneous fields only, a 3D list (multiple entries) or a 2-element tuple (num_fields, field_size) may also be used. IMPORTANT: when fields have different sizes, always use the 2D single-entry format; passing a 3D list with inhomogeneous field sizes raises a ValueError.",\n      "items": {},\n      "type": "array"\n    },\n    "name": {\n      "default": "EM_Composition",\n      "description": "Name for the EMComposition instance.",\n      "type": "string"\n    },\n    "normalize_field_weights": {\n      "default": true,\n      "description": "If true, field_weights are normalized over the number of keys before retrieval. If false, raw weights are used as absolute multipliers.",\n      "type": "boolean"\n    },\n    "normalize_memories": {\n      "default": true,\n      "description": "If true, queries and memory keys are L2-normalized before computing dot-product similarity. Required for concatenate_queries to work.",\n      "type": "boolean"\n    },\n    "purge_by_field_weights": {\n      "default": false,\n      "description": "If true, field_weights are used when selecting which memory slot to overwrite (weakest weighted memory is replaced). If false, the slot with the smallest overall norm is replaced.",\n      "type": "boolean"\n    },\n    "softmax_choice": {\n      "default": "WEIGHTED_AVG",\n      "description": "How softmax scores are used for retrieval. WEIGHTED_AVG (default) returns a weighted combination; ARG_MAX returns the best match; PROBABILISTIC samples. Only WEIGHTED_AVG supports learning.",\n      "enum": [\n        "WEIGHTED_AVG",\n        "ARG_MAX",\n        "PROBABILISTIC"\n      ],\n      "type": "string"\n    },\n    "softmax_gain": {\n      "default": 1,\n      "description": "Inverse temperature (gain) for softmax over match scores. Higher values produce sharper (more winner-take-all) retrieval. Use the string \'ADAPTIVE\' for automatic gain or \'CONTROL\' to attach a ControlMechanism.",\n      "oneOf": [\n        {\n          "type": "number"\n        },\n        {\n          "enum": [\n            "ADAPTIVE",\n            "CONTROL"\n          ],\n          "type": "string"\n        }\n      ]\n    },\n    "softmax_threshold": {\n      "default": 0.001,\n      "description": "Values below this threshold in the softmax input are masked to zero before normalization. Must be > 0 if specified.",\n      "type": "number"\n    },\n    "storage_prob": {\n      "default": 1,\n      "description": "Probability [0.0, 1.0] that an input is stored in memory on each execution.",\n      "maximum": 1,\n      "minimum": 0,\n      "type": "number"\n    },\n    "store_on_optimization": {\n      "default": "FIRST",\n      "description": "During learning, which optimization step(s) trigger memory storage.",\n      "enum": [\n        "FIRST",\n        "LAST",\n        "ALL"\n      ],\n      "type": "string"\n    },\n    "target_fields": {\n      "description": "List of booleans specifying which fields supply error signals during learning. Length must match number of fields. Defaults to all True.",\n      "items": {\n        "type": "boolean"\n      },\n      "type": "array"\n    },\n    "use_gating_for_weighting": {\n      "default": false,\n      "description": "If true, uses output gating instead of standard inputs to apply field weights. Incompatible with enable_learning=true.",\n      "type": "boolean"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\nCRITICAL — memory_template format for inhomogeneous fields: When fields have different sizes (e.g., a 20-element stimulus field and a 25-element context field), you MUST use a 2D list (single-entry format): [[0]*20, [0]*25]. Do NOT wrap it in an extra list to make it 3D (i.e., [[[0]*20, [0]*25]]) — that raises ValueError because numpy cannot create an array from a sequence with inhomogeneous shape. The 3D list format is only safe when all fields have identical size.\n\nfield_weights sentinel: use JSON null (Python None) — not 0 — to mark a value field. A zero weight means the field participates in matching with zero contribution, which is valid but unusual; null means the field is a pure value field and is excluded from matching entirely.\n\nmemory_decay_rate defaults to AUTO (= 1/memory_capacity); pass 0 explicitly to disable decay.\n\nsoftmax_gain default in the constructor signature is 1.0 (not THRESHOLD as stated in the class-level docstring signature).\n\nLearning constraints: enable_learning=true is silently a no-op when there is only one key field or concatenate_queries=true; use_gating_for_weighting=true with enable_learning=true raises an error only at learn() time, not at construction time. ARG_MAX and PROBABILISTIC softmax_choice also raise an error only at learn() time.\n\nNodes cannot be added to an EMComposition after construction (add_node and add_projection are blocked).\n\nmemory_fill as a 2-element list [low, high] triggers random uniform initialization (low is the lower bound, high is the upper bound — note the source code uses memory_fill[1] as upper and memory_fill[0] as lower, so pass [low, high] in that order).'
TOOL_PARAMETERS = { 'properties': { 'concatenate_queries': { 'default': False,
                                           'description': 'If true, all key inputs are '
                                                          'concatenated into a single '
                                                          'vector before matching. '
                                                          'Only valid when all key '
                                                          'field_weights are equal and '
                                                          'normalize_memories is true '
                                                          'and there is more than one '
                                                          'key.',
                                           'type': 'boolean'},
                  'enable_learning': { 'default': True,
                                       'description': 'If true, field_weights can be '
                                                      'learned via backpropagation. '
                                                      'Requires '
                                                      'use_gating_for_weighting=false '
                                                      'and '
                                                      'softmax_choice=WEIGHTED_AVG; '
                                                      'has no effect with '
                                                      'concatenate_queries=true or a '
                                                      'single key field.',
                                       'type': 'boolean'},
                  'field_names': { 'description': 'Names for each field in the memory '
                                                  'entry, in order. Length must match '
                                                  'the number of fields in '
                                                  'memory_template.',
                                   'items': {'type': 'string'},
                                   'type': 'array'},
                  'field_weights': { 'description': 'Weight for each field. Non-null '
                                                    'positive values mark key fields '
                                                    '(used for matching); null marks a '
                                                    'value field (stored/retrieved but '
                                                    'not matched). Default assigns '
                                                    'weight 1 to all fields except the '
                                                    'last, which is null (value). '
                                                    'All-zero weights result in no '
                                                    'retrieval.',
                                     'items': {},
                                     'type': 'array'},
                  'fields': { 'additionalProperties': {},
                              'description': 'Dict mapping field names to their '
                                             'specifications as [field_weight, '
                                             'learn_field_weight, target_field]. When '
                                             'provided, replaces field_names, '
                                             'field_weights, learn_field_weights, and '
                                             'target_fields arguments — do not specify '
                                             'those alongside fields.',
                              'type': 'object'},
                  'learn_field_weights': { 'default': False,
                                           'description': 'Whether field_weights are '
                                                          'learnable. True/False '
                                                          'applies to all key fields; '
                                                          'a list allows per-field '
                                                          'control (True, False, or a '
                                                          'float learning rate). Value '
                                                          'fields (null weight) are '
                                                          'always non-learnable.',
                                           'oneOf': [ {'type': 'boolean'},
                                                      {'items': {}, 'type': 'array'}]},
                  'learning_rate': { 'default': 0.01,
                                     'description': 'Default learning rate for '
                                                    'field_weights not individually '
                                                    'specified. Only applies when '
                                                    'learn_field_weights is enabled.',
                                     'type': 'number'},
                  'memory_capacity': { 'default': 1000,
                                       'description': 'Maximum number of entries the '
                                                      'memory can hold. Defaults to '
                                                      '1000 if not specified.',
                                       'type': 'integer'},
                  'memory_decay_rate': { 'default': 'AUTO',
                                         'description': 'Rate [0.0, 1.0] at which '
                                                        'stored memories decay each '
                                                        'trial. Pass 0 to disable '
                                                        "decay. Defaults to 'AUTO', "
                                                        'which sets rate to '
                                                        '1/memory_capacity.',
                                         'oneOf': [ { 'maximum': 1,
                                                      'minimum': 0,
                                                      'type': 'number'},
                                                    { 'enum': ['AUTO'],
                                                      'type': 'string'}]},
                  'memory_fill': { 'default': 0,
                                   'description': 'Value used to initialize empty '
                                                  'memory slots. Use a scalar (e.g., '
                                                  '0) for uniform fill, or a 2-element '
                                                  'array [low, high] for random '
                                                  'uniform fill in that range.',
                                   'oneOf': [ {'type': 'number'},
                                              { 'items': {'type': 'number'},
                                                'maxItems': 2,
                                                'minItems': 2,
                                                'type': 'array'}]},
                  'memory_template': { 'description': 'Specifies the shape of a memory '
                                                      'entry. Use a 2D list (array of '
                                                      'field arrays) for a '
                                                      'single-entry template — e.g., '
                                                      '[[0,0,0],[0,0,0,0,0]] for two '
                                                      'fields of sizes 3 and 5. For '
                                                      'homogeneous fields only, a 3D '
                                                      'list (multiple entries) or a '
                                                      '2-element tuple (num_fields, '
                                                      'field_size) may also be used. '
                                                      'IMPORTANT: when fields have '
                                                      'different sizes, always use the '
                                                      '2D single-entry format; passing '
                                                      'a 3D list with inhomogeneous '
                                                      'field sizes raises a '
                                                      'ValueError.',
                                       'items': {},
                                       'type': 'array'},
                  'name': { 'default': 'EM_Composition',
                            'description': 'Name for the EMComposition instance.',
                            'type': 'string'},
                  'normalize_field_weights': { 'default': True,
                                               'description': 'If true, field_weights '
                                                              'are normalized over the '
                                                              'number of keys before '
                                                              'retrieval. If false, '
                                                              'raw weights are used as '
                                                              'absolute multipliers.',
                                               'type': 'boolean'},
                  'normalize_memories': { 'default': True,
                                          'description': 'If true, queries and memory '
                                                         'keys are L2-normalized '
                                                         'before computing dot-product '
                                                         'similarity. Required for '
                                                         'concatenate_queries to work.',
                                          'type': 'boolean'},
                  'purge_by_field_weights': { 'default': False,
                                              'description': 'If true, field_weights '
                                                             'are used when selecting '
                                                             'which memory slot to '
                                                             'overwrite (weakest '
                                                             'weighted memory is '
                                                             'replaced). If false, the '
                                                             'slot with the smallest '
                                                             'overall norm is '
                                                             'replaced.',
                                              'type': 'boolean'},
                  'softmax_choice': { 'default': 'WEIGHTED_AVG',
                                      'description': 'How softmax scores are used for '
                                                     'retrieval. WEIGHTED_AVG '
                                                     '(default) returns a weighted '
                                                     'combination; ARG_MAX returns the '
                                                     'best match; PROBABILISTIC '
                                                     'samples. Only WEIGHTED_AVG '
                                                     'supports learning.',
                                      'enum': [ 'WEIGHTED_AVG',
                                                'ARG_MAX',
                                                'PROBABILISTIC'],
                                      'type': 'string'},
                  'softmax_gain': { 'default': 1,
                                    'description': 'Inverse temperature (gain) for '
                                                   'softmax over match scores. Higher '
                                                   'values produce sharper (more '
                                                   'winner-take-all) retrieval. Use '
                                                   "the string 'ADAPTIVE' for "
                                                   "automatic gain or 'CONTROL' to "
                                                   'attach a ControlMechanism.',
                                    'oneOf': [ {'type': 'number'},
                                               { 'enum': ['ADAPTIVE', 'CONTROL'],
                                                 'type': 'string'}]},
                  'softmax_threshold': { 'default': 0.001,
                                         'description': 'Values below this threshold '
                                                        'in the softmax input are '
                                                        'masked to zero before '
                                                        'normalization. Must be > 0 if '
                                                        'specified.',
                                         'type': 'number'},
                  'storage_prob': { 'default': 1,
                                    'description': 'Probability [0.0, 1.0] that an '
                                                   'input is stored in memory on each '
                                                   'execution.',
                                    'maximum': 1,
                                    'minimum': 0,
                                    'type': 'number'},
                  'store_on_optimization': { 'default': 'FIRST',
                                             'description': 'During learning, which '
                                                            'optimization step(s) '
                                                            'trigger memory storage.',
                                             'enum': ['FIRST', 'LAST', 'ALL'],
                                             'type': 'string'},
                  'target_fields': { 'description': 'List of booleans specifying which '
                                                    'fields supply error signals '
                                                    'during learning. Length must '
                                                    'match number of fields. Defaults '
                                                    'to all True.',
                                     'items': {'type': 'boolean'},
                                     'type': 'array'},
                  'use_gating_for_weighting': { 'default': False,
                                                'description': 'If true, uses output '
                                                               'gating instead of '
                                                               'standard inputs to '
                                                               'apply field weights. '
                                                               'Incompatible with '
                                                               'enable_learning=true.',
                                                'type': 'boolean'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = 'CRITICAL — memory_template format for inhomogeneous fields: When fields have different sizes (e.g., a 20-element stimulus field and a 25-element context field), you MUST use a 2D list (single-entry format): [[0]*20, [0]*25]. Do NOT wrap it in an extra list to make it 3D (i.e., [[[0]*20, [0]*25]]) — that raises ValueError because numpy cannot create an array from a sequence with inhomogeneous shape. The 3D list format is only safe when all fields have identical size.\n\nfield_weights sentinel: use JSON null (Python None) — not 0 — to mark a value field. A zero weight means the field participates in matching with zero contribution, which is valid but unusual; null means the field is a pure value field and is excluded from matching entirely.\n\nmemory_decay_rate defaults to AUTO (= 1/memory_capacity); pass 0 explicitly to disable decay.\n\nsoftmax_gain default in the constructor signature is 1.0 (not THRESHOLD as stated in the class-level docstring signature).\n\nLearning constraints: enable_learning=true is silently a no-op when there is only one key field or concatenate_queries=true; use_gating_for_weighting=true with enable_learning=true raises an error only at learn() time, not at construction time. ARG_MAX and PROBABILISTIC softmax_choice also raise an error only at learn() time.\n\nNodes cannot be added to an EMComposition after construction (add_node and add_projection are blocked).\n\nmemory_fill as a 2-element list [low, high] triggers random uniform initialization (low is the lower bound, high is the upper bound — note the source code uses memory_fill[1] as upper and memory_fill[0] as lower, so pass [low, high] in that order).'


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
        'Call this tool to instantiate an EMComposition — a differentiable episodic memory system that stores and retrieves multi-field entries by query-key similarity matching.'
        return _impl(args or {})
