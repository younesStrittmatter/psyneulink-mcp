"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool
from psyneulink_mcp import method_helpers

__source_sha256__ = 'c6d5a410ed9b1d8c352ba2eeb40e1b0a04ab33bd5ff406c45c5fdefb884891e3'
__pnl_qualname__ = 'psyneulink.Composition.add_linear_processing_pathway'
__pnl_kind__ = 'method'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'add_linear_processing_pathway'
TOOL_DESCRIPTION = 'Call this tool after creating a Composition and its node Mechanisms to wire them into an ordered, feed-forward processing pathway. Consecutive nodes receive auto-created MappingProjections; you may optionally interleave explicit Projection handles or supply a default matrix. Returns a string handle for the resulting Pathway object that is added to the Composition.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "composition": {\n      "description": "Handle string for the target Composition, as returned by create_composition.",\n      "type": "string"\n    },\n    "default_projection_matrix": {\n      "description": "2-D numeric array (list of lists) to use as the weight matrix for any auto-created MappingProjections that are not otherwise specified. Overrides MappingProjection\'s built-in default. Must be a concrete numeric matrix \\u2014 PNL keyword strings such as \'FULL_CONNECTIVITY_MATRIX\' are NOT resolved by the runtime and will raise a CompositionError.",\n      "items": {\n        "items": {\n          "type": "number"\n        },\n        "type": "array"\n      },\n      "type": "array"\n    },\n    "name": {\n      "description": "Name to assign to the returned Pathway object. Overrides any name carried by a Pathway object passed as pathway.",\n      "type": "string"\n    },\n    "pathway": {\n      "description": "Ordered sequence of node handle strings (Mechanism or nested Composition handles). Each element projects to the next; consecutive node pairs receive auto-created MappingProjections. Sets of nodes can be expressed as nested arrays. Explicit Projection handle strings may be interleaved between node entries to override auto-created connections.",\n      "items": {\n        "oneOf": [\n          {\n            "type": "string"\n          },\n          {\n            "items": {\n              "type": "string"\n            },\n            "type": "array"\n          }\n        ]\n      },\n      "type": "array"\n    }\n  },\n  "required": [\n    "composition",\n    "pathway"\n  ],\n  "type": "object"\n}\n\nNotes:\nIMPORTANT — default_projection_matrix must be a numeric 2-D array, not a keyword string: passing strings like "FULL_CONNECTIVITY_MATRIX", "IDENTITY_MATRIX", or any other PNL matrix-keyword constant will cause a CompositionError ("Invalid projection … specified") because the runtime helper does not resolve matrix-keyword strings for this parameter. Use an explicit list-of-lists instead (e.g., [[1,1],[1,1]] for 2×2 full connectivity).\n\nIf a learning pathway is needed, use add_linear_learning_pathway instead; any LearningFunction in a (Pathway, LearningFunction) tuple passed here is silently ignored.\n\nControlMechanism nodes whose monitor_for_control attribute is already set will NOT receive auto-created MappingProjections from the preceding node — their presence in the pathway only establishes execution order. A warning is issued and, where possible, a MappingProjection is created from the nearest preceding non-ControlMechanism node to maintain linearity.\n\nIf an identical pathway already exists in the Composition, the existing Pathway is returned with a warning rather than creating a duplicate.\n\nThe pathway argument\'s first element must be a Node (Mechanism or Composition handle), not a Projection — passing a Projection as the first entry raises a CompositionError.'
TOOL_PARAMETERS = { 'properties': { 'composition': { 'description': 'Handle string for the target '
                                                  'Composition, as returned by '
                                                  'create_composition.',
                                   'type': 'string'},
                  'default_projection_matrix': { 'description': '2-D numeric array '
                                                                '(list of lists) to '
                                                                'use as the weight '
                                                                'matrix for any '
                                                                'auto-created '
                                                                'MappingProjections '
                                                                'that are not '
                                                                'otherwise specified. '
                                                                'Overrides '
                                                                "MappingProjection's "
                                                                'built-in default. '
                                                                'Must be a concrete '
                                                                'numeric matrix — PNL '
                                                                'keyword strings such '
                                                                'as '
                                                                "'FULL_CONNECTIVITY_MATRIX' "
                                                                'are NOT resolved by '
                                                                'the runtime and will '
                                                                'raise a '
                                                                'CompositionError.',
                                                 'items': { 'items': {'type': 'number'},
                                                            'type': 'array'},
                                                 'type': 'array'},
                  'name': { 'description': 'Name to assign to the returned Pathway '
                                           'object. Overrides any name carried by a '
                                           'Pathway object passed as pathway.',
                            'type': 'string'},
                  'pathway': { 'description': 'Ordered sequence of node handle strings '
                                              '(Mechanism or nested Composition '
                                              'handles). Each element projects to the '
                                              'next; consecutive node pairs receive '
                                              'auto-created MappingProjections. Sets '
                                              'of nodes can be expressed as nested '
                                              'arrays. Explicit Projection handle '
                                              'strings may be interleaved between node '
                                              'entries to override auto-created '
                                              'connections.',
                               'items': { 'oneOf': [ {'type': 'string'},
                                                     { 'items': {'type': 'string'},
                                                       'type': 'array'}]},
                               'type': 'array'}},
  'required': ['composition', 'pathway'],
  'type': 'object'}
TOOL_NOTES = 'IMPORTANT — default_projection_matrix must be a numeric 2-D array, not a keyword string: passing strings like "FULL_CONNECTIVITY_MATRIX", "IDENTITY_MATRIX", or any other PNL matrix-keyword constant will cause a CompositionError ("Invalid projection … specified") because the runtime helper does not resolve matrix-keyword strings for this parameter. Use an explicit list-of-lists instead (e.g., [[1,1],[1,1]] for 2×2 full connectivity).\n\nIf a learning pathway is needed, use add_linear_learning_pathway instead; any LearningFunction in a (Pathway, LearningFunction) tuple passed here is silently ignored.\n\nControlMechanism nodes whose monitor_for_control attribute is already set will NOT receive auto-created MappingProjections from the preceding node — their presence in the pathway only establishes execution order. A warning is issued and, where possible, a MappingProjection is created from the nearest preceding non-ControlMechanism node to maintain linearity.\n\nIf an identical pathway already exists in the Composition, the existing Pathway is returned with a warning rather than creating a duplicate.\n\nThe pathway argument\'s first element must be a Node (Mechanism or Composition handle), not a Projection — passing a Projection as the first entry raises a CompositionError.'


def _impl(kwargs: dict[str, Any]) -> Any:
    cls = pnl.Composition
    return method_helpers.call_method_tool(
        owner_cls=cls,
        method_name='add_linear_processing_pathway',
        kwargs=kwargs,
        tool_name=TOOL_NAME,
    )


def register(mcp: Any) -> None:
    @captured_tool(mcp, layer="generated", name=TOOL_NAME, description=TOOL_DESCRIPTION)
    def add_linear_processing_pathway(args: dict[str, Any] | None = None) -> Any:
        'Call this tool after creating a Composition and its node Mechanisms to wire them into an ordered, feed-forward processing pathway.'
        return _impl(args or {})
