"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = 'a4db8d0015a636b51f6fa7ad3c3299ed186bc810986e512e925fe45ae7bdac79'
__pnl_qualname__ = 'psyneulink.core.components.functions.nonstateful.transferfunctions.Flag'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_flag'
TOOL_DESCRIPTION = 'Call this tool only when you need to construct a PsyNeuLink Flag enum instance from a raw integer bit-value — for example, to combine or inspect flag states programmatically. The result is a Flag instance whose string representation shows the named flag components (e.g., `<Flag.FOO|BAR: 3>`). In practice, prefer concrete Flag subclasses (e.g., mechanism-specific flag enums) over this base class, which has no named members of its own.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "value": {\n      "description": "Integer bit-pattern representing the desired flag state. Must be a valid combination of bits defined by the concrete Flag subclass; invalid values raise ValueError under STRICT boundary mode.",\n      "type": "integer"\n    }\n  },\n  "required": [\n    "value"\n  ],\n  "type": "object"\n}\n\nNotes:\nThis is the abstract base Flag class (Python enum.Flag subclass) — it defines no concrete named members. Calling it directly with an integer will almost always raise ValueError because no bits are registered on the base class. Agents should target a concrete PsyNeuLink Flag subclass instead. The class enforces STRICT boundary checking: any bit not declared in the subclass\'s member definitions is rejected. Supports bitwise combination via |, &, ^, and ~ operators on existing instances, but those operations are not exposed through this tool — they require Python-side manipulation of the returned object.'
TOOL_PARAMETERS = { 'properties': { 'value': { 'description': 'Integer bit-pattern representing the '
                                            'desired flag state. Must be a valid '
                                            'combination of bits defined by the '
                                            'concrete Flag subclass; invalid values '
                                            'raise ValueError under STRICT boundary '
                                            'mode.',
                             'type': 'integer'}},
  'required': ['value'],
  'type': 'object'}
TOOL_NOTES = "This is the abstract base Flag class (Python enum.Flag subclass) — it defines no concrete named members. Calling it directly with an integer will almost always raise ValueError because no bits are registered on the base class. Agents should target a concrete PsyNeuLink Flag subclass instead. The class enforces STRICT boundary checking: any bit not declared in the subclass's member definitions is rejected. Supports bitwise combination via |, &, ^, and ~ operators on existing instances, but those operations are not exposed through this tool — they require Python-side manipulation of the returned object."


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.Flag
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
    def create_flag(args: dict[str, Any] | None = None) -> Any:
        'Call this tool only when you need to construct a PsyNeuLink Flag enum instance from a raw integer bit-value — for example, to combine or inspect flag states programmatically.'
        return _impl(args or {})
