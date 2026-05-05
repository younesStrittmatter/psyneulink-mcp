"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '9e1715c1248fe793bc2a9a6d57911b460a32ae8a560a7c6415e2b64a8b22e7a0'
__pnl_qualname__ = 'psyneulink.OptimizationFunction'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_optimization_function'
TOOL_DESCRIPTION = 'Use this tool only when you need a placeholder OptimizationFunction instance to pass into a Component constructor before the actual objective/search functions are available — the instance can be fully configured later via its `reset()` method. Do NOT call this expecting a working optimizer: `OptimizationFunction._function` raises `NotImplementedError` by design; use subclass tools (`GridSearch`, `GradientOptimization`) for actual optimization. Returns an `OptimizationFunction` object configured with the serializable parameters below; callable arguments (objective_function, search_function, etc.) must be wired in Python after construction.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "max_iterations": {\n      "description": "Maximum number of optimization iterations before the process halts with a warning and returns the last sample. Default 1000.",\n      "minimum": 1,\n      "type": "integer"\n    },\n    "randomization_dimension": {\n      "description": "Index into search_space whose SampleIterator provides random seeds for num_estimates-based averaging. Set only when multiple stochastic estimates per sample are required.",\n      "minimum": 0,\n      "type": "integer"\n    },\n    "save_samples": {\n      "default": false,\n      "description": "If true, all samples evaluated during the optimization process are saved and returned. Default false.",\n      "type": "boolean"\n    },\n    "save_values": {\n      "default": false,\n      "description": "If true, the objective_function value for every evaluated sample is saved and returned. Default false.",\n      "type": "boolean"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\nCallable parameters — objective_function, search_function, search_termination_function, aggregation_function — cannot be serialized as JSON and therefore cannot be passed through this tool; they must be assigned via Python after construction (using `reset()`) or by subclass. Omitting them triggers a runtime warning on first evaluation but does not crash construction. search_space requires SampleIterator objects and is similarly non-serializable here. The randomization_dimension entry in search_space is automatically moved to the last position by the constructor if both search_space and randomization_dimension are provided. Passing NotImplemented (not None) for any unneeded callable argument suppresses the "using default" warning without disabling the parameter.'
TOOL_PARAMETERS = { 'properties': { 'max_iterations': { 'description': 'Maximum number of optimization '
                                                     'iterations before the process '
                                                     'halts with a warning and returns '
                                                     'the last sample. Default 1000.',
                                      'minimum': 1,
                                      'type': 'integer'},
                  'randomization_dimension': { 'description': 'Index into search_space '
                                                              'whose SampleIterator '
                                                              'provides random seeds '
                                                              'for num_estimates-based '
                                                              'averaging. Set only '
                                                              'when multiple '
                                                              'stochastic estimates '
                                                              'per sample are '
                                                              'required.',
                                               'minimum': 0,
                                               'type': 'integer'},
                  'save_samples': { 'default': False,
                                    'description': 'If true, all samples evaluated '
                                                   'during the optimization process '
                                                   'are saved and returned. Default '
                                                   'false.',
                                    'type': 'boolean'},
                  'save_values': { 'default': False,
                                   'description': 'If true, the objective_function '
                                                  'value for every evaluated sample is '
                                                  'saved and returned. Default false.',
                                   'type': 'boolean'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = 'Callable parameters — objective_function, search_function, search_termination_function, aggregation_function — cannot be serialized as JSON and therefore cannot be passed through this tool; they must be assigned via Python after construction (using `reset()`) or by subclass. Omitting them triggers a runtime warning on first evaluation but does not crash construction. search_space requires SampleIterator objects and is similarly non-serializable here. The randomization_dimension entry in search_space is automatically moved to the last position by the constructor if both search_space and randomization_dimension are provided. Passing NotImplemented (not None) for any unneeded callable argument suppresses the "using default" warning without disabling the parameter.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.OptimizationFunction
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
    def create_optimization_function(args: dict[str, Any] | None = None) -> Any:
        'Use this tool only when you need a placeholder OptimizationFunction instance to pass into a Component constructor before the actual objective/search functions are available — the instance can be fully configured later via its `reset()` method.'
        return _impl(args or {})
