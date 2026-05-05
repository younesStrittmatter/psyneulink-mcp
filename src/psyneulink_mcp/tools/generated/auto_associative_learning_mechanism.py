"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '795cd6e119a9070f6e050dc652c927e159a56fa0257c89792c85fb467548510d'
__pnl_qualname__ = 'psyneulink.AutoAssociativeLearningMechanism'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_auto_associative_learning_mechanism'
TOOL_DESCRIPTION = 'Call this tool to create an AutoAssociativeLearningMechanism, which implements unsupervised Hebbian learning on the recurrent weight matrix of a RecurrentTransferMechanism. Use this when you need explicit control over how a RecurrentTransferMechanism\'s recurrent_projection learns — typically when you want to customize the learning function, learning rate, or learning signals beyond what RecurrentTransferMechanism\'s built-in learning parameter provides. Returns a LearningMechanism object that computes a weight-change matrix (learning_signal) from the activity vector of the recurrent layer.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "default_variable": {\n      "description": "A single-item list or 2d array whose inner element is a 1d numeric array matching the size of the RecurrentTransferMechanism\'s output. E.g., [[0.0, 0.0, 0.0]] for a 3-unit layer. This is required.",\n      "items": {\n        "items": {\n          "type": "number"\n        },\n        "type": "array"\n      },\n      "type": "array"\n    },\n    "function": {\n      "default": "Hebbian",\n      "description": "Name of the LearningFunction to use for computing the weight-change matrix. Must accept a 1d activity vector and return a square weight-change matrix. Default is \'Hebbian\'. Other options include \'Oja\' or \'Kohonen\'.",\n      "type": "string"\n    },\n    "learning_rate": {\n      "description": "Scalar learning rate to scale the weight-change matrix returned by the function. If None, inherits from the enclosing Composition\'s learning_rate, then from the function\'s default_learning_rate. A 1d or 2d array can also be passed for per-unit or per-connection scaling, but must be provided as a flat number here; use the Python API directly for array-valued rates.",\n      "type": "number"\n    },\n    "learning_signals": {\n      "description": "Specifies which AutoAssociativeProjection matrix parameters to train. Each entry can be a Projection, ParameterPort, a (str, Projection) tuple, or a dict. Defaults to LEARNING_SIGNAL (the primary learned projection). Only needed when training additional projections beyond the default.",\n      "items": {},\n      "type": "array"\n    },\n    "modulation": {\n      "default": "ADDITIVE",\n      "description": "How the learning_signal modulates the target matrix parameter. Default is \'ADDITIVE\' (adds the weight-change matrix to the existing weights). Other options: \'MULTIPLICATIVE\', \'OVERRIDE\'.",\n      "type": "string"\n    },\n    "name": {\n      "description": "Optional string name for this mechanism. Auto-generated if omitted.",\n      "type": "string"\n    }\n  },\n  "required": [\n    "default_variable"\n  ],\n  "type": "object"\n}\n\nNotes:\n- AutoAssociativeLearningMechanism is almost always created automatically when you pass `learning=True` to RecurrentTransferMechanism; construct it manually only when you need non-default learning behavior.\n- `default_variable` must be a 2d structure with exactly one inner 1d array (e.g., `[[0, 0, 0]]`), NOT a plain 1d list — the validator will reject a bare 1d array.\n- The function must return a *square* matrix whose side length equals the length of the activity vector; Hebbian, Oja, and Kohonen all satisfy this by design.\n- `learning_rate` as a scalar multiplies the entire weight-change matrix; a 1d array Hadamard-multiplies the *input* (scales per-unit contributions); a 2d array Hadamard-multiplies the *weight matrix* (scales per-connection contributions). Only the scalar case is representable in this JSON schema — pass array-valued rates via the Python API.\n- `modulation=ADDITIVE` means weight updates are *added* to existing weights each trial, which is the standard Hebbian update rule.\n- The mechanism has a single ACTIVATION_INPUT InputPort; connecting additional input sources is not supported.\n- `params` and `prefs` are low-level PsyNeuLink configuration objects; omit them unless you have a specific reason to set them.'
TOOL_PARAMETERS = { 'properties': { 'default_variable': { 'description': 'A single-item list or 2d array '
                                                       'whose inner element is a 1d '
                                                       'numeric array matching the '
                                                       'size of the '
                                                       "RecurrentTransferMechanism's "
                                                       'output. E.g., [[0.0, 0.0, '
                                                       '0.0]] for a 3-unit layer. This '
                                                       'is required.',
                                        'items': { 'items': {'type': 'number'},
                                                   'type': 'array'},
                                        'type': 'array'},
                  'function': { 'default': 'Hebbian',
                                'description': 'Name of the LearningFunction to use '
                                               'for computing the weight-change '
                                               'matrix. Must accept a 1d activity '
                                               'vector and return a square '
                                               'weight-change matrix. Default is '
                                               "'Hebbian'. Other options include 'Oja' "
                                               "or 'Kohonen'.",
                                'type': 'string'},
                  'learning_rate': { 'description': 'Scalar learning rate to scale the '
                                                    'weight-change matrix returned by '
                                                    'the function. If None, inherits '
                                                    "from the enclosing Composition's "
                                                    'learning_rate, then from the '
                                                    "function's default_learning_rate. "
                                                    'A 1d or 2d array can also be '
                                                    'passed for per-unit or '
                                                    'per-connection scaling, but must '
                                                    'be provided as a flat number '
                                                    'here; use the Python API directly '
                                                    'for array-valued rates.',
                                     'type': 'number'},
                  'learning_signals': { 'description': 'Specifies which '
                                                       'AutoAssociativeProjection '
                                                       'matrix parameters to train. '
                                                       'Each entry can be a '
                                                       'Projection, ParameterPort, a '
                                                       '(str, Projection) tuple, or a '
                                                       'dict. Defaults to '
                                                       'LEARNING_SIGNAL (the primary '
                                                       'learned projection). Only '
                                                       'needed when training '
                                                       'additional projections beyond '
                                                       'the default.',
                                        'items': {},
                                        'type': 'array'},
                  'modulation': { 'default': 'ADDITIVE',
                                  'description': 'How the learning_signal modulates '
                                                 'the target matrix parameter. Default '
                                                 "is 'ADDITIVE' (adds the "
                                                 'weight-change matrix to the existing '
                                                 'weights). Other options: '
                                                 "'MULTIPLICATIVE', 'OVERRIDE'.",
                                  'type': 'string'},
                  'name': { 'description': 'Optional string name for this mechanism. '
                                           'Auto-generated if omitted.',
                            'type': 'string'}},
  'required': ['default_variable'],
  'type': 'object'}
TOOL_NOTES = '- AutoAssociativeLearningMechanism is almost always created automatically when you pass `learning=True` to RecurrentTransferMechanism; construct it manually only when you need non-default learning behavior.\n- `default_variable` must be a 2d structure with exactly one inner 1d array (e.g., `[[0, 0, 0]]`), NOT a plain 1d list — the validator will reject a bare 1d array.\n- The function must return a *square* matrix whose side length equals the length of the activity vector; Hebbian, Oja, and Kohonen all satisfy this by design.\n- `learning_rate` as a scalar multiplies the entire weight-change matrix; a 1d array Hadamard-multiplies the *input* (scales per-unit contributions); a 2d array Hadamard-multiplies the *weight matrix* (scales per-connection contributions). Only the scalar case is representable in this JSON schema — pass array-valued rates via the Python API.\n- `modulation=ADDITIVE` means weight updates are *added* to existing weights each trial, which is the standard Hebbian update rule.\n- The mechanism has a single ACTIVATION_INPUT InputPort; connecting additional input sources is not supported.\n- `params` and `prefs` are low-level PsyNeuLink configuration objects; omit them unless you have a specific reason to set them.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.AutoAssociativeLearningMechanism
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
    def create_auto_associative_learning_mechanism(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to create an AutoAssociativeLearningMechanism, which implements unsupervised Hebbian learning on the recurrent weight matrix of a RecurrentTransferMechanism.'
        return _impl(args or {})
