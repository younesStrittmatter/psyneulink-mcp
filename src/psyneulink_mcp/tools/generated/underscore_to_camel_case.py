"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '7d7c4d194f430af0d264406c661b46a80d100114fe0e4c27352fdfa35a73114a'
__pnl_qualname__ = 'psyneulink.underscore_to_camelCase'
__pnl_kind__ = 'function'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'underscore_to_camel_case'
TOOL_DESCRIPTION = 'Call this tool to convert a PsyNeuLink underscore-prefixed attribute name (e.g., `_my_param_name`) into camelCase (e.g., `myParamName`). Use it when translating internal PNL private attribute names to their public camelCase equivalents for display, serialization, or lookup purposes.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "item": {\n      "description": "An underscore-prefixed PsyNeuLink attribute name (e.g., \'_my_param_name\'). The leading character is always stripped before conversion.",\n      "type": "string"\n    }\n  },\n  "required": [\n    "item"\n  ],\n  "type": "object"\n}\n\nNotes:\nThe function unconditionally strips the first character of `item` before processing — it is designed specifically for PNL\'s convention of leading-underscore private attributes. Passing a string without a leading underscore will silently discard its first character, producing incorrect output. The result has its first letter lowercased (true camelCase, not PascalCase).'
TOOL_PARAMETERS = { 'properties': { 'item': { 'description': 'An underscore-prefixed PsyNeuLink '
                                           "attribute name (e.g., '_my_param_name'). "
                                           'The leading character is always stripped '
                                           'before conversion.',
                            'type': 'string'}},
  'required': ['item'],
  'type': 'object'}
TOOL_NOTES = "The function unconditionally strips the first character of `item` before processing — it is designed specifically for PNL's convention of leading-underscore private attributes. Passing a string without a leading underscore will silently discard its first character, producing incorrect output. The result has its first letter lowercased (true camelCase, not PascalCase)."


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.underscore_to_camelCase
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
    def underscore_to_camel_case(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to convert a PsyNeuLink underscore-prefixed attribute name (e.g., `_my_param_name`) into camelCase (e.g., `myParamName`).'
        return _impl(args or {})
