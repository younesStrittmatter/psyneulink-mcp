"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = 'adc23754ebeb0c55bdde1324622b33a509116703503508ee7e7de181a8afeee6'
__pnl_qualname__ = 'psyneulink.ShellClass'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_shell_class'
TOOL_DESCRIPTION = 'Call this tool only when you need a bare-bones Component placeholder — ShellClass is an empty subclass of Component with no added behavior. It is rarely useful to instantiate directly; prefer a concrete subclass (Mechanism, Projection, Function, etc.) for any real modeling task. Returns an initialized ShellClass instance that satisfies the Component interface but provides no functional capability.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "default_variable": {\n      "description": "Template for the input to the component\'s function; also used as the input value when none is provided at execution. Scalar, list, or array.",\n      "oneOf": [\n        {\n          "type": "number"\n        },\n        {\n          "type": "array"\n        }\n      ]\n    },\n    "input_shapes": {\n      "description": "Specifies the shape of default_variable as an array of zeros when default_variable is not provided. Ignored if default_variable is given. Integer or list of integers/tuples.",\n      "oneOf": [\n        {\n          "type": "integer"\n        },\n        {\n          "items": {\n            "oneOf": [\n              {\n                "type": "integer"\n              },\n              {\n                "items": {\n                  "type": "integer"\n                },\n                "type": "array"\n              }\n            ]\n          },\n          "type": "array"\n        }\n      ]\n    },\n    "name": {\n      "description": "String name for this component instance; auto-assigned from registry if omitted.",\n      "type": "string"\n    },\n    "params": {\n      "additionalProperties": true,\n      "description": "Parameter dictionary mapping parameter names to values; overrides constructor argument defaults.",\n      "type": "object"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\nShellClass is defined as `class ShellClass(Component): pass` — it adds nothing to Component. Component itself is documented as abstract and should never be instantiated directly; instantiating ShellClass is equally inadvisable for any real modeling work. The `prefs` and `context` constructor arguments exist on Component but are advanced/internal; omit them unless you have a specific need. The `params` dict values are not type-checked recursively — only top-level keys are validated.'
TOOL_PARAMETERS = { 'properties': { 'default_variable': { 'description': 'Template for the input to the '
                                                       "component's function; also "
                                                       'used as the input value when '
                                                       'none is provided at execution. '
                                                       'Scalar, list, or array.',
                                        'oneOf': [ {'type': 'number'},
                                                   {'type': 'array'}]},
                  'input_shapes': { 'description': 'Specifies the shape of '
                                                   'default_variable as an array of '
                                                   'zeros when default_variable is not '
                                                   'provided. Ignored if '
                                                   'default_variable is given. Integer '
                                                   'or list of integers/tuples.',
                                    'oneOf': [ {'type': 'integer'},
                                               { 'items': { 'oneOf': [ { 'type': 'integer'},
                                                                       { 'items': { 'type': 'integer'},
                                                                         'type': 'array'}]},
                                                 'type': 'array'}]},
                  'name': { 'description': 'String name for this component instance; '
                                           'auto-assigned from registry if omitted.',
                            'type': 'string'},
                  'params': { 'additionalProperties': True,
                              'description': 'Parameter dictionary mapping parameter '
                                             'names to values; overrides constructor '
                                             'argument defaults.',
                              'type': 'object'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = 'ShellClass is defined as `class ShellClass(Component): pass` — it adds nothing to Component. Component itself is documented as abstract and should never be instantiated directly; instantiating ShellClass is equally inadvisable for any real modeling work. The `prefs` and `context` constructor arguments exist on Component but are advanced/internal; omit them unless you have a specific need. The `params` dict values are not type-checked recursively — only top-level keys are validated.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.ShellClass
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
    def create_shell_class(args: dict[str, Any] | None = None) -> Any:
        'Call this tool only when you need a bare-bones Component placeholder — ShellClass is an empty subclass of Component with no added behavior.'
        return _impl(args or {})
