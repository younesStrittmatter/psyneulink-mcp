"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '49ff0535055d97328c0f76806a53021714e2f8577d138152b75b7e15fcaab2e3'
__pnl_qualname__ = 'psyneulink.Function'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_function'
TOOL_DESCRIPTION = 'Do NOT call this tool directly — `Function` is an abstract base class and cannot be instantiated. Use it only as a type reference or to understand the shared parameter interface inherited by all PsyNeuLink function subclasses (e.g., `Linear`, `Logistic`, `Gaussian`). When you need a function object, call the specific subclass tool instead.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "default_variable": {\n      "description": "Template for the input to the function; sets the shape and default value used when no input is provided at execution. Typically a 1-D or 2-D numeric array.",\n      "type": "array"\n    },\n    "input_shapes": {\n      "description": "Shorthand to set default_variable as zero-filled array(s) of the given shape(s). Ignored if default_variable is also supplied and they are incompatible.",\n      "oneOf": [\n        {\n          "type": "integer"\n        },\n        {\n          "items": {\n            "oneOf": [\n              {\n                "type": "integer"\n              },\n              {\n                "items": {\n                  "type": "integer"\n                },\n                "type": "array"\n              }\n            ]\n          },\n          "type": "array"\n        }\n      ]\n    },\n    "name": {\n      "description": "Name for this function instance. If omitted, the registry assigns a default following PsyNeuLink naming conventions.",\n      "type": "string"\n    },\n    "params": {\n      "description": "Parameter dictionary whose keys override constructor argument values. Can include a FUNCTION key to specify or replace the underlying callable.",\n      "type": "object"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\n`Function` is a ShellClass — its `_instantiate_function` is a no-op stub. Calling `psyneulink.Function(...)` directly will raise an error at runtime. The docstring shown in the source is inherited from `Component` and describes parameters shared across all component subclasses, not behavior specific to `Function` itself. `prefs` and `context` are omitted from the schema because they are internal/advanced and should not be set by agents. `default_variable` defaults to `[[0]]` (a 2-D array with a single zero) when neither it nor `input_shapes` is provided.'
TOOL_PARAMETERS = { 'properties': { 'default_variable': { 'description': 'Template for the input to the '
                                                       'function; sets the shape and '
                                                       'default value used when no '
                                                       'input is provided at '
                                                       'execution. Typically a 1-D or '
                                                       '2-D numeric array.',
                                        'type': 'array'},
                  'input_shapes': { 'description': 'Shorthand to set default_variable '
                                                   'as zero-filled array(s) of the '
                                                   'given shape(s). Ignored if '
                                                   'default_variable is also supplied '
                                                   'and they are incompatible.',
                                    'oneOf': [ {'type': 'integer'},
                                               { 'items': { 'oneOf': [ { 'type': 'integer'},
                                                                       { 'items': { 'type': 'integer'},
                                                                         'type': 'array'}]},
                                                 'type': 'array'}]},
                  'name': { 'description': 'Name for this function instance. If '
                                           'omitted, the registry assigns a default '
                                           'following PsyNeuLink naming conventions.',
                            'type': 'string'},
                  'params': { 'description': 'Parameter dictionary whose keys override '
                                             'constructor argument values. Can include '
                                             'a FUNCTION key to specify or replace the '
                                             'underlying callable.',
                              'type': 'object'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = '`Function` is a ShellClass — its `_instantiate_function` is a no-op stub. Calling `psyneulink.Function(...)` directly will raise an error at runtime. The docstring shown in the source is inherited from `Component` and describes parameters shared across all component subclasses, not behavior specific to `Function` itself. `prefs` and `context` are omitted from the schema because they are internal/advanced and should not be set by agents. `default_variable` defaults to `[[0]]` (a 2-D array with a single zero) when neither it nor `input_shapes` is provided.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.Function
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
    def create_function(args: dict[str, Any] | None = None) -> Any:
        'Do NOT call this tool directly — `Function` is an abstract base class and cannot be instantiated.'
        return _impl(args or {})
