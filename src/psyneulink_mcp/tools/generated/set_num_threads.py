"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '2c261d8e248506d7d5fc48ded043ea21921892ed8b84cbd83c908a11afe223e6'
__pnl_qualname__ = 'psyneulink.set_num_threads'
__pnl_kind__ = 'function'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'set_num_threads'
TOOL_DESCRIPTION = 'Call this tool before running compute-intensive PsyNeuLink simulations to control parallelism. It sets the global thread count used by PsyNeuLink and, where available, propagates the limit to PyTorch and native BLAS/threading libraries via environment variables. Returns nothing on success; raises TypeError if n is not an integer or ValueError if n < 1.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "n": {\n      "description": "Number of threads to use globally. Must be >= 1. Set to 1 to force single-threaded execution; set higher to exploit multicore hardware.",\n      "minimum": 1,\n      "type": "integer"\n    }\n  },\n  "required": [\n    "n"\n  ],\n  "type": "object"\n}\n\nNotes:\nThis is a global, process-wide setting — it affects all subsequent PsyNeuLink calls in the same process. Propagation to native libraries (OpenBLAS, MKL, etc.) is best-effort via environment variables and may not take effect if those libraries were already initialized. torch and threadpoolctl propagation is also best-effort and silently skipped if those packages are absent.'
TOOL_PARAMETERS = { 'properties': { 'n': { 'description': 'Number of threads to use globally. Must be >= '
                                        '1. Set to 1 to force single-threaded '
                                        'execution; set higher to exploit multicore '
                                        'hardware.',
                         'minimum': 1,
                         'type': 'integer'}},
  'required': ['n'],
  'type': 'object'}
TOOL_NOTES = 'This is a global, process-wide setting — it affects all subsequent PsyNeuLink calls in the same process. Propagation to native libraries (OpenBLAS, MKL, etc.) is best-effort via environment variables and may not take effect if those libraries were already initialized. torch and threadpoolctl propagation is also best-effort and silently skipped if those packages are absent.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.set_num_threads
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
    def set_num_threads(args: dict[str, Any] | None = None) -> Any:
        'Call this tool before running compute-intensive PsyNeuLink simulations to control parallelism.'
        return _impl(args or {})
