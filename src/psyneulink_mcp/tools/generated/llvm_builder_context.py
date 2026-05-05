"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = 'a189451bdec23a7d3089e41cb44857d1b6af1cadd7b1b2ae743f781352c53304'
__pnl_qualname__ = 'psyneulink.LLVMBuilderContext'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_llvm_builder_context'
TOOL_DESCRIPTION = 'Call this tool only when you need to explicitly instantiate a new LLVM IR code generation context for PsyNeuLink\'s compiled execution backend — for example, when initializing a custom compilation pipeline with non-default floating-point precision. In almost all other cases, use `get_current()` on the existing context instead of creating a new one. Returns a context manager object that tracks LLVM modules, function caches, and compilation stats for a single compilation session.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "float_ty": {\n      "default": "double",\n      "description": "Floating-point precision for compiled code. \'double\' maps to ir.DoubleType() (64-bit, the default); \'float\' maps to ir.FloatType() (32-bit). The host translates this string to the appropriate llvmlite IR type before constructing the context.",\n      "enum": [\n        "double",\n        "float"\n      ],\n      "type": "string"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\nLLVMBuilderContext is a singleton — only one instance may exist at a time. Calling this tool while a context is already active (i.e., `LLVMBuilderContext.is_active()` returns True) will raise an AssertionError. The constructor also immediately calls `init_builtins()`, which compiles a large set of numeric, PRNG, and matrix built-ins into a new LLVM module — this is expensive. Prefer `LLVMBuilderContext.get_current()` to retrieve or lazily create a context using the default double precision. The class is designed to be used as a Python context manager (`with ctx:`); each `with` block creates a new LLVM module and pops it on exit. Agents should only instantiate this directly when they explicitly need 32-bit (float) precision compilation.'
TOOL_PARAMETERS = { 'properties': { 'float_ty': { 'default': 'double',
                                'description': 'Floating-point precision for compiled '
                                               "code. 'double' maps to ir.DoubleType() "
                                               "(64-bit, the default); 'float' maps to "
                                               'ir.FloatType() (32-bit). The host '
                                               'translates this string to the '
                                               'appropriate llvmlite IR type before '
                                               'constructing the context.',
                                'enum': ['double', 'float'],
                                'type': 'string'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = 'LLVMBuilderContext is a singleton — only one instance may exist at a time. Calling this tool while a context is already active (i.e., `LLVMBuilderContext.is_active()` returns True) will raise an AssertionError. The constructor also immediately calls `init_builtins()`, which compiles a large set of numeric, PRNG, and matrix built-ins into a new LLVM module — this is expensive. Prefer `LLVMBuilderContext.get_current()` to retrieve or lazily create a context using the default double precision. The class is designed to be used as a Python context manager (`with ctx:`); each `with` block creates a new LLVM module and pops it on exit. Agents should only instantiate this directly when they explicitly need 32-bit (float) precision compilation.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.LLVMBuilderContext
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
    def create_llvm_builder_context(args: dict[str, Any] | None = None) -> Any:
        "Call this tool only when you need to explicitly instantiate a new LLVM IR code generation context for PsyNeuLink's compiled execution backend — for example, when initializing a custom compilation pipeline with non-default floating-point precision."
        return _impl(args or {})
