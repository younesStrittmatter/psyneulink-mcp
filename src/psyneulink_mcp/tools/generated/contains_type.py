"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '5454942e8d003edba25ab749f67666264eb7f6fc79690e33d3039ccad158f64b'
__pnl_qualname__ = 'psyneulink.contains_type'
__pnl_kind__ = 'function'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'contains_type'
TOOL_DESCRIPTION = 'Call this tool to check whether a (possibly nested) iterable contains at least one instance of a given type. Use it for pre-flight validation of PsyNeuLink data structures — e.g., confirming a parameter list contains a Mechanism or Projection before passing it to a Composition. Returns True if any element at any nesting depth matches the type, False otherwise.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "arr": {\n      "description": "The iterable (list, tuple, or nested collection) to search through. The check is recursive through nested iterables unless the top-level is a numpy matrix.",\n      "items": {},\n      "type": "array"\n    },\n    "typ": {\n      "description": "Fully qualified class name (e.g. \'psyneulink.TransferMechanism\') or a list of such names to match against. Passed as a type or tuple of types to isinstance().",\n      "type": "string"\n    }\n  },\n  "required": [\n    "arr",\n    "typ"\n  ],\n  "type": "object"\n}\n\nNotes:\nThis tool checks elements *inside* arr, not arr itself — use isinstance() if you need to check arr directly. For numpy arrays, only object-dtype (\'O\') and void-dtype (\'V\') arrays are recursed into; numeric dtypes short-circuit by checking only the first element. Passing a numpy matrix as arr disables recursion into its elements. The `typ` parameter in the raw Python API accepts a type or tuple of types; the MCP layer will need to resolve string class names to actual types before calling the underlying function.'
TOOL_PARAMETERS = { 'properties': { 'arr': { 'description': 'The iterable (list, tuple, or nested '
                                          'collection) to search through. The check is '
                                          'recursive through nested iterables unless '
                                          'the top-level is a numpy matrix.',
                           'items': {},
                           'type': 'array'},
                  'typ': { 'description': 'Fully qualified class name (e.g. '
                                          "'psyneulink.TransferMechanism') or a list "
                                          'of such names to match against. Passed as a '
                                          'type or tuple of types to isinstance().',
                           'type': 'string'}},
  'required': ['arr', 'typ'],
  'type': 'object'}
TOOL_NOTES = "This tool checks elements *inside* arr, not arr itself — use isinstance() if you need to check arr directly. For numpy arrays, only object-dtype ('O') and void-dtype ('V') arrays are recursed into; numeric dtypes short-circuit by checking only the first element. Passing a numpy matrix as arr disables recursion into its elements. The `typ` parameter in the raw Python API accepts a type or tuple of types; the MCP layer will need to resolve string class names to actual types before calling the underlying function."


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.contains_type
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
    def contains_type(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to check whether a (possibly nested) iterable contains at least one instance of a given type.'
        return _impl(args or {})
