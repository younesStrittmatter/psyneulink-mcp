"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '71dd8b64e4c42114b6ed3a65bcfa0e0c48af235b32804fa184e32124e4a37884'
__pnl_qualname__ = 'psyneulink.Threshold'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_threshold'
TOOL_DESCRIPTION = 'Use this tool to create a scheduling Condition that halts or gates execution of a PsyNeuLink Composition until a named parameter on a specific node crosses (or reaches) a fixed threshold value. Returns a Threshold Condition object suitable for passing to a Scheduler or as a termination condition.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "atol": {\n      "default": 0,\n      "description": "Absolute tolerance for equality comparisons (\'==\' and \'!=\'). Ignored for inequality comparators.",\n      "type": "number"\n    },\n    "comparator": {\n      "description": "The comparison operator. Equality operators (\'==\', \'!=\') support atol/rtol tolerances; inequality operators ignore tolerances.",\n      "enum": [\n        "<",\n        "<=",\n        ">",\n        ">=",\n        "==",\n        "!="\n      ],\n      "type": "string"\n    },\n    "dependency": {\n      "description": "The name or reference of the PsyNeuLink node whose parameter is monitored.",\n      "type": "string"\n    },\n    "indices": {\n      "default": null,\n      "description": "Index path into the parameter value when it is iterable (e.g., [0] for the first element). Required if the parameter value has more than one item. Can also be a TimeScale enum name string.",\n      "items": {\n        "type": "integer"\n      },\n      "type": "array"\n    },\n    "parameter": {\n      "description": "The name of the parameter on \'dependency\' to compare (e.g., \'value\', \'noise\', \'threshold\'). Must be a valid parameter of the dependency node.",\n      "type": "string"\n    },\n    "rtol": {\n      "default": 0,\n      "description": "Relative tolerance (relative to threshold) for equality comparisons (\'==\' and \'!=\'). Ignored for inequality comparators.",\n      "type": "number"\n    },\n    "threshold": {\n      "description": "The fixed scalar value to compare the parameter against.",\n      "type": "number"\n    }\n  },\n  "required": [\n    "dependency",\n    "parameter",\n    "threshold",\n    "comparator"\n  ],\n  "type": "object"\n}\n\nNotes:\n- `comparator` must be exactly one of: `<`, `<=`, `>`, `>=`, `==`, `!=` — any other string raises ConditionError at construction time.\n- `parameter` must exist on the dependency node — passing an invalid name raises ConditionError immediately.\n- The comparison is always scalar. If the parameter value is a multi-element array or list and `indices` is not provided, the condition will error at evaluation time. Use `indices` to drill into the value (e.g., `[0]` for the first element).\n- `atol` and `rtol` are silently ignored (with a warning) when `comparator` is `<`, `<=`, `>`, or `>=`. Only meaningful for `==` and `!=`.\n- `rtol` is relative to `threshold`, not to the parameter value (mirrors `numpy.isclose` convention).\n- A single integer for `indices` is automatically wrapped in a list internally.'
TOOL_PARAMETERS = { 'properties': { 'atol': { 'default': 0,
                            'description': 'Absolute tolerance for equality '
                                           "comparisons ('==' and '!='). Ignored for "
                                           'inequality comparators.',
                            'type': 'number'},
                  'comparator': { 'description': 'The comparison operator. Equality '
                                                 "operators ('==', '!=') support "
                                                 'atol/rtol tolerances; inequality '
                                                 'operators ignore tolerances.',
                                  'enum': ['<', '<=', '>', '>=', '==', '!='],
                                  'type': 'string'},
                  'dependency': { 'description': 'The name or reference of the '
                                                 'PsyNeuLink node whose parameter is '
                                                 'monitored.',
                                  'type': 'string'},
                  'indices': { 'default': None,
                               'description': 'Index path into the parameter value '
                                              'when it is iterable (e.g., [0] for the '
                                              'first element). Required if the '
                                              'parameter value has more than one item. '
                                              'Can also be a TimeScale enum name '
                                              'string.',
                               'items': {'type': 'integer'},
                               'type': 'array'},
                  'parameter': { 'description': 'The name of the parameter on '
                                                "'dependency' to compare (e.g., "
                                                "'value', 'noise', 'threshold'). Must "
                                                'be a valid parameter of the '
                                                'dependency node.',
                                 'type': 'string'},
                  'rtol': { 'default': 0,
                            'description': 'Relative tolerance (relative to threshold) '
                                           "for equality comparisons ('==' and '!='). "
                                           'Ignored for inequality comparators.',
                            'type': 'number'},
                  'threshold': { 'description': 'The fixed scalar value to compare the '
                                                'parameter against.',
                                 'type': 'number'}},
  'required': ['dependency', 'parameter', 'threshold', 'comparator'],
  'type': 'object'}
TOOL_NOTES = '- `comparator` must be exactly one of: `<`, `<=`, `>`, `>=`, `==`, `!=` — any other string raises ConditionError at construction time.\n- `parameter` must exist on the dependency node — passing an invalid name raises ConditionError immediately.\n- The comparison is always scalar. If the parameter value is a multi-element array or list and `indices` is not provided, the condition will error at evaluation time. Use `indices` to drill into the value (e.g., `[0]` for the first element).\n- `atol` and `rtol` are silently ignored (with a warning) when `comparator` is `<`, `<=`, `>`, or `>=`. Only meaningful for `==` and `!=`.\n- `rtol` is relative to `threshold`, not to the parameter value (mirrors `numpy.isclose` convention).\n- A single integer for `indices` is automatically wrapped in a list internally.'


def _impl(**kwargs: Any) -> Any:
    target = pnl.Threshold
    instance = target(**kwargs)
    return repr(instance)


def register(mcp: Any) -> None:
    @captured_tool(mcp, layer="generated", name=TOOL_NAME, description=TOOL_DESCRIPTION)
    def create_threshold(**kwargs: Any) -> Any:
        'Use this tool to create a scheduling Condition that halts or gates execution of a PsyNeuLink Composition until a named parameter on a specific node crosses (or reaches) a fixed threshold value.'
        return _impl(**kwargs)
