"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '9b4c0d2feb23147f7d25af3ae03decf546fdb1f2e8be53abb8d8168801d60afa'
__pnl_qualname__ = 'psyneulink.Function_Base'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_function__base'
TOOL_DESCRIPTION = 'Do NOT call this tool to create a function instance — `Function_Base` is an abstract base class and cannot be instantiated directly; doing so will raise a `TypeError`. Call it only if you need to introspect or reference the base class itself (e.g., checking `isinstance`). To create an actual PsyNeuLink function, use a concrete subclass tool such as `Linear`, `Logistic`, `Exponential`, `ReLU`, `SoftMax`, etc.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "default_variable": {\n      "default": [\n        0\n      ],\n      "description": "Specifies the format and default value for the input to the function. Typically a number or numpy array. Determines the shape expected by the function\'s execute method.",\n      "items": {\n        "type": "number"\n      },\n      "type": "array"\n    },\n    "name": {\n      "description": "Optional name for the Function instance. If omitted, FunctionRegistry assigns a default name based on the class.",\n      "type": "string"\n    },\n    "owner": {\n      "description": "Name or reference to the Component to which this Function is assigned. Usually set automatically when the function is passed to a Mechanism or Projection.",\n      "type": "string"\n    },\n    "params": {\n      "description": "Optional parameter dictionary overriding constructor argument defaults. Keys are parameter names, values are the desired parameter values.",\n      "type": "object"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\nFunction_Base is decorated with `@abc.abstractmethod` on both `__init__` and `_function` — instantiating it directly raises `TypeError: Can\'t instantiate abstract class`. The `prefs` argument is omitted from the schema because it accepts a PsyNeuLink `PreferenceSet` object, which is not JSON-serializable and is almost never specified by an agent. The `default_variable` constructor argument maps to the `variable` attribute; the schema reflects the default of `numpy.array([0])` as `[0]`.'
TOOL_PARAMETERS = { 'properties': { 'default_variable': { 'default': [0],
                                        'description': 'Specifies the format and '
                                                       'default value for the input to '
                                                       'the function. Typically a '
                                                       'number or numpy array. '
                                                       'Determines the shape expected '
                                                       "by the function's execute "
                                                       'method.',
                                        'items': {'type': 'number'},
                                        'type': 'array'},
                  'name': { 'description': 'Optional name for the Function instance. '
                                           'If omitted, FunctionRegistry assigns a '
                                           'default name based on the class.',
                            'type': 'string'},
                  'owner': { 'description': 'Name or reference to the Component to '
                                            'which this Function is assigned. Usually '
                                            'set automatically when the function is '
                                            'passed to a Mechanism or Projection.',
                             'type': 'string'},
                  'params': { 'description': 'Optional parameter dictionary overriding '
                                             'constructor argument defaults. Keys are '
                                             'parameter names, values are the desired '
                                             'parameter values.',
                              'type': 'object'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = "Function_Base is decorated with `@abc.abstractmethod` on both `__init__` and `_function` — instantiating it directly raises `TypeError: Can't instantiate abstract class`. The `prefs` argument is omitted from the schema because it accepts a PsyNeuLink `PreferenceSet` object, which is not JSON-serializable and is almost never specified by an agent. The `default_variable` constructor argument maps to the `variable` attribute; the schema reflects the default of `numpy.array([0])` as `[0]`."


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.Function_Base
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
    def create_function__base(args: dict[str, Any] | None = None) -> Any:
        'Do NOT call this tool to create a function instance — `Function_Base` is an abstract base class and cannot be instantiated directly; doing so will raise a `TypeError`.'
        return _impl(args or {})
