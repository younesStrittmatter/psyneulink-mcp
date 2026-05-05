"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = 'fbc50a90f84eb72768d96b3c114acb23d3a6417b350cc0ae2977c8b937518372'
__pnl_qualname__ = 'psyneulink.PathwayRole'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_pathway_role'
TOOL_DESCRIPTION = 'Call this tool to retrieve a PathwayRole enum member by integer value when you need to classify, filter, or compare pathway roles within a Composition. Returns the matching PathwayRole member (e.g., ORIGIN, INPUT, INTERNAL, LEARNING). Use it when a PsyNeuLink API expects a PathwayRole argument or when inspecting what role a pathway plays in a Composition\'s structure.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "value": {\n      "description": "Integer value of the PathwayRole member to retrieve. Valid values: ORIGIN=0, INPUT=1, SINGLETON=2, INTERNAL=3, OUTPUT=4, TERMINAL=5, CYCLE=6, CONTROL=7, LEARNING=8.",\n      "maximum": 8,\n      "minimum": 0,\n      "type": "integer"\n    }\n  },\n  "required": [\n    "value"\n  ],\n  "type": "object"\n}\n\nNotes:\nThe enum member is spelled SINGLETON (value 2) in code, but the docstring misspells it as SINGELTON — use the correct spelling when referencing the member by name. CONTROL (value 7) appears inside COMMENT blocks in the docstring, indicating it may be undocumented/internal; it is still a valid enum member. Calling PathwayRole(value=N) uses the Enum metaclass keyword form, which is valid Python.'
TOOL_PARAMETERS = { 'properties': { 'value': { 'description': 'Integer value of the PathwayRole member '
                                            'to retrieve. Valid values: ORIGIN=0, '
                                            'INPUT=1, SINGLETON=2, INTERNAL=3, '
                                            'OUTPUT=4, TERMINAL=5, CYCLE=6, CONTROL=7, '
                                            'LEARNING=8.',
                             'maximum': 8,
                             'minimum': 0,
                             'type': 'integer'}},
  'required': ['value'],
  'type': 'object'}
TOOL_NOTES = 'The enum member is spelled SINGLETON (value 2) in code, but the docstring misspells it as SINGELTON — use the correct spelling when referencing the member by name. CONTROL (value 7) appears inside COMMENT blocks in the docstring, indicating it may be undocumented/internal; it is still a valid enum member. Calling PathwayRole(value=N) uses the Enum metaclass keyword form, which is valid Python.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.PathwayRole
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
    def create_pathway_role(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to retrieve a PathwayRole enum member by integer value when you need to classify, filter, or compare pathway roles within a Composition.'
        return _impl(args or {})
