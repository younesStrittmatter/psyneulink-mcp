"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '99b0f0228a057b8eea03d3ea31279dc458f03ea78c4370df10da502b39c1085c'
__pnl_qualname__ = 'psyneulink.SampleSpec'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_sample_spec'
TOOL_DESCRIPTION = 'Call this tool to define a sampling specification for PsyNeuLink components that accept SampleIterators — primarily OptimizationFunctions (e.g., GridSearch, GaussianProcess). Use it to produce arange-style sequences (start/stop/step), linspace-style sequences (start/stop/num), function-driven samplers (function + optional num), or pass-through custom specs. The returned SampleSpec is consumed by components expecting a SampleIterator specification.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "num": {\n      "description": "Number of samples. With start/stop produces linspace-style evenly-spaced values; with function limits how many times the function is called. Must be compatible with step when both are given.",\n      "type": "integer"\n    },\n    "precision": {\n      "description": "Decimal places used for floating-point rounding when computing num or step. Defaults to 16 (SAMPLE_SPEC_PRECISION).",\n      "type": "integer"\n    },\n    "start": {\n      "description": "First sample value. Required when function is not provided.",\n      "type": "number"\n    },\n    "step": {\n      "description": "Spacing between consecutive samples (arange-style). Mutually exclusive with function. If start/stop/step are all given, num is derived automatically.",\n      "type": "number"\n    },\n    "stop": {\n      "description": "Upper bound (inclusive limit) of the sequence. Required when function is not provided.",\n      "type": "number"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\nThree mutually exclusive modes: (1) range — provide start, stop, and either step or num (not both unless they agree); (2) function — provide a Python callable via the function argument, which cannot be expressed in JSON and is therefore omitted from this schema; (3) custom_spec — an opaque value forwarded to SampleIterator unchanged, also omitted because it requires receiver-specific knowledge. If start/stop/step are floats, precision governs rounding when deriving num; mismatched step+num raises SampleIteratorError at construction time. Some OptimizationFunctions require a SampleSpec with a non-None num; always set num when targeting those components. The function and custom_spec arguments cannot be passed through a standard MCP JSON payload — use the Python API directly for those modes.'
TOOL_PARAMETERS = { 'properties': { 'num': { 'description': 'Number of samples. With start/stop produces '
                                          'linspace-style evenly-spaced values; with '
                                          'function limits how many times the function '
                                          'is called. Must be compatible with step '
                                          'when both are given.',
                           'type': 'integer'},
                  'precision': { 'description': 'Decimal places used for '
                                                'floating-point rounding when '
                                                'computing num or step. Defaults to 16 '
                                                '(SAMPLE_SPEC_PRECISION).',
                                 'type': 'integer'},
                  'start': { 'description': 'First sample value. Required when '
                                            'function is not provided.',
                             'type': 'number'},
                  'step': { 'description': 'Spacing between consecutive samples '
                                           '(arange-style). Mutually exclusive with '
                                           'function. If start/stop/step are all '
                                           'given, num is derived automatically.',
                            'type': 'number'},
                  'stop': { 'description': 'Upper bound (inclusive limit) of the '
                                           'sequence. Required when function is not '
                                           'provided.',
                            'type': 'number'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = 'Three mutually exclusive modes: (1) range — provide start, stop, and either step or num (not both unless they agree); (2) function — provide a Python callable via the function argument, which cannot be expressed in JSON and is therefore omitted from this schema; (3) custom_spec — an opaque value forwarded to SampleIterator unchanged, also omitted because it requires receiver-specific knowledge. If start/stop/step are floats, precision governs rounding when deriving num; mismatched step+num raises SampleIteratorError at construction time. Some OptimizationFunctions require a SampleSpec with a non-None num; always set num when targeting those components. The function and custom_spec arguments cannot be passed through a standard MCP JSON payload — use the Python API directly for those modes.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.SampleSpec
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
    def create_sample_spec(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to define a sampling specification for PsyNeuLink components that accept SampleIterators — primarily OptimizationFunctions (e.g., GridSearch, GaussianProcess).'
        return _impl(args or {})
