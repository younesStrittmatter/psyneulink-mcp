"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = 'e11fb3c585b87f34ee8c7984444811e3a835fe295426930f80b4f78b3de2e48c'
__pnl_qualname__ = 'psyneulink.core.components.functions.nonstateful.distributionfunctions.DEFAULT_SEED'
__pnl_kind__ = 'function'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'default_seed'
TOOL_DESCRIPTION = 'Call this tool to retrieve the default seed value used by PsyNeuLink distribution functions when no explicit seed is provided. Returns a NumPy array containing -1, which PsyNeuLink interprets as "no fixed seed" (i.e., use a random/system-generated seed).\n\nParameters (JSON Schema):\n{\n  "properties": {},\n  "required": [],\n  "type": "object"\n}\n\nNotes:\nThis function takes no arguments and always returns np.array(-1). The value -1 is a sentinel meaning "unseeded/random" — it does not set the seed to -1. Use this to query the default seed sentinel before passing it to distribution functions or to check whether a seed has been overridden from the default.'
TOOL_PARAMETERS = {'properties': {}, 'required': [], 'type': 'object'}
TOOL_NOTES = 'This function takes no arguments and always returns np.array(-1). The value -1 is a sentinel meaning "unseeded/random" — it does not set the seed to -1. Use this to query the default seed sentinel before passing it to distribution functions or to check whether a seed has been overridden from the default.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.DEFAULT_SEED
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
    def default_seed(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to retrieve the default seed value used by PsyNeuLink distribution functions when no explicit seed is provided.'
        return _impl(args or {})
