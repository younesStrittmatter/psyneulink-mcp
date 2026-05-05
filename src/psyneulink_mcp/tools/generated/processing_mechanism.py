"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = 'dfe35aa28c6336d5e8f33aa743164f840aca153be35e4f5a8089509929428014'
__pnl_qualname__ = 'psyneulink.ProcessingMechanism'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_processing_mechanism'
TOOL_DESCRIPTION = 'Call this tool to create a general-purpose ProcessingMechanism node in a PsyNeuLink Composition — use it when no more specialized subclass (TransferMechanism, IntegratorMechanism, etc.) fits the task, or when you need a lightweight node with a custom function. Returns a ProcessingMechanism instance that can be added to a Composition and connected via Projections.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "default_variable": {\n      "description": "Template for the input value(s). Each top-level element defines one InputPort. Overrides input_shapes if both are given.",\n      "items": {},\n      "type": "array"\n    },\n    "function": {\n      "description": "The function applied to each input array. Accepts a PsyNeuLink Function instance (e.g., Linear, Logistic) or a Python callable. Defaults to the identity Linear function if omitted.",\n      "type": "object"\n    },\n    "input_ports": {\n      "description": "Explicit InputPort specification(s). Accepts a list of port names (strings), dicts, or InputPort objects. Rarely needed \\u2014 omit to let default_variable/input_shapes define inputs.",\n      "items": {},\n      "type": "array"\n    },\n    "input_shapes": {\n      "description": "Shorthand for specifying input dimensionality. An integer means a single 1-D InputPort of that length; a list of integers creates one InputPort per element. Ignored when default_variable is provided.",\n      "oneOf": [\n        {\n          "minimum": 1,\n          "type": "integer"\n        },\n        {\n          "items": {\n            "minimum": 1,\n            "type": "integer"\n          },\n          "type": "array"\n        }\n      ]\n    },\n    "name": {\n      "description": "Label for this mechanism; used in Composition graphs and log output.",\n      "type": "string"\n    },\n    "output_ports": {\n      "description": "OutputPort specification(s). Pass a list of port name strings or dicts. Standard names include \'MEAN\', \'MEDIAN\', \'STANDARD_DEVIATION\', \'VARIANCE\', \'MAX_VAL\', \'MAX_ABS_VAL\', \'MAX_ONE_HOT\', \'MAX_ABS_ONE_HOT\', \'MAX_INDICATOR\', \'MAX_ABS_INDICATOR\', \'PROB\'. Omit to auto-create default output port(s).",\n      "oneOf": [\n        {\n          "type": "string"\n        },\n        {\n          "items": {},\n          "type": "array"\n        }\n      ]\n    },\n    "params": {\n      "description": "Optional dict of parameter overrides passed directly to the base Mechanism constructor.",\n      "type": "object"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\nWhen the mechanism has more than one InputPort AND the function is a TransferFunction subclass, OutputPorts are auto-created one-per-InputPort and named after their corresponding InputPort — passing explicit output_ports that number fewer than the inputs triggers partial auto-fill logic rather than an error. Standard output port names (MEAN, MAX_VAL, etc.) operate on axis-0 of the mechanism value; they are additive — include them in output_ports alongside the default port if you need both raw and derived outputs. input_shapes and default_variable are mutually exclusive; if both are supplied, default_variable wins. The prefs parameter is rarely needed from agent code — omit it.'
TOOL_PARAMETERS = { 'properties': { 'default_variable': { 'description': 'Template for the input '
                                                       'value(s). Each top-level '
                                                       'element defines one InputPort. '
                                                       'Overrides input_shapes if both '
                                                       'are given.',
                                        'items': {},
                                        'type': 'array'},
                  'function': { 'description': 'The function applied to each input '
                                               'array. Accepts a PsyNeuLink Function '
                                               'instance (e.g., Linear, Logistic) or a '
                                               'Python callable. Defaults to the '
                                               'identity Linear function if omitted.',
                                'type': 'object'},
                  'input_ports': { 'description': 'Explicit InputPort '
                                                  'specification(s). Accepts a list of '
                                                  'port names (strings), dicts, or '
                                                  'InputPort objects. Rarely needed — '
                                                  'omit to let '
                                                  'default_variable/input_shapes '
                                                  'define inputs.',
                                   'items': {},
                                   'type': 'array'},
                  'input_shapes': { 'description': 'Shorthand for specifying input '
                                                   'dimensionality. An integer means a '
                                                   'single 1-D InputPort of that '
                                                   'length; a list of integers creates '
                                                   'one InputPort per element. Ignored '
                                                   'when default_variable is provided.',
                                    'oneOf': [ {'minimum': 1, 'type': 'integer'},
                                               { 'items': { 'minimum': 1,
                                                            'type': 'integer'},
                                                 'type': 'array'}]},
                  'name': { 'description': 'Label for this mechanism; used in '
                                           'Composition graphs and log output.',
                            'type': 'string'},
                  'output_ports': { 'description': 'OutputPort specification(s). Pass '
                                                   'a list of port name strings or '
                                                   'dicts. Standard names include '
                                                   "'MEAN', 'MEDIAN', "
                                                   "'STANDARD_DEVIATION', 'VARIANCE', "
                                                   "'MAX_VAL', 'MAX_ABS_VAL', "
                                                   "'MAX_ONE_HOT', 'MAX_ABS_ONE_HOT', "
                                                   "'MAX_INDICATOR', "
                                                   "'MAX_ABS_INDICATOR', 'PROB'. Omit "
                                                   'to auto-create default output '
                                                   'port(s).',
                                    'oneOf': [ {'type': 'string'},
                                               {'items': {}, 'type': 'array'}]},
                  'params': { 'description': 'Optional dict of parameter overrides '
                                             'passed directly to the base Mechanism '
                                             'constructor.',
                              'type': 'object'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = 'When the mechanism has more than one InputPort AND the function is a TransferFunction subclass, OutputPorts are auto-created one-per-InputPort and named after their corresponding InputPort — passing explicit output_ports that number fewer than the inputs triggers partial auto-fill logic rather than an error. Standard output port names (MEAN, MAX_VAL, etc.) operate on axis-0 of the mechanism value; they are additive — include them in output_ports alongside the default port if you need both raw and derived outputs. input_shapes and default_variable are mutually exclusive; if both are supplied, default_variable wins. The prefs parameter is rarely needed from agent code — omit it.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.ProcessingMechanism
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
    def create_processing_mechanism(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to create a general-purpose ProcessingMechanism node in a PsyNeuLink Composition — use it when no more specialized subclass (TransferMechanism, IntegratorMechanism, etc.) fits the task, or when you need a lightweight node with a custom function.'
        return _impl(args or {})
