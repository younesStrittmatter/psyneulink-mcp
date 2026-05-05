"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '378353aa7b8912120b3042002f0b3ebfaae6132fe296dfbbd1df638343fd2762'
__pnl_qualname__ = 'psyneulink.StandardOutputPorts'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_standard_output_ports'
TOOL_DESCRIPTION = 'Call this tool when defining or inspecting the standard OutputPort specifications for a custom PsyNeuLink Component class — specifically when you need to instantiate a `StandardOutputPorts` collection that maps named output ports to owner value indices. The result is an object whose `.data` attribute holds a list of OutputPort specification dicts, `.names` returns port name strings, and `.get_port_dict(name)` retrieves a copy of any individual port\'s spec dict.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "indices": {\n      "description": "Controls how OWNER_VALUE indices are assigned. PRIMARY assigns (OWNER_VALUE, PRIMARY) to all ports without an explicit VARIABLE; SEQUENTIAL assigns incrementing ints (0, 1, 2, \\u2026) to each port in order. Pass a JSON array of ints instead for explicit per-port indices. Omit (null) to leave VARIABLE unset for ports that don\'t already specify it.",\n      "enum": [\n        "PRIMARY",\n        "SEQUENTIAL"\n      ],\n      "type": "string"\n    },\n    "output_port_dicts": {\n      "description": "List of dicts, each specifying one standard OutputPort. All items must be dicts \\u2014 non-dict items raise an error.",\n      "items": {\n        "description": "A dict specifying one OutputPort, typically containing at minimum a NAME key and optionally VARIABLE.",\n        "type": "object"\n      },\n      "type": "array"\n    },\n    "owner": {\n      "description": "The Component instance (or its string name/reference) that owns these OutputPorts. Must be a PsyNeuLink Component subclass instance.",\n      "type": "string"\n    }\n  },\n  "required": [\n    "owner",\n    "output_port_dicts"\n  ],\n  "type": "object"\n}\n\nNotes:\nThe `indices` parameter also accepts a list of integers (one per port dict) for fully explicit index assignment, but the JSON Schema enum above only covers the string keywords; pass a JSON array when you need per-port integer control. The SEQUENTIAL keyword assigns indices by position in `output_port_dicts`, overriding any VARIABLE already set in individual dicts. PRIMARY only fills in ports that have no VARIABLE entry — it does not override pre-specified ones. Each port\'s NAME is registered as a read-only property on the owner\'s class at instantiation time, which is a permanent side-effect on the class (not just the instance). `get_port_dict` returns None (not an error) when the name is not found.'
TOOL_PARAMETERS = { 'properties': { 'indices': { 'description': 'Controls how OWNER_VALUE indices are '
                                              'assigned. PRIMARY assigns (OWNER_VALUE, '
                                              'PRIMARY) to all ports without an '
                                              'explicit VARIABLE; SEQUENTIAL assigns '
                                              'incrementing ints (0, 1, 2, …) to each '
                                              'port in order. Pass a JSON array of '
                                              'ints instead for explicit per-port '
                                              'indices. Omit (null) to leave VARIABLE '
                                              "unset for ports that don't already "
                                              'specify it.',
                               'enum': ['PRIMARY', 'SEQUENTIAL'],
                               'type': 'string'},
                  'output_port_dicts': { 'description': 'List of dicts, each '
                                                        'specifying one standard '
                                                        'OutputPort. All items must be '
                                                        'dicts — non-dict items raise '
                                                        'an error.',
                                         'items': { 'description': 'A dict specifying '
                                                                   'one OutputPort, '
                                                                   'typically '
                                                                   'containing at '
                                                                   'minimum a NAME key '
                                                                   'and optionally '
                                                                   'VARIABLE.',
                                                    'type': 'object'},
                                         'type': 'array'},
                  'owner': { 'description': 'The Component instance (or its string '
                                            'name/reference) that owns these '
                                            'OutputPorts. Must be a PsyNeuLink '
                                            'Component subclass instance.',
                             'type': 'string'}},
  'required': ['owner', 'output_port_dicts'],
  'type': 'object'}
TOOL_NOTES = "The `indices` parameter also accepts a list of integers (one per port dict) for fully explicit index assignment, but the JSON Schema enum above only covers the string keywords; pass a JSON array when you need per-port integer control. The SEQUENTIAL keyword assigns indices by position in `output_port_dicts`, overriding any VARIABLE already set in individual dicts. PRIMARY only fills in ports that have no VARIABLE entry — it does not override pre-specified ones. Each port's NAME is registered as a read-only property on the owner's class at instantiation time, which is a permanent side-effect on the class (not just the instance). `get_port_dict` returns None (not an error) when the name is not found."


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.StandardOutputPorts
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
    def create_standard_output_ports(args: dict[str, Any] | None = None) -> Any:
        'Call this tool when defining or inspecting the standard OutputPort specifications for a custom PsyNeuLink Component class — specifically when you need to instantiate a `StandardOutputPorts` collection that maps named output ports to owner value indices.'
        return _impl(args or {})
