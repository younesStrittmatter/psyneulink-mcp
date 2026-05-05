"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '378c73e0124697365b3673e07ccb2a335906c42d26361515090a90de7d5543b4'
__pnl_qualname__ = 'psyneulink.unproxy_weakproxy'
__pnl_kind__ = 'function'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'unproxy_weakproxy'
TOOL_DESCRIPTION = 'Call this tool when you hold a weakref proxy object (created via `weakref.proxy(obj)`) and need to recover the underlying Python object it references. Returns the actual dereferenced object — useful when PsyNeuLink internals hand back a proxy and you need to inspect or pass the real instance. Handles both instance proxies and class proxies.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "proxy": {\n      "description": "The weakref proxy object to dereference. Note: this must be a live weakref.proxy instance accessible in the current PsyNeuLink runtime \\u2014 pass the variable name or handle referencing the proxy object.",\n      "type": "string"\n    }\n  },\n  "required": [\n    "proxy"\n  ],\n  "type": "object"\n}\n\nNotes:\nThis is a low-level Python runtime utility; it only makes sense when a weakref proxy object is already in scope in the runtime session. Passing a plain string or non-proxy object will likely raise AttributeError. Two resolution paths exist internally: for proxies to instances, it recovers via `__repr__.__self__`; for proxies to classes, via `__mro__[0]`. In practice, agents will rarely need to call this directly — it is primarily used by PsyNeuLink internals. If the referenced object has already been garbage-collected, the proxy will be dead and this call will raise ReferenceError.'
TOOL_PARAMETERS = { 'properties': { 'proxy': { 'description': 'The weakref proxy object to dereference. '
                                            'Note: this must be a live weakref.proxy '
                                            'instance accessible in the current '
                                            'PsyNeuLink runtime — pass the variable '
                                            'name or handle referencing the proxy '
                                            'object.',
                             'type': 'string'}},
  'required': ['proxy'],
  'type': 'object'}
TOOL_NOTES = 'This is a low-level Python runtime utility; it only makes sense when a weakref proxy object is already in scope in the runtime session. Passing a plain string or non-proxy object will likely raise AttributeError. Two resolution paths exist internally: for proxies to instances, it recovers via `__repr__.__self__`; for proxies to classes, via `__mro__[0]`. In practice, agents will rarely need to call this directly — it is primarily used by PsyNeuLink internals. If the referenced object has already been garbage-collected, the proxy will be dead and this call will raise ReferenceError.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.unproxy_weakproxy
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
    def unproxy_weakproxy(args: dict[str, Any] | None = None) -> Any:
        'Call this tool when you hold a weakref proxy object (created via `weakref.proxy(obj)`) and need to recover the underlying Python object it references.'
        return _impl(args or {})
