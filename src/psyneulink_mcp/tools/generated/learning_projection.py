"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = 'ef9f13562ee41f121ebb65f073d1afefdc8a4df951db357de0491c29f0cc5eae'
__pnl_qualname__ = 'psyneulink.LearningProjection'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_learning_projection'
TOOL_DESCRIPTION = 'Call this tool to explicitly create a LearningProjection that carries weight-change signals from a LearningMechanism (or its LearningSignal) to the MATRIX ParameterPort of a MappingProjection, enabling learning on that projection\'s weights. Use it when you need fine-grained control over how a specific MappingProjection is trained — for instance, to wire up a custom learning rule, override `learning_enabled` timing, or connect a pre-built LearningMechanism to a target weight matrix. The result is a LearningProjection object whose `weight_change_matrix` (2D array) is applied to the learned projection\'s matrix on each learning step.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "error_function": {\n      "description": "Name or spec of the function used by the TARGET/ComparatorMechanism to compute the error signal. Must accept a 2-item variable (SAMPLE and TARGET). Defaults to LinearCombination(weights=[[-1],[1]]).",\n      "type": "string"\n    },\n    "exponent": {\n      "description": "Exponent applied to the learning signal value. Standard Projection exponent parameter.",\n      "type": "number"\n    },\n    "learning_enabled": {\n      "description": "Controls whether/when weight changes are applied: true/false to enable or disable, \'online\' to apply during execution, \'after\' to apply after the learned projection completes. If omitted, inherits from the sender LearningMechanism.",\n      "enum": [\n        "true",\n        "false",\n        "online",\n        "after"\n      ],\n      "type": "string"\n    },\n    "learning_function": {\n      "description": "Deprecated. Name or spec of the learning function passed to the LearningMechanism. Defaults to BackPropagation. Prefer setting the learning function on the LearningMechanism directly.",\n      "type": "string"\n    },\n    "name": {\n      "description": "Optional string name for the LearningProjection instance.",\n      "type": "string"\n    },\n    "params": {\n      "additionalProperties": true,\n      "description": "Optional dict of additional parameter overrides passed to the base Projection constructor.",\n      "type": "object"\n    },\n    "receiver": {\n      "description": "Name of the MappingProjection (or its MATRIX ParameterPort) whose weight matrix will be modified. If a MappingProjection name is given, PNL resolves it to its MATRIX ParameterPort automatically. If omitted, initialization is deferred.",\n      "type": "string"\n    },\n    "sender": {\n      "description": "Name of the LearningMechanism or LearningSignal that provides the learning signal. If omitted, initialization is deferred until the projection is placed in a Composition context.",\n      "type": "string"\n    },\n    "weight": {\n      "description": "Scalar weight applied to the learning signal value before it modifies the matrix. Standard Projection weight parameter.",\n      "type": "number"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\nInitialization is deferred (no error raised immediately) if either sender or receiver is omitted — the projection becomes active only once both are resolved inside a Composition. Passing a MappingProjection as receiver is valid; PNL auto-resolves it to the MATRIX ParameterPort, so you do not need to specify the ParameterPort explicitly. `learning_function` is a legacy argument preserved for backward compatibility; the docstring explicitly advises against using it — set the learning function on the LearningMechanism instead. `learning_enabled` defaults to the sender LearningMechanism\'s value if not set here. The `weight_change_matrix` (same as `value`) is a 2D ndarray; rows correspond to the learned projection\'s sender, columns to its receiver. In practice, LearningProjections are created automatically when you add learning to a Composition — only create one explicitly when you need non-default wiring or learning control.'
TOOL_PARAMETERS = { 'properties': { 'error_function': { 'description': 'Name or spec of the function '
                                                     'used by the '
                                                     'TARGET/ComparatorMechanism to '
                                                     'compute the error signal. Must '
                                                     'accept a 2-item variable (SAMPLE '
                                                     'and TARGET). Defaults to '
                                                     'LinearCombination(weights=[[-1],[1]]).',
                                      'type': 'string'},
                  'exponent': { 'description': 'Exponent applied to the learning '
                                               'signal value. Standard Projection '
                                               'exponent parameter.',
                                'type': 'number'},
                  'learning_enabled': { 'description': 'Controls whether/when weight '
                                                       'changes are applied: '
                                                       'true/false to enable or '
                                                       "disable, 'online' to apply "
                                                       "during execution, 'after' to "
                                                       'apply after the learned '
                                                       'projection completes. If '
                                                       'omitted, inherits from the '
                                                       'sender LearningMechanism.',
                                        'enum': ['true', 'false', 'online', 'after'],
                                        'type': 'string'},
                  'learning_function': { 'description': 'Deprecated. Name or spec of '
                                                        'the learning function passed '
                                                        'to the LearningMechanism. '
                                                        'Defaults to BackPropagation. '
                                                        'Prefer setting the learning '
                                                        'function on the '
                                                        'LearningMechanism directly.',
                                         'type': 'string'},
                  'name': { 'description': 'Optional string name for the '
                                           'LearningProjection instance.',
                            'type': 'string'},
                  'params': { 'additionalProperties': True,
                              'description': 'Optional dict of additional parameter '
                                             'overrides passed to the base Projection '
                                             'constructor.',
                              'type': 'object'},
                  'receiver': { 'description': 'Name of the MappingProjection (or its '
                                               'MATRIX ParameterPort) whose weight '
                                               'matrix will be modified. If a '
                                               'MappingProjection name is given, PNL '
                                               'resolves it to its MATRIX '
                                               'ParameterPort automatically. If '
                                               'omitted, initialization is deferred.',
                                'type': 'string'},
                  'sender': { 'description': 'Name of the LearningMechanism or '
                                             'LearningSignal that provides the '
                                             'learning signal. If omitted, '
                                             'initialization is deferred until the '
                                             'projection is placed in a Composition '
                                             'context.',
                              'type': 'string'},
                  'weight': { 'description': 'Scalar weight applied to the learning '
                                             'signal value before it modifies the '
                                             'matrix. Standard Projection weight '
                                             'parameter.',
                              'type': 'number'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = "Initialization is deferred (no error raised immediately) if either sender or receiver is omitted — the projection becomes active only once both are resolved inside a Composition. Passing a MappingProjection as receiver is valid; PNL auto-resolves it to the MATRIX ParameterPort, so you do not need to specify the ParameterPort explicitly. `learning_function` is a legacy argument preserved for backward compatibility; the docstring explicitly advises against using it — set the learning function on the LearningMechanism instead. `learning_enabled` defaults to the sender LearningMechanism's value if not set here. The `weight_change_matrix` (same as `value`) is a 2D ndarray; rows correspond to the learned projection's sender, columns to its receiver. In practice, LearningProjections are created automatically when you add learning to a Composition — only create one explicitly when you need non-default wiring or learning control."


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.LearningProjection
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
    def create_learning_projection(args: dict[str, Any] | None = None) -> Any:
        "Call this tool to explicitly create a LearningProjection that carries weight-change signals from a LearningMechanism (or its LearningSignal) to the MATRIX ParameterPort of a MappingProjection, enabling learning on that projection's weights."
        return _impl(args or {})
