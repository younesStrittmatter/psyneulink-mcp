"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = 'a19c4e2c6e45641361eba5168a30834dbec8c93ac1175809ae2a0e0ee1e45012'
__pnl_qualname__ = 'psyneulink.core.components.mechanisms.modulatory.control.controlmechanism.validate_monitored_port_spec'
__pnl_kind__ = 'function'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'validate_monitored_port_spec'
TOOL_DESCRIPTION = 'Call this tool to validate a list of monitored-port specifications before or during ControlMechanism construction. It resolves each entry in spec_list (OutputPort, Mechanism, MonitoredOutputPortTuple, tuple, or dict forms) and raises a ControlMechanismError immediately if any spec cannot be resolved to a valid OutputPort or Mechanism. No return value on success.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "owner": {\n      "description": "Name of the ControlMechanism that owns the monitored-port specs; used in error messages and for port-spec parsing context.",\n      "type": "string"\n    },\n    "spec_list": {\n      "description": "List of monitored-output-port specifications to validate. Each element may be an OutputPort name (string), a Mechanism name (string), a dict representing an InputPort specification, or a two-element array [port_spec, weight] tuple.",\n      "items": {\n        "oneOf": [\n          {\n            "type": "string"\n          },\n          {\n            "type": "object"\n          },\n          {\n            "type": "array"\n          }\n        ]\n      },\n      "type": "array"\n    }\n  },\n  "required": [\n    "owner",\n    "spec_list"\n  ],\n  "type": "object"\n}\n\nNotes:\nThis is a validation-only function; it returns None on success and raises ControlMechanismError on the first invalid spec. It is an internal helper — calling it requires that `owner` is an already-instantiated ControlMechanism object, not just a name string. Spec types that are Mechanism subclasses (not instances) are explicitly rejected with a descriptive error. Non-OutputPort Port subclasses (e.g., InputPort) are also explicitly rejected. Dict specs are parsed as InputPort specification dicts and the first projection target is extracted to check validity.'
TOOL_PARAMETERS = { 'properties': { 'owner': { 'description': 'Name of the ControlMechanism that owns '
                                            'the monitored-port specs; used in error '
                                            'messages and for port-spec parsing '
                                            'context.',
                             'type': 'string'},
                  'spec_list': { 'description': 'List of monitored-output-port '
                                                'specifications to validate. Each '
                                                'element may be an OutputPort name '
                                                '(string), a Mechanism name (string), '
                                                'a dict representing an InputPort '
                                                'specification, or a two-element array '
                                                '[port_spec, weight] tuple.',
                                 'items': { 'oneOf': [ {'type': 'string'},
                                                       {'type': 'object'},
                                                       {'type': 'array'}]},
                                 'type': 'array'}},
  'required': ['owner', 'spec_list'],
  'type': 'object'}
TOOL_NOTES = 'This is a validation-only function; it returns None on success and raises ControlMechanismError on the first invalid spec. It is an internal helper — calling it requires that `owner` is an already-instantiated ControlMechanism object, not just a name string. Spec types that are Mechanism subclasses (not instances) are explicitly rejected with a descriptive error. Non-OutputPort Port subclasses (e.g., InputPort) are also explicitly rejected. Dict specs are parsed as InputPort specification dicts and the first projection target is extracted to check validity.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.validate_monitored_port_spec
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
    def validate_monitored_port_spec(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to validate a list of monitored-port specifications before or during ControlMechanism construction.'
        return _impl(args or {})
