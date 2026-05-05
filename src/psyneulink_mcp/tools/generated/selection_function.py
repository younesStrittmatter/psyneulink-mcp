"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '4daec0cd01c2c3c68675be36ab6d3bd317c4c9b766ad274df7a0a9f9e39814cf'
__pnl_qualname__ = 'psyneulink.SelectionFunction'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_selection_function'
TOOL_DESCRIPTION = 'Call this tool to instantiate a SelectionFunction base object when you need the abstract parent class of PsyNeuLink\'s selection function family — functions that pick one value and zero out the rest. In practice, prefer concrete subclasses (e.g., OneHot) unless you are introspecting the type hierarchy or passing a SelectionFunction type reference to a mechanism\'s function parameter. Returns a SelectionFunction instance with componentType set to SELECTION_FUNCTION_TYPE.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "default_variable": {\n      "description": "Default input value for the function. Should be a numeric array matching the expected input shape.",\n      "items": {\n        "type": "number"\n      },\n      "type": "array"\n    },\n    "name": {\n      "description": "Optional name for this function instance.",\n      "type": "string"\n    },\n    "owner": {\n      "description": "Name of the PsyNeuLink component that owns this function, if applicable.",\n      "type": "string"\n    },\n    "params": {\n      "additionalProperties": true,\n      "description": "Optional dict of parameter overrides to pass at construction time.",\n      "type": "object"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\nSelectionFunction is an abstract base class — it has no selection logic of its own. Instantiating it directly will not perform any meaningful computation. Use concrete subclasses such as OneHot for actual selection behavior. The class exists primarily for isinstance checks and as a type token for mechanism function parameters.'
TOOL_PARAMETERS = { 'properties': { 'default_variable': { 'description': 'Default input value for the '
                                                       'function. Should be a numeric '
                                                       'array matching the expected '
                                                       'input shape.',
                                        'items': {'type': 'number'},
                                        'type': 'array'},
                  'name': { 'description': 'Optional name for this function instance.',
                            'type': 'string'},
                  'owner': { 'description': 'Name of the PsyNeuLink component that '
                                            'owns this function, if applicable.',
                             'type': 'string'},
                  'params': { 'additionalProperties': True,
                              'description': 'Optional dict of parameter overrides to '
                                             'pass at construction time.',
                              'type': 'object'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = 'SelectionFunction is an abstract base class — it has no selection logic of its own. Instantiating it directly will not perform any meaningful computation. Use concrete subclasses such as OneHot for actual selection behavior. The class exists primarily for isinstance checks and as a type token for mechanism function parameters.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.SelectionFunction
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
    def create_selection_function(args: dict[str, Any] | None = None) -> Any:
        "Call this tool to instantiate a SelectionFunction base object when you need the abstract parent class of PsyNeuLink's selection function family — functions that pick one value and zero out the rest."
        return _impl(args or {})
