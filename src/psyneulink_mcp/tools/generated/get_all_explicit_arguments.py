"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '54010b6e136fba7c71c6e12cf753a822b7c9d28046f02e84f24ab329460f88b9'
__pnl_qualname__ = 'psyneulink.get_all_explicit_arguments'
__pnl_kind__ = 'function'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'get_all_explicit_arguments'
TOOL_DESCRIPTION = 'Call this tool when you need to discover all explicitly named parameters that a PsyNeuLink method accepts, including parameters defined on parent classes. This is useful before constructing a call to an inherited or overridden method when you are unsure which named arguments are valid. Returns a set of parameter name strings (excludes *args and **kwargs catch-alls).\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "cls_": {\n      "description": "Fully qualified or short class name whose MRO will be walked (e.g. \'TransferMechanism\'). The host resolves this string to the actual class object before calling the function.",\n      "type": "string"\n    },\n    "func_str": {\n      "description": "Name of the method to inspect (e.g. \'execute\', \'__init__\'). Must exist on at least one class in the MRO of cls_.",\n      "type": "string"\n    }\n  },\n  "required": [\n    "cls_",\n    "func_str"\n  ],\n  "type": "object"\n}\n\nNotes:\ncls_ must be an actual Python class object at call time, but MCP parameters are JSON-only; the host template must resolve the string name to a class before forwarding. If the method on a given MRO level has no *args or **kwargs, the walk stops there — arguments defined only on higher ancestors are not included. The result is a Python set (unordered, no duplicates), not a list. \'self\' and \'cls\' are typically included in the returned set since they appear as regular positional parameters in the signature.'
TOOL_PARAMETERS = { 'properties': { 'cls_': { 'description': 'Fully qualified or short class name whose '
                                           'MRO will be walked (e.g. '
                                           "'TransferMechanism'). The host resolves "
                                           'this string to the actual class object '
                                           'before calling the function.',
                            'type': 'string'},
                  'func_str': { 'description': 'Name of the method to inspect (e.g. '
                                               "'execute', '__init__'). Must exist on "
                                               'at least one class in the MRO of cls_.',
                                'type': 'string'}},
  'required': ['cls_', 'func_str'],
  'type': 'object'}
TOOL_NOTES = "cls_ must be an actual Python class object at call time, but MCP parameters are JSON-only; the host template must resolve the string name to a class before forwarding. If the method on a given MRO level has no *args or **kwargs, the walk stops there — arguments defined only on higher ancestors are not included. The result is a Python set (unordered, no duplicates), not a list. 'self' and 'cls' are typically included in the returned set since they appear as regular positional parameters in the signature."


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.get_all_explicit_arguments
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
    def get_all_explicit_arguments(args: dict[str, Any] | None = None) -> Any:
        'Call this tool when you need to discover all explicitly named parameters that a PsyNeuLink method accepts, including parameters defined on parent classes.'
        return _impl(args or {})
