"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '733dcbe9fbc21126fc34fab1ba389b5a7640f1b50afdc92a48a6926a99fba394'
__pnl_qualname__ = 'psyneulink.UserDefinedFunction'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_user_defined_function'
TOOL_DESCRIPTION = 'Use this tool to create a UserDefinedFunction that wraps a custom computation as a PsyNeuLink Function, suitable for assigning to a Mechanism, Projection, InputPort, or OutputPort via its `function` parameter. Pass `custom_function` as a string expression (e.g., `"amplitude * variable[0] + bias"`) referencing `variable` as the 2d-array input; any other names in the expression become modulation-capable parameters. Returns a UserDefinedFunction instance ready to pass as `function=` to any Component constructor.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "custom_function": {\n      "description": "A string expression to evaluate as the custom computation. Use `variable` to refer to the input (always a 2d numpy array, access rows via variable[0], variable[1], etc.). Any other identifiers become named parameters that can be modulated by ControlSignals. Example: \\"amplitude * np.sin(2 * np.pi * variable[0] + phase)\\".",\n      "type": "string"\n    },\n    "default_variable": {\n      "description": "Default value and shape for the input variable, expressed as a 2d array (list of lists). Must be compatible with the Component\'s variable format. If omitted, inferred from the function\'s first argument default.",\n      "items": {\n        "items": {\n          "type": "number"\n        },\n        "type": "array"\n      },\n      "type": "array"\n    },\n    "name": {\n      "description": "Name for this UserDefinedFunction instance. If omitted, a default is assigned by FunctionRegistry.",\n      "type": "string"\n    },\n    "params": {\n      "additionalProperties": true,\n      "description": "Parameter specification dictionary. Use to designate ADDITIVE_PARAM and/or MULTIPLICATIVE_PARAM for GatingSignal modulation when the UDF is assigned to an InputPort or OutputPort. Example: {\\"ADDITIVE_PARAM\\": \\"bias\\", \\"MULTIPLICATIVE_PARAM\\": \\"amplitude\\"}.",\n      "type": "object"\n    }\n  },\n  "required": [\n    "custom_function"\n  ],\n  "type": "object"\n}\n\nNotes:\n- `custom_function` cannot be None; omitting it raises FunctionError.\n- In MCP context, only string expressions are supported for `custom_function` (Python callables cannot be serialized over MCP). String expressions are evaluated with `eval()` and have limited flexibility compared to named Python functions.\n- The input `variable` is always passed as a 2d numpy array regardless of how the Component\'s `input_shapes` is defined; index rows as `variable[0]`, `variable[1]`, etc.\n- Any additional keyword arguments beyond the documented parameters (e.g., `amplitude=1.0`, `phase=0`) are treated as default values for custom parameters identified in the string expression. Pass them as extra kwargs if you want non-zero defaults.\n- String expressions support numpy via `np.*` but not arbitrary imports; built-in Python functions like `sum` are available.\n- For gating (ADDITIVE/MULTIPLICATIVE modulation), the `params` dict entries must use the exact PNL string constants `"ADDITIVE_PARAM"` and `"MULTIPLICATIVE_PARAM"` as keys.\n- Compiled execution (`ExecutionMode.LLVMRun`) does NOT support lambda functions, loops, dicts, nested functions, closures, or most libraries—only NumPy arrays and `exp`/`tanh` are supported in compiled mode.\n- `default_variable` must be specified as a 2d structure (list of lists); a flat 1d list will be rejected or misinterpreted by downstream Components that expect 2d variables.'
TOOL_PARAMETERS = { 'properties': { 'custom_function': { 'description': 'A string expression to evaluate '
                                                      'as the custom computation. Use '
                                                      '`variable` to refer to the '
                                                      'input (always a 2d numpy array, '
                                                      'access rows via variable[0], '
                                                      'variable[1], etc.). Any other '
                                                      'identifiers become named '
                                                      'parameters that can be '
                                                      'modulated by ControlSignals. '
                                                      'Example: "amplitude * np.sin(2 '
                                                      '* np.pi * variable[0] + '
                                                      'phase)".',
                                       'type': 'string'},
                  'default_variable': { 'description': 'Default value and shape for '
                                                       'the input variable, expressed '
                                                       'as a 2d array (list of lists). '
                                                       'Must be compatible with the '
                                                       "Component's variable format. "
                                                       'If omitted, inferred from the '
                                                       "function's first argument "
                                                       'default.',
                                        'items': { 'items': {'type': 'number'},
                                                   'type': 'array'},
                                        'type': 'array'},
                  'name': { 'description': 'Name for this UserDefinedFunction '
                                           'instance. If omitted, a default is '
                                           'assigned by FunctionRegistry.',
                            'type': 'string'},
                  'params': { 'additionalProperties': True,
                              'description': 'Parameter specification dictionary. Use '
                                             'to designate ADDITIVE_PARAM and/or '
                                             'MULTIPLICATIVE_PARAM for GatingSignal '
                                             'modulation when the UDF is assigned to '
                                             'an InputPort or OutputPort. Example: '
                                             '{"ADDITIVE_PARAM": "bias", '
                                             '"MULTIPLICATIVE_PARAM": "amplitude"}.',
                              'type': 'object'}},
  'required': ['custom_function'],
  'type': 'object'}
TOOL_NOTES = '- `custom_function` cannot be None; omitting it raises FunctionError.\n- In MCP context, only string expressions are supported for `custom_function` (Python callables cannot be serialized over MCP). String expressions are evaluated with `eval()` and have limited flexibility compared to named Python functions.\n- The input `variable` is always passed as a 2d numpy array regardless of how the Component\'s `input_shapes` is defined; index rows as `variable[0]`, `variable[1]`, etc.\n- Any additional keyword arguments beyond the documented parameters (e.g., `amplitude=1.0`, `phase=0`) are treated as default values for custom parameters identified in the string expression. Pass them as extra kwargs if you want non-zero defaults.\n- String expressions support numpy via `np.*` but not arbitrary imports; built-in Python functions like `sum` are available.\n- For gating (ADDITIVE/MULTIPLICATIVE modulation), the `params` dict entries must use the exact PNL string constants `"ADDITIVE_PARAM"` and `"MULTIPLICATIVE_PARAM"` as keys.\n- Compiled execution (`ExecutionMode.LLVMRun`) does NOT support lambda functions, loops, dicts, nested functions, closures, or most libraries—only NumPy arrays and `exp`/`tanh` are supported in compiled mode.\n- `default_variable` must be specified as a 2d structure (list of lists); a flat 1d list will be rejected or misinterpreted by downstream Components that expect 2d variables.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.UserDefinedFunction
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
    def create_user_defined_function(args: dict[str, Any] | None = None) -> Any:
        'Use this tool to create a UserDefinedFunction that wraps a custom computation as a PsyNeuLink Function, suitable for assigning to a Mechanism, Projection, InputPort, or OutputPort via its `function` parameter.'
        return _impl(args or {})
