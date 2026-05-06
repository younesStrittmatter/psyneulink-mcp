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
TOOL_DESCRIPTION = 'Call this to instantiate an EMComposition — a differentiable episodic memory store that supports content-addressable retrieval and optional learning of field weights. Returns a named EMComposition that can be run with `composition_run` or embedded in a larger Composition. Use when you need a memory module that stores key-value entries and retrieves the best match via softmax over dot-product similarity.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "concatenate_queries": {\n      "default": false,\n      "description": "If true, concatenate all key inputs into a single vector before matching. Requires all key fields to have equal weights and normalize_memories=true; only valid when there is more than one key.",\n      "type": "boolean"\n    },\n    "enable_learning": {\n      "default": true,\n      "description": "Whether to construct learning pathways for field weights. Requires use_gating_for_weighting=false and softmax_choice=WEIGHTED_AVG.",\n      "type": "boolean"\n    },\n    "field_names": {\n      "description": "Names for each field in the memory template. Length must equal number of fields. Ignored if \'fields\' dict is provided.",\n      "items": {\n        "type": "string"\n      },\n      "type": "array"\n    },\n    "field_weights": {\n      "description": "Relative weight for each field during retrieval matching. Non-zero = key field (used for matching); null/None = value field (stored/retrieved but not matched). Default treats all but last field as keys. Ignored if \'fields\' dict is provided.",\n      "items": {\n        "type": "number"\n      },\n      "type": "array"\n    },\n    "fields": {\n      "description": "Dict mapping field_name -> {field_weight, learn_field_weight, target_field} or (weight, learn, target) tuple. Replaces field_names, field_weights, learn_field_weights, and target_fields \\u2014 specifying both raises an error.",\n      "type": "object"\n    },\n    "learn_field_weights": {\n      "default": false,\n      "description": "Whether field weights are learnable. Boolean (applies to all key fields) or list of bools/floats per field. Ignored if \'fields\' dict is provided.",\n      "oneOf": [\n        {\n          "type": "boolean"\n        },\n        {\n          "items": {\n            "oneOf": [\n              {\n                "type": "boolean"\n              },\n              {\n                "type": "number"\n              }\n            ]\n          },\n          "type": "array"\n        }\n      ]\n    },\n    "learning_rate": {\n      "description": "Default learning rate for learnable field weights. Applies to fields not given an explicit rate in \'learn_field_weights\'. Effective default is 0.01.",\n      "type": "number"\n    },\n    "memory_capacity": {\n      "description": "Maximum number of entries storable in memory. Defaults to 1000 if not specified.",\n      "minimum": 1,\n      "type": "integer"\n    },\n    "memory_decay_rate": {\n      "default": "AUTO",\n      "description": "Rate at which existing memories decay on each storage event. Float in [0, 1], or the string \'AUTO\' (resolves to 1/memory_capacity). Set to 0 to disable decay.",\n      "oneOf": [\n        {\n          "maximum": 1,\n          "minimum": 0,\n          "type": "number"\n        },\n        {\n          "enum": [\n            "AUTO"\n          ],\n          "type": "string"\n        }\n      ]\n    },\n    "memory_fill": {\n      "default": 0,\n      "description": "Value used to initialize empty memory slots. Scalar (e.g. 0) or 2-element tuple (low, high) for uniform random fill.",\n      "oneOf": [\n        {\n          "type": "number"\n        },\n        {\n          "items": {\n            "type": "number"\n          },\n          "maxItems": 2,\n          "minItems": 2,\n          "type": "array"\n        }\n      ]\n    },\n    "memory_template": {\n      "description": "Specifies the shape of memory entries. Pass a 2D list [[field0_values], [field1_values], ...] for a single-entry template (REQUIRED when fields have different sizes). Pass a 3D list [[[f0], [f1]], [[f0], [f1]], ...] only if all fields have the same size. Can also be a 2- or 3-tuple of ints (num_fields, field_size) or (num_entries, num_fields, field_size).",\n      "items": {},\n      "type": "array"\n    },\n    "name": {\n      "default": "EM_Composition",\n      "description": "Name for the EMComposition instance.",\n      "type": "string"\n    },\n    "normalize_field_weights": {\n      "default": true,\n      "description": "If true, field weights are normalized to sum to 1 across key fields. If false, weights are used as absolute values.",\n      "type": "boolean"\n    },\n    "normalize_memories": {\n      "default": true,\n      "description": "If true, normalize keys and memory entries before computing dot-product similarity. Recommended; required for concatenate_queries.",\n      "type": "boolean"\n    },\n    "purge_by_field_weights": {\n      "default": false,\n      "description": "If true, field weights influence which memory slot is replaced when capacity is full.",\n      "type": "boolean"\n    },\n    "seed": {\n      "description": "Random seed for reproducible stochastic behavior (e.g. PROBABILISTIC softmax_choice, random memory_fill).",\n      "type": "integer"\n    },\n    "softmax_choice": {\n      "default": "WEIGHTED_AVG",\n      "description": "How softmax weights are used for retrieval. WEIGHTED_AVG: weighted average (required for learning). ARG_MAX: return entry with highest match. PROBABILISTIC: sample proportional to match.",\n      "enum": [\n        "WEIGHTED_AVG",\n        "ARG_MAX",\n        "PROBABILISTIC"\n      ],\n      "type": "string"\n    },\n    "softmax_gain": {\n      "default": 1,\n      "description": "Inverse temperature for softmax over match scores. Scalar float, or the string \'ADAPTIVE\' (auto-tuned) or \'CONTROL\' (controlled by a ControlMechanism).",\n      "oneOf": [\n        {\n          "type": "number"\n        },\n        {\n          "enum": [\n            "ADAPTIVE",\n            "CONTROL"\n          ],\n          "type": "string"\n        }\n      ]\n    },\n    "softmax_threshold": {\n      "default": 0.001,\n      "description": "Values below this threshold are masked out before softmax. Set to null to disable masking.",\n      "type": "number"\n    },\n    "storage_prob": {\n      "default": 1,\n      "description": "Probability [0, 1] that a new input is stored in memory on each execution.",\n      "maximum": 1,\n      "minimum": 0,\n      "type": "number"\n    },\n    "store_on_optimization": {\n      "default": "FIRST",\n      "description": "During learning, which optimization step(s) trigger memory storage.",\n      "enum": [\n        "FIRST",\n        "LAST",\n        "ALL"\n      ],\n      "type": "string"\n    },\n    "target_fields": {\n      "description": "List of booleans indicating which fields supply error signals during learning. Length must equal number of fields. Ignored if \'fields\' dict is provided.",\n      "items": {\n        "type": "boolean"\n      },\n      "type": "array"\n    },\n    "use_gating_for_weighting": {\n      "default": false,\n      "description": "If true, use output gating instead of a standard input to apply field weights. Incompatible with enable_learning=true.",\n      "type": "boolean"\n    },\n    "use_storage_node": {\n      "default": true,\n      "description": "If true (default), use an EMStorageMechanism node for storage, which is required when embedding the EMComposition inside another Composition. Set to false only for debugging.",\n      "type": "boolean"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\nCRITICAL (from recent feedback): When fields have **different sizes**, always pass `memory_template` as a 2D list — a single-entry template like `[[0]*20, [0]*25]`. Do NOT wrap it in an extra outer list (e.g. `[[[0]*20, [0]*25]]`). That 3D form triggers a numpy inhomogeneous-array crash inside `_parse_memory_template` because numpy cannot build an array from fields of unequal lengths. Use the 3D form only when all fields have the same size.\n\nOther caveats:\n- `fields` dict is the preferred way to specify field structure; passing `fields` alongside `field_names`/`field_weights`/`learn_field_weights`/`target_fields` raises an error (or warning).\n- `field_weights=None` for a field marks it as a value field (stored/retrieved but not used in matching). Default: all fields except the last are keys.\n- `memory_decay_rate=\'AUTO\'` resolves at construction time to `1 / memory_capacity`; pass `0` explicitly to disable decay.\n- `softmax_choice` of `ARG_MAX` or `PROBABILISTIC` is incompatible with `learn()` — will raise an error if called.\n- `enable_learning=True` with `concatenate_queries=True` or only one key field has no effect on field weights and emits a warning; set `enable_learning=False` in those cases.\n- `use_gating_for_weighting=True` + `enable_learning=True` raises an error when `learn()` is called.\n- Nodes and projections cannot be added to an EMComposition after construction.\n- If all memory entries are initialized to zero and `normalize_memories=True`, a divide-by-zero warning is issued; use a non-zero `memory_fill` to avoid it.'
TOOL_PARAMETERS = { 'properties': { 'concatenate_queries': { 'default': False,
                                           'description': 'If true, concatenate all '
                                                          'key inputs into a single '
                                                          'vector before matching. '
                                                          'Requires all key fields to '
                                                          'have equal weights and '
                                                          'normalize_memories=true; '
                                                          'only valid when there is '
                                                          'more than one key.',
                                           'type': 'boolean'},
                  'enable_learning': { 'default': True,
                                       'description': 'Whether to construct learning '
                                                      'pathways for field weights. '
                                                      'Requires '
                                                      'use_gating_for_weighting=false '
                                                      'and '
                                                      'softmax_choice=WEIGHTED_AVG.',
                                       'type': 'boolean'},
                  'field_names': { 'description': 'Names for each field in the memory '
                                                  'template. Length must equal number '
                                                  "of fields. Ignored if 'fields' dict "
                                                  'is provided.',
                                   'items': {'type': 'string'},
                                   'type': 'array'},
                  'field_weights': { 'description': 'Relative weight for each field '
                                                    'during retrieval matching. '
                                                    'Non-zero = key field (used for '
                                                    'matching); null/None = value '
                                                    'field (stored/retrieved but not '
                                                    'matched). Default treats all but '
                                                    'last field as keys. Ignored if '
                                                    "'fields' dict is provided.",
                                     'items': {'type': 'number'},
                                     'type': 'array'},
                  'fields': { 'description': 'Dict mapping field_name -> '
                                             '{field_weight, learn_field_weight, '
                                             'target_field} or (weight, learn, target) '
                                             'tuple. Replaces field_names, '
                                             'field_weights, learn_field_weights, and '
                                             'target_fields — specifying both raises '
                                             'an error.',
                              'type': 'object'},
                  'learn_field_weights': { 'default': False,
                                           'description': 'Whether field weights are '
                                                          'learnable. Boolean (applies '
                                                          'to all key fields) or list '
                                                          'of bools/floats per field. '
                                                          "Ignored if 'fields' dict is "
                                                          'provided.',
                                           'oneOf': [ {'type': 'boolean'},
                                                      { 'items': { 'oneOf': [ { 'type': 'boolean'},
                                                                              { 'type': 'number'}]},
                                                        'type': 'array'}]},
                  'learning_rate': { 'description': 'Default learning rate for '
                                                    'learnable field weights. Applies '
                                                    'to fields not given an explicit '
                                                    "rate in 'learn_field_weights'. "
                                                    'Effective default is 0.01.',
                                     'type': 'number'},
                  'memory_capacity': { 'description': 'Maximum number of entries '
                                                      'storable in memory. Defaults to '
                                                      '1000 if not specified.',
                                       'minimum': 1,
                                       'type': 'integer'},
                  'memory_decay_rate': { 'default': 'AUTO',
                                         'description': 'Rate at which existing '
                                                        'memories decay on each '
                                                        'storage event. Float in [0, '
                                                        "1], or the string 'AUTO' "
                                                        '(resolves to '
                                                        '1/memory_capacity). Set to 0 '
                                                        'to disable decay.',
                                         'oneOf': [ { 'maximum': 1,
                                                      'minimum': 0,
                                                      'type': 'number'},
                                                    { 'enum': ['AUTO'],
                                                      'type': 'string'}]},
                  'memory_fill': { 'default': 0,
                                   'description': 'Value used to initialize empty '
                                                  'memory slots. Scalar (e.g. 0) or '
                                                  '2-element tuple (low, high) for '
                                                  'uniform random fill.',
                                   'oneOf': [ {'type': 'number'},
                                              { 'items': {'type': 'number'},
                                                'maxItems': 2,
                                                'minItems': 2,
                                                'type': 'array'}]},
                  'memory_template': { 'description': 'Specifies the shape of memory '
                                                      'entries. Pass a 2D list '
                                                      '[[field0_values], '
                                                      '[field1_values], ...] for a '
                                                      'single-entry template (REQUIRED '
                                                      'when fields have different '
                                                      'sizes). Pass a 3D list [[[f0], '
                                                      '[f1]], [[f0], [f1]], ...] only '
                                                      'if all fields have the same '
                                                      'size. Can also be a 2- or '
                                                      '3-tuple of ints (num_fields, '
                                                      'field_size) or (num_entries, '
                                                      'num_fields, field_size).',
                                       'items': {},
                                       'type': 'array'},
                  'name': { 'default': 'EM_Composition',
                            'description': 'Name for the EMComposition instance.',
                            'type': 'string'},
                  'normalize_field_weights': { 'default': True,
                                               'description': 'If true, field weights '
                                                              'are normalized to sum '
                                                              'to 1 across key fields. '
                                                              'If false, weights are '
                                                              'used as absolute '
                                                              'values.',
                                               'type': 'boolean'},
                  'normalize_memories': { 'default': True,
                                          'description': 'If true, normalize keys and '
                                                         'memory entries before '
                                                         'computing dot-product '
                                                         'similarity. Recommended; '
                                                         'required for '
                                                         'concatenate_queries.',
                                          'type': 'boolean'},
                  'purge_by_field_weights': { 'default': False,
                                              'description': 'If true, field weights '
                                                             'influence which memory '
                                                             'slot is replaced when '
                                                             'capacity is full.',
                                              'type': 'boolean'},
                  'seed': { 'description': 'Random seed for reproducible stochastic '
                                           'behavior (e.g. PROBABILISTIC '
                                           'softmax_choice, random memory_fill).',
                            'type': 'integer'},
                  'softmax_choice': { 'default': 'WEIGHTED_AVG',
                                      'description': 'How softmax weights are used for '
                                                     'retrieval. WEIGHTED_AVG: '
                                                     'weighted average (required for '
                                                     'learning). ARG_MAX: return entry '
                                                     'with highest match. '
                                                     'PROBABILISTIC: sample '
                                                     'proportional to match.',
                                      'enum': [ 'WEIGHTED_AVG',
                                                'ARG_MAX',
                                                'PROBABILISTIC'],
                                      'type': 'string'},
                  'softmax_gain': { 'default': 1,
                                    'description': 'Inverse temperature for softmax '
                                                   'over match scores. Scalar float, '
                                                   "or the string 'ADAPTIVE' "
                                                   "(auto-tuned) or 'CONTROL' "
                                                   '(controlled by a '
                                                   'ControlMechanism).',
                                    'oneOf': [ {'type': 'number'},
                                               { 'enum': ['ADAPTIVE', 'CONTROL'],
                                                 'type': 'string'}]},
                  'softmax_threshold': { 'default': 0.001,
                                         'description': 'Values below this threshold '
                                                        'are masked out before '
                                                        'softmax. Set to null to '
                                                        'disable masking.',
                                         'type': 'number'},
                  'storage_prob': { 'default': 1,
                                    'description': 'Probability [0, 1] that a new '
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
                  'target_fields': { 'description': 'List of booleans indicating which '
                                                    'fields supply error signals '
                                                    'during learning. Length must '
                                                    'equal number of fields. Ignored '
                                                    "if 'fields' dict is provided.",
                                     'items': {'type': 'boolean'},
                                     'type': 'array'},
                  'use_gating_for_weighting': { 'default': False,
                                                'description': 'If true, use output '
                                                               'gating instead of a '
                                                               'standard input to '
                                                               'apply field weights. '
                                                               'Incompatible with '
                                                               'enable_learning=true.',
                                                'type': 'boolean'},
                  'use_storage_node': { 'default': True,
                                        'description': 'If true (default), use an '
                                                       'EMStorageMechanism node for '
                                                       'storage, which is required '
                                                       'when embedding the '
                                                       'EMComposition inside another '
                                                       'Composition. Set to false only '
                                                       'for debugging.',
                                        'type': 'boolean'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = "CRITICAL (from recent feedback): When fields have **different sizes**, always pass `memory_template` as a 2D list — a single-entry template like `[[0]*20, [0]*25]`. Do NOT wrap it in an extra outer list (e.g. `[[[0]*20, [0]*25]]`). That 3D form triggers a numpy inhomogeneous-array crash inside `_parse_memory_template` because numpy cannot build an array from fields of unequal lengths. Use the 3D form only when all fields have the same size.\n\nOther caveats:\n- `fields` dict is the preferred way to specify field structure; passing `fields` alongside `field_names`/`field_weights`/`learn_field_weights`/`target_fields` raises an error (or warning).\n- `field_weights=None` for a field marks it as a value field (stored/retrieved but not used in matching). Default: all fields except the last are keys.\n- `memory_decay_rate='AUTO'` resolves at construction time to `1 / memory_capacity`; pass `0` explicitly to disable decay.\n- `softmax_choice` of `ARG_MAX` or `PROBABILISTIC` is incompatible with `learn()` — will raise an error if called.\n- `enable_learning=True` with `concatenate_queries=True` or only one key field has no effect on field weights and emits a warning; set `enable_learning=False` in those cases.\n- `use_gating_for_weighting=True` + `enable_learning=True` raises an error when `learn()` is called.\n- Nodes and projections cannot be added to an EMComposition after construction.\n- If all memory entries are initialized to zero and `normalize_memories=True`, a divide-by-zero warning is issued; use a non-zero `memory_fill` to avoid it."


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
        'Call this to instantiate an EMComposition — a differentiable episodic memory store that supports content-addressable retrieval and optional learning of field weights.'
        return _impl(args or {})
