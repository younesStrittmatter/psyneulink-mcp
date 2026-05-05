"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '97fed121ffaf4dda9895f2be62a7c8d877392a59c994df16b591979df9f4436b'
__pnl_qualname__ = 'psyneulink.MatrixTransform'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_matrix_transform'
TOOL_DESCRIPTION = 'Call this tool to instantiate a MatrixTransform function that transforms a 1d input array via matrix multiplication (DOT_PRODUCT) or element-wise absolute difference (L0). Use it when you need a standalone weight-matrix transform, as a function argument for a Mechanism/Port, or as the function of a MappingProjection. Returns a 1d array whose length equals the number of columns in the matrix.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "default_variable": {\n      "description": "Template 1d array for the input; its length must equal the number of rows (outer index) of the matrix. Determines the input dimensionality when no owner is present.",\n      "items": {\n        "type": "number"\n      },\n      "type": "array"\n    },\n    "matrix": {\n      "description": "Weight matrix used for the transform. Accepts: a scalar (fills all elements), a 1d/2d list or np.ndarray, or (when used as a Projection function only) a matrix keyword string such as \'IDENTITY_MATRIX\', \'FULL_CONNECTIVITY_MATRIX\', \'RANDOM_CONNECTIVITY_MATRIX\'. Shape must be (len(variable), output_size). Defaults to a square identity matrix sized to variable when unspecified.",\n      "oneOf": [\n        {\n          "type": "number"\n        },\n        {\n          "items": {\n            "type": "number"\n          },\n          "type": "array"\n        },\n        {\n          "items": {\n            "items": {\n              "type": "number"\n            },\n            "type": "array"\n          },\n          "type": "array"\n        },\n        {\n          "enum": [\n            "IDENTITY_MATRIX",\n            "HOLLOW_MATRIX",\n            "FULL_CONNECTIVITY_MATRIX",\n            "RANDOM_CONNECTIVITY_MATRIX",\n            "AUTO_ASSIGN_MATRIX"\n          ],\n          "type": "string"\n        }\n      ]\n    },\n    "name": {\n      "description": "Name for this MatrixTransform instance. Auto-assigned by FunctionRegistry if omitted.",\n      "type": "string"\n    },\n    "normalize": {\n      "default": false,\n      "description": "If true, normalizes the result by the product of the norms of variable and matrix. With DOT_PRODUCT this yields cosine similarity. With L0 this yields 1 - normalized_difference (larger = more similar). Do not set true when variable is a scalar and operation is L0.",\n      "type": "boolean"\n    },\n    "operation": {\n      "default": "DOT_PRODUCT",\n      "description": "DOT_PRODUCT (default): returns np.dot(variable, matrix). L0: returns sum of absolute elementwise differences |variable - matrix|. WARNING: L0 without normalize produces SMALLER values for more similar vectors \\u2014 the opposite direction from DOT_PRODUCT.",\n      "enum": [\n        "DOT_PRODUCT",\n        "L0"\n      ],\n      "type": "string"\n    },\n    "params": {\n      "additionalProperties": true,\n      "description": "Optional parameter dictionary overriding constructor arguments. Keys are parameter name strings, values override the corresponding constructor arguments.",\n      "type": "object"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\nMatrix shape convention: rows (outer index) correspond to input elements (variable length), columns (inner index) correspond to output elements — so matrix.shape == (len(variable), output_size). Matrix keywords (IDENTITY_MATRIX, etc.) are ONLY valid when MatrixTransform is the function of a Projection; passing a keyword when instantiating standalone or inside a Mechanism raises FunctionError. L0 without normalize gives smaller values for similar vectors (closer to 0), opposite to DOT_PRODUCT — set normalize=True if larger-means-more-similar semantics are desired. normalize=True with L0 is invalid when variable is scalar (single element) due to divide-by-zero risk. The `owner` and `prefs` arguments are infrastructure-level and should not be passed by an agent unless building custom PNL component hierarchies.'
TOOL_PARAMETERS = { 'properties': { 'default_variable': { 'description': 'Template 1d array for the '
                                                       'input; its length must equal '
                                                       'the number of rows (outer '
                                                       'index) of the matrix. '
                                                       'Determines the input '
                                                       'dimensionality when no owner '
                                                       'is present.',
                                        'items': {'type': 'number'},
                                        'type': 'array'},
                  'matrix': { 'description': 'Weight matrix used for the transform. '
                                             'Accepts: a scalar (fills all elements), '
                                             'a 1d/2d list or np.ndarray, or (when '
                                             'used as a Projection function only) a '
                                             'matrix keyword string such as '
                                             "'IDENTITY_MATRIX', "
                                             "'FULL_CONNECTIVITY_MATRIX', "
                                             "'RANDOM_CONNECTIVITY_MATRIX'. Shape must "
                                             'be (len(variable), output_size). '
                                             'Defaults to a square identity matrix '
                                             'sized to variable when unspecified.',
                              'oneOf': [ {'type': 'number'},
                                         {'items': {'type': 'number'}, 'type': 'array'},
                                         { 'items': { 'items': {'type': 'number'},
                                                      'type': 'array'},
                                           'type': 'array'},
                                         { 'enum': [ 'IDENTITY_MATRIX',
                                                     'HOLLOW_MATRIX',
                                                     'FULL_CONNECTIVITY_MATRIX',
                                                     'RANDOM_CONNECTIVITY_MATRIX',
                                                     'AUTO_ASSIGN_MATRIX'],
                                           'type': 'string'}]},
                  'name': { 'description': 'Name for this MatrixTransform instance. '
                                           'Auto-assigned by FunctionRegistry if '
                                           'omitted.',
                            'type': 'string'},
                  'normalize': { 'default': False,
                                 'description': 'If true, normalizes the result by the '
                                                'product of the norms of variable and '
                                                'matrix. With DOT_PRODUCT this yields '
                                                'cosine similarity. With L0 this '
                                                'yields 1 - normalized_difference '
                                                '(larger = more similar). Do not set '
                                                'true when variable is a scalar and '
                                                'operation is L0.',
                                 'type': 'boolean'},
                  'operation': { 'default': 'DOT_PRODUCT',
                                 'description': 'DOT_PRODUCT (default): returns '
                                                'np.dot(variable, matrix). L0: returns '
                                                'sum of absolute elementwise '
                                                'differences |variable - matrix|. '
                                                'WARNING: L0 without normalize '
                                                'produces SMALLER values for more '
                                                'similar vectors — the opposite '
                                                'direction from DOT_PRODUCT.',
                                 'enum': ['DOT_PRODUCT', 'L0'],
                                 'type': 'string'},
                  'params': { 'additionalProperties': True,
                              'description': 'Optional parameter dictionary overriding '
                                             'constructor arguments. Keys are '
                                             'parameter name strings, values override '
                                             'the corresponding constructor arguments.',
                              'type': 'object'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = 'Matrix shape convention: rows (outer index) correspond to input elements (variable length), columns (inner index) correspond to output elements — so matrix.shape == (len(variable), output_size). Matrix keywords (IDENTITY_MATRIX, etc.) are ONLY valid when MatrixTransform is the function of a Projection; passing a keyword when instantiating standalone or inside a Mechanism raises FunctionError. L0 without normalize gives smaller values for similar vectors (closer to 0), opposite to DOT_PRODUCT — set normalize=True if larger-means-more-similar semantics are desired. normalize=True with L0 is invalid when variable is scalar (single element) due to divide-by-zero risk. The `owner` and `prefs` arguments are infrastructure-level and should not be passed by an agent unless building custom PNL component hierarchies.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.MatrixTransform
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
    def create_matrix_transform(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to instantiate a MatrixTransform function that transforms a 1d input array via matrix multiplication (DOT_PRODUCT) or element-wise absolute difference (L0).'
        return _impl(args or {})
