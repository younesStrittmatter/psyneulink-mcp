"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = 'fd0c1edc8811f2ed59ed0d4e43e35ea2b094b7fb57921172f9f6aa4e59c0c345'
__pnl_qualname__ = 'psyneulink.System_Base'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_system__base'
TOOL_DESCRIPTION = 'Do NOT call this tool directly. `System_Base` is an abstract shell class (`class System_Base(ShellClass): pass`) with no constructor body — it is a marker type in PsyNeuLink\'s legacy System hierarchy and will raise an error if instantiated. Agents building neural-network models should use `Composition` instead, which is the current PsyNeuLink API for assembling Mechanisms into a network.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "name": {\n      "description": "Optional name for the object; a default is assigned by the relevant Registry if omitted.",\n      "type": "string"\n    },\n    "params": {\n      "additionalProperties": true,\n      "description": "Optional parameter dictionary overriding constructor-argument defaults.",\n      "type": "object"\n    },\n    "prefs": {\n      "additionalProperties": true,\n      "description": "Optional PreferenceSet or specification dict controlling logging, reporting, and verbosity.",\n      "type": "object"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\nSystem_Base is defined as `class System_Base(ShellClass): pass` — it has no implementation body and no constructor of its own. The docstring shown is inherited from the Component base class and does not reflect System_Base\'s own API. The PsyNeuLink System API (of which System_Base is a part) is superseded by Composition in current PNL versions; prefer Composition for all model-building tasks. Any attempt to instantiate System_Base directly is almost certain to fail or produce a non-functional object.'
TOOL_PARAMETERS = { 'properties': { 'name': { 'description': 'Optional name for the object; a default is '
                                           'assigned by the relevant Registry if '
                                           'omitted.',
                            'type': 'string'},
                  'params': { 'additionalProperties': True,
                              'description': 'Optional parameter dictionary overriding '
                                             'constructor-argument defaults.',
                              'type': 'object'},
                  'prefs': { 'additionalProperties': True,
                             'description': 'Optional PreferenceSet or specification '
                                            'dict controlling logging, reporting, and '
                                            'verbosity.',
                             'type': 'object'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = "System_Base is defined as `class System_Base(ShellClass): pass` — it has no implementation body and no constructor of its own. The docstring shown is inherited from the Component base class and does not reflect System_Base's own API. The PsyNeuLink System API (of which System_Base is a part) is superseded by Composition in current PNL versions; prefer Composition for all model-building tasks. Any attempt to instantiate System_Base directly is almost certain to fail or produce a non-functional object."


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.System_Base
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
    def create_system__base(args: dict[str, Any] | None = None) -> Any:
        'Do NOT call this tool directly.'
        return _impl(args or {})
