"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '4e679efa836b5893353a26b320b514ebe48f40d2f71989d8d1aee59178255630'
__pnl_qualname__ = 'psyneulink.is_matrix'
__pnl_kind__ = 'function'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'is_matrix'
TOOL_DESCRIPTION = 'Call this tool to test whether a value is a valid PsyNeuLink matrix — i.e., something that can serve as a weight or projection matrix. Returns True for matrix-keyword strings, lists, numpy arrays, or anything convertible to a numpy matrix; returns False for None, PsyNeuLink Components, dicts, and sets. Use this before passing a candidate value to a Projection or MappingProjection to avoid silent type errors.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "m": {\n      "description": "The value to test. Pass a matrix-keyword string (e.g. \'IDENTITY_MATRIX\', \'HOLLOW_MATRIX\', \'RANDOM_CONNECTIVITY_MATRIX\'), a 2-D list of lists representing a numeric matrix, or a scalar number.",\n      "oneOf": [\n        {\n          "type": "string"\n        },\n        {\n          "items": {\n            "items": {\n              "type": "number"\n            },\n            "type": "array"\n          },\n          "type": "array"\n        },\n        {\n          "type": "number"\n        }\n      ]\n    }\n  },\n  "required": [\n    "m"\n  ],\n  "type": "object"\n}\n\nNotes:\nCallables (e.g. random_matrix) cannot be passed through JSON/MCP; test their return value directly instead. PsyNeuLink Component instances, dicts, sets, and None always return False regardless of shape. A flat 1-D list is not accepted as a matrix (numpy.matrix rejects rank-1 inputs from flat lists in some versions); pass a nested list-of-lists instead.'
TOOL_PARAMETERS = { 'properties': { 'm': { 'description': 'The value to test. Pass a matrix-keyword '
                                        "string (e.g. 'IDENTITY_MATRIX', "
                                        "'HOLLOW_MATRIX', "
                                        "'RANDOM_CONNECTIVITY_MATRIX'), a 2-D list of "
                                        'lists representing a numeric matrix, or a '
                                        'scalar number.',
                         'oneOf': [ {'type': 'string'},
                                    { 'items': { 'items': {'type': 'number'},
                                                 'type': 'array'},
                                      'type': 'array'},
                                    {'type': 'number'}]}},
  'required': ['m'],
  'type': 'object'}
TOOL_NOTES = 'Callables (e.g. random_matrix) cannot be passed through JSON/MCP; test their return value directly instead. PsyNeuLink Component instances, dicts, sets, and None always return False regardless of shape. A flat 1-D list is not accepted as a matrix (numpy.matrix rejects rank-1 inputs from flat lists in some versions); pass a nested list-of-lists instead.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.is_matrix
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
    def is_matrix(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to test whether a value is a valid PsyNeuLink matrix — i.e., something that can serve as a weight or projection matrix.'
        return _impl(args or {})
