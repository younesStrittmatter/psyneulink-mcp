"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool
from psyneulink_mcp import method_helpers

__source_sha256__ = 'dec7e2c43aedb463acfd67c48474c4696ad2076bf6106724e0c762890841f8e3'
__pnl_qualname__ = 'psyneulink.Composition.add_backpropagation_learning_pathway'
__pnl_kind__ = 'method'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'add_backpropagation_learning_pathway'
TOOL_DESCRIPTION = 'Call this tool after nodes and projections have been added to a Composition to wire up a backpropagation (gradient-descent) learning pathway between a sequence of Mechanisms. Use it when you want supervised learning with a target signal — it automatically creates LearningMechanisms, a ComparatorMechanism, and LearningProjections for the specified pathway. Returns a Pathway handle representing the newly added learning pathway.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "composition": {\n      "description": "Handle string for the Composition instance returned by create_composition (or equivalent constructor).",\n      "type": "string"\n    },\n    "default_projection_matrix": {\n      "description": "Matrix keyword string (e.g. \'RANDOM_CONNECTIVITY_MATRIX\', \'IDENTITY_MATRIX\') or a function name used for any MappingProjection in the pathway that lacks an explicit matrix. Overrides the MappingProjection default. Omit to use framework defaults.",\n      "type": "string"\n    },\n    "error_function": {\n      "description": "Name of the PsyNeuLink Function (e.g. \'LinearCombination\') assigned to the ComparatorMechanism to compute the error between target and output. Defaults to LinearCombination.",\n      "type": "string"\n    },\n    "learning_rate": {\n      "description": "Step size for the Backpropagation weight updates. Defaults to 0.05 if omitted.",\n      "type": "number"\n    },\n    "learning_update": {\n      "description": "When learned_projection weights are updated within each TRIAL: \'online\' (after every execution), \'after\' (once after the full trial, default), or false (disabled).",\n      "oneOf": [\n        {\n          "type": "boolean"\n        },\n        {\n          "enum": [\n            "online",\n            "after"\n          ],\n          "type": "string"\n        }\n      ]\n    },\n    "loss_spec": {\n      "description": "Loss function used to compute the error term. Defaults to \'MSE\' (mean-squared error). Maps to psyneulink.Loss values.",\n      "enum": [\n        "MSE",\n        "SSE",\n        "CROSS_ENTROPY",\n        "L0"\n      ],\n      "type": "string"\n    },\n    "name": {\n      "description": "Name assigned to the resulting Pathway object. Overrides any name already on a Pathway object passed in pathway.",\n      "type": "string"\n    },\n    "pathway": {\n      "description": "Ordered list of Mechanism handle strings (and optional MappingProjection specs between them) defining the processing pathway to make learnable. Any MappingProjections in the list become the learned_projections. Specify as a flat list of Mechanism handles, or interleaved [mech, projection, mech, ...] for explicit projection control.",\n      "items": {},\n      "type": "array"\n    }\n  },\n  "required": [\n    "composition",\n    "pathway"\n  ],\n  "type": "object"\n}\n\nNotes:\n- learning_rate default is 0.05 (set inside BackPropagation), not None — passing None lets the framework use that default; do not pass 0 unless you intend to disable learning.\n- loss_spec accepts psyneulink.Loss enum values; the string enum values listed (\'MSE\', \'SSE\', etc.) are the symbolic names — the runtime must resolve them to Loss members.\n- default_projection_matrix can also be a numeric list/array or a RandomMatrix spec, but since the runtime resolves strings to PNL objects, pass keyword strings where possible.\n- The pathway must form a linear (non-branching) chain; branching topologies require add_linear_learning_pathway with a custom learning_function.\n- MappingProjections between pathway nodes are created automatically if not specified; existing projections in the Composition are reused.\n- Call run() with a targets dict keyed to the terminal Mechanism after adding this pathway to actually train the weights.'
TOOL_PARAMETERS = { 'properties': { 'composition': { 'description': 'Handle string for the Composition '
                                                  'instance returned by '
                                                  'create_composition (or equivalent '
                                                  'constructor).',
                                   'type': 'string'},
                  'default_projection_matrix': { 'description': 'Matrix keyword string '
                                                                '(e.g. '
                                                                "'RANDOM_CONNECTIVITY_MATRIX', "
                                                                "'IDENTITY_MATRIX') or "
                                                                'a function name used '
                                                                'for any '
                                                                'MappingProjection in '
                                                                'the pathway that '
                                                                'lacks an explicit '
                                                                'matrix. Overrides the '
                                                                'MappingProjection '
                                                                'default. Omit to use '
                                                                'framework defaults.',
                                                 'type': 'string'},
                  'error_function': { 'description': 'Name of the PsyNeuLink Function '
                                                     "(e.g. 'LinearCombination') "
                                                     'assigned to the '
                                                     'ComparatorMechanism to compute '
                                                     'the error between target and '
                                                     'output. Defaults to '
                                                     'LinearCombination.',
                                      'type': 'string'},
                  'learning_rate': { 'description': 'Step size for the Backpropagation '
                                                    'weight updates. Defaults to 0.05 '
                                                    'if omitted.',
                                     'type': 'number'},
                  'learning_update': { 'description': 'When learned_projection weights '
                                                      'are updated within each TRIAL: '
                                                      "'online' (after every "
                                                      "execution), 'after' (once after "
                                                      'the full trial, default), or '
                                                      'false (disabled).',
                                       'oneOf': [ {'type': 'boolean'},
                                                  { 'enum': ['online', 'after'],
                                                    'type': 'string'}]},
                  'loss_spec': { 'description': 'Loss function used to compute the '
                                                "error term. Defaults to 'MSE' "
                                                '(mean-squared error). Maps to '
                                                'psyneulink.Loss values.',
                                 'enum': ['MSE', 'SSE', 'CROSS_ENTROPY', 'L0'],
                                 'type': 'string'},
                  'name': { 'description': 'Name assigned to the resulting Pathway '
                                           'object. Overrides any name already on a '
                                           'Pathway object passed in pathway.',
                            'type': 'string'},
                  'pathway': { 'description': 'Ordered list of Mechanism handle '
                                              'strings (and optional MappingProjection '
                                              'specs between them) defining the '
                                              'processing pathway to make learnable. '
                                              'Any MappingProjections in the list '
                                              'become the learned_projections. Specify '
                                              'as a flat list of Mechanism handles, or '
                                              'interleaved [mech, projection, mech, '
                                              '...] for explicit projection control.',
                               'items': {},
                               'type': 'array'}},
  'required': ['composition', 'pathway'],
  'type': 'object'}
TOOL_NOTES = "- learning_rate default is 0.05 (set inside BackPropagation), not None — passing None lets the framework use that default; do not pass 0 unless you intend to disable learning.\n- loss_spec accepts psyneulink.Loss enum values; the string enum values listed ('MSE', 'SSE', etc.) are the symbolic names — the runtime must resolve them to Loss members.\n- default_projection_matrix can also be a numeric list/array or a RandomMatrix spec, but since the runtime resolves strings to PNL objects, pass keyword strings where possible.\n- The pathway must form a linear (non-branching) chain; branching topologies require add_linear_learning_pathway with a custom learning_function.\n- MappingProjections between pathway nodes are created automatically if not specified; existing projections in the Composition are reused.\n- Call run() with a targets dict keyed to the terminal Mechanism after adding this pathway to actually train the weights."


def _impl(kwargs: dict[str, Any]) -> Any:
    cls = pnl.Composition
    return method_helpers.call_method_tool(
        owner_cls=cls,
        method_name='add_backpropagation_learning_pathway',
        kwargs=kwargs,
        tool_name=TOOL_NAME,
    )


def register(mcp: Any) -> None:
    @captured_tool(mcp, layer="generated", name=TOOL_NAME, description=TOOL_DESCRIPTION)
    def add_backpropagation_learning_pathway(args: dict[str, Any] | None = None) -> Any:
        'Call this tool after nodes and projections have been added to a Composition to wire up a backpropagation (gradient-descent) learning pathway between a sequence of Mechanisms.'
        return _impl(args or {})
