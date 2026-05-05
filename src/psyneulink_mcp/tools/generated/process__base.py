"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '101257d497e79f9d5e647f25c3300451f8ca5773e01894336f10bbea7f0b6f86'
__pnl_qualname__ = 'psyneulink.Process_Base'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_process__base'
TOOL_DESCRIPTION = 'Do NOT call this tool directly — Process_Base is an abstract shell class (body is literally `pass`) that serves only as a marker base class in PsyNeuLink\'s type hierarchy. Use a concrete Process subclass instead. If you are inspecting the type hierarchy or need to isinstance-check a component against the Process_Base marker, this tool can construct the shell object, but the result will not be functional.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "default_variable": {\n      "description": "Template for the input to the component\'s function; also used as the default input when none is provided at execution. Typically a scalar or list/array of numbers.",\n      "type": "array"\n    },\n    "input_shapes": {\n      "description": "Specifies default_variable as zero-filled array(s) of the given shape(s) when default_variable is not provided. Checked for compatibility if default_variable is also provided.",\n      "oneOf": [\n        {\n          "type": "integer"\n        },\n        {\n          "items": {\n            "oneOf": [\n              {\n                "type": "integer"\n              },\n              {\n                "items": {\n                  "type": "integer"\n                },\n                "type": "array"\n              }\n            ]\n          },\n          "type": "array"\n        }\n      ]\n    },\n    "name": {\n      "description": "Name for this component instance. If omitted, a default name is assigned by the relevant PsyNeuLink registry.",\n      "type": "string"\n    },\n    "params": {\n      "additionalProperties": true,\n      "description": "Parameter dictionary mapping parameter keyword names to values. Overrides any values assigned via constructor arguments.",\n      "type": "object"\n    },\n    "prefs": {\n      "additionalProperties": true,\n      "description": "PreferenceSet or specification dict controlling component preferences. Defaults to class-level preferences if omitted.",\n      "type": "object"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\nProcess_Base is defined as `class Process_Base(ShellClass): pass` — it has no constructor body and no functional implementation. It exists solely as a marker/tag in PsyNeuLink\'s class hierarchy. Directly instantiating it will either raise an error or produce an inert object. The docstring shown is inherited from Component and describes the general Component API, not anything specific to Process_Base. Agents should use a concrete subclass (e.g., a specific Process type) rather than this shell. The `context` parameter from the Component signature is omitted here because it is an internal framework argument not intended for external callers.'
TOOL_PARAMETERS = { 'properties': { 'default_variable': { 'description': 'Template for the input to the '
                                                       "component's function; also "
                                                       'used as the default input when '
                                                       'none is provided at execution. '
                                                       'Typically a scalar or '
                                                       'list/array of numbers.',
                                        'type': 'array'},
                  'input_shapes': { 'description': 'Specifies default_variable as '
                                                   'zero-filled array(s) of the given '
                                                   'shape(s) when default_variable is '
                                                   'not provided. Checked for '
                                                   'compatibility if default_variable '
                                                   'is also provided.',
                                    'oneOf': [ {'type': 'integer'},
                                               { 'items': { 'oneOf': [ { 'type': 'integer'},
                                                                       { 'items': { 'type': 'integer'},
                                                                         'type': 'array'}]},
                                                 'type': 'array'}]},
                  'name': { 'description': 'Name for this component instance. If '
                                           'omitted, a default name is assigned by the '
                                           'relevant PsyNeuLink registry.',
                            'type': 'string'},
                  'params': { 'additionalProperties': True,
                              'description': 'Parameter dictionary mapping parameter '
                                             'keyword names to values. Overrides any '
                                             'values assigned via constructor '
                                             'arguments.',
                              'type': 'object'},
                  'prefs': { 'additionalProperties': True,
                             'description': 'PreferenceSet or specification dict '
                                            'controlling component preferences. '
                                            'Defaults to class-level preferences if '
                                            'omitted.',
                             'type': 'object'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = "Process_Base is defined as `class Process_Base(ShellClass): pass` — it has no constructor body and no functional implementation. It exists solely as a marker/tag in PsyNeuLink's class hierarchy. Directly instantiating it will either raise an error or produce an inert object. The docstring shown is inherited from Component and describes the general Component API, not anything specific to Process_Base. Agents should use a concrete subclass (e.g., a specific Process type) rather than this shell. The `context` parameter from the Component signature is omitted here because it is an internal framework argument not intended for external callers."


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.Process_Base
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
    def create_process__base(args: dict[str, Any] | None = None) -> Any:
        "Do NOT call this tool directly — Process_Base is an abstract shell class (body is literally `pass`) that serves only as a marker base class in PsyNeuLink's type hierarchy."
        return _impl(args or {})
