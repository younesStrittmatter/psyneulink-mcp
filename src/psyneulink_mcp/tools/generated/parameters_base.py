"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '38be90c76f6707abc01ce047aa88ddc1dc919a28cccb71dd272aa86056878f2f'
__pnl_qualname__ = 'psyneulink.ParametersBase'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_parameters_base'
TOOL_DESCRIPTION = 'Call this tool only when you need to directly instantiate a standalone parameter container for a PsyNeuLink Component owner — for example, when introspecting or programmatically constructing the parameter hierarchy of a component outside normal Component initialization. In practice, ParametersBase is instantiated automatically as an inner class by every PsyNeuLink Component; you rarely need to call this tool directly unless building low-level parameter infrastructure or writing tests that inspect parameter inheritance chains.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "owner": {\n      "description": "The PsyNeuLink Component instance (or class name as a string reference) that owns this parameter container. Every ParametersBase must be bound to an owner.",\n      "type": "string"\n    },\n    "parent": {\n      "default": null,\n      "description": "Optional reference to a parent ParametersBase from which parameters are inherited. Omit to create a root-level parameter container with no inheritance chain.",\n      "type": "string"\n    }\n  },\n  "required": [\n    "owner"\n  ],\n  "type": "object"\n}\n\nNotes:\nParametersBase is an internal infrastructure class — it is automatically created and managed during normal Component construction. Directly instantiating it is unusual and typically only warranted for low-level introspection or testing. The constructor validates all parameter default values and resolves aliases eagerly, so any inconsistency between __init__ signature defaults and Parameters class declarations will raise an AssertionError at construction time. The `parent` argument drives parameter inheritance: parameters not explicitly specified on the owner are copied (or aliased) from parent. Passing an incompatible owner/parent pair will silently inherit mismatched parameter trees.'
TOOL_PARAMETERS = { 'properties': { 'owner': { 'description': 'The PsyNeuLink Component instance (or '
                                            'class name as a string reference) that '
                                            'owns this parameter container. Every '
                                            'ParametersBase must be bound to an owner.',
                             'type': 'string'},
                  'parent': { 'default': None,
                              'description': 'Optional reference to a parent '
                                             'ParametersBase from which parameters are '
                                             'inherited. Omit to create a root-level '
                                             'parameter container with no inheritance '
                                             'chain.',
                              'type': 'string'}},
  'required': ['owner'],
  'type': 'object'}
TOOL_NOTES = 'ParametersBase is an internal infrastructure class — it is automatically created and managed during normal Component construction. Directly instantiating it is unusual and typically only warranted for low-level introspection or testing. The constructor validates all parameter default values and resolves aliases eagerly, so any inconsistency between __init__ signature defaults and Parameters class declarations will raise an AssertionError at construction time. The `parent` argument drives parameter inheritance: parameters not explicitly specified on the owner are copied (or aliased) from parent. Passing an incompatible owner/parent pair will silently inherit mismatched parameter trees.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.ParametersBase
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
    def create_parameters_base(args: dict[str, Any] | None = None) -> Any:
        'Call this tool only when you need to directly instantiate a standalone parameter container for a PsyNeuLink Component owner — for example, when introspecting or programmatically constructing the parameter hierarchy of a component outside normal Component initialization.'
        return _impl(args or {})
