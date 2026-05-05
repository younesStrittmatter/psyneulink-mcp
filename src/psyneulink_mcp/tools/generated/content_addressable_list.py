"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '6fbf03ea9f8bcb1a24664b0f33428c01b3120c074cff340a692e4fd02a4c8844'
__pnl_qualname__ = 'psyneulink.ContentAddressableList'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_content_addressable_list'
TOOL_DESCRIPTION = 'Call this tool to construct a named, ordered collection of PsyNeuLink Components that supports both numeric-index and string-key (attribute-value) access. The result behaves like a list but also allows lookup and assignment by the value of a designated attribute (default: `name`). Use this when you need to assemble a custom component collection with dict-like named access; note that PsyNeuLink already returns ContentAddressableList instances from attributes like `mechanism.output_ports` — only call this tool when you need to build such a collection from scratch.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "component_type": {\n      "description": "Name of the PsyNeuLink class whose instances this list will hold (e.g. \'OutputPort\', \'InputPort\', \'Mechanism\'). Resolved via getattr(psyneulink, component_type) at call time.",\n      "type": "string"\n    },\n    "key": {\n      "description": "Attribute of component_type to use for named (string-key) access. Must be a string attribute present on the class. Defaults to \'name\'.",\n      "type": "string"\n    },\n    "name": {\n      "description": "Display name for this ContentAddressableList. Defaults to the component_type class name.",\n      "type": "string"\n    }\n  },\n  "required": [\n    "component_type"\n  ],\n  "type": "object"\n}\n\nNotes:\nThe constructor\'s `component_type` argument must be an actual Python class object — not a string. The MCP template will need to resolve the string name to a class via `getattr(psyneulink, component_type)` before passing it; if that resolution step is absent the call raises `UtilitiesError(\'component_type arg … must be a class\')`. The `list` initializer argument is omitted from the schema because it requires live Component instances that cannot be expressed as JSON; pass it only from Python-side wrappers. The `key` attribute must already exist on the target class at import time or construction fails. ContentAddressableList instances are returned automatically from nearly every multi-port attribute on Mechanisms and Compositions (e.g. `mech.output_ports`, `comp.nodes`) — constructing one manually is rare and usually only needed for custom aggregations.'
TOOL_PARAMETERS = { 'properties': { 'component_type': { 'description': 'Name of the PsyNeuLink class '
                                                     'whose instances this list will '
                                                     "hold (e.g. 'OutputPort', "
                                                     "'InputPort', 'Mechanism'). "
                                                     'Resolved via getattr(psyneulink, '
                                                     'component_type) at call time.',
                                      'type': 'string'},
                  'key': { 'description': 'Attribute of component_type to use for '
                                          'named (string-key) access. Must be a string '
                                          'attribute present on the class. Defaults to '
                                          "'name'.",
                           'type': 'string'},
                  'name': { 'description': 'Display name for this '
                                           'ContentAddressableList. Defaults to the '
                                           'component_type class name.',
                            'type': 'string'}},
  'required': ['component_type'],
  'type': 'object'}
TOOL_NOTES = "The constructor's `component_type` argument must be an actual Python class object — not a string. The MCP template will need to resolve the string name to a class via `getattr(psyneulink, component_type)` before passing it; if that resolution step is absent the call raises `UtilitiesError('component_type arg … must be a class')`. The `list` initializer argument is omitted from the schema because it requires live Component instances that cannot be expressed as JSON; pass it only from Python-side wrappers. The `key` attribute must already exist on the target class at import time or construction fails. ContentAddressableList instances are returned automatically from nearly every multi-port attribute on Mechanisms and Compositions (e.g. `mech.output_ports`, `comp.nodes`) — constructing one manually is rare and usually only needed for custom aggregations."


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.ContentAddressableList
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
    def create_content_addressable_list(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to construct a named, ordered collection of PsyNeuLink Components that supports both numeric-index and string-key (attribute-value) access.'
        return _impl(args or {})
