"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = 'dfb0b9138521898a09f27b7f1bf79090f410398971d95d3a2225d3cee2ada21c'
__pnl_qualname__ = 'psyneulink.core.components.functions.nonstateful.objectivefunctions.get_matrix'
__pnl_kind__ = 'function'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'get_matrix'
TOOL_DESCRIPTION = 'Call this tool when you need to construct a weight/connectivity matrix for use in a PsyNeuLink projection or function. Pass a keyword string (e.g. "IDENTITY_MATRIX", "FULL_CONNECTIVITY_MATRIX"), a scalar fill value, or a 2-D list of numbers along with the desired row and column counts; the tool returns a 2-D numpy array shaped rows × cols, or None when the specification is unrecognized.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "cols": {\n      "default": 1,\n      "description": "Number of columns (receiver dimensionality) in the output matrix.",\n      "type": "integer"\n    },\n    "rows": {\n      "default": 1,\n      "description": "Number of rows (sender dimensionality) in the output matrix.",\n      "type": "integer"\n    },\n    "specification": {\n      "description": "What the matrix should contain. Accepted forms: (1) a keyword string \\u2014 one of \'AUTO_ASSIGN_MATRIX\', \'IDENTITY_MATRIX\', \'HOLLOW_MATRIX\', \'INVERSE_HOLLOW_MATRIX\', \'FULL_CONNECTIVITY_MATRIX\', \'ZERO_MATRIX\', \'RANDOM_CONNECTIVITY_MATRIX\', \'KAIMING_MATRIX\', \'XAVIER_MATRIX\', \'ORTHOGONAL_MATRIX\'; (2) a single number used as a fill value; or (3) a 2-D list of numbers (list of rows, each row a list of floats).",\n      "oneOf": [\n        {\n          "type": "string"\n        },\n        {\n          "type": "number"\n        },\n        {\n          "items": {\n            "items": {\n              "type": "number"\n            },\n            "type": "array"\n          },\n          "type": "array"\n        }\n      ]\n    }\n  },\n  "required": [\n    "specification"\n  ],\n  "type": "object"\n}\n\nNotes:\nIDENTITY_MATRIX, HOLLOW_MATRIX, and INVERSE_HOLLOW_MATRIX require rows == cols; passing them with rows ≠ cols raises a FunctionError rather than returning None. AUTO_ASSIGN_MATRIX automatically picks IDENTITY_MATRIX when rows == cols, otherwise FULL_CONNECTIVITY_MATRIX — prefer it when you are unsure of the shape at call time. An unrecognised specification silently returns None instead of raising an error, so always check the return value. The `context` parameter is an internal PsyNeuLink argument and should never be passed by agents. When specification is a 2-D list or ndarray the rows/cols arguments are ignored — the matrix dimensions come from the provided data.'
TOOL_PARAMETERS = { 'properties': { 'cols': { 'default': 1,
                            'description': 'Number of columns (receiver '
                                           'dimensionality) in the output matrix.',
                            'type': 'integer'},
                  'rows': { 'default': 1,
                            'description': 'Number of rows (sender dimensionality) in '
                                           'the output matrix.',
                            'type': 'integer'},
                  'specification': { 'description': 'What the matrix should contain. '
                                                    'Accepted forms: (1) a keyword '
                                                    'string — one of '
                                                    "'AUTO_ASSIGN_MATRIX', "
                                                    "'IDENTITY_MATRIX', "
                                                    "'HOLLOW_MATRIX', "
                                                    "'INVERSE_HOLLOW_MATRIX', "
                                                    "'FULL_CONNECTIVITY_MATRIX', "
                                                    "'ZERO_MATRIX', "
                                                    "'RANDOM_CONNECTIVITY_MATRIX', "
                                                    "'KAIMING_MATRIX', "
                                                    "'XAVIER_MATRIX', "
                                                    "'ORTHOGONAL_MATRIX'; (2) a single "
                                                    'number used as a fill value; or '
                                                    '(3) a 2-D list of numbers (list '
                                                    'of rows, each row a list of '
                                                    'floats).',
                                     'oneOf': [ {'type': 'string'},
                                                {'type': 'number'},
                                                { 'items': { 'items': { 'type': 'number'},
                                                             'type': 'array'},
                                                  'type': 'array'}]}},
  'required': ['specification'],
  'type': 'object'}
TOOL_NOTES = 'IDENTITY_MATRIX, HOLLOW_MATRIX, and INVERSE_HOLLOW_MATRIX require rows == cols; passing them with rows ≠ cols raises a FunctionError rather than returning None. AUTO_ASSIGN_MATRIX automatically picks IDENTITY_MATRIX when rows == cols, otherwise FULL_CONNECTIVITY_MATRIX — prefer it when you are unsure of the shape at call time. An unrecognised specification silently returns None instead of raising an error, so always check the return value. The `context` parameter is an internal PsyNeuLink argument and should never be passed by agents. When specification is a 2-D list or ndarray the rows/cols arguments are ignored — the matrix dimensions come from the provided data.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.get_matrix
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
    def get_matrix(args: dict[str, Any] | None = None) -> Any:
        'Call this tool when you need to construct a weight/connectivity matrix for use in a PsyNeuLink projection or function.'
        return _impl(args or {})
