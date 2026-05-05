"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = 'b49d4a3b9b27486e488e3eb62eb3a9313fc20a2170b37eebb6b79b803fa7dedb'
__pnl_qualname__ = 'psyneulink.StatefulFunction'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_stateful_function'
TOOL_DESCRIPTION = 'Call this tool to instantiate a StatefulFunction — an abstract base class for PsyNeuLink functions whose output depends on accumulated state (previous_value). Do NOT call this directly; it is abstract and will raise a FunctionError. Use it only as a conceptual reference or as a base when configuring subclasses (IntegratorFunction, AdaptiveIntegratorFunction, etc.). The result of a concrete subclass invocation is a stateful function object that tracks previous_value across calls.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "default_variable": {\n      "description": "Template defining the shape/type of the input. Accepts a number or 1d array. Sets the expected input dimensionality for rate and noise validation.",\n      "oneOf": [\n        {\n          "type": "number"\n        },\n        {\n          "items": {\n            "type": "number"\n          },\n          "type": "array"\n        }\n      ]\n    },\n    "initializer": {\n      "description": "Initial value for previous_value. Must be a float or 1d array matching the length of default_variable. Default is 0.0.",\n      "oneOf": [\n        {\n          "type": "number"\n        },\n        {\n          "items": {\n            "type": "number"\n          },\n          "type": "array"\n        }\n      ]\n    },\n    "name": {\n      "description": "Optional name for this function instance. Auto-assigned from FunctionRegistry if omitted.",\n      "type": "string"\n    },\n    "noise": {\n      "default": 0,\n      "description": "Offset added on each call. Float = static offset (same every execution). For truly random noise, pass a DistributionFunction object by name/reference. Array must match length of default_variable. Default 0.0.",\n      "oneOf": [\n        {\n          "type": "number"\n        },\n        {\n          "items": {\n            "type": "number"\n          },\n          "type": "array"\n        }\n      ]\n    },\n    "rate": {\n      "default": 1,\n      "description": "Scaling parameter applied on each call in a subclass-dependent way. Float or 1d array; array length must match default_variable. Default 1.0.",\n      "oneOf": [\n        {\n          "type": "number"\n        },\n        {\n          "items": {\n            "type": "number"\n          },\n          "type": "array"\n        }\n      ]\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\nStatefulFunction is abstract — _function raises FunctionError by design. Instantiating psyneulink.StatefulFunction directly will fail. Use a concrete subclass (e.g., SimpleIntegrator, AdaptiveIntegrator, DriftDiffusionIntegrator). If noise is a float or fixed array it is a static offset, not stochastic; wrap in a DistributionFunction for per-execution randomness. A ParameterPort for noise is only created if noise is fully numeric at construction time. Rate array length must equal the size of default_variable or be length 1; mismatches raise FunctionError unless variable shape is FLEXIBLE. The initializer parameter (singular) seeds previous_value; the initializers attribute (plural, list) names all initialization attributes for subclasses with multiple stateful attributes.'
TOOL_PARAMETERS = { 'properties': { 'default_variable': { 'description': 'Template defining the '
                                                       'shape/type of the input. '
                                                       'Accepts a number or 1d array. '
                                                       'Sets the expected input '
                                                       'dimensionality for rate and '
                                                       'noise validation.',
                                        'oneOf': [ {'type': 'number'},
                                                   { 'items': {'type': 'number'},
                                                     'type': 'array'}]},
                  'initializer': { 'description': 'Initial value for previous_value. '
                                                  'Must be a float or 1d array '
                                                  'matching the length of '
                                                  'default_variable. Default is 0.0.',
                                   'oneOf': [ {'type': 'number'},
                                              { 'items': {'type': 'number'},
                                                'type': 'array'}]},
                  'name': { 'description': 'Optional name for this function instance. '
                                           'Auto-assigned from FunctionRegistry if '
                                           'omitted.',
                            'type': 'string'},
                  'noise': { 'default': 0,
                             'description': 'Offset added on each call. Float = static '
                                            'offset (same every execution). For truly '
                                            'random noise, pass a DistributionFunction '
                                            'object by name/reference. Array must '
                                            'match length of default_variable. Default '
                                            '0.0.',
                             'oneOf': [ {'type': 'number'},
                                        { 'items': {'type': 'number'},
                                          'type': 'array'}]},
                  'rate': { 'default': 1,
                            'description': 'Scaling parameter applied on each call in '
                                           'a subclass-dependent way. Float or 1d '
                                           'array; array length must match '
                                           'default_variable. Default 1.0.',
                            'oneOf': [ {'type': 'number'},
                                       { 'items': {'type': 'number'},
                                         'type': 'array'}]}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = 'StatefulFunction is abstract — _function raises FunctionError by design. Instantiating psyneulink.StatefulFunction directly will fail. Use a concrete subclass (e.g., SimpleIntegrator, AdaptiveIntegrator, DriftDiffusionIntegrator). If noise is a float or fixed array it is a static offset, not stochastic; wrap in a DistributionFunction for per-execution randomness. A ParameterPort for noise is only created if noise is fully numeric at construction time. Rate array length must equal the size of default_variable or be length 1; mismatches raise FunctionError unless variable shape is FLEXIBLE. The initializer parameter (singular) seeds previous_value; the initializers attribute (plural, list) names all initialization attributes for subclasses with multiple stateful attributes.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.StatefulFunction
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
    def create_stateful_function(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to instantiate a StatefulFunction — an abstract base class for PsyNeuLink functions whose output depends on accumulated state (previous_value).'
        return _impl(args or {})
