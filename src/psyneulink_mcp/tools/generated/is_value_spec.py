"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = 'ce05a7b520eaa2d29ff6af7a4f4907c52a3a7693aa05d955a9c67141806d9c85'
__pnl_qualname__ = 'psyneulink.is_value_spec'
__pnl_kind__ = 'function'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'is_value_spec'
TOOL_DESCRIPTION = 'Call this tool to check whether a candidate value qualifies as a PsyNeuLink "value spec" — i.e., a numeric scalar, numeric numpy array, or a purely numeric list (no PNL Components or callables). Returns a boolean: True if valid, False otherwise. Use it before passing a value to a PNL parameter that expects a numeric specification to avoid downstream type errors.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "spec": {\n      "description": "The candidate value to test. Pass a number, a flat or nested numeric list (e.g. [1.0, 2.0] or [[1,0],[0,1]]), or a numeric numpy array encoded as a nested list. Non-numeric types, PNL Components, and callables will return False.",\n      "oneOf": [\n        {\n          "type": "number"\n        },\n        {\n          "items": {},\n          "type": "array"\n        }\n      ]\n    }\n  },\n  "required": [\n    "spec"\n  ],\n  "type": "object"\n}\n\nNotes:\nReturns False for anything that is not a Number, a numpy array, or a purely numeric list — including strings, dicts, PNL Component instances, and Python functions. Nested lists are accepted as long as every leaf element is numeric and no element is a Component or function type. numpy arrays must be passed as nested JSON arrays; the host template passes them to the function directly.'
TOOL_PARAMETERS = { 'properties': { 'spec': { 'description': 'The candidate value to test. Pass a '
                                           'number, a flat or nested numeric list '
                                           '(e.g. [1.0, 2.0] or [[1,0],[0,1]]), or a '
                                           'numeric numpy array encoded as a nested '
                                           'list. Non-numeric types, PNL Components, '
                                           'and callables will return False.',
                            'oneOf': [ {'type': 'number'},
                                       {'items': {}, 'type': 'array'}]}},
  'required': ['spec'],
  'type': 'object'}
TOOL_NOTES = 'Returns False for anything that is not a Number, a numpy array, or a purely numeric list — including strings, dicts, PNL Component instances, and Python functions. Nested lists are accepted as long as every leaf element is numeric and no element is a Component or function type. numpy arrays must be passed as nested JSON arrays; the host template passes them to the function directly.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.is_value_spec
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
    def is_value_spec(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to check whether a candidate value qualifies as a PsyNeuLink "value spec" — i.e., a numeric scalar, numeric numpy array, or a purely numeric list (no PNL Components or callables).'
        return _impl(args or {})
