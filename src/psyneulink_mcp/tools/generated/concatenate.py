"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '33890f43540025323cae2f0d859640f9e510713e7cf61448f7b508b720cd3115'
__pnl_qualname__ = 'psyneulink.Concatenate'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_concatenate'
TOOL_DESCRIPTION = 'Use Concatenate when you need a function that flattens multiple arrays into a single 1D vector — for example, as the `function` of a Mechanism or Projection that receives multi-array input and must produce a unified representation. The output is `np.hstack(variable) * scale + offset`, a 1D array whose length equals the sum of all input array lengths. Call this to construct the function object, then assign it to a component\'s `function` parameter.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "default_variable": {\n      "description": "Template for the input: a list of numeric arrays to be concatenated. Defines the expected input shape; all entries must be numeric.",\n      "items": {\n        "items": {\n          "type": "number"\n        },\n        "type": "array"\n      },\n      "type": "array"\n    },\n    "name": {\n      "description": "Optional name for the function instance; if omitted, FunctionRegistry assigns a default.",\n      "type": "string"\n    },\n    "offset": {\n      "default": 0,\n      "description": "Scalar value added to every element of the concatenated output after scale is applied.",\n      "type": "number"\n    },\n    "scale": {\n      "default": 1,\n      "description": "Scalar multiplier applied to every element of the concatenated output before adding offset.",\n      "type": "number"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\nscale and offset must be scalars — passing an array raises FunctionError. All elements of default_variable must be numeric; non-numeric entries raise FunctionError at validation time. The function always changes the output shape (changes_shape=True): input is 2D (list of arrays) but output is a flat 1D array, so downstream components must expect a 1D vector. The derivative of this function returns scale regardless of input. params, owner, and prefs are advanced PNL internals; omit them unless integrating into a larger PNL object graph.'
TOOL_PARAMETERS = { 'properties': { 'default_variable': { 'description': 'Template for the input: a list '
                                                       'of numeric arrays to be '
                                                       'concatenated. Defines the '
                                                       'expected input shape; all '
                                                       'entries must be numeric.',
                                        'items': { 'items': {'type': 'number'},
                                                   'type': 'array'},
                                        'type': 'array'},
                  'name': { 'description': 'Optional name for the function instance; '
                                           'if omitted, FunctionRegistry assigns a '
                                           'default.',
                            'type': 'string'},
                  'offset': { 'default': 0,
                              'description': 'Scalar value added to every element of '
                                             'the concatenated output after scale is '
                                             'applied.',
                              'type': 'number'},
                  'scale': { 'default': 1,
                             'description': 'Scalar multiplier applied to every '
                                            'element of the concatenated output before '
                                            'adding offset.',
                             'type': 'number'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = 'scale and offset must be scalars — passing an array raises FunctionError. All elements of default_variable must be numeric; non-numeric entries raise FunctionError at validation time. The function always changes the output shape (changes_shape=True): input is 2D (list of arrays) but output is a flat 1D array, so downstream components must expect a 1D vector. The derivative of this function returns scale regardless of input. params, owner, and prefs are advanced PNL internals; omit them unless integrating into a larger PNL object graph.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.Concatenate
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
    def create_concatenate(args: dict[str, Any] | None = None) -> Any:
        'Use Concatenate when you need a function that flattens multiple arrays into a single 1D vector — for example, as the `function` of a Mechanism or Projection that receives multi-array input and must produce a unified representation.'
        return _impl(args or {})
