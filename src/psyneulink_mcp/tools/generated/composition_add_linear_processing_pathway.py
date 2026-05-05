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
TOOL_DESCRIPTION = 'Call this tool to wire a feed-forward chain of Mechanisms (and/or nested Compositions) into an existing Composition in one step. Pass an ordered list of node handles — the tool auto-creates MappingProjections between consecutive nodes — and returns a Pathway handle string. Use this whenever you want to connect two or more nodes linearly; prefer it over repeated `add_projection` calls for sequential pipelines.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "composition": {\n      "description": "Handle string of the target Composition, as returned by create_composition.",\n      "type": "string"\n    },\n    "default_projection_matrix": {\n      "default": null,\n      "description": "Matrix to use for any unspecified MappingProjections, overriding the PNL default. Accepts a nested number array (e.g. [[1,0],[0,1]]), a matrix-keyword string (e.g. \'IDENTITY_MATRIX\', \'FULL_CONNECTIVITY_MATRIX\'), or null to keep the PNL default (identity). Only applied where no explicit projection is given in pathway.",\n      "type": [\n        "array",\n        "string",\n        "null"\n      ]\n    },\n    "name": {\n      "default": null,\n      "description": "Name to assign to the returned Pathway. Supersedes any name embedded in a Pathway object passed as pathway. Omit to let PNL auto-name.",\n      "type": [\n        "string",\n        "null"\n      ]\n    },\n    "pathway": {\n      "description": "Ordered list of node handle strings defining the chain. Elements may be: (1) a node handle string (Mechanism or Composition), (2) an array of node handle strings for a parallel fan-in/fan-out layer, or (3) a matrix spec (nested number array or keyword string such as \'IDENTITY_MATRIX\') interleaved between two node entries to override the projection between that specific pair. Auto-created MappingProjections connect every consecutive pair that lacks an explicit projection.",\n      "items": {\n        "oneOf": [\n          {\n            "description": "Node handle or matrix keyword string.",\n            "type": "string"\n          },\n          {\n            "description": "A parallel set of node handles or a matrix row.",\n            "type": "array"\n          },\n          {\n            "description": "Scalar matrix spec (rare).",\n            "type": "number"\n          }\n        ]\n      },\n      "minItems": 2,\n      "type": "array"\n    }\n  },\n  "required": [\n    "composition",\n    "pathway"\n  ],\n  "type": "object"\n}\n\nNotes:\n• The first and last elements of `pathway` MUST be node handles (strings or arrays of strings), never a projection spec — a leading or trailing projection raises CompositionError.\n• If a 2-item (Pathway, LearningFunction) tuple is passed as `pathway`, the LearningFunction is silently ignored. For learning pathways use add_linear_learning_pathway instead.\n• ControlMechanisms that have monitor_for_control set are automatically removed from the projection chain with a warning; no MappingProjection is added to them. The tool compensates by wiring the preceding non-control node directly to the following node.\n• If the specified pathway is structurally identical to one that already exists in the Composition, the existing Pathway is returned unchanged (with a warning) — no duplicate is created.\n• Nested Compositions in the pathway are connected via their INPUT-role nodes (as receivers) and OUTPUT-role nodes (as senders); if the nested Composition has no such nodes yet, CompositionError is raised.\n• `default_projection_matrix` only fills gaps — it does not override an explicit projection spec interleaved in `pathway`.'
TOOL_PARAMETERS = { 'properties': { 'composition': { 'description': 'Handle string of the target '
                                                  'Composition, as returned by '
                                                  'create_composition.',
                                   'type': 'string'},
                  'default_projection_matrix': { 'default': None,
                                                 'description': 'Matrix to use for any '
                                                                'unspecified '
                                                                'MappingProjections, '
                                                                'overriding the PNL '
                                                                'default. Accepts a '
                                                                'nested number array '
                                                                '(e.g. [[1,0],[0,1]]), '
                                                                'a matrix-keyword '
                                                                'string (e.g. '
                                                                "'IDENTITY_MATRIX', "
                                                                "'FULL_CONNECTIVITY_MATRIX'), "
                                                                'or null to keep the '
                                                                'PNL default '
                                                                '(identity). Only '
                                                                'applied where no '
                                                                'explicit projection '
                                                                'is given in pathway.',
                                                 'type': ['array', 'string', 'null']},
                  'name': { 'default': None,
                            'description': 'Name to assign to the returned Pathway. '
                                           'Supersedes any name embedded in a Pathway '
                                           'object passed as pathway. Omit to let PNL '
                                           'auto-name.',
                            'type': ['string', 'null']},
                  'pathway': { 'description': 'Ordered list of node handle strings '
                                              'defining the chain. Elements may be: '
                                              '(1) a node handle string (Mechanism or '
                                              'Composition), (2) an array of node '
                                              'handle strings for a parallel '
                                              'fan-in/fan-out layer, or (3) a matrix '
                                              'spec (nested number array or keyword '
                                              "string such as 'IDENTITY_MATRIX') "
                                              'interleaved between two node entries to '
                                              'override the projection between that '
                                              'specific pair. Auto-created '
                                              'MappingProjections connect every '
                                              'consecutive pair that lacks an explicit '
                                              'projection.',
                               'items': { 'oneOf': [ { 'description': 'Node handle or '
                                                                      'matrix keyword '
                                                                      'string.',
                                                       'type': 'string'},
                                                     { 'description': 'A parallel set '
                                                                      'of node handles '
                                                                      'or a matrix '
                                                                      'row.',
                                                       'type': 'array'},
                                                     { 'description': 'Scalar matrix '
                                                                      'spec (rare).',
                                                       'type': 'number'}]},
                               'minItems': 2,
                               'type': 'array'}},
  'required': ['composition', 'pathway'],
  'type': 'object'}
TOOL_NOTES = '• The first and last elements of `pathway` MUST be node handles (strings or arrays of strings), never a projection spec — a leading or trailing projection raises CompositionError.\n• If a 2-item (Pathway, LearningFunction) tuple is passed as `pathway`, the LearningFunction is silently ignored. For learning pathways use add_linear_learning_pathway instead.\n• ControlMechanisms that have monitor_for_control set are automatically removed from the projection chain with a warning; no MappingProjection is added to them. The tool compensates by wiring the preceding non-control node directly to the following node.\n• If the specified pathway is structurally identical to one that already exists in the Composition, the existing Pathway is returned unchanged (with a warning) — no duplicate is created.\n• Nested Compositions in the pathway are connected via their INPUT-role nodes (as receivers) and OUTPUT-role nodes (as senders); if the nested Composition has no such nodes yet, CompositionError is raised.\n• `default_projection_matrix` only fills gaps — it does not override an explicit projection spec interleaved in `pathway`.'


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
        'Call this tool to wire a feed-forward chain of Mechanisms (and/or nested Compositions) into an existing Composition in one step.'
        return _impl(args or {})
