"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = 'a7273fc0bfb3615dba3f157b880289c3f9659623f2ac8c0db2a16f8737bb2f3e'
__pnl_qualname__ = 'psyneulink.ExecutionMode'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_execution_mode'
TOOL_DESCRIPTION = 'Call this tool to obtain a `psyneulink.ExecutionMode` enum value for use as the `execution_mode` argument of a Composition\'s `execute`, `run`, or `learn` methods. Returns the named enum member so the caller can pass it directly to those methods. Use this whenever you need to select between interpreted Python, CPU-compiled LLVM, GPU-compiled PTX, PyTorch (AutodiffComposition only), or automatic fallback execution.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "mode": {\n      "default": "Python",\n      "description": "Name of the execution mode to retrieve. \'Python\' (default) uses the Python interpreter. \'LLVM\' compiles and runs Nodes/Projections individually. \'LLVMRun\' compiles and runs multiple trials \\u2014 fastest CPU-compiled option. \'Auto\' progressively tries LLVMRun, LLVMExec, LLVM, then falls back to Python. \'PyTorch\' runs AutodiffComposition.learn via PyTorch and run via Python \\u2014 do not use with standard Composition. \'PTX\' and \'PTXRun\' use CUDA for GPU execution.",\n      "enum": [\n        "Python",\n        "LLVM",\n        "LLVMRun",\n        "Auto",\n        "PyTorch",\n        "PTX",\n        "PTXRun"\n      ],\n      "type": "string"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\n- `PyTorch` must only be used with `AutodiffComposition`. Passing it to a standard `Composition` is silently accepted but will NOT execute `learn` via PyTorch — this is an easy footgun.\n- `PTX` and `PTXRun` require a CUDA-capable GPU; they will fail at runtime on CPU-only machines.\n- `_LLVMExec` (compile each trial individually) is intentionally omitted — it is a private/internal flag not intended for direct agent use.\n- `Python = 0` (integer zero) is the underlying value for the default mode; `Auto` is a composite flag that combines `_Fallback | _Run | _Exec | _LLVM` and is the safest way to request compiled execution without knowing whether the hardware supports it.'
TOOL_PARAMETERS = { 'properties': { 'mode': { 'default': 'Python',
                            'description': 'Name of the execution mode to retrieve. '
                                           "'Python' (default) uses the Python "
                                           "interpreter. 'LLVM' compiles and runs "
                                           "Nodes/Projections individually. 'LLVMRun' "
                                           'compiles and runs multiple trials — '
                                           "fastest CPU-compiled option. 'Auto' "
                                           'progressively tries LLVMRun, LLVMExec, '
                                           "LLVM, then falls back to Python. 'PyTorch' "
                                           'runs AutodiffComposition.learn via PyTorch '
                                           'and run via Python — do not use with '
                                           "standard Composition. 'PTX' and 'PTXRun' "
                                           'use CUDA for GPU execution.',
                            'enum': [ 'Python',
                                      'LLVM',
                                      'LLVMRun',
                                      'Auto',
                                      'PyTorch',
                                      'PTX',
                                      'PTXRun'],
                            'type': 'string'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = '- `PyTorch` must only be used with `AutodiffComposition`. Passing it to a standard `Composition` is silently accepted but will NOT execute `learn` via PyTorch — this is an easy footgun.\n- `PTX` and `PTXRun` require a CUDA-capable GPU; they will fail at runtime on CPU-only machines.\n- `_LLVMExec` (compile each trial individually) is intentionally omitted — it is a private/internal flag not intended for direct agent use.\n- `Python = 0` (integer zero) is the underlying value for the default mode; `Auto` is a composite flag that combines `_Fallback | _Run | _Exec | _LLVM` and is the safest way to request compiled execution without knowing whether the hardware supports it.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.ExecutionMode
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
    def create_execution_mode(args: dict[str, Any] | None = None) -> Any:
        "Call this tool to obtain a `psyneulink.ExecutionMode` enum value for use as the `execution_mode` argument of a Composition's `execute`, `run`, or `learn` methods."
        return _impl(args or {})
