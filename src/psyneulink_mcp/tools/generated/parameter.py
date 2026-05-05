"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '92357d5eb5a74989bd419f1ab693f7e889676f0f6c3c982c48efc7074fb9d8b0'
__pnl_qualname__ = 'psyneulink.Parameter'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_parameter'
TOOL_DESCRIPTION = 'Call this tool to create a psyneulink.Parameter descriptor that defines a single named parameter on a PsyNeuLink Component — specifying its default value, statefulness, modulability, logging behavior, history tracking, and type constraints. Use it when introspecting or programmatically constructing a Component\'s Parameters inner class; the result is a Parameter instance whose attributes govern how the owning Component stores and updates that parameter across execution contexts.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "aliases": {\n      "description": "Alternative names by which this parameter is also known (e.g., \'allocation\' is an alias for \'variable\' on ControlSignal). Provide as a list of strings.",\n      "items": {\n        "type": "string"\n      },\n      "type": "array"\n    },\n    "bool_as_number": {\n      "default": true,\n      "description": "If true (default), boolean values inside otherwise-numeric arrays are coerced to 0/1, preserving numeric dtype. Set false to allow mixed object-dtype arrays.",\n      "type": "boolean"\n    },\n    "constructor_argument": {\n      "description": "The name of the argument in the owning Component\'s __init__ that corresponds to this parameter, if they differ.",\n      "type": [\n        "string",\n        "null"\n      ]\n    },\n    "default_value": {\n      "description": "The default value of the parameter returned when no context-specific value exists. Accepts any serializable scalar, array, or null."\n    },\n    "delivery_condition": {\n      "default": "OFF",\n      "description": "LogCondition name string specifying when to deliver this parameter\'s value over an RPC pipeline. Default is \'OFF\'.",\n      "type": "string"\n    },\n    "dependencies": {\n      "description": "Set of other parameter names (on the same Component) that must be instantiated before this one.",\n      "items": {\n        "type": "string"\n      },\n      "type": "array"\n    },\n    "fallback_value": {\n      "description": "Behavior when get() is called for a context with no stored value. Pass the string \'default\' to return default_value instead of raising ParameterNoValueError. Pass any other serializable value to return that literal as the fallback.",\n      "type": [\n        "string",\n        "number",\n        "boolean",\n        "null"\n      ]\n    },\n    "function_arg": {\n      "default": true,\n      "description": "If true (default), this parameter is treated as an argument to the owning Component\'s function.",\n      "type": "boolean"\n    },\n    "history_max_length": {\n      "default": 1,\n      "description": "Maximum number of previous values to retain in history per execution context. Default is 1 (one prior value accessible via get_previous).",\n      "minimum": 0,\n      "type": "integer"\n    },\n    "history_min_length": {\n      "default": 0,\n      "description": "Minimum history length required for correct computation. Override only when an algorithm requires prior values (e.g., integrators).",\n      "minimum": 0,\n      "type": "integer"\n    },\n    "initializer": {\n      "description": "Name of another Parameter that serves as this parameter\'s initializer for StatefulFunctions.",\n      "type": [\n        "string",\n        "null"\n      ]\n    },\n    "log_condition": {\n      "default": "OFF",\n      "description": "LogCondition name string specifying when to automatically log this parameter (e.g., \'OFF\', \'EXECUTION\', \'ALL_ASSIGNMENTS\'). Default is \'OFF\'.",\n      "type": "string"\n    },\n    "loggable": {\n      "default": true,\n      "description": "If true (default), the parameter\'s values can be logged via PsyNeuLink\'s logging system.",\n      "type": "boolean"\n    },\n    "mdf_name": {\n      "description": "The name to use when exporting this parameter to MDF (Model Description Format). Defaults to the parameter\'s name.",\n      "type": [\n        "string",\n        "null"\n      ]\n    },\n    "modulable": {\n      "default": false,\n      "description": "If true, the parameter can be modulated by a ModulatoryProjection and will be assigned a ParameterPort on the owning Mechanism or Projection.",\n      "type": "boolean"\n    },\n    "modulation_combination_function": {\n      "description": "How to combine multiple ModulatoryProjection values: \'MULTIPLICATIVE\', \'PRODUCT\', \'ADDITIVE\', \'SUM\', or null to infer from parameter name alias. Only relevant when modulable=true.",\n      "type": [\n        "string",\n        "null"\n      ]\n    },\n    "name": {\n      "description": "The parameter\'s name. Normally inferred from the class attribute name inside a Parameters class; only set explicitly when constructing a Parameter outside a class body.",\n      "type": "string"\n    },\n    "pnl_internal": {\n      "default": false,\n      "description": "If true, marks this parameter as a PsyNeuLink implementation detail rather than a conceptually meaningful model parameter. Hides it from typical user-facing views.",\n      "type": "boolean"\n    },\n    "read_only": {\n      "default": false,\n      "description": "If true, the parameter cannot be set by the user without passing override=True. Use for computed outputs like \'value\' and \'variable\'.",\n      "type": "boolean"\n    },\n    "reference": {\n      "default": false,\n      "description": "If true, this parameter is not used in computation directly; it stores a value for initializing other Components and will not be auto-instantiated.",\n      "type": "boolean"\n    },\n    "retain_old_simulation_data": {\n      "default": false,\n      "description": "If true, values computed during simulations are preserved for later inspection instead of being discarded after use.",\n      "type": "boolean"\n    },\n    "specify_none": {\n      "default": false,\n      "description": "If true, a user-supplied value of None is treated as an intentional specification (sets _user_specified=True) rather than being ignored.",\n      "type": "boolean"\n    },\n    "stateful": {\n      "default": true,\n      "description": "If true (default), the parameter maintains independent values per execution context. Set false for parameters that are global across all contexts (e.g., structural constants).",\n      "type": "boolean"\n    },\n    "structural": {\n      "default": false,\n      "description": "If true, marks the parameter as structural (affects Component identity/structure rather than function).",\n      "type": "boolean"\n    },\n    "user": {\n      "default": true,\n      "description": "If true (default), this parameter is considered user-facing and will appear in typical parameter listings.",\n      "type": "boolean"\n    },\n    "valid_types": {\n      "description": "List of Python type name strings representing acceptable value types (e.g., [\'int\', \'float\']). Currently informational only; validation uses the owning Component\'s _validate_* methods.",\n      "items": {\n        "type": "string"\n      },\n      "type": [\n        "array",\n        "null"\n      ]\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\n- `getter` and `setter` are function hooks in the source signature but cannot be passed via MCP (not JSON-serializable); omit them — the generated tool body has no way to accept callables.\n- `default_value` is a positional-before-`*` argument in `__init__`; all other parameters are keyword-only. Pass `default_value` by name to be safe.\n- `stateful=True` is the default: every unique `execution_id` (Composition run) gets its own value slot. Set `stateful=False` only for parameters that truly must be shared across all contexts (e.g., structural weights that cannot change per-context).\n- `log_condition` and `delivery_condition` accept LogCondition enum members in Python, but pass them as strings here (e.g., `"EXECUTION"`, `"ALL_ASSIGNMENTS"`, `"OFF"`); the MCP layer will need to convert.\n- `function_arg` defaults to `True` in the `__init__` signature but `False` in the docstring — the signature is authoritative; default is `True`.\n- `valid_types` in the source is a tuple of actual Python `type` objects; the JSON schema accepts strings, but the host must resolve them to real types before passing to PNL.\n- `fallback_value` defaults to `ParameterNoValueError` (a sentinel class), meaning `get()` raises on missing context. Pass the string `"default"` (the `DEFAULT` keyword) to return `default_value` silently instead.\n- Private arguments (`_owner`, `_inherited`, `_inherited_source`, `_user_specified`, `_scalar_converted`, `_tracking_compiled_struct`) are intentionally excluded from the schema — they are set by PNL infrastructure, not by agents.\n- `Parameter` objects are typically defined as class-level attributes inside a Component\'s `Parameters(ParametersBase)` inner class, not constructed standalone. Standalone construction requires manually setting `_owner` afterward, which is not exposed here.'
TOOL_PARAMETERS = { 'properties': { 'aliases': { 'description': 'Alternative names by which this '
                                              'parameter is also known (e.g., '
                                              "'allocation' is an alias for 'variable' "
                                              'on ControlSignal). Provide as a list of '
                                              'strings.',
                               'items': {'type': 'string'},
                               'type': 'array'},
                  'bool_as_number': { 'default': True,
                                      'description': 'If true (default), boolean '
                                                     'values inside otherwise-numeric '
                                                     'arrays are coerced to 0/1, '
                                                     'preserving numeric dtype. Set '
                                                     'false to allow mixed '
                                                     'object-dtype arrays.',
                                      'type': 'boolean'},
                  'constructor_argument': { 'description': 'The name of the argument '
                                                           "in the owning Component's "
                                                           '__init__ that corresponds '
                                                           'to this parameter, if they '
                                                           'differ.',
                                            'type': ['string', 'null']},
                  'default_value': { 'description': 'The default value of the '
                                                    'parameter returned when no '
                                                    'context-specific value exists. '
                                                    'Accepts any serializable scalar, '
                                                    'array, or null.'},
                  'delivery_condition': { 'default': 'OFF',
                                          'description': 'LogCondition name string '
                                                         'specifying when to deliver '
                                                         "this parameter's value over "
                                                         'an RPC pipeline. Default is '
                                                         "'OFF'.",
                                          'type': 'string'},
                  'dependencies': { 'description': 'Set of other parameter names (on '
                                                   'the same Component) that must be '
                                                   'instantiated before this one.',
                                    'items': {'type': 'string'},
                                    'type': 'array'},
                  'fallback_value': { 'description': 'Behavior when get() is called '
                                                     'for a context with no stored '
                                                     "value. Pass the string 'default' "
                                                     'to return default_value instead '
                                                     'of raising '
                                                     'ParameterNoValueError. Pass any '
                                                     'other serializable value to '
                                                     'return that literal as the '
                                                     'fallback.',
                                      'type': ['string', 'number', 'boolean', 'null']},
                  'function_arg': { 'default': True,
                                    'description': 'If true (default), this parameter '
                                                   'is treated as an argument to the '
                                                   "owning Component's function.",
                                    'type': 'boolean'},
                  'history_max_length': { 'default': 1,
                                          'description': 'Maximum number of previous '
                                                         'values to retain in history '
                                                         'per execution context. '
                                                         'Default is 1 (one prior '
                                                         'value accessible via '
                                                         'get_previous).',
                                          'minimum': 0,
                                          'type': 'integer'},
                  'history_min_length': { 'default': 0,
                                          'description': 'Minimum history length '
                                                         'required for correct '
                                                         'computation. Override only '
                                                         'when an algorithm requires '
                                                         'prior values (e.g., '
                                                         'integrators).',
                                          'minimum': 0,
                                          'type': 'integer'},
                  'initializer': { 'description': 'Name of another Parameter that '
                                                  "serves as this parameter's "
                                                  'initializer for StatefulFunctions.',
                                   'type': ['string', 'null']},
                  'log_condition': { 'default': 'OFF',
                                     'description': 'LogCondition name string '
                                                    'specifying when to automatically '
                                                    "log this parameter (e.g., 'OFF', "
                                                    "'EXECUTION', 'ALL_ASSIGNMENTS'). "
                                                    "Default is 'OFF'.",
                                     'type': 'string'},
                  'loggable': { 'default': True,
                                'description': "If true (default), the parameter's "
                                               "values can be logged via PsyNeuLink's "
                                               'logging system.',
                                'type': 'boolean'},
                  'mdf_name': { 'description': 'The name to use when exporting this '
                                               'parameter to MDF (Model Description '
                                               "Format). Defaults to the parameter's "
                                               'name.',
                                'type': ['string', 'null']},
                  'modulable': { 'default': False,
                                 'description': 'If true, the parameter can be '
                                                'modulated by a ModulatoryProjection '
                                                'and will be assigned a ParameterPort '
                                                'on the owning Mechanism or '
                                                'Projection.',
                                 'type': 'boolean'},
                  'modulation_combination_function': { 'description': 'How to combine '
                                                                      'multiple '
                                                                      'ModulatoryProjection '
                                                                      'values: '
                                                                      "'MULTIPLICATIVE', "
                                                                      "'PRODUCT', "
                                                                      "'ADDITIVE', "
                                                                      "'SUM', or null "
                                                                      'to infer from '
                                                                      'parameter name '
                                                                      'alias. Only '
                                                                      'relevant when '
                                                                      'modulable=true.',
                                                       'type': ['string', 'null']},
                  'name': { 'description': "The parameter's name. Normally inferred "
                                           'from the class attribute name inside a '
                                           'Parameters class; only set explicitly when '
                                           'constructing a Parameter outside a class '
                                           'body.',
                            'type': 'string'},
                  'pnl_internal': { 'default': False,
                                    'description': 'If true, marks this parameter as a '
                                                   'PsyNeuLink implementation detail '
                                                   'rather than a conceptually '
                                                   'meaningful model parameter. Hides '
                                                   'it from typical user-facing views.',
                                    'type': 'boolean'},
                  'read_only': { 'default': False,
                                 'description': 'If true, the parameter cannot be set '
                                                'by the user without passing '
                                                'override=True. Use for computed '
                                                "outputs like 'value' and 'variable'.",
                                 'type': 'boolean'},
                  'reference': { 'default': False,
                                 'description': 'If true, this parameter is not used '
                                                'in computation directly; it stores a '
                                                'value for initializing other '
                                                'Components and will not be '
                                                'auto-instantiated.',
                                 'type': 'boolean'},
                  'retain_old_simulation_data': { 'default': False,
                                                  'description': 'If true, values '
                                                                 'computed during '
                                                                 'simulations are '
                                                                 'preserved for later '
                                                                 'inspection instead '
                                                                 'of being discarded '
                                                                 'after use.',
                                                  'type': 'boolean'},
                  'specify_none': { 'default': False,
                                    'description': 'If true, a user-supplied value of '
                                                   'None is treated as an intentional '
                                                   'specification (sets '
                                                   '_user_specified=True) rather than '
                                                   'being ignored.',
                                    'type': 'boolean'},
                  'stateful': { 'default': True,
                                'description': 'If true (default), the parameter '
                                               'maintains independent values per '
                                               'execution context. Set false for '
                                               'parameters that are global across all '
                                               'contexts (e.g., structural constants).',
                                'type': 'boolean'},
                  'structural': { 'default': False,
                                  'description': 'If true, marks the parameter as '
                                                 'structural (affects Component '
                                                 'identity/structure rather than '
                                                 'function).',
                                  'type': 'boolean'},
                  'user': { 'default': True,
                            'description': 'If true (default), this parameter is '
                                           'considered user-facing and will appear in '
                                           'typical parameter listings.',
                            'type': 'boolean'},
                  'valid_types': { 'description': 'List of Python type name strings '
                                                  'representing acceptable value types '
                                                  "(e.g., ['int', 'float']). Currently "
                                                  'informational only; validation uses '
                                                  "the owning Component's _validate_* "
                                                  'methods.',
                                   'items': {'type': 'string'},
                                   'type': ['array', 'null']}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = '- `getter` and `setter` are function hooks in the source signature but cannot be passed via MCP (not JSON-serializable); omit them — the generated tool body has no way to accept callables.\n- `default_value` is a positional-before-`*` argument in `__init__`; all other parameters are keyword-only. Pass `default_value` by name to be safe.\n- `stateful=True` is the default: every unique `execution_id` (Composition run) gets its own value slot. Set `stateful=False` only for parameters that truly must be shared across all contexts (e.g., structural weights that cannot change per-context).\n- `log_condition` and `delivery_condition` accept LogCondition enum members in Python, but pass them as strings here (e.g., `"EXECUTION"`, `"ALL_ASSIGNMENTS"`, `"OFF"`); the MCP layer will need to convert.\n- `function_arg` defaults to `True` in the `__init__` signature but `False` in the docstring — the signature is authoritative; default is `True`.\n- `valid_types` in the source is a tuple of actual Python `type` objects; the JSON schema accepts strings, but the host must resolve them to real types before passing to PNL.\n- `fallback_value` defaults to `ParameterNoValueError` (a sentinel class), meaning `get()` raises on missing context. Pass the string `"default"` (the `DEFAULT` keyword) to return `default_value` silently instead.\n- Private arguments (`_owner`, `_inherited`, `_inherited_source`, `_user_specified`, `_scalar_converted`, `_tracking_compiled_struct`) are intentionally excluded from the schema — they are set by PNL infrastructure, not by agents.\n- `Parameter` objects are typically defined as class-level attributes inside a Component\'s `Parameters(ParametersBase)` inner class, not constructed standalone. Standalone construction requires manually setting `_owner` afterward, which is not exposed here.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.Parameter
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
    def create_parameter(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to create a psyneulink.Parameter descriptor that defines a single named parameter on a PsyNeuLink Component — specifying its default value, statefulness, modulability, logging behavior, history tracking, and type constraints.'
        return _impl(args or {})
