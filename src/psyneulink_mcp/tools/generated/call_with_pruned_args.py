"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '3ef2e326ef5acecc489d6db4406b0c75ee37865adaf2d0f06ad0e3bc1b3939f2'
__pnl_qualname__ = 'psyneulink.core.components.functions.nonstateful.optimizationfunctions.call_with_pruned_args'
__pnl_kind__ = 'function'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'call_with_pruned_args'
TOOL_DESCRIPTION = 'Call this tool when you want to invoke a PsyNeuLink function but have a superset of keyword arguments and are unsure which ones the target accepts. It silently drops any kwargs not present in the target\'s signature, then calls the function and returns its result — preventing TypeError from unexpected keyword arguments.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "args": {\n      "default": [],\n      "description": "Positional arguments to forward to func, in order.",\n      "items": {\n        "type": "string"\n      },\n      "type": "array"\n    },\n    "func": {\n      "description": "Dotted import path of the PsyNeuLink callable to invoke (e.g. \'psyneulink.core.components.mechanisms.processing.transfermechanism.TransferMechanism\').",\n      "type": "string"\n    },\n    "kwargs": {\n      "additionalProperties": true,\n      "default": {},\n      "description": "Keyword arguments to forward; any key not present in func\'s signature is silently discarded before the call.",\n      "type": "object"\n    }\n  },\n  "required": [\n    "func"\n  ],\n  "type": "object"\n}\n\nNotes:\nPruning is silent: misspelled or unsupported kwarg names are dropped without any warning or error, so the call will succeed but the ignored argument will have no effect. Positional args are also pruned against the signature, so excess positional args are dropped too. This tool is primarily a utility wrapper — prefer calling the target tool directly when you know its accepted parameters.'
TOOL_PARAMETERS = { 'properties': { 'args': { 'default': [],
                            'description': 'Positional arguments to forward to func, '
                                           'in order.',
                            'items': {'type': 'string'},
                            'type': 'array'},
                  'func': { 'description': 'Dotted import path of the PsyNeuLink '
                                           'callable to invoke (e.g. '
                                           "'psyneulink.core.components.mechanisms.processing.transfermechanism.TransferMechanism').",
                            'type': 'string'},
                  'kwargs': { 'additionalProperties': True,
                              'default': {},
                              'description': 'Keyword arguments to forward; any key '
                                             "not present in func's signature is "
                                             'silently discarded before the call.',
                              'type': 'object'}},
  'required': ['func'],
  'type': 'object'}
TOOL_NOTES = 'Pruning is silent: misspelled or unsupported kwarg names are dropped without any warning or error, so the call will succeed but the ignored argument will have no effect. Positional args are also pruned against the signature, so excess positional args are dropped too. This tool is primarily a utility wrapper — prefer calling the target tool directly when you know its accepted parameters.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.call_with_pruned_args
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
    def call_with_pruned_args(args: dict[str, Any] | None = None) -> Any:
        'Call this tool when you want to invoke a PsyNeuLink function but have a superset of keyword arguments and are unsure which ones the target accepts.'
        return _impl(args or {})
