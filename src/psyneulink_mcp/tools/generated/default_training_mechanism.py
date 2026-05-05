"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '0addba16e0ce6776d61c74c71c391976d5e10b22286a6dc2ffee5546c7f34506'
__pnl_qualname__ = 'psyneulink.DefaultTrainingMechanism'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_default_training_mechanism'
TOOL_DESCRIPTION = 'Call this tool to instantiate a DefaultTrainingMechanism (an alias for ObjectiveMechanism) that monitors the output values of one or more mechanisms or ports and evaluates them with a combining function. Use this when building a learning composition that needs a training signal — the result is a mechanism whose OUTCOME output port holds a 1d array representing the evaluated objective value.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "function": {\n      "default": "LinearCombination",\n      "description": "Name or spec of the function used to combine monitored values into the OUTCOME output. Defaults to LinearCombination. Can be any TransformFunction or ObjectiveFunction that accepts a 2d array.",\n      "type": "string"\n    },\n    "monitor": {\n      "description": "List of OutputPorts, Mechanisms, or port specification dicts whose values will be monitored and passed to the function. Each entry can be a string name, a (port, weight, exponent, matrix) tuple, or a dict. Required for meaningful use.",\n      "items": {\n        "type": "string"\n      },\n      "type": "array"\n    },\n    "name": {\n      "description": "Optional string name for the mechanism instance.",\n      "type": "string"\n    },\n    "output_ports": {\n      "default": [\n        "OUTCOME"\n      ],\n      "description": "Output port specifications for the mechanism. Defaults to [OUTCOME]. Only override if additional output ports are needed beyond the standard OUTCOME port.",\n      "items": {\n        "type": "string"\n      },\n      "type": "array"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\nDefaultTrainingMechanism is an alias for ObjectiveMechanism — the class name in error messages and repr will be ObjectiveMechanism. The `monitor` arg maps internally to `input_ports`; each monitored OutputPort gets a MappingProjection to a corresponding InputPort. If `monitor` is omitted or an empty list at construction time, the mechanism gets a single default InputPort with no afferents — you must call `add_to_monitor()` before running. The deprecated `monitored_output_ports` kwarg is accepted for backwards compatibility but raises a warning; always use `monitor`. Per-entry weights and exponents can be specified via tuple syntax (OutputPort, weight, exponent, matrix) in the monitor list and are forwarded to the function\'s `weights`/`exponents` parameters. The OUTCOME output value is a 1d numpy array.'
TOOL_PARAMETERS = { 'properties': { 'function': { 'default': 'LinearCombination',
                                'description': 'Name or spec of the function used to '
                                               'combine monitored values into the '
                                               'OUTCOME output. Defaults to '
                                               'LinearCombination. Can be any '
                                               'TransformFunction or ObjectiveFunction '
                                               'that accepts a 2d array.',
                                'type': 'string'},
                  'monitor': { 'description': 'List of OutputPorts, Mechanisms, or '
                                              'port specification dicts whose values '
                                              'will be monitored and passed to the '
                                              'function. Each entry can be a string '
                                              'name, a (port, weight, exponent, '
                                              'matrix) tuple, or a dict. Required for '
                                              'meaningful use.',
                               'items': {'type': 'string'},
                               'type': 'array'},
                  'name': { 'description': 'Optional string name for the mechanism '
                                           'instance.',
                            'type': 'string'},
                  'output_ports': { 'default': ['OUTCOME'],
                                    'description': 'Output port specifications for the '
                                                   'mechanism. Defaults to [OUTCOME]. '
                                                   'Only override if additional output '
                                                   'ports are needed beyond the '
                                                   'standard OUTCOME port.',
                                    'items': {'type': 'string'},
                                    'type': 'array'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = "DefaultTrainingMechanism is an alias for ObjectiveMechanism — the class name in error messages and repr will be ObjectiveMechanism. The `monitor` arg maps internally to `input_ports`; each monitored OutputPort gets a MappingProjection to a corresponding InputPort. If `monitor` is omitted or an empty list at construction time, the mechanism gets a single default InputPort with no afferents — you must call `add_to_monitor()` before running. The deprecated `monitored_output_ports` kwarg is accepted for backwards compatibility but raises a warning; always use `monitor`. Per-entry weights and exponents can be specified via tuple syntax (OutputPort, weight, exponent, matrix) in the monitor list and are forwarded to the function's `weights`/`exponents` parameters. The OUTCOME output value is a 1d numpy array."


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.DefaultTrainingMechanism
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
    def create_default_training_mechanism(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to instantiate a DefaultTrainingMechanism (an alias for ObjectiveMechanism) that monitors the output values of one or more mechanisms or ports and evaluates them with a combining function.'
        return _impl(args or {})
