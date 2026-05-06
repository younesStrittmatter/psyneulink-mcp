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
TOOL_DESCRIPTION = 'Call this tool after creating a Composition and all required Mechanism/node handles to wire them into a sequential feed-forward processing chain. Pass an ordered list of node handles in `pathway`; auto-created MappingProjections connect each consecutive pair. Returns a serialized Pathway handle representing the wired sequence.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "composition": {\n      "description": "Handle string for the target Composition, as returned by create_composition or an equivalent constructor tool.",\n      "type": "string"\n    },\n    "default_projection_matrix": {\n      "description": "Numeric 2-D matrix (list of lists of numbers) to use for all auto-created MappingProjections that are not otherwise specified. Omit to accept the MappingProjection default (identity-like). Do NOT pass PNL keyword strings such as \'FULL_CONNECTIVITY_MATRIX\' here \\u2014 they are not resolved and will raise a CompositionError.",\n      "items": {\n        "items": {\n          "type": "number"\n        },\n        "type": "array"\n      },\n      "type": "array"\n    },\n    "name": {\n      "description": "Optional name for the resulting Pathway object. Overrides any name embedded in a Pathway object passed as pathway.",\n      "type": "string"\n    },\n    "pathway": {\n      "description": "Ordered list of node handle strings (Mechanisms or nested Compositions). Handles are resolved to live PNL objects at call time. May optionally interleave projection handle strings between node handles to override auto-created MappingProjections for specific edges.",\n      "items": {\n        "type": "string"\n      },\n      "type": "array"\n    }\n  },\n  "required": [\n    "composition",\n    "pathway"\n  ],\n  "type": "object"\n}\n\nNotes:\nHISTORICAL FAILURE — do NOT pass PNL keyword strings (e.g. "FULL_CONNECTIVITY_MATRIX", "IDENTITY_MATRIX") as default_projection_matrix. The runtime helper does not resolve matrix-keyword strings, so PNL receives a bare string and raises CompositionError: Invalid projection (...). Use a numeric array (e.g. [[1,0],[0,1]]) or omit the argument entirely.\n\nIf pathway is a 2-item (Pathway, LearningFunction) tuple, the LearningFunction is silently ignored; use add_linear_learning_pathway instead if learning is needed.\n\nAny ControlMechanism in the pathway that already has monitor_for_control set, and any ObjectiveMechanism already projecting to a ControlMechanism, will be dropped from the auto-wiring step (a warning is emitted but no exception is raised).\n\nDuplicate pathway specifications (same nodes, same order) return the pre-existing Pathway rather than creating a new one.'
TOOL_PARAMETERS = { 'properties': { 'composition': { 'description': 'Handle string for the target '
                                                  'Composition, as returned by '
                                                  'create_composition or an equivalent '
                                                  'constructor tool.',
                                   'type': 'string'},
                  'default_projection_matrix': { 'description': 'Numeric 2-D matrix '
                                                                '(list of lists of '
                                                                'numbers) to use for '
                                                                'all auto-created '
                                                                'MappingProjections '
                                                                'that are not '
                                                                'otherwise specified. '
                                                                'Omit to accept the '
                                                                'MappingProjection '
                                                                'default '
                                                                '(identity-like). Do '
                                                                'NOT pass PNL keyword '
                                                                'strings such as '
                                                                "'FULL_CONNECTIVITY_MATRIX' "
                                                                'here — they are not '
                                                                'resolved and will '
                                                                'raise a '
                                                                'CompositionError.',
                                                 'items': { 'items': {'type': 'number'},
                                                            'type': 'array'},
                                                 'type': 'array'},
                  'name': { 'description': 'Optional name for the resulting Pathway '
                                           'object. Overrides any name embedded in a '
                                           'Pathway object passed as pathway.',
                            'type': 'string'},
                  'pathway': { 'description': 'Ordered list of node handle strings '
                                              '(Mechanisms or nested Compositions). '
                                              'Handles are resolved to live PNL '
                                              'objects at call time. May optionally '
                                              'interleave projection handle strings '
                                              'between node handles to override '
                                              'auto-created MappingProjections for '
                                              'specific edges.',
                               'items': {'type': 'string'},
                               'type': 'array'}},
  'required': ['composition', 'pathway'],
  'type': 'object'}
TOOL_NOTES = 'HISTORICAL FAILURE — do NOT pass PNL keyword strings (e.g. "FULL_CONNECTIVITY_MATRIX", "IDENTITY_MATRIX") as default_projection_matrix. The runtime helper does not resolve matrix-keyword strings, so PNL receives a bare string and raises CompositionError: Invalid projection (...). Use a numeric array (e.g. [[1,0],[0,1]]) or omit the argument entirely.\n\nIf pathway is a 2-item (Pathway, LearningFunction) tuple, the LearningFunction is silently ignored; use add_linear_learning_pathway instead if learning is needed.\n\nAny ControlMechanism in the pathway that already has monitor_for_control set, and any ObjectiveMechanism already projecting to a ControlMechanism, will be dropped from the auto-wiring step (a warning is emitted but no exception is raised).\n\nDuplicate pathway specifications (same nodes, same order) return the pre-existing Pathway rather than creating a new one.'


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
        'Call this tool after creating a Composition and all required Mechanism/node handles to wire them into a sequential feed-forward processing chain.'
        return _impl(args or {})
