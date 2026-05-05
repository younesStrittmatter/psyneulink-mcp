"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = 'c365b08916a80129ed4347bfd513d51ee39d30ad49ee117a970ec94e45ad81dc'
__pnl_qualname__ = 'psyneulink.SharedParameter'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_shared_parameter'
TOOL_DESCRIPTION = 'Call this tool when defining a Component parameter that should act as a user-friendly alias pointing to a parameter on one of the Component\'s sub-attributes (typically its `function`). Use it instead of a plain `Parameter` when the value is owned and stored by another object but should be readable and writable from the parent Component directly. Returns a `SharedParameter` instance that transparently delegates gets and sets to the target parameter.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "attribute_name": {\n      "default": "function",\n      "description": "Name of the attribute or Parameter on the owning Component that contains the target parameter. Defaults to \'function\', meaning the Component\'s function attribute is the intermediary.",\n      "type": "string"\n    },\n    "default_value": {\n      "description": "Initial/default value for the shared parameter. If `primary` is False, the target\'s default takes precedence over this value.",\n      "type": [\n        "number",\n        "boolean",\n        "string",\n        "null"\n      ]\n    },\n    "primary": {\n      "default": false,\n      "description": "If True, this SharedParameter\'s default_value overrides the target parameter\'s default. If False (default), the target\'s default takes precedence.",\n      "type": "boolean"\n    },\n    "shared_parameter_name": {\n      "description": "Name of the parameter on the object identified by `attribute_name` that this SharedParameter delegates to. Defaults to the name assigned to this SharedParameter itself.",\n      "type": "string"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\nSharedParameter is a class-definition-time construct used when building Component subclasses — it is not a runtime tool for end-users manipulating model values. The `getter` and `setter` defaults already handle delegation correctly; only override them for non-standard delegation logic. If `attribute_name` is omitted, it defaults to `\'function\'`, so the target is `component.function.<shared_parameter_name>`. If `shared_parameter_name` is omitted, it defaults to the name under which this object is stored on the Parameters class. The source must resolve to a non-stateful parameter; attaching a SharedParameter whose target is stateful raises `ParameterError`. Do not mix instance-level and class-level parameter targets — this raises `ParameterInvalidSourceError`.'
TOOL_PARAMETERS = { 'properties': { 'attribute_name': { 'default': 'function',
                                      'description': 'Name of the attribute or '
                                                     'Parameter on the owning '
                                                     'Component that contains the '
                                                     'target parameter. Defaults to '
                                                     "'function', meaning the "
                                                     "Component's function attribute "
                                                     'is the intermediary.',
                                      'type': 'string'},
                  'default_value': { 'description': 'Initial/default value for the '
                                                    'shared parameter. If `primary` is '
                                                    "False, the target's default takes "
                                                    'precedence over this value.',
                                     'type': ['number', 'boolean', 'string', 'null']},
                  'primary': { 'default': False,
                               'description': "If True, this SharedParameter's "
                                              'default_value overrides the target '
                                              "parameter's default. If False "
                                              "(default), the target's default takes "
                                              'precedence.',
                               'type': 'boolean'},
                  'shared_parameter_name': { 'description': 'Name of the parameter on '
                                                            'the object identified by '
                                                            '`attribute_name` that '
                                                            'this SharedParameter '
                                                            'delegates to. Defaults to '
                                                            'the name assigned to this '
                                                            'SharedParameter itself.',
                                             'type': 'string'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = "SharedParameter is a class-definition-time construct used when building Component subclasses — it is not a runtime tool for end-users manipulating model values. The `getter` and `setter` defaults already handle delegation correctly; only override them for non-standard delegation logic. If `attribute_name` is omitted, it defaults to `'function'`, so the target is `component.function.<shared_parameter_name>`. If `shared_parameter_name` is omitted, it defaults to the name under which this object is stored on the Parameters class. The source must resolve to a non-stateful parameter; attaching a SharedParameter whose target is stateful raises `ParameterError`. Do not mix instance-level and class-level parameter targets — this raises `ParameterInvalidSourceError`."


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.SharedParameter
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
    def create_shared_parameter(args: dict[str, Any] | None = None) -> Any:
        "Call this tool when defining a Component parameter that should act as a user-friendly alias pointing to a parameter on one of the Component's sub-attributes (typically its `function`)."
        return _impl(args or {})
