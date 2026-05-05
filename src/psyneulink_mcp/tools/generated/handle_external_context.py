"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '0c1735499a99881a68da8b40a8b3ce6f65b02ff8c97061f28e20342443a60753'
__pnl_qualname__ = 'psyneulink.core.components.functions.nonstateful.learningfunctions.handle_external_context'
__pnl_kind__ = 'function'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'handle_external_context'
TOOL_DESCRIPTION = 'Call this tool when you need to create a decorator that automatically injects a PsyNeuLink `Context` into a method that requires one but may be called without it. The result is a decorator (not a modeling artifact) — apply it to a function to ensure that function always receives a valid `Context` with the specified default flags. Useful when wrapping custom PsyNeuLink-aware callables before passing them to the framework.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "execution_id": {\n      "description": "Optional fixed execution ID to embed in the fallback Context. If omitted, the ID is inferred from the first positional argument or left as None.",\n      "type": "string"\n    },\n    "execution_phase": {\n      "default": "IDLE",\n      "description": "Name of the ContextFlags value to use as the default \'execution_phase\' field when no Context is supplied. Typical values: \'IDLE\', \'PROCESSING\', \'LEARNING\'. Defaults to \'IDLE\'.",\n      "type": "string"\n    },\n    "fallback_default": {\n      "default": false,\n      "description": "If true and no context is provided, uses the default_execution_id from the first positional argument as the fallback execution ID. Mutually exclusive with fallback_most_recent.",\n      "type": "boolean"\n    },\n    "fallback_most_recent": {\n      "default": false,\n      "description": "If true and no context is provided, uses the most_recent_context.execution_id from the first positional argument as the fallback execution ID. Mutually exclusive with fallback_default.",\n      "type": "boolean"\n    },\n    "source": {\n      "default": "COMMAND_LINE",\n      "description": "Name of the ContextFlags value to use as the default \'source\' field when no Context is supplied. Typical values: \'COMMAND_LINE\', \'INTERNAL\', \'LEARNING\'. Defaults to \'COMMAND_LINE\'.",\n      "type": "string"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\nThis function is a decorator factory: it returns a decorator, not a modeling result. Calling the tool yields a decorator object — you must then apply that decorator to a target function. fallback_most_recent and fallback_default are mutually exclusive; setting both raises an AssertionError at decoration time, not at call time. The source and execution_phase parameters accept ContextFlags enum *names* as strings (e.g. \'COMMAND_LINE\'), which the host must resolve to actual ContextFlags members. Additional keyword arguments (context_kwargs) are forwarded to Context.__init__ when a fallback Context is constructed. This is a low-level internal utility; most modeling workflows should not need to call it directly.'
TOOL_PARAMETERS = { 'properties': { 'execution_id': { 'description': 'Optional fixed execution ID to '
                                                   'embed in the fallback Context. If '
                                                   'omitted, the ID is inferred from '
                                                   'the first positional argument or '
                                                   'left as None.',
                                    'type': 'string'},
                  'execution_phase': { 'default': 'IDLE',
                                       'description': 'Name of the ContextFlags value '
                                                      'to use as the default '
                                                      "'execution_phase' field when no "
                                                      'Context is supplied. Typical '
                                                      "values: 'IDLE', 'PROCESSING', "
                                                      "'LEARNING'. Defaults to 'IDLE'.",
                                       'type': 'string'},
                  'fallback_default': { 'default': False,
                                        'description': 'If true and no context is '
                                                       'provided, uses the '
                                                       'default_execution_id from the '
                                                       'first positional argument as '
                                                       'the fallback execution ID. '
                                                       'Mutually exclusive with '
                                                       'fallback_most_recent.',
                                        'type': 'boolean'},
                  'fallback_most_recent': { 'default': False,
                                            'description': 'If true and no context is '
                                                           'provided, uses the '
                                                           'most_recent_context.execution_id '
                                                           'from the first positional '
                                                           'argument as the fallback '
                                                           'execution ID. Mutually '
                                                           'exclusive with '
                                                           'fallback_default.',
                                            'type': 'boolean'},
                  'source': { 'default': 'COMMAND_LINE',
                              'description': 'Name of the ContextFlags value to use as '
                                             "the default 'source' field when no "
                                             'Context is supplied. Typical values: '
                                             "'COMMAND_LINE', 'INTERNAL', 'LEARNING'. "
                                             "Defaults to 'COMMAND_LINE'.",
                              'type': 'string'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = "This function is a decorator factory: it returns a decorator, not a modeling result. Calling the tool yields a decorator object — you must then apply that decorator to a target function. fallback_most_recent and fallback_default are mutually exclusive; setting both raises an AssertionError at decoration time, not at call time. The source and execution_phase parameters accept ContextFlags enum *names* as strings (e.g. 'COMMAND_LINE'), which the host must resolve to actual ContextFlags members. Additional keyword arguments (context_kwargs) are forwarded to Context.__init__ when a fallback Context is constructed. This is a low-level internal utility; most modeling workflows should not need to call it directly."


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.handle_external_context
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
    def handle_external_context(args: dict[str, Any] | None = None) -> Any:
        'Call this tool when you need to create a decorator that automatically injects a PsyNeuLink `Context` into a method that requires one but may be called without it.'
        return _impl(args or {})
