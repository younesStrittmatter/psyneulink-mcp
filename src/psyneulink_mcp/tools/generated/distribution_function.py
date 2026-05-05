"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = 'ed8869eb79331cd1e4a1e06cf05324dab7a2c3ef444e6e94c29eac82f49e897a'
__pnl_qualname__ = 'psyneulink.DistributionFunction'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_distribution_function'
TOOL_DESCRIPTION = 'Call this tool to instantiate a PsyNeuLink DistributionFunction base class, which serves as the abstract parent for all distribution-based functions (e.g., NormalDist, UniformDist, GammaDist). Use it when you need to assign a stochastic sampling function to a Mechanism\'s noise or function parameter and want to reference the base type — in practice, call a concrete subclass tool instead unless you are introspecting the class hierarchy or building a generic wrapper.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "name": {\n      "description": "Name for this Function instance. If omitted, a default is assigned by FunctionRegistry.",\n      "type": "string"\n    },\n    "owner": {\n      "description": "Name of the PsyNeuLink Component to assign this Function to.",\n      "type": "string"\n    },\n    "params": {\n      "description": "Parameter dictionary overriding constructor argument values. Keys are parameter names, values are parameter values.",\n      "type": "object"\n    },\n    "variable": {\n      "description": "Format and default value for the input to the function. Determines the shape of values the function will operate on.",\n      "items": {\n        "type": "number"\n      },\n      "type": "array"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\nDistributionFunction is abstract — instantiating it directly will raise an error or produce a non-functional object. Always use a concrete subclass (NormalDist, UniformDist, GammaDist, ExponentialDist, etc.) in modeling workflows. The `prefs` parameter is omitted from the schema because passing raw PreferenceSet objects via JSON is not practical; leave it unset to use class defaults. The `variable` shape is stored in MDF export via `as_mdf_model`; if you later export to MDF, ensure the variable shape matches what the owning Mechanism expects.'
TOOL_PARAMETERS = { 'properties': { 'name': { 'description': 'Name for this Function instance. If '
                                           'omitted, a default is assigned by '
                                           'FunctionRegistry.',
                            'type': 'string'},
                  'owner': { 'description': 'Name of the PsyNeuLink Component to '
                                            'assign this Function to.',
                             'type': 'string'},
                  'params': { 'description': 'Parameter dictionary overriding '
                                             'constructor argument values. Keys are '
                                             'parameter names, values are parameter '
                                             'values.',
                              'type': 'object'},
                  'variable': { 'description': 'Format and default value for the input '
                                               'to the function. Determines the shape '
                                               'of values the function will operate '
                                               'on.',
                                'items': {'type': 'number'},
                                'type': 'array'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = 'DistributionFunction is abstract — instantiating it directly will raise an error or produce a non-functional object. Always use a concrete subclass (NormalDist, UniformDist, GammaDist, ExponentialDist, etc.) in modeling workflows. The `prefs` parameter is omitted from the schema because passing raw PreferenceSet objects via JSON is not practical; leave it unset to use class defaults. The `variable` shape is stored in MDF export via `as_mdf_model`; if you later export to MDF, ensure the variable shape matches what the owning Mechanism expects.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.DistributionFunction
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
    def create_distribution_function(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to instantiate a PsyNeuLink DistributionFunction base class, which serves as the abstract parent for all distribution-based functions (e.g., NormalDist, UniformDist, GammaDist).'
        return _impl(args or {})
