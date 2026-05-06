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
TOOL_DESCRIPTION = 'Call this tool to construct an EMComposition — a differentiable episodic memory module that stores multi-field entries (query keys + value fields), retrieves the best-matching stored memory via softmax over dot-product similarity, and optionally learns per-field weights via backpropagation. Returns a handle to the constructed EMComposition that can be run standalone or embedded as a nested Composition.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "concatenate_queries": {\n      "default": false,\n      "description": "If true, all key field inputs are concatenated into a single vector before matching. Only effective when there are multiple keys with equal weights and normalize_memories=true.",\n      "type": "boolean"\n    },\n    "enable_learning": {\n      "default": true,\n      "description": "Enables backpropagation learning of field_weights. Requires use_gating_for_weighting=false and softmax_choice=WEIGHTED_AVG.",\n      "type": "boolean"\n    },\n    "field_names": {\n      "default": null,\n      "description": "Names for each field in memory_template order. Ignored (with a warning) if fields is also specified.",\n      "items": {\n        "type": "string"\n      },\n      "type": "array"\n    },\n    "field_weights": {\n      "default": null,\n      "description": "Per-field retrieval weights. Non-null/non-zero values mark key fields (used in matching); null or 0 marks value fields (stored but not matched). Defaults to all-keys-equal-weight with the last field as a value field when null.",\n      "items": {\n        "type": "number"\n      },\n      "type": "array"\n    },\n    "fields": {\n      "additionalProperties": true,\n      "default": null,\n      "description": "Dict mapping field name -> {\\"field_weight\\": float|null, \\"learn_field_weight\\": bool|float|null, \\"target_field\\": bool} (or equivalent tuple/list). When specified, replaces field_names, field_weights, learn_field_weights, and target_fields \\u2014 do not supply those alongside this arg.",\n      "type": "object"\n    },\n    "learn_field_weights": {\n      "default": false,\n      "description": "Whether field_weights are learnable. True/False applies to all key fields; a list of bool/float per field sets per-field learning rates (False disables, a positive float overrides learning_rate for that field).",\n      "oneOf": [\n        {\n          "type": "boolean"\n        },\n        {\n          "items": {\n            "oneOf": [\n              {\n                "type": "boolean"\n              },\n              {\n                "type": "number"\n              }\n            ]\n          },\n          "type": "array"\n        }\n      ]\n    },\n    "learning_rate": {\n      "default": null,\n      "description": "Default learning rate for field_weights not individually specified in learn_field_weights or fields. Approximately 0.01 by default.",\n      "type": "number"\n    },\n    "memory_capacity": {\n      "default": null,\n      "description": "Maximum number of entries the memory can hold. Defaults to 1000 internally when null.",\n      "type": "integer"\n    },\n    "memory_decay_rate": {\n      "default": "AUTO",\n      "description": "Rate at which stored memories decay each cycle. \'AUTO\' sets it to 1/memory_capacity. 0 disables decay. Must be in [0,1].",\n      "oneOf": [\n        {\n          "maximum": 1,\n          "minimum": 0,\n          "type": "number"\n        },\n        {\n          "enum": [\n            "AUTO"\n          ],\n          "type": "string"\n        }\n      ]\n    },\n    "memory_fill": {\n      "default": 0,\n      "description": "Value(s) used to initialise empty memory slots. A scalar fills with that constant; a 2-element array [low, high] fills with uniform random values in that range.",\n      "oneOf": [\n        {\n          "type": "number"\n        },\n        {\n          "items": {\n            "type": "number"\n          },\n          "maxItems": 2,\n          "minItems": 2,\n          "type": "array"\n        }\n      ]\n    },\n    "memory_template": {\n      "default": [\n        [\n          0\n        ],\n        [\n          0\n        ]\n      ],\n      "description": "2D list specifying a single memory entry shape: each inner list is one field whose length sets the field size. E.g. [[0,0,0],[0,0]] defines 2 fields of sizes 3 and 2. Do NOT wrap in an extra outer list (avoid 3D) when fields have different sizes \\u2014 that triggers a numpy inhomogeneous-array ValueError. For a full memory matrix pre-fill, use a 3D list only when all fields have the same length.",\n      "items": {\n        "items": {\n          "type": "number"\n        },\n        "type": "array"\n      },\n      "type": "array"\n    },\n    "name": {\n      "default": "EM_Composition",\n      "description": "Name of the EMComposition.",\n      "type": "string"\n    },\n    "normalize_field_weights": {\n      "default": true,\n      "description": "If true, field_weights are normalised to sum to 1 over key fields; if false, used as absolute scaling.",\n      "type": "boolean"\n    },\n    "normalize_memories": {\n      "default": true,\n      "description": "If true, queries and memory entries are L2-normalised before computing dot-product similarity.",\n      "type": "boolean"\n    },\n    "purge_by_field_weights": {\n      "default": false,\n      "description": "If true, field_weights are used to identify the weakest memory slot when storage capacity is exceeded.",\n      "type": "boolean"\n    },\n    "seed": {\n      "default": null,\n      "description": "Random seed for reproducible stochastic storage (storage_prob < 1) and memory initialisation.",\n      "type": "integer"\n    },\n    "softmax_choice": {\n      "default": "WEIGHTED_AVG",\n      "description": "How the softmax distribution is used for retrieval. WEIGHTED_AVG (default) is required for learning; ARG_MAX and PROBABILISTIC raise an error if learn() is called.",\n      "enum": [\n        "WEIGHTED_AVG",\n        "ARG_MAX",\n        "PROBABILISTIC"\n      ],\n      "type": "string"\n    },\n    "softmax_gain": {\n      "default": 1,\n      "description": "Inverse temperature for softmax over match scores. A positive float sharpens or flattens retrieval; \'ADAPTIVE\' adjusts automatically; \'CONTROL\' delegates to a ControlMechanism.",\n      "oneOf": [\n        {\n          "exclusiveMinimum": 0,\n          "type": "number"\n        },\n        {\n          "enum": [\n            "ADAPTIVE",\n            "CONTROL"\n          ],\n          "type": "string"\n        }\n      ]\n    },\n    "softmax_threshold": {\n      "default": 0.001,\n      "description": "Mask threshold: softmax inputs below this value are zeroed before normalisation. Set to null to disable.",\n      "exclusiveMinimum": 0,\n      "type": "number"\n    },\n    "storage_prob": {\n      "default": 1,\n      "description": "Probability [0,1] that a presented input is stored in memory after retrieval.",\n      "maximum": 1,\n      "minimum": 0,\n      "type": "number"\n    },\n    "store_on_optimization": {\n      "default": "FIRST",\n      "description": "During learning, which optimisation step(s) trigger storage: FIRST (default), LAST, or ALL.",\n      "enum": [\n        "FIRST",\n        "ALL",\n        "LAST"\n      ],\n      "type": "string"\n    },\n    "target_fields": {\n      "default": null,\n      "description": "One bool per field indicating which fields supply error signals during learning. Length must match number of fields. Defaults to all true.",\n      "items": {\n        "type": "boolean"\n      },\n      "type": "array"\n    },\n    "use_gating_for_weighting": {\n      "default": false,\n      "description": "If true, uses GatingMechanisms instead of ProcessingMechanisms to apply field weights; incompatible with enable_learning=true.",\n      "type": "boolean"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\nCRITICAL (fixes issue #17): memory_template must be a **2D** list — one inner list per field — when specifying a single entry template, even if fields have different lengths. Example for 2 fields of sizes 20 and 25: [[0]*20, [0]*25]. Never wrap a single entry in an extra outer list (i.e. do NOT pass [[[0]*20, [0]*25]]); that 3D form causes a numpy inhomogeneous-array ValueError when field sizes differ.\n\n- memory_capacity defaults to 1000 internally when not specified; memory_decay_rate="AUTO" resolves to 1/memory_capacity.\n- Default field_weights assigns all fields as keys (weight 1) except the last, which is a value field (weight None/0). Explicitly pass field_weights if this default is wrong for your use case.\n- fields dict is mutually exclusive with field_names, field_weights, learn_field_weights, and target_fields; mixing them raises an error or silently ignores the individual args.\n- enable_learning=True + use_gating_for_weighting=True will NOT raise at construction but WILL raise at learn() time.\n- enable_learning=True + softmax_choice in {ARG_MAX, PROBABILISTIC} similarly defers the error to learn() time.\n- concatenate_queries=True is silently overridden to False if field weights are unequal, normalize_memories=False, or there is only one key field.\n- Nodes and Projections cannot be added to an EMComposition after construction (raises EMCompositionError).\n- learn() defaults to ExecutionMode.PyTorch with a warning if execution_mode is not supplied.\n- memory is a read-only attribute; new entries are added by calling run() or learn() with them as inputs.'
TOOL_PARAMETERS = { 'properties': { 'concatenate_queries': { 'default': False,
                                           'description': 'If true, all key field '
                                                          'inputs are concatenated '
                                                          'into a single vector before '
                                                          'matching. Only effective '
                                                          'when there are multiple '
                                                          'keys with equal weights and '
                                                          'normalize_memories=true.',
                                           'type': 'boolean'},
                  'enable_learning': { 'default': True,
                                       'description': 'Enables backpropagation '
                                                      'learning of field_weights. '
                                                      'Requires '
                                                      'use_gating_for_weighting=false '
                                                      'and '
                                                      'softmax_choice=WEIGHTED_AVG.',
                                       'type': 'boolean'},
                  'field_names': { 'default': None,
                                   'description': 'Names for each field in '
                                                  'memory_template order. Ignored '
                                                  '(with a warning) if fields is also '
                                                  'specified.',
                                   'items': {'type': 'string'},
                                   'type': 'array'},
                  'field_weights': { 'default': None,
                                     'description': 'Per-field retrieval weights. '
                                                    'Non-null/non-zero values mark key '
                                                    'fields (used in matching); null '
                                                    'or 0 marks value fields (stored '
                                                    'but not matched). Defaults to '
                                                    'all-keys-equal-weight with the '
                                                    'last field as a value field when '
                                                    'null.',
                                     'items': {'type': 'number'},
                                     'type': 'array'},
                  'fields': { 'additionalProperties': True,
                              'default': None,
                              'description': 'Dict mapping field name -> '
                                             '{"field_weight": float|null, '
                                             '"learn_field_weight": bool|float|null, '
                                             '"target_field": bool} (or equivalent '
                                             'tuple/list). When specified, replaces '
                                             'field_names, field_weights, '
                                             'learn_field_weights, and target_fields — '
                                             'do not supply those alongside this arg.',
                              'type': 'object'},
                  'learn_field_weights': { 'default': False,
                                           'description': 'Whether field_weights are '
                                                          'learnable. True/False '
                                                          'applies to all key fields; '
                                                          'a list of bool/float per '
                                                          'field sets per-field '
                                                          'learning rates (False '
                                                          'disables, a positive float '
                                                          'overrides learning_rate for '
                                                          'that field).',
                                           'oneOf': [ {'type': 'boolean'},
                                                      { 'items': { 'oneOf': [ { 'type': 'boolean'},
                                                                              { 'type': 'number'}]},
                                                        'type': 'array'}]},
                  'learning_rate': { 'default': None,
                                     'description': 'Default learning rate for '
                                                    'field_weights not individually '
                                                    'specified in learn_field_weights '
                                                    'or fields. Approximately 0.01 by '
                                                    'default.',
                                     'type': 'number'},
                  'memory_capacity': { 'default': None,
                                       'description': 'Maximum number of entries the '
                                                      'memory can hold. Defaults to '
                                                      '1000 internally when null.',
                                       'type': 'integer'},
                  'memory_decay_rate': { 'default': 'AUTO',
                                         'description': 'Rate at which stored memories '
                                                        "decay each cycle. 'AUTO' sets "
                                                        'it to 1/memory_capacity. 0 '
                                                        'disables decay. Must be in '
                                                        '[0,1].',
                                         'oneOf': [ { 'maximum': 1,
                                                      'minimum': 0,
                                                      'type': 'number'},
                                                    { 'enum': ['AUTO'],
                                                      'type': 'string'}]},
                  'memory_fill': { 'default': 0,
                                   'description': 'Value(s) used to initialise empty '
                                                  'memory slots. A scalar fills with '
                                                  'that constant; a 2-element array '
                                                  '[low, high] fills with uniform '
                                                  'random values in that range.',
                                   'oneOf': [ {'type': 'number'},
                                              { 'items': {'type': 'number'},
                                                'maxItems': 2,
                                                'minItems': 2,
                                                'type': 'array'}]},
                  'memory_template': { 'default': [[0], [0]],
                                       'description': '2D list specifying a single '
                                                      'memory entry shape: each inner '
                                                      'list is one field whose length '
                                                      'sets the field size. E.g. '
                                                      '[[0,0,0],[0,0]] defines 2 '
                                                      'fields of sizes 3 and 2. Do NOT '
                                                      'wrap in an extra outer list '
                                                      '(avoid 3D) when fields have '
                                                      'different sizes — that triggers '
                                                      'a numpy inhomogeneous-array '
                                                      'ValueError. For a full memory '
                                                      'matrix pre-fill, use a 3D list '
                                                      'only when all fields have the '
                                                      'same length.',
                                       'items': { 'items': {'type': 'number'},
                                                  'type': 'array'},
                                       'type': 'array'},
                  'name': { 'default': 'EM_Composition',
                            'description': 'Name of the EMComposition.',
                            'type': 'string'},
                  'normalize_field_weights': { 'default': True,
                                               'description': 'If true, field_weights '
                                                              'are normalised to sum '
                                                              'to 1 over key fields; '
                                                              'if false, used as '
                                                              'absolute scaling.',
                                               'type': 'boolean'},
                  'normalize_memories': { 'default': True,
                                          'description': 'If true, queries and memory '
                                                         'entries are L2-normalised '
                                                         'before computing dot-product '
                                                         'similarity.',
                                          'type': 'boolean'},
                  'purge_by_field_weights': { 'default': False,
                                              'description': 'If true, field_weights '
                                                             'are used to identify the '
                                                             'weakest memory slot when '
                                                             'storage capacity is '
                                                             'exceeded.',
                                              'type': 'boolean'},
                  'seed': { 'default': None,
                            'description': 'Random seed for reproducible stochastic '
                                           'storage (storage_prob < 1) and memory '
                                           'initialisation.',
                            'type': 'integer'},
                  'softmax_choice': { 'default': 'WEIGHTED_AVG',
                                      'description': 'How the softmax distribution is '
                                                     'used for retrieval. WEIGHTED_AVG '
                                                     '(default) is required for '
                                                     'learning; ARG_MAX and '
                                                     'PROBABILISTIC raise an error if '
                                                     'learn() is called.',
                                      'enum': [ 'WEIGHTED_AVG',
                                                'ARG_MAX',
                                                'PROBABILISTIC'],
                                      'type': 'string'},
                  'softmax_gain': { 'default': 1,
                                    'description': 'Inverse temperature for softmax '
                                                   'over match scores. A positive '
                                                   'float sharpens or flattens '
                                                   "retrieval; 'ADAPTIVE' adjusts "
                                                   "automatically; 'CONTROL' delegates "
                                                   'to a ControlMechanism.',
                                    'oneOf': [ { 'exclusiveMinimum': 0,
                                                 'type': 'number'},
                                               { 'enum': ['ADAPTIVE', 'CONTROL'],
                                                 'type': 'string'}]},
                  'softmax_threshold': { 'default': 0.001,
                                         'description': 'Mask threshold: softmax '
                                                        'inputs below this value are '
                                                        'zeroed before normalisation. '
                                                        'Set to null to disable.',
                                         'exclusiveMinimum': 0,
                                         'type': 'number'},
                  'storage_prob': { 'default': 1,
                                    'description': 'Probability [0,1] that a presented '
                                                   'input is stored in memory after '
                                                   'retrieval.',
                                    'maximum': 1,
                                    'minimum': 0,
                                    'type': 'number'},
                  'store_on_optimization': { 'default': 'FIRST',
                                             'description': 'During learning, which '
                                                            'optimisation step(s) '
                                                            'trigger storage: FIRST '
                                                            '(default), LAST, or ALL.',
                                             'enum': ['FIRST', 'ALL', 'LAST'],
                                             'type': 'string'},
                  'target_fields': { 'default': None,
                                     'description': 'One bool per field indicating '
                                                    'which fields supply error signals '
                                                    'during learning. Length must '
                                                    'match number of fields. Defaults '
                                                    'to all true.',
                                     'items': {'type': 'boolean'},
                                     'type': 'array'},
                  'use_gating_for_weighting': { 'default': False,
                                                'description': 'If true, uses '
                                                               'GatingMechanisms '
                                                               'instead of '
                                                               'ProcessingMechanisms '
                                                               'to apply field '
                                                               'weights; incompatible '
                                                               'with '
                                                               'enable_learning=true.',
                                                'type': 'boolean'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = 'CRITICAL (fixes issue #17): memory_template must be a **2D** list — one inner list per field — when specifying a single entry template, even if fields have different lengths. Example for 2 fields of sizes 20 and 25: [[0]*20, [0]*25]. Never wrap a single entry in an extra outer list (i.e. do NOT pass [[[0]*20, [0]*25]]); that 3D form causes a numpy inhomogeneous-array ValueError when field sizes differ.\n\n- memory_capacity defaults to 1000 internally when not specified; memory_decay_rate="AUTO" resolves to 1/memory_capacity.\n- Default field_weights assigns all fields as keys (weight 1) except the last, which is a value field (weight None/0). Explicitly pass field_weights if this default is wrong for your use case.\n- fields dict is mutually exclusive with field_names, field_weights, learn_field_weights, and target_fields; mixing them raises an error or silently ignores the individual args.\n- enable_learning=True + use_gating_for_weighting=True will NOT raise at construction but WILL raise at learn() time.\n- enable_learning=True + softmax_choice in {ARG_MAX, PROBABILISTIC} similarly defers the error to learn() time.\n- concatenate_queries=True is silently overridden to False if field weights are unequal, normalize_memories=False, or there is only one key field.\n- Nodes and Projections cannot be added to an EMComposition after construction (raises EMCompositionError).\n- learn() defaults to ExecutionMode.PyTorch with a warning if execution_mode is not supplied.\n- memory is a read-only attribute; new entries are added by calling run() or learn() with them as inputs.'


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
        'Call this tool to construct an EMComposition — a differentiable episodic memory module that stores multi-field entries (query keys + value fields), retrieves the best-matching stored memory via softmax over dot-product similarity, and optionally learns per-field weights via backpropagation.'
        return _impl(args or {})
