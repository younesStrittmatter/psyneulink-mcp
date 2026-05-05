"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = 'fe5d8782f8ea3fd8452cc259a38a86b6c0704acffb143770145a03b08d79753e'
__pnl_qualname__ = 'psyneulink.library.components.mechanisms.processing.integrator.episodicmemorymechanism.deprecation_warning'
__pnl_kind__ = 'function'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'deprecation_warning'
TOOL_DESCRIPTION = 'Call this tool when you need to check whether any deprecated argument names were passed to a PsyNeuLink component and obtain a mapping of their canonical replacements. Returns a dict of {real_arg_name: value} for any deprecated args found in kwargs, and emits Python warnings for each — useful when constructing components programmatically and you want to surface or handle deprecated-arg usage rather than silently ignoring it.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "additional_msg": {\n      "description": "Optional extra text appended to each warning message.",\n      "type": "string"\n    },\n    "component": {\n      "description": "The class name of the PsyNeuLink component being constructed (e.g., \'TransferMechanism\'). Used only for the text of the warning message.",\n      "type": "string"\n    },\n    "deprecated_args": {\n      "additionalProperties": {\n        "type": "string"\n      },\n      "description": "Mapping of deprecated argument names to their canonical replacements, e.g. {\\"old_param\\": \\"new_param\\"}.",\n      "type": "object"\n    },\n    "kwargs": {\n      "additionalProperties": true,\n      "description": "The keyword arguments dict passed to the component. Deprecated arg entries will be popped from this dict in-place as a side effect.",\n      "type": "object"\n    },\n    "method": {\n      "description": "Name of the method where the deprecated arg appeared (default: \'constructor\'). Used only in warning text.",\n      "type": "string"\n    }\n  },\n  "required": [\n    "component",\n    "kwargs",\n    "deprecated_args"\n  ],\n  "type": "object"\n}\n\nNotes:\nThis is an internal PsyNeuLink utility — it is rarely the right tool for an agent to call directly. It modifies `kwargs` in-place (pops deprecated keys) as a side effect, so the caller\'s dict is mutated. The return value maps canonical arg names to values only for deprecated args that were actually present in kwargs; absent deprecated args produce no entry. If both the deprecated arg and its replacement are present in kwargs, the deprecated arg\'s value wins and a warning is emitted. The `component` parameter here is typed as string (class name) because JSON cannot represent a live Python object; the generated template must resolve this to an actual component instance before calling.'
TOOL_PARAMETERS = { 'properties': { 'additional_msg': { 'description': 'Optional extra text appended to '
                                                     'each warning message.',
                                      'type': 'string'},
                  'component': { 'description': 'The class name of the PsyNeuLink '
                                                'component being constructed (e.g., '
                                                "'TransferMechanism'). Used only for "
                                                'the text of the warning message.',
                                 'type': 'string'},
                  'deprecated_args': { 'additionalProperties': {'type': 'string'},
                                       'description': 'Mapping of deprecated argument '
                                                      'names to their canonical '
                                                      'replacements, e.g. '
                                                      '{"old_param": "new_param"}.',
                                       'type': 'object'},
                  'kwargs': { 'additionalProperties': True,
                              'description': 'The keyword arguments dict passed to the '
                                             'component. Deprecated arg entries will '
                                             'be popped from this dict in-place as a '
                                             'side effect.',
                              'type': 'object'},
                  'method': { 'description': 'Name of the method where the deprecated '
                                             "arg appeared (default: 'constructor'). "
                                             'Used only in warning text.',
                              'type': 'string'}},
  'required': ['component', 'kwargs', 'deprecated_args'],
  'type': 'object'}
TOOL_NOTES = "This is an internal PsyNeuLink utility — it is rarely the right tool for an agent to call directly. It modifies `kwargs` in-place (pops deprecated keys) as a side effect, so the caller's dict is mutated. The return value maps canonical arg names to values only for deprecated args that were actually present in kwargs; absent deprecated args produce no entry. If both the deprecated arg and its replacement are present in kwargs, the deprecated arg's value wins and a warning is emitted. The `component` parameter here is typed as string (class name) because JSON cannot represent a live Python object; the generated template must resolve this to an actual component instance before calling."


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.deprecation_warning
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
    def deprecation_warning(args: dict[str, Any] | None = None) -> Any:
        'Call this tool when you need to check whether any deprecated argument names were passed to a PsyNeuLink component and obtain a mapping of their canonical replacements.'
        return _impl(args or {})
