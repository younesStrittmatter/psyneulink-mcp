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
TOOL_DESCRIPTION = 'Constructs a `psyneulink.EMComposition` — an `AutodiffComposition` subclass that implements a differentiable, content-addressable episodic memory whose `field_weights` can be learned. Use it when the model needs key/value memory with per-field weighted similarity matching, softmax retrieval, and (optionally) backprop-trainable weights — i.e., differentiable analogues of `EpisodicMemoryMechanism`. Beyond what `AutodiffComposition` / `Composition` already provide, this tool builds the full retrieval+storage subgraph for you (query/value input nodes, match nodes, optional concatenation, softmax retrieval, retrieved nodes, and an `EMStorageMechanism`). Returns a handle to a registered `EMComposition` that can be nested inside another `Composition` or used standalone via `run`/`learn`.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "concatenate_queries": {\n      "default": false,\n      "description": "If true, all key inputs are concatenated into a single vector before matching. Silently downgraded to false if there is only one key, if key field_weights aren\'t all equal, or if normalize_memories is false. Incompatible with learning of field_weights.",\n      "type": "boolean"\n    },\n    "enable_learning": {\n      "default": true,\n      "description": "If true, build PsyNeuLink learning pathways. Must be false when use_gating_for_weighting=true and when softmax_choice is ARG_MAX or PROBABILISTIC.",\n      "type": "boolean"\n    },\n    "field_names": {\n      "default": null,\n      "description": "Names for each field (length must equal number of fields in memory_template). Ignored if \'fields\' is supplied.",\n      "items": {\n        "type": "string"\n      },\n      "type": [\n        "array",\n        "null"\n      ]\n    },\n    "field_weights": {\n      "default": null,\n      "description": "Relative weight for each field during retrieval matching. Use a positive number for keys; null entries mark the field as a value (stored/retrieved but not matched). Length must match number of fields. Ignored if \'fields\' is supplied.",\n      "items": {\n        "type": [\n          "number",\n          "null"\n        ]\n      },\n      "type": [\n        "array",\n        "null"\n      ]\n    },\n    "fields": {\n      "additionalProperties": {\n        "properties": {\n          "field_weight": {\n            "type": [\n              "number",\n              "null"\n            ]\n          },\n          "learn_field_weight": {\n            "type": [\n              "boolean",\n              "number",\n              "null"\n            ]\n          },\n          "target_field": {\n            "type": "boolean"\n          }\n        },\n        "type": "object"\n      },\n      "default": null,\n      "description": "Dict keyed by field name, where each value is a dict with keys \'field_weight\' (float or null \\u2014 null marks the field as a value rather than a key), \'learn_field_weight\' (bool/float/null), and \'target_field\' (bool). One entry per field; the count must match the number of fields in memory_template. When supplied, do NOT also pass field_names / field_weights / learn_field_weights / target_fields \\u2014 those will be ignored with a warning.",\n      "type": [\n        "object",\n        "null"\n      ]\n    },\n    "learn_field_weights": {\n      "default": false,\n      "description": "Whether field_weights are learnable. Bool applies to all key fields; a list (length = num fields) gives per-field bool/learning_rate. Ignored if \'fields\' is supplied.",\n      "oneOf": [\n        {\n          "type": "boolean"\n        },\n        {\n          "items": {\n            "type": [\n              "boolean",\n              "number",\n              "null"\n            ]\n          },\n          "type": "array"\n        }\n      ]\n    },\n    "learning_rate": {\n      "default": 0.01,\n      "description": "Default learning rate for any field_weight not given its own rate. Dict form is NOT accepted here \\u2014 use \'fields\' or \'learn_field_weights\' for per-field rates.",\n      "type": "number"\n    },\n    "memory_capacity": {\n      "default": null,\n      "description": "Number of items the memory holds. If null/omitted, defaults to 1000 (or to the leading dimension of memory_template if it is 3D).",\n      "type": [\n        "integer",\n        "null"\n      ]\n    },\n    "memory_decay_rate": {\n      "default": "AUTO",\n      "description": "Per-step decay applied to existing memories before each store. Number in [0, 1], or \'AUTO\' to set 1/memory_capacity, or 0 to disable decay.",\n      "oneOf": [\n        {\n          "type": "number"\n        },\n        {\n          "enum": [\n            "AUTO"\n          ],\n          "type": "string"\n        }\n      ]\n    },\n    "memory_fill": {\n      "default": 0,\n      "description": "Value used to fill memory at initialization. Scalar fills all entries with that value; a 2-element array [low, high] draws uniform random fills. If memories are normalized, avoid all-zeros (a divide-by-zero warning will fire); use a small nonzero scalar or [low, high].",\n      "oneOf": [\n        {\n          "type": "number"\n        },\n        {\n          "items": {\n            "type": "number"\n          },\n          "maxItems": 2,\n          "minItems": 2,\n          "type": "array"\n        }\n      ]\n    },\n    "memory_template": {\n      "default": [\n        [\n          0\n        ],\n        [\n          0\n        ]\n      ],\n      "description": "Shape/contents of a memory entry. MUST be a 2D or 3D array of arrays (one inner array per field, e.g. [[0]*5, [0]*5] for two 5-dim fields, or a 3D list-of-entries for a partially-filled memory). Do NOT pass a flat list of ints like [2, 20] \\u2014 the tuple-shape form (num_fields, field_len) is only honored for Python tuples, and a JSON array is interpreted as a list, which raises \'object of type int has no len()\'. Use [[0]*20, [0]*20] instead.",\n      "oneOf": [\n        {\n          "items": {\n            "items": {\n              "type": "number"\n            },\n            "type": "array"\n          },\n          "type": "array"\n        },\n        {\n          "items": {\n            "items": {\n              "items": {\n                "type": "number"\n              },\n              "type": "array"\n            },\n            "type": "array"\n          },\n          "type": "array"\n        }\n      ]\n    },\n    "name": {\n      "default": "EM_Composition",\n      "description": "Name of the EMComposition instance.",\n      "type": "string"\n    },\n    "normalize_field_weights": {\n      "default": true,\n      "description": "If true, field_weights are normalized to sum to 1 across keys; if false, used as absolute weights.",\n      "type": "boolean"\n    },\n    "normalize_memories": {\n      "default": true,\n      "description": "If true, keys and stored memories are L2-normalized before dot product (cosine similarity). Set false to use raw dot products.",\n      "type": "boolean"\n    },\n    "purge_by_field_weights": {\n      "default": false,\n      "description": "If true, weight per-field norms by field_weights when picking the slot to overwrite.",\n      "type": "boolean"\n    },\n    "softmax_choice": {\n      "description": "How softmax output is used for retrieval: \'WEIGHTED_AVG\' (default), \'ARG_MAX\', or \'PROBABILISTIC\'. PREFER OMITTING this argument: explicitly passing \'WEIGHTED_AVG\' currently triggers a PsyNeuLink type-validation error inside SoftMax/OneHot. ARG_MAX and PROBABILISTIC only work with enable_learning=false (using them with learning will raise from the learn() method).",\n      "enum": [\n        "WEIGHTED_AVG",\n        "ARG_MAX",\n        "PROBABILISTIC"\n      ],\n      "type": "string"\n    },\n    "softmax_gain": {\n      "default": 1,\n      "description": "Inverse temperature for the retrieval softmax. Number for fixed gain, \'ADAPTIVE\' for entropy-adaptive gain, or \'CONTROL\' to add a ControlMechanism that learns gain.",\n      "oneOf": [\n        {\n          "type": "number"\n        },\n        {\n          "enum": [\n            "ADAPTIVE",\n            "CONTROL"\n          ],\n          "type": "string"\n        }\n      ]\n    },\n    "softmax_threshold": {\n      "default": 0.001,\n      "description": "Mask threshold below which softmax inputs are zeroed. Must be > 0 if specified, or null.",\n      "type": [\n        "number",\n        "null"\n      ]\n    },\n    "storage_prob": {\n      "default": 1,\n      "description": "Probability in [0, 1] of storing the current input on each execution.",\n      "type": "number"\n    },\n    "store_on_optimization": {\n      "default": "FIRST",\n      "description": "Which optimization step(s) within a learning trial trigger storage.",\n      "enum": [\n        "FIRST",\n        "LAST",\n        "ALL"\n      ],\n      "type": "string"\n    },\n    "target_fields": {\n      "default": null,\n      "description": "Per-field bool list selecting which retrieved fields receive error signals during learning. Length must equal number of fields. Ignored if \'fields\' is supplied.",\n      "items": {\n        "type": "boolean"\n      },\n      "type": [\n        "array",\n        "null"\n      ]\n    },\n    "use_gating_for_weighting": {\n      "default": false,\n      "description": "If true, weight match_nodes via output gating instead of multiplicative input. Forces enable_learning=false.",\n      "type": "boolean"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\nmemory_template gotcha (recurring failure mode in feedback): a JSON array of plain ints like [2, 20] is interpreted as a list (not a Python tuple), so PsyNeuLink does NOT treat it as a (num_fields, field_len) shape spec — it tries to read each int as a field and crashes with "object of type \'int\' has no len()". Always pass concrete arrays of arrays, e.g. [[0.0001]*20, [0.0001]*20] for two 20-dim fields. softmax_choice=\'WEIGHTED_AVG\' has been observed to raise a beartype error inside the inner OneHot function (OneHot\'s mode= literal does not include \'WEIGHTED_AVG\'); the safest call is to omit softmax_choice entirely. ARG_MAX and PROBABILISTIC are only usable when enable_learning=false. fields and the legacy field_names/field_weights/learn_field_weights/target_fields args are mutually exclusive — passing both warns and silently ignores the legacy ones. With normalize_memories=true, all-zero memory initialization triggers a divide-by-zero warning at construction; pass a nonzero memory_fill (scalar or [low, high]). learning_rate as a dict is rejected by EMComposition (unlike AutodiffComposition); use \'fields\' or \'learn_field_weights\' for per-field rates. concatenate_queries silently downgrades to false unless num_keys>1, all key field_weights are equal, and normalize_memories is true; it is also incompatible with learning. memory_decay_rate=\'AUTO\' resolves to 1/memory_capacity at construction time.'
TOOL_PARAMETERS = { 'properties': { 'concatenate_queries': { 'default': False,
                                           'description': 'If true, all key inputs are '
                                                          'concatenated into a single '
                                                          'vector before matching. '
                                                          'Silently downgraded to '
                                                          'false if there is only one '
                                                          'key, if key field_weights '
                                                          "aren't all equal, or if "
                                                          'normalize_memories is '
                                                          'false. Incompatible with '
                                                          'learning of field_weights.',
                                           'type': 'boolean'},
                  'enable_learning': { 'default': True,
                                       'description': 'If true, build PsyNeuLink '
                                                      'learning pathways. Must be '
                                                      'false when '
                                                      'use_gating_for_weighting=true '
                                                      'and when softmax_choice is '
                                                      'ARG_MAX or PROBABILISTIC.',
                                       'type': 'boolean'},
                  'field_names': { 'default': None,
                                   'description': 'Names for each field (length must '
                                                  'equal number of fields in '
                                                  'memory_template). Ignored if '
                                                  "'fields' is supplied.",
                                   'items': {'type': 'string'},
                                   'type': ['array', 'null']},
                  'field_weights': { 'default': None,
                                     'description': 'Relative weight for each field '
                                                    'during retrieval matching. Use a '
                                                    'positive number for keys; null '
                                                    'entries mark the field as a value '
                                                    '(stored/retrieved but not '
                                                    'matched). Length must match '
                                                    'number of fields. Ignored if '
                                                    "'fields' is supplied.",
                                     'items': {'type': ['number', 'null']},
                                     'type': ['array', 'null']},
                  'fields': { 'additionalProperties': { 'properties': { 'field_weight': { 'type': [ 'number',
                                                                                                    'null']},
                                                                        'learn_field_weight': { 'type': [ 'boolean',
                                                                                                          'number',
                                                                                                          'null']},
                                                                        'target_field': { 'type': 'boolean'}},
                                                        'type': 'object'},
                              'default': None,
                              'description': 'Dict keyed by field name, where each '
                                             "value is a dict with keys 'field_weight' "
                                             '(float or null — null marks the field as '
                                             'a value rather than a key), '
                                             "'learn_field_weight' (bool/float/null), "
                                             "and 'target_field' (bool). One entry per "
                                             'field; the count must match the number '
                                             'of fields in memory_template. When '
                                             'supplied, do NOT also pass field_names / '
                                             'field_weights / learn_field_weights / '
                                             'target_fields — those will be ignored '
                                             'with a warning.',
                              'type': ['object', 'null']},
                  'learn_field_weights': { 'default': False,
                                           'description': 'Whether field_weights are '
                                                          'learnable. Bool applies to '
                                                          'all key fields; a list '
                                                          '(length = num fields) gives '
                                                          'per-field '
                                                          'bool/learning_rate. Ignored '
                                                          "if 'fields' is supplied.",
                                           'oneOf': [ {'type': 'boolean'},
                                                      { 'items': { 'type': [ 'boolean',
                                                                             'number',
                                                                             'null']},
                                                        'type': 'array'}]},
                  'learning_rate': { 'default': 0.01,
                                     'description': 'Default learning rate for any '
                                                    'field_weight not given its own '
                                                    'rate. Dict form is NOT accepted '
                                                    "here — use 'fields' or "
                                                    "'learn_field_weights' for "
                                                    'per-field rates.',
                                     'type': 'number'},
                  'memory_capacity': { 'default': None,
                                       'description': 'Number of items the memory '
                                                      'holds. If null/omitted, '
                                                      'defaults to 1000 (or to the '
                                                      'leading dimension of '
                                                      'memory_template if it is 3D).',
                                       'type': ['integer', 'null']},
                  'memory_decay_rate': { 'default': 'AUTO',
                                         'description': 'Per-step decay applied to '
                                                        'existing memories before each '
                                                        'store. Number in [0, 1], or '
                                                        "'AUTO' to set "
                                                        '1/memory_capacity, or 0 to '
                                                        'disable decay.',
                                         'oneOf': [ {'type': 'number'},
                                                    { 'enum': ['AUTO'],
                                                      'type': 'string'}]},
                  'memory_fill': { 'default': 0,
                                   'description': 'Value used to fill memory at '
                                                  'initialization. Scalar fills all '
                                                  'entries with that value; a '
                                                  '2-element array [low, high] draws '
                                                  'uniform random fills. If memories '
                                                  'are normalized, avoid all-zeros (a '
                                                  'divide-by-zero warning will fire); '
                                                  'use a small nonzero scalar or [low, '
                                                  'high].',
                                   'oneOf': [ {'type': 'number'},
                                              { 'items': {'type': 'number'},
                                                'maxItems': 2,
                                                'minItems': 2,
                                                'type': 'array'}]},
                  'memory_template': { 'default': [[0], [0]],
                                       'description': 'Shape/contents of a memory '
                                                      'entry. MUST be a 2D or 3D array '
                                                      'of arrays (one inner array per '
                                                      'field, e.g. [[0]*5, [0]*5] for '
                                                      'two 5-dim fields, or a 3D '
                                                      'list-of-entries for a '
                                                      'partially-filled memory). Do '
                                                      'NOT pass a flat list of ints '
                                                      'like [2, 20] — the tuple-shape '
                                                      'form (num_fields, field_len) is '
                                                      'only honored for Python tuples, '
                                                      'and a JSON array is interpreted '
                                                      "as a list, which raises 'object "
                                                      "of type int has no len()'. Use "
                                                      '[[0]*20, [0]*20] instead.',
                                       'oneOf': [ { 'items': { 'items': { 'type': 'number'},
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
                                               'description': 'If true, field_weights '
                                                              'are normalized to sum '
                                                              'to 1 across keys; if '
                                                              'false, used as absolute '
                                                              'weights.',
                                               'type': 'boolean'},
                  'normalize_memories': { 'default': True,
                                          'description': 'If true, keys and stored '
                                                         'memories are L2-normalized '
                                                         'before dot product (cosine '
                                                         'similarity). Set false to '
                                                         'use raw dot products.',
                                          'type': 'boolean'},
                  'purge_by_field_weights': { 'default': False,
                                              'description': 'If true, weight '
                                                             'per-field norms by '
                                                             'field_weights when '
                                                             'picking the slot to '
                                                             'overwrite.',
                                              'type': 'boolean'},
                  'softmax_choice': { 'description': 'How softmax output is used for '
                                                     "retrieval: 'WEIGHTED_AVG' "
                                                     "(default), 'ARG_MAX', or "
                                                     "'PROBABILISTIC'. PREFER OMITTING "
                                                     'this argument: explicitly '
                                                     "passing 'WEIGHTED_AVG' currently "
                                                     'triggers a PsyNeuLink '
                                                     'type-validation error inside '
                                                     'SoftMax/OneHot. ARG_MAX and '
                                                     'PROBABILISTIC only work with '
                                                     'enable_learning=false (using '
                                                     'them with learning will raise '
                                                     'from the learn() method).',
                                      'enum': [ 'WEIGHTED_AVG',
                                                'ARG_MAX',
                                                'PROBABILISTIC'],
                                      'type': 'string'},
                  'softmax_gain': { 'default': 1,
                                    'description': 'Inverse temperature for the '
                                                   'retrieval softmax. Number for '
                                                   "fixed gain, 'ADAPTIVE' for "
                                                   'entropy-adaptive gain, or '
                                                   "'CONTROL' to add a "
                                                   'ControlMechanism that learns gain.',
                                    'oneOf': [ {'type': 'number'},
                                               { 'enum': ['ADAPTIVE', 'CONTROL'],
                                                 'type': 'string'}]},
                  'softmax_threshold': { 'default': 0.001,
                                         'description': 'Mask threshold below which '
                                                        'softmax inputs are zeroed. '
                                                        'Must be > 0 if specified, or '
                                                        'null.',
                                         'type': ['number', 'null']},
                  'storage_prob': { 'default': 1,
                                    'description': 'Probability in [0, 1] of storing '
                                                   'the current input on each '
                                                   'execution.',
                                    'type': 'number'},
                  'store_on_optimization': { 'default': 'FIRST',
                                             'description': 'Which optimization '
                                                            'step(s) within a learning '
                                                            'trial trigger storage.',
                                             'enum': ['FIRST', 'LAST', 'ALL'],
                                             'type': 'string'},
                  'target_fields': { 'default': None,
                                     'description': 'Per-field bool list selecting '
                                                    'which retrieved fields receive '
                                                    'error signals during learning. '
                                                    'Length must equal number of '
                                                    "fields. Ignored if 'fields' is "
                                                    'supplied.',
                                     'items': {'type': 'boolean'},
                                     'type': ['array', 'null']},
                  'use_gating_for_weighting': { 'default': False,
                                                'description': 'If true, weight '
                                                               'match_nodes via output '
                                                               'gating instead of '
                                                               'multiplicative input. '
                                                               'Forces '
                                                               'enable_learning=false.',
                                                'type': 'boolean'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = 'memory_template gotcha (recurring failure mode in feedback): a JSON array of plain ints like [2, 20] is interpreted as a list (not a Python tuple), so PsyNeuLink does NOT treat it as a (num_fields, field_len) shape spec — it tries to read each int as a field and crashes with "object of type \'int\' has no len()". Always pass concrete arrays of arrays, e.g. [[0.0001]*20, [0.0001]*20] for two 20-dim fields. softmax_choice=\'WEIGHTED_AVG\' has been observed to raise a beartype error inside the inner OneHot function (OneHot\'s mode= literal does not include \'WEIGHTED_AVG\'); the safest call is to omit softmax_choice entirely. ARG_MAX and PROBABILISTIC are only usable when enable_learning=false. fields and the legacy field_names/field_weights/learn_field_weights/target_fields args are mutually exclusive — passing both warns and silently ignores the legacy ones. With normalize_memories=true, all-zero memory initialization triggers a divide-by-zero warning at construction; pass a nonzero memory_fill (scalar or [low, high]). learning_rate as a dict is rejected by EMComposition (unlike AutodiffComposition); use \'fields\' or \'learn_field_weights\' for per-field rates. concatenate_queries silently downgrades to false unless num_keys>1, all key field_weights are equal, and normalize_memories is true; it is also incompatible with learning. memory_decay_rate=\'AUTO\' resolves to 1/memory_capacity at construction time.'


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
        'Constructs a `psyneulink.EMComposition` — an `AutodiffComposition` subclass that implements a differentiable, content-addressable episodic memory whose `field_weights` can be learned.'
        return _impl(args or {})
