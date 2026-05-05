"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = 'b60e1cca9be70ea38c543d8b7eefec036bbb8ce0fbb6dd9167ebf0b0b56878c7'
__pnl_qualname__ = 'psyneulink.ParameterPort'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_parameter_port'
TOOL_DESCRIPTION = 'Call this tool to explicitly inspect or reference a ParameterPort that mediates how a Mechanism or MappingProjection parameter gets its effective value — particularly when you need to attach a ControlProjection or LearningProjection to modulate a parameter at runtime. ParameterPorts are normally auto-created during Mechanism/Projection construction; invoke this tool only when you need to construct one explicitly to inspect its metadata or pass it to a projection spec. Returns a ParameterPort object whose `.value` reflects the parameter\'s effective (possibly modulated) value.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "function": {\n      "description": "Function used to compute the ParameterPort\'s effective value from its variable under modulatory influence. Default is LinearCombination(operation=PRODUCT). Specify as a PsyNeuLink function expression string.",\n      "type": "string"\n    },\n    "name": {\n      "description": "Optional name for the ParameterPort. If omitted, PsyNeuLink assigns one automatically based on the parameter name.",\n      "type": "string"\n    },\n    "owner": {\n      "description": "Name of the Mechanism or MappingProjection to which this ParameterPort belongs. Must already be instantiated. For a function parameter, specify the Mechanism or Projection that owns the function, not the function itself.",\n      "type": "string"\n    },\n    "parameter_name": {\n      "description": "Name of the parameter on the owner (or its function) that this ParameterPort represents.",\n      "type": "string"\n    },\n    "projections": {\n      "description": "ControlProjection(s) or LearningProjection(s) to assign as modulatory afferents. PathwayProjections and GatingProjections are explicitly forbidden and will raise an error.",\n      "items": {\n        "type": "string"\n      },\n      "type": "array"\n    },\n    "reference_value": {\n      "description": "Default value of the parameter this ParameterPort is responsible for. Must be compatible in format (shape/dtype) with the parameter\'s expected value. Accepts a scalar, list, or array.",\n      "oneOf": [\n        {\n          "type": "number"\n        },\n        {\n          "items": {\n            "type": "number"\n          },\n          "type": "array"\n        }\n      ]\n    },\n    "variable": {\n      "description": "Initial value of the parameter attribute on the owner or its function. Sets the ParameterPort\'s starting variable. Accepts a scalar, list, or array.",\n      "oneOf": [\n        {\n          "type": "number"\n        },\n        {\n          "items": {\n            "type": "number"\n          },\n          "type": "array"\n        }\n      ]\n    }\n  },\n  "required": [\n    "owner"\n  ],\n  "type": "object"\n}\n\nNotes:\nParameterPort.__init__ raises ParameterPortError if called without a proper internal context — it cannot be constructed standalone via a direct constructor call in normal user code. ParameterPorts are auto-created for every tunable parameter when a Mechanism or Projection is instantiated; prefer accessing them via `owner.parameter_ports[\'param_name\']` rather than constructing them directly. Only ControlProjections and LearningProjections may be passed as `projections`; GatingProjections and PathwayProjections raise PortError. The docstring and signature disagree on the default function operation (SUM vs PRODUCT); the actual runtime default is Linear (identity), not LinearCombination. `.value` may differ from the owner\'s raw parameter attribute if modulatory projections are active.'
TOOL_PARAMETERS = { 'properties': { 'function': { 'description': 'Function used to compute the '
                                               "ParameterPort's effective value from "
                                               'its variable under modulatory '
                                               'influence. Default is '
                                               'LinearCombination(operation=PRODUCT). '
                                               'Specify as a PsyNeuLink function '
                                               'expression string.',
                                'type': 'string'},
                  'name': { 'description': 'Optional name for the ParameterPort. If '
                                           'omitted, PsyNeuLink assigns one '
                                           'automatically based on the parameter name.',
                            'type': 'string'},
                  'owner': { 'description': 'Name of the Mechanism or '
                                            'MappingProjection to which this '
                                            'ParameterPort belongs. Must already be '
                                            'instantiated. For a function parameter, '
                                            'specify the Mechanism or Projection that '
                                            'owns the function, not the function '
                                            'itself.',
                             'type': 'string'},
                  'parameter_name': { 'description': 'Name of the parameter on the '
                                                     'owner (or its function) that '
                                                     'this ParameterPort represents.',
                                      'type': 'string'},
                  'projections': { 'description': 'ControlProjection(s) or '
                                                  'LearningProjection(s) to assign as '
                                                  'modulatory afferents. '
                                                  'PathwayProjections and '
                                                  'GatingProjections are explicitly '
                                                  'forbidden and will raise an error.',
                                   'items': {'type': 'string'},
                                   'type': 'array'},
                  'reference_value': { 'description': 'Default value of the parameter '
                                                      'this ParameterPort is '
                                                      'responsible for. Must be '
                                                      'compatible in format '
                                                      '(shape/dtype) with the '
                                                      "parameter's expected value. "
                                                      'Accepts a scalar, list, or '
                                                      'array.',
                                       'oneOf': [ {'type': 'number'},
                                                  { 'items': {'type': 'number'},
                                                    'type': 'array'}]},
                  'variable': { 'description': 'Initial value of the parameter '
                                               'attribute on the owner or its '
                                               "function. Sets the ParameterPort's "
                                               'starting variable. Accepts a scalar, '
                                               'list, or array.',
                                'oneOf': [ {'type': 'number'},
                                           { 'items': {'type': 'number'},
                                             'type': 'array'}]}},
  'required': ['owner'],
  'type': 'object'}
TOOL_NOTES = "ParameterPort.__init__ raises ParameterPortError if called without a proper internal context — it cannot be constructed standalone via a direct constructor call in normal user code. ParameterPorts are auto-created for every tunable parameter when a Mechanism or Projection is instantiated; prefer accessing them via `owner.parameter_ports['param_name']` rather than constructing them directly. Only ControlProjections and LearningProjections may be passed as `projections`; GatingProjections and PathwayProjections raise PortError. The docstring and signature disagree on the default function operation (SUM vs PRODUCT); the actual runtime default is Linear (identity), not LinearCombination. `.value` may differ from the owner's raw parameter attribute if modulatory projections are active."


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.ParameterPort
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
    def create_parameter_port(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to explicitly inspect or reference a ParameterPort that mediates how a Mechanism or MappingProjection parameter gets its effective value — particularly when you need to attach a ControlProjection or LearningProjection to modulate a parameter at runtime.'
        return _impl(args or {})
