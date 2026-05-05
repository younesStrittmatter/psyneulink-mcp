"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool
from psyneulink_mcp import method_helpers

__source_sha256__ = '093d25a3bff0f43a028d6ab023f5910c8bfbc82451fbc806329a767443e5846c'
__pnl_qualname__ = 'psyneulink.Composition.add_reinforcement_learning_pathway'
__pnl_kind__ = 'method'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'add_reinforcement_learning_pathway'
TOOL_DESCRIPTION = 'Call this tool to add a reinforcement learning (RL) pathway to an existing Composition — use it when two Mechanisms should be connected with a MappingProjection that learns via the Reinforcement rule (reward-signal-based weight updates). The tool returns a Pathway object handle representing the learned connection added to the Composition.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "composition": {\n      "description": "Handle string of the Composition to add the pathway to, as returned by create_composition.",\n      "type": "string"\n    },\n    "default_projection_matrix": {\n      "description": "Matrix to use for any auto-created MappingProjections. Pass a nested numeric array, a MATRIX_KEYWORD string (e.g. \'IDENTITY_MATRIX\'), or a function handle string. Omit to use MappingProjection defaults.",\n      "oneOf": [\n        {\n          "type": "array"\n        },\n        {\n          "type": "string"\n        }\n      ]\n    },\n    "error_function": {\n      "description": "Handle string or bare class name (e.g. \'LinearCombination\') for the function assigned to the ComparatorMechanism that computes the error signal. Defaults to LinearCombination.",\n      "type": "string"\n    },\n    "learning_rate": {\n      "description": "Learning rate for the ReinforcementLearning function of the LearningMechanism. Defaults to 0.05 if omitted.",\n      "type": "number"\n    },\n    "learning_update": {\n      "description": "When to update the learned projection\'s matrix each trial. \'online\' updates during execution; \'after\' updates after the trial completes; true/false enable/disable learning. Defaults to \'online\' per the method signature (note: docstring incorrectly states AFTER).",\n      "oneOf": [\n        {\n          "enum": [\n            "online",\n            "after"\n          ],\n          "type": "string"\n        },\n        {\n          "type": "boolean"\n        }\n      ]\n    },\n    "name": {\n      "description": "Name for the returned Pathway object. Overrides any name carried by a Pathway passed in pathway.",\n      "type": "string"\n    },\n    "pathway": {\n      "description": "Two- or three-element list of handle strings: [input_node, output_node] or [input_node, mapping_projection, output_node]. If two nodes are given, a default MappingProjection is created automatically as the learned projection.",\n      "items": {\n        "type": "string"\n      },\n      "type": "array"\n    }\n  },\n  "required": [\n    "composition",\n    "pathway"\n  ],\n  "type": "object"\n}\n\nNotes:\nThere is a discrepancy between the docstring (claims default learning_update is AFTER) and the actual method signature (default is \'online\'). The source code is authoritative — default is \'online\'. The learning_rate argument is typed Optional in the signature with default None, but the docstring advertises 0.05 as the effective default; the actual 0.05 fallback is applied inside add_linear_learning_pathway, not here. Pathway elements must be handles to already-added Mechanisms or Projections — nodes not yet added to the Composition will cause an error. error_function and default_projection_matrix accept PsyNeuLink handle strings that the runtime resolves to live objects before dispatch.'
TOOL_PARAMETERS = { 'properties': { 'composition': { 'description': 'Handle string of the Composition to '
                                                  'add the pathway to, as returned by '
                                                  'create_composition.',
                                   'type': 'string'},
                  'default_projection_matrix': { 'description': 'Matrix to use for any '
                                                                'auto-created '
                                                                'MappingProjections. '
                                                                'Pass a nested numeric '
                                                                'array, a '
                                                                'MATRIX_KEYWORD string '
                                                                '(e.g. '
                                                                "'IDENTITY_MATRIX'), "
                                                                'or a function handle '
                                                                'string. Omit to use '
                                                                'MappingProjection '
                                                                'defaults.',
                                                 'oneOf': [ {'type': 'array'},
                                                            {'type': 'string'}]},
                  'error_function': { 'description': 'Handle string or bare class name '
                                                     "(e.g. 'LinearCombination') for "
                                                     'the function assigned to the '
                                                     'ComparatorMechanism that '
                                                     'computes the error signal. '
                                                     'Defaults to LinearCombination.',
                                      'type': 'string'},
                  'learning_rate': { 'description': 'Learning rate for the '
                                                    'ReinforcementLearning function of '
                                                    'the LearningMechanism. Defaults '
                                                    'to 0.05 if omitted.',
                                     'type': 'number'},
                  'learning_update': { 'description': 'When to update the learned '
                                                      "projection's matrix each trial. "
                                                      "'online' updates during "
                                                      "execution; 'after' updates "
                                                      'after the trial completes; '
                                                      'true/false enable/disable '
                                                      "learning. Defaults to 'online' "
                                                      'per the method signature (note: '
                                                      'docstring incorrectly states '
                                                      'AFTER).',
                                       'oneOf': [ { 'enum': ['online', 'after'],
                                                    'type': 'string'},
                                                  {'type': 'boolean'}]},
                  'name': { 'description': 'Name for the returned Pathway object. '
                                           'Overrides any name carried by a Pathway '
                                           'passed in pathway.',
                            'type': 'string'},
                  'pathway': { 'description': 'Two- or three-element list of handle '
                                              'strings: [input_node, output_node] or '
                                              '[input_node, mapping_projection, '
                                              'output_node]. If two nodes are given, a '
                                              'default MappingProjection is created '
                                              'automatically as the learned '
                                              'projection.',
                               'items': {'type': 'string'},
                               'type': 'array'}},
  'required': ['composition', 'pathway'],
  'type': 'object'}
TOOL_NOTES = "There is a discrepancy between the docstring (claims default learning_update is AFTER) and the actual method signature (default is 'online'). The source code is authoritative — default is 'online'. The learning_rate argument is typed Optional in the signature with default None, but the docstring advertises 0.05 as the effective default; the actual 0.05 fallback is applied inside add_linear_learning_pathway, not here. Pathway elements must be handles to already-added Mechanisms or Projections — nodes not yet added to the Composition will cause an error. error_function and default_projection_matrix accept PsyNeuLink handle strings that the runtime resolves to live objects before dispatch."


def _impl(kwargs: dict[str, Any]) -> Any:
    cls = pnl.Composition
    return method_helpers.call_method_tool(
        owner_cls=cls,
        method_name='add_reinforcement_learning_pathway',
        kwargs=kwargs,
        tool_name=TOOL_NAME,
    )


def register(mcp: Any) -> None:
    @captured_tool(mcp, layer="generated", name=TOOL_NAME, description=TOOL_DESCRIPTION)
    def add_reinforcement_learning_pathway(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to add a reinforcement learning (RL) pathway to an existing Composition — use it when two Mechanisms should be connected with a MappingProjection that learns via the Reinforcement rule (reward-signal-based weight updates).'
        return _impl(args or {})
