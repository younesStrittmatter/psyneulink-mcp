"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = 'b0a1002620ef79e638852ae6d30798f1c91b3d7b3130f5f2aca5b16b7988d89e'
__pnl_qualname__ = 'psyneulink.type_match'
__pnl_kind__ = 'function'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'type_match'
TOOL_DESCRIPTION = 'Call this to coerce a value to a specific PsyNeuLink-compatible numeric or container type. Use it when you have a value that needs to match a known target type (int, float, ndarray, or list) before passing it to a PNL component. Returns the value cast to the requested type, or the original value unchanged if it already matches.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "value": {\n      "description": "The value to coerce. May be a number, list, or array-like.",\n      "oneOf": [\n        {\n          "type": "number"\n        },\n        {\n          "type": "integer"\n        },\n        {\n          "type": "boolean"\n        },\n        {\n          "items": {},\n          "type": "array"\n        },\n        {\n          "type": "string"\n        }\n      ]\n    },\n    "value_type": {\n      "description": "Target type name. Pass \'int\', \'float\', \'ndarray\', \'list\', or \'None\'. The host maps these strings to the corresponding Python/NumPy types before calling.",\n      "enum": [\n        "int",\n        "float",\n        "ndarray",\n        "list",\n        "None"\n      ],\n      "type": "string"\n    }\n  },\n  "required": [\n    "value",\n    "value_type"\n  ],\n  "type": "object"\n}\n\nNotes:\nvalue_type must be passed as a string label — the host resolves \'int\'→int, \'float\'→float, \'ndarray\'→np.ndarray, \'list\'→list, \'None\'→None before the actual call. The two None variants behave differently: value_type=\'None\' always returns Python None regardless of value; value_type=\'NoneType\' (not in the enum) returns value unchanged — only the five listed labels are supported. Raises UtilitiesError for any other type string.'
TOOL_PARAMETERS = { 'properties': { 'value': { 'description': 'The value to coerce. May be a number, '
                                            'list, or array-like.',
                             'oneOf': [ {'type': 'number'},
                                        {'type': 'integer'},
                                        {'type': 'boolean'},
                                        {'items': {}, 'type': 'array'},
                                        {'type': 'string'}]},
                  'value_type': { 'description': "Target type name. Pass 'int', "
                                                 "'float', 'ndarray', 'list', or "
                                                 "'None'. The host maps these strings "
                                                 'to the corresponding Python/NumPy '
                                                 'types before calling.',
                                  'enum': ['int', 'float', 'ndarray', 'list', 'None'],
                                  'type': 'string'}},
  'required': ['value', 'value_type'],
  'type': 'object'}
TOOL_NOTES = "value_type must be passed as a string label — the host resolves 'int'→int, 'float'→float, 'ndarray'→np.ndarray, 'list'→list, 'None'→None before the actual call. The two None variants behave differently: value_type='None' always returns Python None regardless of value; value_type='NoneType' (not in the enum) returns value unchanged — only the five listed labels are supported. Raises UtilitiesError for any other type string."


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.type_match
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
    def type_match(args: dict[str, Any] | None = None) -> Any:
        'Call this to coerce a value to a specific PsyNeuLink-compatible numeric or container type.'
        return _impl(args or {})
