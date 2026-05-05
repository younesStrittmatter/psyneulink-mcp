"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = 'be8e4fd4910359cd1b19e5fccccc2d4160135f49f26e6dbf8816e423646a1998'
__pnl_qualname__ = 'psyneulink.EMStorageMechanism'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_em_storage_mechanism'
TOOL_DESCRIPTION = 'Call this tool to create the storage (write) component of a custom episodic memory system — an EMStorageMechanism that writes a new entry into a memory matrix by modifying the `matrix` parameters of `MappingProjections` via its `learning_signals`. Use it when building a hand-assembled EM architecture outside of `EMComposition`, or when you need explicit control over storage probability, decay rate, field weighting, or key/value field layout. The result is a `LearningMechanism` instance whose `learning_signals` directly update the projection matrices that implement the memory store.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "concatenation_node": {\n      "description": "Name or reference to an OutputPort or Mechanism where key-field values are concatenated before matching. When set, only one match learning_signal is required instead of one per key field.",\n      "type": "string"\n    },\n    "decay_rate": {\n      "default": 0,\n      "description": "Rate [0, 1] at which existing memory entries decay before the new entry is written. Applied to the full memory matrix each execution cycle.",\n      "maximum": 1,\n      "minimum": 0,\n      "type": "number"\n    },\n    "default_variable": {\n      "description": "2d array (list of 1d arrays) defining the shape of each field in a memory entry. Each inner array is a shape template for the corresponding field; must match the value shape of the corresponding OutputPort in `fields`.",\n      "items": {\n        "items": {\n          "type": "number"\n        },\n        "type": "array"\n      },\n      "type": "array"\n    },\n    "field_types": {\n      "description": "List of 1s (key fields) and 0s (value fields), one per entry in `fields`. Keys are used for content-addressable matching; values are retrieved. Must be the same length as `fields`.",\n      "items": {\n        "enum": [\n          0,\n          1\n        ],\n        "type": "integer"\n      },\n      "type": "array"\n    },\n    "field_weights": {\n      "description": "Optional floats in [0, 1] weighting each field\'s norm when identifying the weakest (least-used) memory slot. If omitted, norms are computed across all fields jointly.",\n      "items": {\n        "maximum": 1,\n        "minimum": 0,\n        "type": "number"\n      },\n      "type": "array"\n    },\n    "fields": {\n      "description": "OutputPort(s), Mechanism(s), or Projection(s) whose values supply the content for each field of a memory entry. Must be the same length as `default_variable`.",\n      "items": {},\n      "type": "array"\n    },\n    "function": {\n      "default": "EMStorage",\n      "description": "Learning function used to assign each field value to the memory matrix. Defaults to EMStorage. Custom functions must accept variable, memory_matrix, axis, storage_location, storage_prob, and decay_rate arguments.",\n      "type": "string"\n    },\n    "learning_signals": {\n      "description": "ParameterPorts (or Projections/tuples thereof) for the `matrix` parameter of the MappingProjections implementing memory. Required count: num_key_fields + len(fields), or 1 + len(fields) if concatenation_node is set. Match-field signals come first, then retrieval-field signals in original field order.",\n      "items": {},\n      "type": "array"\n    },\n    "memory_matrix": {\n      "description": "2d array defining the memory store shape. Rows are memory entries; columns are fields. Each row must have the same shape as `default_variable`.",\n      "items": {\n        "type": "array"\n      },\n      "type": "array"\n    },\n    "modulation": {\n      "default": "OVERRIDE",\n      "description": "How learning_signals modify the projection matrix parameters. OVERRIDE (default) writes entries exactly as specified; other values can produce unpredictable results.",\n      "enum": [\n        "OVERRIDE",\n        "ADDITIVE",\n        "MULTIPLICATIVE"\n      ],\n      "type": "string"\n    },\n    "name": {\n      "description": "Optional name for the mechanism instance.",\n      "type": "string"\n    },\n    "params": {\n      "description": "Optional dict of additional parameter overrides.",\n      "type": "object"\n    },\n    "storage_prob": {\n      "default": 1,\n      "description": "Probability [0, 1] that the current entry is stored on each execution. Modulable (aliases to MULTIPLICATIVE_PARAM).",\n      "maximum": 1,\n      "minimum": 0,\n      "type": "number"\n    }\n  },\n  "required": [\n    "default_variable",\n    "fields",\n    "field_types",\n    "learning_signals"\n  ],\n  "type": "object"\n}\n\nNotes:\n- `default_variable` is required as the first positional arg (named `default_variable` in `__init__`, not `variable`) — passing it as `variable` will fail.\n- `learning_signals` count must equal `num_match_fields + len(fields)`: `num_match_fields` is 1 if `concatenation_node` is set, otherwise the count of 1s in `field_types`. Passing the wrong count raises an error.\n- Match learning_signals (key fields) correspond to `axis=0` projections; retrieval learning_signals (all fields) correspond to `axis=1` projections — order matters and must align with `field_types`.\n- `memory_matrix` is read-only after construction (computed via a getter from the underlying projection matrices); pass it at construction time to set the initial memory shape.\n- `storage_prob` is a `FunctionParameter` delegated to the `EMStorage` function, not a direct Mechanism parameter — it can be modulated at runtime via `MULTIPLICATIVE_PARAM`.\n- `decay_rate` is applied to the entire memory matrix *before* the new entry is written each cycle.\n- `EMStorageMechanism` is normally created automatically inside `EMComposition`; instantiate it directly only when assembling a custom memory architecture where you control the MappingProjections manually.\n- `field_weights` validation will reject the list if its length differs from the number of fields, even if `None` items are present — pass `None` (omit the argument) to skip weighting entirely.'
TOOL_PARAMETERS = { 'properties': { 'concatenation_node': { 'description': 'Name or reference to an '
                                                         'OutputPort or Mechanism '
                                                         'where key-field values are '
                                                         'concatenated before '
                                                         'matching. When set, only one '
                                                         'match learning_signal is '
                                                         'required instead of one per '
                                                         'key field.',
                                          'type': 'string'},
                  'decay_rate': { 'default': 0,
                                  'description': 'Rate [0, 1] at which existing memory '
                                                 'entries decay before the new entry '
                                                 'is written. Applied to the full '
                                                 'memory matrix each execution cycle.',
                                  'maximum': 1,
                                  'minimum': 0,
                                  'type': 'number'},
                  'default_variable': { 'description': '2d array (list of 1d arrays) '
                                                       'defining the shape of each '
                                                       'field in a memory entry. Each '
                                                       'inner array is a shape '
                                                       'template for the corresponding '
                                                       'field; must match the value '
                                                       'shape of the corresponding '
                                                       'OutputPort in `fields`.',
                                        'items': { 'items': {'type': 'number'},
                                                   'type': 'array'},
                                        'type': 'array'},
                  'field_types': { 'description': 'List of 1s (key fields) and 0s '
                                                  '(value fields), one per entry in '
                                                  '`fields`. Keys are used for '
                                                  'content-addressable matching; '
                                                  'values are retrieved. Must be the '
                                                  'same length as `fields`.',
                                   'items': {'enum': [0, 1], 'type': 'integer'},
                                   'type': 'array'},
                  'field_weights': { 'description': 'Optional floats in [0, 1] '
                                                    "weighting each field's norm when "
                                                    'identifying the weakest '
                                                    '(least-used) memory slot. If '
                                                    'omitted, norms are computed '
                                                    'across all fields jointly.',
                                     'items': { 'maximum': 1,
                                                'minimum': 0,
                                                'type': 'number'},
                                     'type': 'array'},
                  'fields': { 'description': 'OutputPort(s), Mechanism(s), or '
                                             'Projection(s) whose values supply the '
                                             'content for each field of a memory '
                                             'entry. Must be the same length as '
                                             '`default_variable`.',
                              'items': {},
                              'type': 'array'},
                  'function': { 'default': 'EMStorage',
                                'description': 'Learning function used to assign each '
                                               'field value to the memory matrix. '
                                               'Defaults to EMStorage. Custom '
                                               'functions must accept variable, '
                                               'memory_matrix, axis, storage_location, '
                                               'storage_prob, and decay_rate '
                                               'arguments.',
                                'type': 'string'},
                  'learning_signals': { 'description': 'ParameterPorts (or '
                                                       'Projections/tuples thereof) '
                                                       'for the `matrix` parameter of '
                                                       'the MappingProjections '
                                                       'implementing memory. Required '
                                                       'count: num_key_fields + '
                                                       'len(fields), or 1 + '
                                                       'len(fields) if '
                                                       'concatenation_node is set. '
                                                       'Match-field signals come '
                                                       'first, then retrieval-field '
                                                       'signals in original field '
                                                       'order.',
                                        'items': {},
                                        'type': 'array'},
                  'memory_matrix': { 'description': '2d array defining the memory '
                                                    'store shape. Rows are memory '
                                                    'entries; columns are fields. Each '
                                                    'row must have the same shape as '
                                                    '`default_variable`.',
                                     'items': {'type': 'array'},
                                     'type': 'array'},
                  'modulation': { 'default': 'OVERRIDE',
                                  'description': 'How learning_signals modify the '
                                                 'projection matrix parameters. '
                                                 'OVERRIDE (default) writes entries '
                                                 'exactly as specified; other values '
                                                 'can produce unpredictable results.',
                                  'enum': ['OVERRIDE', 'ADDITIVE', 'MULTIPLICATIVE'],
                                  'type': 'string'},
                  'name': { 'description': 'Optional name for the mechanism instance.',
                            'type': 'string'},
                  'params': { 'description': 'Optional dict of additional parameter '
                                             'overrides.',
                              'type': 'object'},
                  'storage_prob': { 'default': 1,
                                    'description': 'Probability [0, 1] that the '
                                                   'current entry is stored on each '
                                                   'execution. Modulable (aliases to '
                                                   'MULTIPLICATIVE_PARAM).',
                                    'maximum': 1,
                                    'minimum': 0,
                                    'type': 'number'}},
  'required': ['default_variable', 'fields', 'field_types', 'learning_signals'],
  'type': 'object'}
TOOL_NOTES = '- `default_variable` is required as the first positional arg (named `default_variable` in `__init__`, not `variable`) — passing it as `variable` will fail.\n- `learning_signals` count must equal `num_match_fields + len(fields)`: `num_match_fields` is 1 if `concatenation_node` is set, otherwise the count of 1s in `field_types`. Passing the wrong count raises an error.\n- Match learning_signals (key fields) correspond to `axis=0` projections; retrieval learning_signals (all fields) correspond to `axis=1` projections — order matters and must align with `field_types`.\n- `memory_matrix` is read-only after construction (computed via a getter from the underlying projection matrices); pass it at construction time to set the initial memory shape.\n- `storage_prob` is a `FunctionParameter` delegated to the `EMStorage` function, not a direct Mechanism parameter — it can be modulated at runtime via `MULTIPLICATIVE_PARAM`.\n- `decay_rate` is applied to the entire memory matrix *before* the new entry is written each cycle.\n- `EMStorageMechanism` is normally created automatically inside `EMComposition`; instantiate it directly only when assembling a custom memory architecture where you control the MappingProjections manually.\n- `field_weights` validation will reject the list if its length differs from the number of fields, even if `None` items are present — pass `None` (omit the argument) to skip weighting entirely.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.EMStorageMechanism
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
    def create_em_storage_mechanism(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to create the storage (write) component of a custom episodic memory system — an EMStorageMechanism that writes a new entry into a memory matrix by modifying the `matrix` parameters of `MappingProjections` via its `learning_signals`.'
        return _impl(args or {})
