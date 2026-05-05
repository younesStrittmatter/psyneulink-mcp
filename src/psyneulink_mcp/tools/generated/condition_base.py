"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = 'e42877d29e47b88a3ec9f7abf4470b66a2fc6f0bb250904caffc2352a2c7d98c'
__pnl_qualname__ = 'psyneulink.ConditionBase'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_condition_base'
TOOL_DESCRIPTION = 'Call this tool only when you need a reference to the abstract ConditionBase type itself — for example, to check isinstance membership or to document a parameter that accepts any condition. Do NOT call this to create a usable scheduling condition; instead use a concrete subclass such as Always, AfterNCalls, WhenFinished, etc. This tool cannot be instantiated meaningfully on its own.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "owner": {\n      "description": "Name or identifier of the node (Component) with which this condition is associated; determines which node\'s execution the condition governs. Most concrete subclasses accept this implicitly \\u2014 pass it here only if a concrete subclass constructor requires it explicitly.",\n      "type": "string"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\nConditionBase is an abstract class — instantiating it directly will not produce a working condition and will raise an error if MDF serialization is attempted (as_mdf_model always raises ConditionError). Always use a concrete Condition subclass (e.g., Always, AfterNCalls, BeforeNCalls, WhenFinished, Any, All) instead. The owner attribute is typically set automatically when the condition is attached to a node in a Composition, not passed by the agent.'
TOOL_PARAMETERS = { 'properties': { 'owner': { 'description': 'Name or identifier of the node '
                                            '(Component) with which this condition is '
                                            "associated; determines which node's "
                                            'execution the condition governs. Most '
                                            'concrete subclasses accept this '
                                            'implicitly — pass it here only if a '
                                            'concrete subclass constructor requires it '
                                            'explicitly.',
                             'type': 'string'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = 'ConditionBase is an abstract class — instantiating it directly will not produce a working condition and will raise an error if MDF serialization is attempted (as_mdf_model always raises ConditionError). Always use a concrete Condition subclass (e.g., Always, AfterNCalls, BeforeNCalls, WhenFinished, Any, All) instead. The owner attribute is typically set automatically when the condition is attached to a node in a Composition, not passed by the agent.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.ConditionBase
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
    def create_condition_base(args: dict[str, Any] | None = None) -> Any:
        'Call this tool only when you need a reference to the abstract ConditionBase type itself — for example, to check isinstance membership or to document a parameter that accepts any condition.'
        return _impl(args or {})
