"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = 'b0e81ccd1199434c5c779a4a7d7ef21f1288be54ed0029d5fd884aeba7e4d107'
__pnl_qualname__ = 'psyneulink.core.components.functions.nonstateful.distributionfunctions.check_user_specified'
__pnl_kind__ = 'function'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'check_user_specified'
TOOL_DESCRIPTION = 'Call this tool only when you need to wrap a PsyNeuLink `__init__` constructor so that the resulting instance automatically records which keyword arguments were explicitly provided by the caller (vs. left at defaults). The wrapped constructor populates `self._user_specified_args` on the instance. This is an internal bookkeeping decorator — most agents building or configuring PsyNeuLink models will never need to call it directly; it is invoked automatically during object construction inside PsyNeuLink\'s class hierarchy.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "func": {\n      "description": "Fully-qualified name of the constructor function to wrap (e.g. \'psyneulink.core.components.mechanisms.processing.transfermechanism.TransferMechanism.__init__\'). NOTE: because MCP parameters are JSON-serialized, the host resolves this string to the actual callable before passing it to check_user_specified.",\n      "type": "string"\n    }\n  },\n  "required": [\n    "func"\n  ],\n  "type": "object"\n}\n\nNotes:\nThis symbol is a Python decorator factory, not a data-in/data-out tool. Its sole argument `func` is a Python callable, which cannot be passed directly over JSON/MCP. Practically, agents should never call this tool — it is used internally by PsyNeuLink\'s metaclass/constructor chain to populate `_user_specified_args` on instances. If you find yourself wanting to call it, reconsider whether you actually need to inspect `_user_specified_args` on an already-constructed object instead. There is no return value visible to the agent; the decorator returns a wrapped function that is only meaningful inside Python\'s import-time class construction.'
TOOL_PARAMETERS = { 'properties': { 'func': { 'description': 'Fully-qualified name of the constructor '
                                           'function to wrap (e.g. '
                                           "'psyneulink.core.components.mechanisms.processing.transfermechanism.TransferMechanism.__init__'). "
                                           'NOTE: because MCP parameters are '
                                           'JSON-serialized, the host resolves this '
                                           'string to the actual callable before '
                                           'passing it to check_user_specified.',
                            'type': 'string'}},
  'required': ['func'],
  'type': 'object'}
TOOL_NOTES = "This symbol is a Python decorator factory, not a data-in/data-out tool. Its sole argument `func` is a Python callable, which cannot be passed directly over JSON/MCP. Practically, agents should never call this tool — it is used internally by PsyNeuLink's metaclass/constructor chain to populate `_user_specified_args` on instances. If you find yourself wanting to call it, reconsider whether you actually need to inspect `_user_specified_args` on an already-constructed object instead. There is no return value visible to the agent; the decorator returns a wrapped function that is only meaningful inside Python's import-time class construction."


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.check_user_specified
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
    def check_user_specified(args: dict[str, Any] | None = None) -> Any:
        'Call this tool only when you need to wrap a PsyNeuLink `__init__` constructor so that the resulting instance automatically records which keyword arguments were explicitly provided by the caller (vs.'
        return _impl(args or {})
