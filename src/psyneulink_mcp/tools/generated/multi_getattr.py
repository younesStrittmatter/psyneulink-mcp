"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '71877ac5c25c310dc5a3bdb759a9d956fd7361edc22ee0ccbad5620b1f4d4fa7'
__pnl_qualname__ = 'psyneulink.multi_getattr'
__pnl_kind__ = 'function'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'multi_getattr'
TOOL_DESCRIPTION = 'Call this tool to retrieve a deeply nested attribute from a PsyNeuLink object using dot-notation (e.g., "parameters.value.default_value") without writing a chain of getattr calls. Returns the resolved attribute value, or a default if provided and any step in the chain is missing.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "attr": {\n      "description": "Dot-separated attribute path to retrieve, e.g. \'parameters.value.default_value\'.",\n      "type": "string"\n    },\n    "default": {\n      "description": "Value to return if any attribute in the chain is missing. If omitted, an AttributeError is raised on missing attributes.",\n      "type": "string"\n    },\n    "obj": {\n      "description": "The PsyNeuLink object (or its variable name in the current namespace) to traverse. Must resolve to an actual Python object at runtime.",\n      "type": "string"\n    }\n  },\n  "required": [\n    "obj",\n    "attr"\n  ],\n  "type": "object"\n}\n\nNotes:\nThe default parameter uses a truthiness check (`if default:`), so passing a falsy value (0, False, empty string, empty list) as the default will behave as if no default was given — an AttributeError will be raised instead of returning the falsy default. Only pass default when you need a non-falsy sentinel. obj is expected to be a live Python object reference, not a string name; the MCP host must resolve it before calling this function.'
TOOL_PARAMETERS = { 'properties': { 'attr': { 'description': 'Dot-separated attribute path to retrieve, '
                                           "e.g. 'parameters.value.default_value'.",
                            'type': 'string'},
                  'default': { 'description': 'Value to return if any attribute in the '
                                              'chain is missing. If omitted, an '
                                              'AttributeError is raised on missing '
                                              'attributes.',
                               'type': 'string'},
                  'obj': { 'description': 'The PsyNeuLink object (or its variable name '
                                          'in the current namespace) to traverse. Must '
                                          'resolve to an actual Python object at '
                                          'runtime.',
                           'type': 'string'}},
  'required': ['obj', 'attr'],
  'type': 'object'}
TOOL_NOTES = 'The default parameter uses a truthiness check (`if default:`), so passing a falsy value (0, False, empty string, empty list) as the default will behave as if no default was given — an AttributeError will be raised instead of returning the falsy default. Only pass default when you need a non-falsy sentinel. obj is expected to be a live Python object reference, not a string name; the MCP host must resolve it before calling this function.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.multi_getattr
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
    def multi_getattr(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to retrieve a deeply nested attribute from a PsyNeuLink object using dot-notation (e.g., "parameters.value.default_value") without writing a chain of getattr calls.'
        return _impl(args or {})
