"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool
from psyneulink_mcp import method_helpers

__source_sha256__ = 'a15ac93059fa817d87c3585b2ddfa68fa8beae134fec68d79c74bcf30c94fa53'
__pnl_qualname__ = 'psyneulink.Composition.add_td_learning_pathway'
__pnl_kind__ = 'method'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'add_td_learning_pathway'
TOOL_DESCRIPTION = 'Call this tool to add a TD (Temporal Difference) reinforcement learning pathway to an existing Composition using the TDLearning function. Use it when building a reward-prediction-error learning circuit between two Mechanisms. Returns a Pathway object representing the added TD learning pathway.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "composition": {\n      "description": "Handle string of the Composition to add the pathway to, as returned by create_composition.",\n      "type": "string"\n    },\n    "default_projection_matrix": {\n      "description": "Handle string or matrix keyword (e.g. \'RANDOM_CONNECTIVITY_MATRIX\') specifying the matrix for any auto-created MappingProjections. Overrides the MappingProjection default. Omit to use default.",\n      "type": "string"\n    },\n    "learning_rate": {\n      "description": "Learning rate for the TDLearning function of the LearningMechanism. Default is 0.05.",\n      "type": "number"\n    },\n    "learning_update": {\n      "description": "When the learned projection\'s matrix is updated each trial. \'online\' updates during execution; \'after\' updates at the end of each TRIAL. Default is \'online\' (note: docstring incorrectly states \'AFTER\').",\n      "enum": [\n        "online",\n        "after"\n      ],\n      "type": "string"\n    },\n    "name": {\n      "description": "Name for the Pathway. Overrides any name already assigned to a Pathway object passed in pathway.",\n      "type": "string"\n    },\n    "pathway": {\n      "description": "List of two or three handle strings: [Node1, Node2] or [Node1, MappingProjection, Node2]. If a MappingProjection handle is included, it becomes the learned projection; otherwise a default MappingProjection is created automatically.",\n      "items": {\n        "type": "string"\n      },\n      "type": "array"\n    }\n  },\n  "required": [\n    "composition",\n    "pathway"\n  ],\n  "type": "object"\n}\n\nNotes:\nThe source-code default for learning_update is \'online\', but the docstring says \'AFTER\' — trust the source; actual default is \'online\'. The error_function parameter appears in the docstring and method signature but is silently dropped: the implementation does not forward it to add_linear_learning_pathway, so passing it has no effect. Pathway node handles must be strings referencing live Mechanism objects registered with the runtime (e.g. handles from create_transfer_mechanism). This method is a thin wrapper around add_linear_learning_pathway with learning_function fixed to TDLearning; for any learning function other than TDLearning, use add_linear_learning_pathway directly.'
TOOL_PARAMETERS = { 'properties': { 'composition': { 'description': 'Handle string of the Composition to '
                                                  'add the pathway to, as returned by '
                                                  'create_composition.',
                                   'type': 'string'},
                  'default_projection_matrix': { 'description': 'Handle string or '
                                                                'matrix keyword (e.g. '
                                                                "'RANDOM_CONNECTIVITY_MATRIX') "
                                                                'specifying the matrix '
                                                                'for any auto-created '
                                                                'MappingProjections. '
                                                                'Overrides the '
                                                                'MappingProjection '
                                                                'default. Omit to use '
                                                                'default.',
                                                 'type': 'string'},
                  'learning_rate': { 'description': 'Learning rate for the TDLearning '
                                                    'function of the '
                                                    'LearningMechanism. Default is '
                                                    '0.05.',
                                     'type': 'number'},
                  'learning_update': { 'description': "When the learned projection's "
                                                      'matrix is updated each trial. '
                                                      "'online' updates during "
                                                      "execution; 'after' updates at "
                                                      'the end of each TRIAL. Default '
                                                      "is 'online' (note: docstring "
                                                      "incorrectly states 'AFTER').",
                                       'enum': ['online', 'after'],
                                       'type': 'string'},
                  'name': { 'description': 'Name for the Pathway. Overrides any name '
                                           'already assigned to a Pathway object '
                                           'passed in pathway.',
                            'type': 'string'},
                  'pathway': { 'description': 'List of two or three handle strings: '
                                              '[Node1, Node2] or [Node1, '
                                              'MappingProjection, Node2]. If a '
                                              'MappingProjection handle is included, '
                                              'it becomes the learned projection; '
                                              'otherwise a default MappingProjection '
                                              'is created automatically.',
                               'items': {'type': 'string'},
                               'type': 'array'}},
  'required': ['composition', 'pathway'],
  'type': 'object'}
TOOL_NOTES = "The source-code default for learning_update is 'online', but the docstring says 'AFTER' — trust the source; actual default is 'online'. The error_function parameter appears in the docstring and method signature but is silently dropped: the implementation does not forward it to add_linear_learning_pathway, so passing it has no effect. Pathway node handles must be strings referencing live Mechanism objects registered with the runtime (e.g. handles from create_transfer_mechanism). This method is a thin wrapper around add_linear_learning_pathway with learning_function fixed to TDLearning; for any learning function other than TDLearning, use add_linear_learning_pathway directly."


def _impl(kwargs: dict[str, Any]) -> Any:
    cls = pnl.Composition
    return method_helpers.call_method_tool(
        owner_cls=cls,
        method_name='add_td_learning_pathway',
        kwargs=kwargs,
        tool_name=TOOL_NAME,
    )


def register(mcp: Any) -> None:
    @captured_tool(mcp, layer="generated", name=TOOL_NAME, description=TOOL_DESCRIPTION)
    def add_td_learning_pathway(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to add a TD (Temporal Difference) reinforcement learning pathway to an existing Composition using the TDLearning function.'
        return _impl(args or {})
