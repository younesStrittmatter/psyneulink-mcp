"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '471c65452d591ff8e0270afdeb8e535a0f97b3b23673c7bc21e9c32a6524cf80'
__pnl_qualname__ = 'psyneulink.core.components.mechanisms.processing.integratormechanism.ProcessingMechanism_Base'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_processing_mechanism__base'
TOOL_DESCRIPTION = 'Do NOT call this tool directly — ProcessingMechanism_Base is an abstract base class that cannot be instantiated. Use the concrete `ProcessingMechanism` tool or a specific subclass (e.g., TransferMechanism, IntegratorMechanism) instead. This tool exists only as a reference entry; attempting to instantiate it will raise an error.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "default_variable": {\n      "description": "The default input value for the mechanism. Sets the shape/dtype expected on each execution.",\n      "items": {},\n      "type": "array"\n    },\n    "function": {\n      "description": "The function applied to the mechanism\'s input to produce its output. Must be a PsyNeuLink Function or a Python callable.",\n      "type": "string"\n    },\n    "input_ports": {\n      "description": "Specification of the mechanism\'s input ports. Can be a list of port specs, names, or dicts.",\n      "items": {},\n      "type": "array"\n    },\n    "input_shapes": {\n      "description": "Integer or list of integers specifying the size of each input port. Alternative to default_variable for shape specification.",\n      "oneOf": [\n        {\n          "type": "integer"\n        },\n        {\n          "items": {\n            "type": "integer"\n          },\n          "type": "array"\n        }\n      ]\n    },\n    "name": {\n      "description": "String name for the mechanism instance, used in logs and graph visualizations.",\n      "type": "string"\n    },\n    "output_ports": {\n      "description": "Specification of the mechanism\'s output ports. Can be names from standard_output_port_names (e.g. MEAN, MEDIAN, VARIANCE, MAX_VAL, MAX_ONE_HOT, PROB) or custom port dicts.",\n      "items": {},\n      "type": "array"\n    },\n    "params": {\n      "description": "Dictionary of parameter overrides. Rarely needed; prefer explicit keyword arguments.",\n      "type": "object"\n    },\n    "prefs": {\n      "description": "PreferenceSet or dict of preference settings for this instance. Omit to use class defaults.",\n      "type": "object"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\nProcessingMechanism_Base is abstract and must never be instantiated directly — the docstring explicitly forbids it. Calling this tool will raise an error at runtime. Always use the concrete ProcessingMechanism subclass tools instead. The class defines a rich set of standard_output_ports beyond the Mechanism_Base defaults: MEAN, MEDIAN, STANDARD_DEVIATION, VARIANCE, MAX_VAL, MAX_ABS_VAL, MAX_ONE_HOT, MAX_ABS_ONE_HOT, MAX_INDICATOR, MAX_ABS_INDICATOR, and PROB (SoftMax); these names can be passed in output_ports to any concrete subclass.'
TOOL_PARAMETERS = { 'properties': { 'default_variable': { 'description': 'The default input value for '
                                                       'the mechanism. Sets the '
                                                       'shape/dtype expected on each '
                                                       'execution.',
                                        'items': {},
                                        'type': 'array'},
                  'function': { 'description': 'The function applied to the '
                                               "mechanism's input to produce its "
                                               'output. Must be a PsyNeuLink Function '
                                               'or a Python callable.',
                                'type': 'string'},
                  'input_ports': { 'description': "Specification of the mechanism's "
                                                  'input ports. Can be a list of port '
                                                  'specs, names, or dicts.',
                                   'items': {},
                                   'type': 'array'},
                  'input_shapes': { 'description': 'Integer or list of integers '
                                                   'specifying the size of each input '
                                                   'port. Alternative to '
                                                   'default_variable for shape '
                                                   'specification.',
                                    'oneOf': [ {'type': 'integer'},
                                               { 'items': {'type': 'integer'},
                                                 'type': 'array'}]},
                  'name': { 'description': 'String name for the mechanism instance, '
                                           'used in logs and graph visualizations.',
                            'type': 'string'},
                  'output_ports': { 'description': "Specification of the mechanism's "
                                                   'output ports. Can be names from '
                                                   'standard_output_port_names (e.g. '
                                                   'MEAN, MEDIAN, VARIANCE, MAX_VAL, '
                                                   'MAX_ONE_HOT, PROB) or custom port '
                                                   'dicts.',
                                    'items': {},
                                    'type': 'array'},
                  'params': { 'description': 'Dictionary of parameter overrides. '
                                             'Rarely needed; prefer explicit keyword '
                                             'arguments.',
                              'type': 'object'},
                  'prefs': { 'description': 'PreferenceSet or dict of preference '
                                            'settings for this instance. Omit to use '
                                            'class defaults.',
                             'type': 'object'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = 'ProcessingMechanism_Base is abstract and must never be instantiated directly — the docstring explicitly forbids it. Calling this tool will raise an error at runtime. Always use the concrete ProcessingMechanism subclass tools instead. The class defines a rich set of standard_output_ports beyond the Mechanism_Base defaults: MEAN, MEDIAN, STANDARD_DEVIATION, VARIANCE, MAX_VAL, MAX_ABS_VAL, MAX_ONE_HOT, MAX_ABS_ONE_HOT, MAX_INDICATOR, MAX_ABS_INDICATOR, and PROB (SoftMax); these names can be passed in output_ports to any concrete subclass.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.ProcessingMechanism_Base
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
    def create_processing_mechanism__base(args: dict[str, Any] | None = None) -> Any:
        'Do NOT call this tool directly — ProcessingMechanism_Base is an abstract base class that cannot be instantiated.'
        return _impl(args or {})
