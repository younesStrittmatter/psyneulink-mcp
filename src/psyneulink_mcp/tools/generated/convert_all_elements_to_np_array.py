"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = 'ef72b48e3da853802c725da5b537fbb536a24a3e67fa52a94a6ea3c2640c5a41'
__pnl_qualname__ = 'psyneulink.convert_all_elements_to_np_array'
__pnl_kind__ = 'function'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'convert_all_elements_to_np_array'
TOOL_DESCRIPTION = 'Call this tool when you need to normalize a nested Python list, tuple, or mixed iterable into a numpy array — including ragged (inhomogeneous) structures that numpy.asarray alone would reject. Use it before passing structured numeric data to PsyNeuLink components that expect numpy inputs, or when you want to uniformly cast numeric types (e.g., float32 → float64) throughout a nested structure. Returns a numpy array wrapping the converted input.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "arr": {\n      "description": "The input to convert. May be a scalar, list, tuple, numpy array, or nested combination. Strings are treated as scalars, not iterated.",\n      "oneOf": [\n        {\n          "type": "number"\n        },\n        {\n          "type": "array"\n        },\n        {\n          "type": "boolean"\n        }\n      ]\n    },\n    "cast_from": {\n      "description": "Numpy dtype name (e.g. \'float32\', \'int32\') identifying the source dtype to cast. Elements whose dtype matches this value will be converted to cast_to. Requires cast_to to also be set.",\n      "type": "string"\n    },\n    "cast_to": {\n      "description": "Numpy dtype name (e.g. \'float64\', \'int64\') to cast matched elements into. Only used when cast_from is set.",\n      "type": "string"\n    },\n    "dtype": {\n      "description": "Numpy dtype name (e.g. \'float64\', \'int32\') to apply to the output array when not using cast_from/cast_to. Ignored if cast_from is provided.",\n      "type": "string"\n    }\n  },\n  "required": [\n    "arr"\n  ],\n  "type": "object"\n}\n\nNotes:\ncast_from/cast_to and dtype are mutually exclusive in intent — dtype is ignored when cast_from is set. dtype, cast_from, and cast_to must be passed as dtype name strings (e.g. "float64") since JSON cannot represent numpy dtype objects; the host must resolve these strings to numpy dtypes before calling. Ragged (inhomogeneous-shape) inputs produce an object-dtype numpy array where each element is itself a numpy array, not a uniform multidimensional array. Non-iterable scalars and strings are wrapped directly with numpy.asarray. numpy.matrix inputs with object dtype are flattened to a 1-D array.'
TOOL_PARAMETERS = { 'properties': { 'arr': { 'description': 'The input to convert. May be a scalar, '
                                          'list, tuple, numpy array, or nested '
                                          'combination. Strings are treated as '
                                          'scalars, not iterated.',
                           'oneOf': [ {'type': 'number'},
                                      {'type': 'array'},
                                      {'type': 'boolean'}]},
                  'cast_from': { 'description': "Numpy dtype name (e.g. 'float32', "
                                                "'int32') identifying the source dtype "
                                                'to cast. Elements whose dtype matches '
                                                'this value will be converted to '
                                                'cast_to. Requires cast_to to also be '
                                                'set.',
                                 'type': 'string'},
                  'cast_to': { 'description': "Numpy dtype name (e.g. 'float64', "
                                              "'int64') to cast matched elements into. "
                                              'Only used when cast_from is set.',
                               'type': 'string'},
                  'dtype': { 'description': "Numpy dtype name (e.g. 'float64', "
                                            "'int32') to apply to the output array "
                                            'when not using cast_from/cast_to. Ignored '
                                            'if cast_from is provided.',
                             'type': 'string'}},
  'required': ['arr'],
  'type': 'object'}
TOOL_NOTES = 'cast_from/cast_to and dtype are mutually exclusive in intent — dtype is ignored when cast_from is set. dtype, cast_from, and cast_to must be passed as dtype name strings (e.g. "float64") since JSON cannot represent numpy dtype objects; the host must resolve these strings to numpy dtypes before calling. Ragged (inhomogeneous-shape) inputs produce an object-dtype numpy array where each element is itself a numpy array, not a uniform multidimensional array. Non-iterable scalars and strings are wrapped directly with numpy.asarray. numpy.matrix inputs with object dtype are flattened to a 1-D array.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.convert_all_elements_to_np_array
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
    def convert_all_elements_to_np_array(args: dict[str, Any] | None = None) -> Any:
        'Call this tool when you need to normalize a nested Python list, tuple, or mixed iterable into a numpy array — including ragged (inhomogeneous) structures that numpy.asarray alone would reject.'
        return _impl(args or {})
