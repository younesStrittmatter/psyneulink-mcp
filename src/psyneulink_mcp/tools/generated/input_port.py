"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '00be3273578f0cd302ec6eac681f1fc05ad2402709d7044d38b232dff1fefc14'
__pnl_qualname__ = 'psyneulink.InputPort'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_input_port'
TOOL_DESCRIPTION = 'Call this tool to create a standalone InputPort specification — use it when you need to configure a custom input receptor for a Mechanism with non-default aggregation, weighting, or projection wiring before attaching it via the Mechanism\'s `input_ports` argument. Returns an InputPort instance (or a deferred-init stub if no `owner` is supplied) that collects values from incoming MappingProjections, ControlProjections, or GatingProjections and combines them via a configurable function (default: element-wise sum).\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "combine": {\n      "description": "Convenience shorthand for LinearCombination\'s operation argument \\u2014 \'sum\' (default) or \'product\'. Cannot be specified if `function` is a non-LinearCombination Function, or if it conflicts with the operation already set on a LinearCombination passed to `function`.",\n      "enum": [\n        "sum",\n        "product"\n      ],\n      "type": "string"\n    },\n    "default_input": {\n      "description": "Set to \'DEFAULT_VARIABLE\' to use the InputPort\'s default variable value when no afferent Projections are active (e.g., for a bias unit). If omitted (default None), executing without afferents raises an error. Setting this automatically sets internal_only=True.",\n      "enum": [\n        "DEFAULT_VARIABLE"\n      ],\n      "type": "string"\n    },\n    "exponent": {\n      "description": "Scalar exponent applied to this InputPort\'s value when the owner Mechanism combines InputPort values. Must be an int or float. Default is None (no exponentiation).",\n      "type": "number"\n    },\n    "function": {\n      "description": "Function applied to aggregate incoming Projection values. Default is LinearCombination(operation=SUM). Must produce output with the same shape as the assigned item of the owner Mechanism\'s variable. Using a non-TransformFunction when multiple Projections are received produces a warning and only the first Projection\'s value is used.",\n      "type": "string"\n    },\n    "internal_only": {\n      "description": "If True, this InputPort does not require (or accept) external input when its Mechanism is an INPUT Node of a Composition. Automatically set True when default_input=\'DEFAULT_VARIABLE\'. Default is False.",\n      "type": "boolean"\n    },\n    "name": {\n      "description": "Name for the InputPort. If omitted, a default name is assigned by the PortRegistry of the owning Mechanism.",\n      "type": "string"\n    },\n    "projections": {\n      "description": "List of Projection specifications (MappingProjection, ControlProjection, GatingProjection) the InputPort should receive. If provided without `variable` or `input_shapes`, variable shape is inferred from the sender(s).",\n      "items": {\n        "type": "string"\n      },\n      "type": "array"\n    },\n    "reference_value": {\n      "description": "Template matching the item of the owner Mechanism\'s variable this InputPort is assigned to; used to validate the InputPort\'s value. Usually left unset when creating InputPorts inline.",\n      "type": "array"\n    },\n    "variable": {\n      "description": "Shape template for the InputPort\'s variable \\u2014 each incoming Projection\'s value must match this format. If omitted and `projections` is given, shape is inferred from the sender\'s value.",\n      "type": "array"\n    },\n    "weight": {\n      "description": "Scalar multiplier applied to this InputPort\'s value when the owner Mechanism combines InputPort values. Must be an int or float. Default is None (no weighting).",\n      "type": "number"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\nInputPort is almost always specified inline as an element of a Mechanism\'s `input_ports` argument rather than constructed standalone — standalone construction requires an `owner` or the object will be in deferred-init status and cannot be executed. The `combine` and `function` arguments must be consistent: passing both raises an error unless `function` is a LinearCombination with the same operation as `combine`. `weight` and `exponent` here apply at the Mechanism level (how its function combines the values of all InputPorts), not inside the InputPort\'s own aggregation function. Setting `default_input=\'DEFAULT_VARIABLE\'` silently forces `internal_only=True`, which excludes the Mechanism from being treated as a Composition INPUT Node. Projection values fed to the InputPort must all share the same shape as `variable`; mismatches are caught at instantiation time, not at construction.'
TOOL_PARAMETERS = { 'properties': { 'combine': { 'description': 'Convenience shorthand for '
                                              "LinearCombination's operation argument "
                                              "— 'sum' (default) or 'product'. Cannot "
                                              'be specified if `function` is a '
                                              'non-LinearCombination Function, or if '
                                              'it conflicts with the operation already '
                                              'set on a LinearCombination passed to '
                                              '`function`.',
                               'enum': ['sum', 'product'],
                               'type': 'string'},
                  'default_input': { 'description': "Set to 'DEFAULT_VARIABLE' to use "
                                                    "the InputPort's default variable "
                                                    'value when no afferent '
                                                    'Projections are active (e.g., for '
                                                    'a bias unit). If omitted (default '
                                                    'None), executing without '
                                                    'afferents raises an error. '
                                                    'Setting this automatically sets '
                                                    'internal_only=True.',
                                     'enum': ['DEFAULT_VARIABLE'],
                                     'type': 'string'},
                  'exponent': { 'description': 'Scalar exponent applied to this '
                                               "InputPort's value when the owner "
                                               'Mechanism combines InputPort values. '
                                               'Must be an int or float. Default is '
                                               'None (no exponentiation).',
                                'type': 'number'},
                  'function': { 'description': 'Function applied to aggregate incoming '
                                               'Projection values. Default is '
                                               'LinearCombination(operation=SUM). Must '
                                               'produce output with the same shape as '
                                               'the assigned item of the owner '
                                               "Mechanism's variable. Using a "
                                               'non-TransformFunction when multiple '
                                               'Projections are received produces a '
                                               'warning and only the first '
                                               "Projection's value is used.",
                                'type': 'string'},
                  'internal_only': { 'description': 'If True, this InputPort does not '
                                                    'require (or accept) external '
                                                    'input when its Mechanism is an '
                                                    'INPUT Node of a Composition. '
                                                    'Automatically set True when '
                                                    "default_input='DEFAULT_VARIABLE'. "
                                                    'Default is False.',
                                     'type': 'boolean'},
                  'name': { 'description': 'Name for the InputPort. If omitted, a '
                                           'default name is assigned by the '
                                           'PortRegistry of the owning Mechanism.',
                            'type': 'string'},
                  'projections': { 'description': 'List of Projection specifications '
                                                  '(MappingProjection, '
                                                  'ControlProjection, '
                                                  'GatingProjection) the InputPort '
                                                  'should receive. If provided without '
                                                  '`variable` or `input_shapes`, '
                                                  'variable shape is inferred from the '
                                                  'sender(s).',
                                   'items': {'type': 'string'},
                                   'type': 'array'},
                  'reference_value': { 'description': 'Template matching the item of '
                                                      "the owner Mechanism's variable "
                                                      'this InputPort is assigned to; '
                                                      'used to validate the '
                                                      "InputPort's value. Usually left "
                                                      'unset when creating InputPorts '
                                                      'inline.',
                                       'type': 'array'},
                  'variable': { 'description': "Shape template for the InputPort's "
                                               "variable — each incoming Projection's "
                                               'value must match this format. If '
                                               'omitted and `projections` is given, '
                                               "shape is inferred from the sender's "
                                               'value.',
                                'type': 'array'},
                  'weight': { 'description': 'Scalar multiplier applied to this '
                                             "InputPort's value when the owner "
                                             'Mechanism combines InputPort values. '
                                             'Must be an int or float. Default is None '
                                             '(no weighting).',
                              'type': 'number'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = "InputPort is almost always specified inline as an element of a Mechanism's `input_ports` argument rather than constructed standalone — standalone construction requires an `owner` or the object will be in deferred-init status and cannot be executed. The `combine` and `function` arguments must be consistent: passing both raises an error unless `function` is a LinearCombination with the same operation as `combine`. `weight` and `exponent` here apply at the Mechanism level (how its function combines the values of all InputPorts), not inside the InputPort's own aggregation function. Setting `default_input='DEFAULT_VARIABLE'` silently forces `internal_only=True`, which excludes the Mechanism from being treated as a Composition INPUT Node. Projection values fed to the InputPort must all share the same shape as `variable`; mismatches are caught at instantiation time, not at construction."


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.InputPort
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
    def create_input_port(args: dict[str, Any] | None = None) -> Any:
        "Call this tool to create a standalone InputPort specification — use it when you need to configure a custom input receptor for a Mechanism with non-default aggregation, weighting, or projection wiring before attaching it via the Mechanism's `input_ports` argument."
        return _impl(args or {})
