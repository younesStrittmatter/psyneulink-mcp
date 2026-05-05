"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = 'b18ba16beeceab67a4b1b4569185ee3e777a8c5eae90a16bfa101e1992d15065'
__pnl_qualname__ = 'psyneulink.Context'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_context'
TOOL_DESCRIPTION = 'Call this tool when you need to explicitly construct a Context object to pass as the `context` argument to PsyNeuLink Component or Composition methods (e.g., `run`, `execute`, `learn`). Use it when you want to tag an execution with a custom `execution_id`, attach a diagnostic `string`, or override the default execution phase or source flags. In most workflows PsyNeuLink auto-creates contexts internally — only call this when you need non-default control over context metadata.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "execution_id": {\n      "description": "Unique identifier for this execution context. Defaults to an auto-generated timestamp string if omitted.",\n      "type": "string"\n    },\n    "execution_phase": {\n      "description": "Phase of execution to record. Defaults to IDLE. Use PROCESSING for normal forward-pass runs, LEARNING during training, CONTROL when a controller is acting.",\n      "enum": [\n        "IDLE",\n        "PREPARING",\n        "PROCESSING",\n        "LEARNING",\n        "CONTROL"\n      ],\n      "type": "string"\n    },\n    "source": {\n      "description": "Origin of the call that created this context. Defaults to NONE. Use COMMAND_LINE when invoking from a script or agent; COMPOSITION when called from within a Composition\'s run loop.",\n      "enum": [\n        "NONE",\n        "CONSTRUCTOR",\n        "COMMAND_LINE",\n        "COMPOSITION"\n      ],\n      "type": "string"\n    },\n    "string": {\n      "default": "",\n      "description": "Optional free-text message attached to this context, useful for debugging or logging. Distinct from flags_string.",\n      "type": "string"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\n- `execution_id` auto-generates a high-resolution timestamp string (e.g., "2025-01-15 12:34:56.123456 UTC") when omitted; pass an explicit string only if you need a stable, repeatable ID.\n- `owner` and `composition` expect live Python Component/Composition objects and cannot be passed via JSON — they are set to None by default and should be wired by the host if needed.\n- `flags`, `execution_phase`, and `source` are partially redundant: `flags` is the bitwise OR of the other two. If you pass both `flags` and `execution_phase`/`source`, they must agree or PNL raises a ContextError.\n- `rpc_pipeline` (a Queue for PsyNeuLinkView RPC) is omitted from the schema — not needed in agent-driven workflows.\n- `runmode` is omitted; it defaults to DEFAULT_MODE and should only be changed if you are deliberately targeting the LLVM or PTX (GPU) backends.\n- The `execution_phase` and `source` string values in this schema must be mapped to `ContextFlags` enum members by the host before calling the constructor.'
TOOL_PARAMETERS = { 'properties': { 'execution_id': { 'description': 'Unique identifier for this '
                                                   'execution context. Defaults to an '
                                                   'auto-generated timestamp string if '
                                                   'omitted.',
                                    'type': 'string'},
                  'execution_phase': { 'description': 'Phase of execution to record. '
                                                      'Defaults to IDLE. Use '
                                                      'PROCESSING for normal '
                                                      'forward-pass runs, LEARNING '
                                                      'during training, CONTROL when a '
                                                      'controller is acting.',
                                       'enum': [ 'IDLE',
                                                 'PREPARING',
                                                 'PROCESSING',
                                                 'LEARNING',
                                                 'CONTROL'],
                                       'type': 'string'},
                  'source': { 'description': 'Origin of the call that created this '
                                             'context. Defaults to NONE. Use '
                                             'COMMAND_LINE when invoking from a script '
                                             'or agent; COMPOSITION when called from '
                                             "within a Composition's run loop.",
                              'enum': [ 'NONE',
                                        'CONSTRUCTOR',
                                        'COMMAND_LINE',
                                        'COMPOSITION'],
                              'type': 'string'},
                  'string': { 'default': '',
                              'description': 'Optional free-text message attached to '
                                             'this context, useful for debugging or '
                                             'logging. Distinct from flags_string.',
                              'type': 'string'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = '- `execution_id` auto-generates a high-resolution timestamp string (e.g., "2025-01-15 12:34:56.123456 UTC") when omitted; pass an explicit string only if you need a stable, repeatable ID.\n- `owner` and `composition` expect live Python Component/Composition objects and cannot be passed via JSON — they are set to None by default and should be wired by the host if needed.\n- `flags`, `execution_phase`, and `source` are partially redundant: `flags` is the bitwise OR of the other two. If you pass both `flags` and `execution_phase`/`source`, they must agree or PNL raises a ContextError.\n- `rpc_pipeline` (a Queue for PsyNeuLinkView RPC) is omitted from the schema — not needed in agent-driven workflows.\n- `runmode` is omitted; it defaults to DEFAULT_MODE and should only be changed if you are deliberately targeting the LLVM or PTX (GPU) backends.\n- The `execution_phase` and `source` string values in this schema must be mapped to `ContextFlags` enum members by the host before calling the constructor.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.Context
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
    def create_context(args: dict[str, Any] | None = None) -> Any:
        'Call this tool when you need to explicitly construct a Context object to pass as the `context` argument to PsyNeuLink Component or Composition methods (e.g., `run`, `execute`, `learn`).'
        return _impl(args or {})
