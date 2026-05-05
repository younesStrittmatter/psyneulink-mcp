"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = 'd8c007bf89379bd13588392139b4772df8ab11d4616387b02906045f135ac087'
__pnl_qualname__ = 'psyneulink.MappingProjection'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_mapping_projection'
TOOL_DESCRIPTION = 'Call this tool to create a weighted connection (MappingProjection) between the OutputPort of one Mechanism and the InputPort of another. Use it whenever you need to wire two mechanisms together in a composition, optionally specifying a weight matrix and whether the connection should be learnable. Returns a handle string to the created MappingProjection object.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "learnable": {\n      "default": true,\n      "description": "If false, the matrix can never be modified by learning, regardless of any learning_rate or Composition-level learning settings.",\n      "type": "boolean"\n    },\n    "learning_rate": {\n      "description": "Projection-specific learning rate. Numeric value overrides Composition default; false disables learning for this projection even if learnable=true; true or omitting inherits Composition learning_rate. Cannot be a numeric value when learnable=false.",\n      "oneOf": [\n        {\n          "type": "number"\n        },\n        {\n          "type": "boolean"\n        }\n      ]\n    },\n    "matrix": {\n      "default": "DEFAULT_MATRIX",\n      "description": "Weight matrix or keyword. Defaults to AUTO_ASSIGN_MATRIX (IDENTITY if dimensions match, FULL_CONNECTIVITY otherwise).",\n      "oneOf": [\n        {\n          "description": "Explicit 2D weight matrix; shape must be [sender_output_size x receiver_input_size].",\n          "items": {\n            "items": {\n              "type": "number"\n            },\n            "type": "array"\n          },\n          "type": "array"\n        },\n        {\n          "description": "Keyword shorthand for common matrix types.",\n          "enum": [\n            "DEFAULT_MATRIX",\n            "IDENTITY_MATRIX",\n            "FULL_CONNECTIVITY_MATRIX",\n            "HOLLOW_MATRIX",\n            "RANDOM_CONNECTIVITY_MATRIX"\n          ],\n          "type": "string"\n        }\n      ]\n    },\n    "name": {\n      "description": "Optional name. Auto-generated as \'MappingProjection from <sender>[OutputPort] to <receiver>[InputPort]\' if omitted.",\n      "type": "string"\n    },\n    "receiver": {\n      "description": "Handle of the destination Mechanism or InputPort. Uses the primary InputPort if a Mechanism handle is given. Omit only when the projection will be assigned implicitly by a composition pathway.",\n      "type": "string"\n    },\n    "sender": {\n      "description": "Handle of the source Mechanism or OutputPort. Uses the primary OutputPort if a Mechanism handle is given. Omit only when the projection will be assigned implicitly by a composition pathway.",\n      "type": "string"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\nDuplicateProjectionError is raised if an identical projection already exists between the same sender-receiver pair — this has been observed in practice. Before calling this tool, verify no projection already connects the intended sender and receiver (e.g., via list_composition_projections or by tracking what you have already created). Matrix rows correspond to sender output elements and columns to receiver input elements; mismatched dimensions raise ProjectionError unless a keyword string is used (PNL will attempt auto-reshape for FULL_CONNECTIVITY_MATRIX but not IDENTITY_MATRIX or HOLLOW_MATRIX). Specifying a numeric learning_rate when learnable=false raises MappingError at construction time. If sender or receiver is omitted, the projection enters deferred initialization and must be resolved when added to a Composition pathway.'
TOOL_PARAMETERS = { 'properties': { 'learnable': { 'default': True,
                                 'description': 'If false, the matrix can never be '
                                                'modified by learning, regardless of '
                                                'any learning_rate or '
                                                'Composition-level learning settings.',
                                 'type': 'boolean'},
                  'learning_rate': { 'description': 'Projection-specific learning '
                                                    'rate. Numeric value overrides '
                                                    'Composition default; false '
                                                    'disables learning for this '
                                                    'projection even if '
                                                    'learnable=true; true or omitting '
                                                    'inherits Composition '
                                                    'learning_rate. Cannot be a '
                                                    'numeric value when '
                                                    'learnable=false.',
                                     'oneOf': [ {'type': 'number'},
                                                {'type': 'boolean'}]},
                  'matrix': { 'default': 'DEFAULT_MATRIX',
                              'description': 'Weight matrix or keyword. Defaults to '
                                             'AUTO_ASSIGN_MATRIX (IDENTITY if '
                                             'dimensions match, FULL_CONNECTIVITY '
                                             'otherwise).',
                              'oneOf': [ { 'description': 'Explicit 2D weight matrix; '
                                                          'shape must be '
                                                          '[sender_output_size x '
                                                          'receiver_input_size].',
                                           'items': { 'items': {'type': 'number'},
                                                      'type': 'array'},
                                           'type': 'array'},
                                         { 'description': 'Keyword shorthand for '
                                                          'common matrix types.',
                                           'enum': [ 'DEFAULT_MATRIX',
                                                     'IDENTITY_MATRIX',
                                                     'FULL_CONNECTIVITY_MATRIX',
                                                     'HOLLOW_MATRIX',
                                                     'RANDOM_CONNECTIVITY_MATRIX'],
                                           'type': 'string'}]},
                  'name': { 'description': 'Optional name. Auto-generated as '
                                           "'MappingProjection from "
                                           '<sender>[OutputPort] to '
                                           "<receiver>[InputPort]' if omitted.",
                            'type': 'string'},
                  'receiver': { 'description': 'Handle of the destination Mechanism or '
                                               'InputPort. Uses the primary InputPort '
                                               'if a Mechanism handle is given. Omit '
                                               'only when the projection will be '
                                               'assigned implicitly by a composition '
                                               'pathway.',
                                'type': 'string'},
                  'sender': { 'description': 'Handle of the source Mechanism or '
                                             'OutputPort. Uses the primary OutputPort '
                                             'if a Mechanism handle is given. Omit '
                                             'only when the projection will be '
                                             'assigned implicitly by a composition '
                                             'pathway.',
                              'type': 'string'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = 'DuplicateProjectionError is raised if an identical projection already exists between the same sender-receiver pair — this has been observed in practice. Before calling this tool, verify no projection already connects the intended sender and receiver (e.g., via list_composition_projections or by tracking what you have already created). Matrix rows correspond to sender output elements and columns to receiver input elements; mismatched dimensions raise ProjectionError unless a keyword string is used (PNL will attempt auto-reshape for FULL_CONNECTIVITY_MATRIX but not IDENTITY_MATRIX or HOLLOW_MATRIX). Specifying a numeric learning_rate when learnable=false raises MappingError at construction time. If sender or receiver is omitted, the projection enters deferred initialization and must be resolved when added to a Composition pathway.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.MappingProjection
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
    def create_mapping_projection(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to create a weighted connection (MappingProjection) between the OutputPort of one Mechanism and the InputPort of another.'
        return _impl(args or {})
