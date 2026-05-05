"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '22dc00f1dff2db847c457b293dfccbdcb8ce6eedfd62768a0767bffe2c14b1a5'
__pnl_qualname__ = 'psyneulink.core.components.functions.nonstateful.transferfunctions.auto'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_auto'
TOOL_DESCRIPTION = 'Call this tool to create an `auto` sentinel instance for use as an enum member value in PsyNeuLink transfer function enumerations. It produces an `auto` object that, when assigned inside an `Enum` class body, is replaced with an automatically incremented integer. Use this when constructing or introspecting PsyNeuLink enum-typed parameters that require auto-assigned values rather than explicit integers.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "value": {\n      "description": "Optional seed value for the auto instance. Omit to let the enum machinery assign the next available integer automatically.",\n      "type": "number"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\nThis is Python\'s standard `enum.auto` class, re-exported from PsyNeuLink\'s transfer functions namespace. It has no PsyNeuLink-specific behavior. `auto()` instances are only meaningful inside an `Enum` class body — instantiating one outside that context returns a plain object whose `.value` is a sentinel (`_auto_null`) and which will not behave as an enum member. Do not use this to set runtime parameter values on PsyNeuLink mechanisms; use the concrete enum member (e.g. `TransferFunction.LINEAR`) instead.'
TOOL_PARAMETERS = { 'properties': { 'value': { 'description': 'Optional seed value for the auto '
                                            'instance. Omit to let the enum machinery '
                                            'assign the next available integer '
                                            'automatically.',
                             'type': 'number'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = "This is Python's standard `enum.auto` class, re-exported from PsyNeuLink's transfer functions namespace. It has no PsyNeuLink-specific behavior. `auto()` instances are only meaningful inside an `Enum` class body — instantiating one outside that context returns a plain object whose `.value` is a sentinel (`_auto_null`) and which will not behave as an enum member. Do not use this to set runtime parameter values on PsyNeuLink mechanisms; use the concrete enum member (e.g. `TransferFunction.LINEAR`) instead."


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.auto
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
    def create_auto(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to create an `auto` sentinel instance for use as an enum member value in PsyNeuLink transfer function enumerations.'
        return _impl(args or {})
