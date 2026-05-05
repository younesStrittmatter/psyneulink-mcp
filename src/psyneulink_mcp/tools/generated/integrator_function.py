"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '8a17d1e7ef745b7ec20cf5925290acde573cbabda2806b3a7aa26ce0cc966916'
__pnl_qualname__ = 'psyneulink.IntegratorFunction'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_integrator_function'
TOOL_DESCRIPTION = 'Call this tool to instantiate a base IntegratorFunction that integrates a variable over time by accumulating its value with a prior state. Use this when you need the abstract integrator base class — prefer a concrete subclass (e.g., SimpleIntegrator, AdaptiveIntegrator, DriftDiffusionIntegrator) for actual modeling; use IntegratorFunction directly only to inspect defaults or as a type reference. Returns a configured IntegratorFunction object; calling it will raise an error since _function is not implemented.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "default_variable": {\n      "description": "Template for the value to be integrated. If an array, each element is integrated independently. Determines the shape expected on every call.",\n      "type": [\n        "number",\n        "array"\n      ]\n    },\n    "initializer": {\n      "description": "Starting value(s) for integration; sets previous_value before the first execution. Must match length of default_variable if an array. Defaults to 0.0.",\n      "oneOf": [\n        {\n          "type": "number"\n        },\n        {\n          "items": {\n            "type": "number"\n          },\n          "type": "array"\n        }\n      ]\n    },\n    "name": {\n      "description": "Optional name for this function instance. Defaults to a registry-assigned name if omitted.",\n      "type": "string"\n    },\n    "noise": {\n      "description": "Offset added to the integral on each execution. Use a DistributionFunction (passed as a string name or object) for per-execution random noise. Default: 0.0.",\n      "oneOf": [\n        {\n          "type": "number"\n        },\n        {\n          "items": {\n            "type": "number"\n          },\n          "type": "array"\n        }\n      ]\n    },\n    "rate": {\n      "description": "Rate of integration applied to the variable. A scalar applies uniformly; an array applies elementwise and must match the length of default_variable. Default: 1.0.",\n      "oneOf": [\n        {\n          "type": "number"\n        },\n        {\n          "items": {\n            "type": "number"\n          },\n          "type": "array"\n        }\n      ]\n    },\n    "time_step_size": {\n      "description": "Timing precision of the integration process. Relevant for subclasses that implement continuous-time dynamics. Default: 1.0.",\n      "type": "number"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\nIntegratorFunction is an abstract base class — its _function raises FunctionError if called directly. Always prefer a concrete subclass for actual computation. When any parameter (rate, noise, initializer) is specified as an array with length > 1, all such array parameters must share the same length, and default_variable (if not user-specified) will be inferred to match that length. If default_variable is user-specified, array parameters must match its innermost dimension length. A scalar parameter applies uniformly across all elements; an array parameter applies elementwise (Hadamard). For random noise that varies per execution and per element, pass a DistributionFunction — a float noise value is a fixed offset identical across all executions.'
TOOL_PARAMETERS = { 'properties': { 'default_variable': { 'description': 'Template for the value to be '
                                                       'integrated. If an array, each '
                                                       'element is integrated '
                                                       'independently. Determines the '
                                                       'shape expected on every call.',
                                        'type': ['number', 'array']},
                  'initializer': { 'description': 'Starting value(s) for integration; '
                                                  'sets previous_value before the '
                                                  'first execution. Must match length '
                                                  'of default_variable if an array. '
                                                  'Defaults to 0.0.',
                                   'oneOf': [ {'type': 'number'},
                                              { 'items': {'type': 'number'},
                                                'type': 'array'}]},
                  'name': { 'description': 'Optional name for this function instance. '
                                           'Defaults to a registry-assigned name if '
                                           'omitted.',
                            'type': 'string'},
                  'noise': { 'description': 'Offset added to the integral on each '
                                            'execution. Use a DistributionFunction '
                                            '(passed as a string name or object) for '
                                            'per-execution random noise. Default: 0.0.',
                             'oneOf': [ {'type': 'number'},
                                        { 'items': {'type': 'number'},
                                          'type': 'array'}]},
                  'rate': { 'description': 'Rate of integration applied to the '
                                           'variable. A scalar applies uniformly; an '
                                           'array applies elementwise and must match '
                                           'the length of default_variable. Default: '
                                           '1.0.',
                            'oneOf': [ {'type': 'number'},
                                       {'items': {'type': 'number'}, 'type': 'array'}]},
                  'time_step_size': { 'description': 'Timing precision of the '
                                                     'integration process. Relevant '
                                                     'for subclasses that implement '
                                                     'continuous-time dynamics. '
                                                     'Default: 1.0.',
                                      'type': 'number'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = 'IntegratorFunction is an abstract base class — its _function raises FunctionError if called directly. Always prefer a concrete subclass for actual computation. When any parameter (rate, noise, initializer) is specified as an array with length > 1, all such array parameters must share the same length, and default_variable (if not user-specified) will be inferred to match that length. If default_variable is user-specified, array parameters must match its innermost dimension length. A scalar parameter applies uniformly across all elements; an array parameter applies elementwise (Hadamard). For random noise that varies per execution and per element, pass a DistributionFunction — a float noise value is a fixed offset identical across all executions.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.IntegratorFunction
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
    def create_integrator_function(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to instantiate a base IntegratorFunction that integrates a variable over time by accumulating its value with a prior state.'
        return _impl(args or {})
