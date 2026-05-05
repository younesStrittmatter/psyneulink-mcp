"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '64a701acee35a8c3a34bb41555e4221bb4f5dd8b6f8c2ba754c63ffd87f625eb'
__pnl_qualname__ = 'psyneulink.Projection'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_projection'
TOOL_DESCRIPTION = 'Call this tool only when you need a generic Projection type reference (e.g., for type-checking, isinstance tests, or dynamic dispatch) — not to create a projection. `psyneulink.Projection` is an abstract shell class; instantiating it directly always raises `ShellClassError`. Use `MappingProjection`, `ControlProjection`, or `GatingProjection` tools to actually create projection objects.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "name": {\n      "description": "Optional name string for the projection; a default is assigned by the registry if omitted.",\n      "type": "string"\n    },\n    "params": {\n      "description": "Optional parameter dictionary overriding constructor arguments. Keys are parameter names, values are the overriding values.",\n      "type": "object"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\n`Projection` is an abstract shell class — its `validate_states` and `_validate_params` methods immediately raise `ShellClassError`. Never instantiate it directly; always use a concrete subclass (`MappingProjection`, `ControlProjection`, `GatingProjection`, `LearningProjection`, etc.). The docstring shown is inherited from `Component` and describes the general Component interface, not `Projection`-specific behavior. This tool exists only for reference/typing purposes.'
TOOL_PARAMETERS = { 'properties': { 'name': { 'description': 'Optional name string for the projection; a '
                                           'default is assigned by the registry if '
                                           'omitted.',
                            'type': 'string'},
                  'params': { 'description': 'Optional parameter dictionary overriding '
                                             'constructor arguments. Keys are '
                                             'parameter names, values are the '
                                             'overriding values.',
                              'type': 'object'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = '`Projection` is an abstract shell class — its `validate_states` and `_validate_params` methods immediately raise `ShellClassError`. Never instantiate it directly; always use a concrete subclass (`MappingProjection`, `ControlProjection`, `GatingProjection`, `LearningProjection`, etc.). The docstring shown is inherited from `Component` and describes the general Component interface, not `Projection`-specific behavior. This tool exists only for reference/typing purposes.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.Projection
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
    def create_projection(args: dict[str, Any] | None = None) -> Any:
        'Call this tool only when you need a generic Projection type reference (e.g., for type-checking, isinstance tests, or dynamic dispatch) — not to create a projection.'
        return _impl(args or {})
