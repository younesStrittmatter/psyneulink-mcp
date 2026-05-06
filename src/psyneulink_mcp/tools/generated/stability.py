"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '916cb886244fa17c05f9c7a530637204d9910513e4055d8cb83e33936e1c10af'
__pnl_qualname__ = 'psyneulink.core.components.functions.nonstateful.objectivefunctions.Stability'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_stability'
TOOL_DESCRIPTION = 'Call `create_stability` when you need a PsyNeuLink `Stability` objective function that measures how stable a 1-D state vector is under recurrent weight dynamics. Use it before building a `RecurrentTransferMechanism` or any network that requires an energy/distance stability metric. Returns a `Stability` handle that can be passed as the `function` argument to other PNL components.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "default_variable": {\n      "description": "1-D list of numbers defining both the size of the state space and its default values. REQUIRED \\u2014 always supply this (e.g. [0,0,0] for size 3). Using only `input_shapes` without this has caused a NoneType TypeError in matrix arithmetic (issue #1).",\n      "items": {\n        "type": "number"\n      },\n      "type": "array"\n    },\n    "input_shapes": {\n      "description": "Alternative to default_variable: length of the state array (zeros used as values). Unreliable when used alone \\u2014 pass `default_variable` instead whenever possible.",\n      "type": "integer"\n    },\n    "matrix": {\n      "default": "HOLLOW_MATRIX",\n      "description": "Recurrent weight matrix keyword. HOLLOW_MATRIX (default) eliminates self-connections. Custom numeric matrices cannot be passed through this JSON interface.",\n      "enum": [\n        "HOLLOW_MATRIX",\n        "IDENTITY_MATRIX",\n        "FULL_CONNECTIVITY_MATRIX",\n        "RANDOM_CONNECTIVITY_MATRIX"\n      ],\n      "type": "string"\n    },\n    "metric": {\n      "default": "ENERGY",\n      "description": "Stability/distance metric. ENERGY computes Hopfield-style energy. ENTROPY is internally converted to CROSS_ENTROPY by PNL.",\n      "enum": [\n        "ENERGY",\n        "ENTROPY",\n        "EUCLIDEAN",\n        "MAX_ABS_DIFF",\n        "COSINE",\n        "CORRELATION",\n        "CROSS_ENTROPY",\n        "L0",\n        "NORMED_L0_SIMILARITY",\n        "ANGLE"\n      ],\n      "type": "string"\n    },\n    "normalize": {\n      "default": false,\n      "description": "If true, divides the stability result by the length of the state vector, producing a per-unit metric.",\n      "type": "boolean"\n    }\n  },\n  "required": [\n    "default_variable"\n  ],\n  "type": "object"\n}\n\nNotes:\nCRITICAL: Do NOT pass `name` as a parameter. `Stability.__init__` does not accept `name`; doing so raises `TypeError: unexpected keyword argument \'name\'` (confirmed issue #2). The name attribute is set internally by PNL.\n\nCRITICAL: Always supply `default_variable` as a concrete list of numbers. Using `input_shapes` alone (without `default_variable`) causes `TypeError: unsupported operand type(s) for *: \'NoneType\' and \'float\'` during matrix instantiation (confirmed issue #1).\n\n`transfer_fct` (a Python callable) cannot be serialized to JSON and is excluded from this schema; it defaults to None.\n\nENTROPY metric is silently converted to CROSS_ENTROPY internally — expected behavior, not a bug.\n\nDo not pass `matrix` as the string `"HOLLOW_MATRIX"` if you can omit it; the default already applies HOLLOW_MATRIX correctly.'
TOOL_PARAMETERS = { 'properties': { 'default_variable': { 'description': '1-D list of numbers defining '
                                                       'both the size of the state '
                                                       'space and its default values. '
                                                       'REQUIRED — always supply this '
                                                       '(e.g. [0,0,0] for size 3). '
                                                       'Using only `input_shapes` '
                                                       'without this has caused a '
                                                       'NoneType TypeError in matrix '
                                                       'arithmetic (issue #1).',
                                        'items': {'type': 'number'},
                                        'type': 'array'},
                  'input_shapes': { 'description': 'Alternative to default_variable: '
                                                   'length of the state array (zeros '
                                                   'used as values). Unreliable when '
                                                   'used alone — pass '
                                                   '`default_variable` instead '
                                                   'whenever possible.',
                                    'type': 'integer'},
                  'matrix': { 'default': 'HOLLOW_MATRIX',
                              'description': 'Recurrent weight matrix keyword. '
                                             'HOLLOW_MATRIX (default) eliminates '
                                             'self-connections. Custom numeric '
                                             'matrices cannot be passed through this '
                                             'JSON interface.',
                              'enum': [ 'HOLLOW_MATRIX',
                                        'IDENTITY_MATRIX',
                                        'FULL_CONNECTIVITY_MATRIX',
                                        'RANDOM_CONNECTIVITY_MATRIX'],
                              'type': 'string'},
                  'metric': { 'default': 'ENERGY',
                              'description': 'Stability/distance metric. ENERGY '
                                             'computes Hopfield-style energy. ENTROPY '
                                             'is internally converted to CROSS_ENTROPY '
                                             'by PNL.',
                              'enum': [ 'ENERGY',
                                        'ENTROPY',
                                        'EUCLIDEAN',
                                        'MAX_ABS_DIFF',
                                        'COSINE',
                                        'CORRELATION',
                                        'CROSS_ENTROPY',
                                        'L0',
                                        'NORMED_L0_SIMILARITY',
                                        'ANGLE'],
                              'type': 'string'},
                  'normalize': { 'default': False,
                                 'description': 'If true, divides the stability result '
                                                'by the length of the state vector, '
                                                'producing a per-unit metric.',
                                 'type': 'boolean'}},
  'required': ['default_variable'],
  'type': 'object'}
TOOL_NOTES = 'CRITICAL: Do NOT pass `name` as a parameter. `Stability.__init__` does not accept `name`; doing so raises `TypeError: unexpected keyword argument \'name\'` (confirmed issue #2). The name attribute is set internally by PNL.\n\nCRITICAL: Always supply `default_variable` as a concrete list of numbers. Using `input_shapes` alone (without `default_variable`) causes `TypeError: unsupported operand type(s) for *: \'NoneType\' and \'float\'` during matrix instantiation (confirmed issue #1).\n\n`transfer_fct` (a Python callable) cannot be serialized to JSON and is excluded from this schema; it defaults to None.\n\nENTROPY metric is silently converted to CROSS_ENTROPY internally — expected behavior, not a bug.\n\nDo not pass `matrix` as the string `"HOLLOW_MATRIX"` if you can omit it; the default already applies HOLLOW_MATRIX correctly.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.Stability
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
    def create_stability(args: dict[str, Any] | None = None) -> Any:
        'Call `create_stability` when you need a PsyNeuLink `Stability` objective function that measures how stable a 1-D state vector is under recurrent weight dynamics.'
        return _impl(args or {})
