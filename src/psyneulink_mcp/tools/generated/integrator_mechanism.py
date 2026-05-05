"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = 'ebe64c85e51b68a589479e72b66c9ae55b7b24730b47a384e3dba712b8eba1d6'
__pnl_qualname__ = 'psyneulink.IntegratorMechanism'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_integrator_mechanism'
TOOL_DESCRIPTION = 'Call this tool to create an IntegratorMechanism node for use in a PsyNeuLink Composition when you need a processing unit that accumulates or integrates its input over time. Use it when building models that require temporal integration (e.g., evidence accumulation, leaky integration, drift-diffusion). Returns an IntegratorMechanism instance whose output reflects the integrated history of its inputs via the specified IntegratorFunction.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "default_variable": {\n      "description": "Default input value. Sets the dimensionality of the mechanism\'s input. If omitted, inferred from function variable shape.",\n      "items": {\n        "type": "number"\n      },\n      "type": "array"\n    },\n    "function": {\n      "description": "Name of an IntegratorFunction to use (e.g., \'AdaptiveIntegrator\', \'SimpleIntegrator\', \'DriftDiffusionIntegrator\'). Default is AdaptiveIntegrator with rate=0.5. Must be an IntegratorFunction subclass.",\n      "type": "string"\n    },\n    "input_ports": {\n      "description": "List of input port names or specifications. Typically omitted; use default_variable or input_shapes to set dimensionality instead.",\n      "items": {\n        "type": "string"\n      },\n      "type": "array"\n    },\n    "input_shapes": {\n      "description": "Scalar integer specifying the length of the input vector, as an alternative to default_variable.",\n      "type": "integer"\n    },\n    "name": {\n      "description": "Name for this IntegratorMechanism instance. Used to identify it in Compositions and logs.",\n      "type": "string"\n    },\n    "output_ports": {\n      "description": "List of output port names or specifications. Defaults to a single output port exposing the integrated value.",\n      "items": {\n        "type": "string"\n      },\n      "type": "array"\n    },\n    "reset_default": {\n      "description": "Default value to which the mechanism resets when its reset parameter is non-zero. Scalar or array matching input dimensionality. Default is 0.",\n      "oneOf": [\n        {\n          "type": "number"\n        },\n        {\n          "items": {\n            "type": "number"\n          },\n          "type": "array"\n        }\n      ]\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\n- The `function` parameter must be an IntegratorFunction subclass (not a generic Function). Passing a non-integrator function raises an error.\n- If `default_variable` length is 1 but the specified function\'s variable is longer, the mechanism automatically reshapes to match the function — no error is raised in this case.\n- `reset_default` sets the *default* reset target value; it does not trigger a reset on construction unless it is non-zero (which would cause a reset during initialization).\n- The `reset` attribute (not a constructor arg) is modulable at runtime — setting it to a non-zero value via a ControlSignal will trigger a reset on the next execution.\n- `input_shapes` accepts a scalar int; for multi-dimensional inputs use `default_variable` instead.\n- When passing `function` as a string in this MCP tool, the host template is expected to resolve it; if passing a pre-instantiated function object is needed, check whether the host supports object-valued parameters.'
TOOL_PARAMETERS = { 'properties': { 'default_variable': { 'description': 'Default input value. Sets the '
                                                       'dimensionality of the '
                                                       "mechanism's input. If omitted, "
                                                       'inferred from function '
                                                       'variable shape.',
                                        'items': {'type': 'number'},
                                        'type': 'array'},
                  'function': { 'description': 'Name of an IntegratorFunction to use '
                                               "(e.g., 'AdaptiveIntegrator', "
                                               "'SimpleIntegrator', "
                                               "'DriftDiffusionIntegrator'). Default "
                                               'is AdaptiveIntegrator with rate=0.5. '
                                               'Must be an IntegratorFunction '
                                               'subclass.',
                                'type': 'string'},
                  'input_ports': { 'description': 'List of input port names or '
                                                  'specifications. Typically omitted; '
                                                  'use default_variable or '
                                                  'input_shapes to set dimensionality '
                                                  'instead.',
                                   'items': {'type': 'string'},
                                   'type': 'array'},
                  'input_shapes': { 'description': 'Scalar integer specifying the '
                                                   'length of the input vector, as an '
                                                   'alternative to default_variable.',
                                    'type': 'integer'},
                  'name': { 'description': 'Name for this IntegratorMechanism '
                                           'instance. Used to identify it in '
                                           'Compositions and logs.',
                            'type': 'string'},
                  'output_ports': { 'description': 'List of output port names or '
                                                   'specifications. Defaults to a '
                                                   'single output port exposing the '
                                                   'integrated value.',
                                    'items': {'type': 'string'},
                                    'type': 'array'},
                  'reset_default': { 'description': 'Default value to which the '
                                                    'mechanism resets when its reset '
                                                    'parameter is non-zero. Scalar or '
                                                    'array matching input '
                                                    'dimensionality. Default is 0.',
                                     'oneOf': [ {'type': 'number'},
                                                { 'items': {'type': 'number'},
                                                  'type': 'array'}]}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = "- The `function` parameter must be an IntegratorFunction subclass (not a generic Function). Passing a non-integrator function raises an error.\n- If `default_variable` length is 1 but the specified function's variable is longer, the mechanism automatically reshapes to match the function — no error is raised in this case.\n- `reset_default` sets the *default* reset target value; it does not trigger a reset on construction unless it is non-zero (which would cause a reset during initialization).\n- The `reset` attribute (not a constructor arg) is modulable at runtime — setting it to a non-zero value via a ControlSignal will trigger a reset on the next execution.\n- `input_shapes` accepts a scalar int; for multi-dimensional inputs use `default_variable` instead.\n- When passing `function` as a string in this MCP tool, the host template is expected to resolve it; if passing a pre-instantiated function object is needed, check whether the host supports object-valued parameters."


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.IntegratorMechanism
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
    def create_integrator_mechanism(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to create an IntegratorMechanism node for use in a PsyNeuLink Composition when you need a processing unit that accumulates or integrates its input over time.'
        return _impl(args or {})
