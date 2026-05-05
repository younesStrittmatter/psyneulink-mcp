"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '8258de96de46fc56d48b2aa0e20cf8784c99e5929d7037a271479332e7b16c70'
__pnl_qualname__ = 'psyneulink.PredictionErrorMechanism'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_prediction_error_mechanism'
TOOL_DESCRIPTION = 'Call this tool when building a reinforcement learning or temporal-difference model that needs a prediction error signal — specifically, when you have a predicted reward (sample) and an actual reward (target) and want to compute the delta used to drive learning. Returns an OUTCOME OutputPort containing the element-wise prediction error array, shifted so the final timestep error is always 0 (per the TD convention in Montague et al.).\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "function": {\n      "description": "Function used to compute prediction error from sample and target. Defaults to PredictionErrorDeltaFunction (TD delta). Specify as a string name or omit for default.",\n      "type": "string"\n    },\n    "learning_rate": {\n      "default": 0.3,\n      "description": "Controls weighting of later timesteps vs earlier ones in the delta calculation. Higher values weight later timesteps more. Default is 0.3.",\n      "type": "number"\n    },\n    "name": {\n      "description": "Optional name for the mechanism instance. Used for identification in the Composition graph.",\n      "type": "string"\n    },\n    "output_ports": {\n      "description": "Output ports to expose. Defaults to [OUTCOME], which is the primary output containing the prediction error vector. Rarely needs to be changed.",\n      "items": {\n        "type": "string"\n      },\n      "type": "array"\n    },\n    "sample": {\n      "description": "The SAMPLE InputPort source \\u2014 the predicted reward signal. Specify as a Mechanism name, OutputPort name, or numeric value. Evaluated by the function against target.",\n      "type": "string"\n    },\n    "target": {\n      "description": "The TARGET InputPort source \\u2014 the actual reward signal. Used by the function to evaluate the sample (predicted reward).",\n      "type": "string"\n    }\n  },\n  "required": [\n    "sample",\n    "target"\n  ],\n  "type": "object"\n}\n\nNotes:\nThe output delta array is shifted: the first element of the raw TD delta is dropped and a 0 is appended at the end, so the array length matches the input but the final timestep error is always 0. This matches the Montague et al. TD convention. `sample` and `target` accept OutputPort objects, Mechanism instances, dicts, numbers, or strings — when called via MCP, pass the name of the source Mechanism or OutputPort as a string and let PNL resolve the connection. `learning_rate` is modulable at runtime (can be changed after construction). The mechanism inherits all ComparatorMechanism arguments (e.g., `default_variable`, `size`, `input_ports`) via **kwargs but these are rarely needed.'
TOOL_PARAMETERS = { 'properties': { 'function': { 'description': 'Function used to compute prediction '
                                               'error from sample and target. Defaults '
                                               'to PredictionErrorDeltaFunction (TD '
                                               'delta). Specify as a string name or '
                                               'omit for default.',
                                'type': 'string'},
                  'learning_rate': { 'default': 0.3,
                                     'description': 'Controls weighting of later '
                                                    'timesteps vs earlier ones in the '
                                                    'delta calculation. Higher values '
                                                    'weight later timesteps more. '
                                                    'Default is 0.3.',
                                     'type': 'number'},
                  'name': { 'description': 'Optional name for the mechanism instance. '
                                           'Used for identification in the Composition '
                                           'graph.',
                            'type': 'string'},
                  'output_ports': { 'description': 'Output ports to expose. Defaults '
                                                   'to [OUTCOME], which is the primary '
                                                   'output containing the prediction '
                                                   'error vector. Rarely needs to be '
                                                   'changed.',
                                    'items': {'type': 'string'},
                                    'type': 'array'},
                  'sample': { 'description': 'The SAMPLE InputPort source — the '
                                             'predicted reward signal. Specify as a '
                                             'Mechanism name, OutputPort name, or '
                                             'numeric value. Evaluated by the function '
                                             'against target.',
                              'type': 'string'},
                  'target': { 'description': 'The TARGET InputPort source — the actual '
                                             'reward signal. Used by the function to '
                                             'evaluate the sample (predicted reward).',
                              'type': 'string'}},
  'required': ['sample', 'target'],
  'type': 'object'}
TOOL_NOTES = 'The output delta array is shifted: the first element of the raw TD delta is dropped and a 0 is appended at the end, so the array length matches the input but the final timestep error is always 0. This matches the Montague et al. TD convention. `sample` and `target` accept OutputPort objects, Mechanism instances, dicts, numbers, or strings — when called via MCP, pass the name of the source Mechanism or OutputPort as a string and let PNL resolve the connection. `learning_rate` is modulable at runtime (can be changed after construction). The mechanism inherits all ComparatorMechanism arguments (e.g., `default_variable`, `size`, `input_ports`) via **kwargs but these are rarely needed.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.PredictionErrorMechanism
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
    def create_prediction_error_mechanism(args: dict[str, Any] | None = None) -> Any:
        'Call this tool when building a reinforcement learning or temporal-difference model that needs a prediction error signal — specifically, when you have a predicted reward (sample) and an actual reward (target) and want to compute the delta used to drive learning.'
        return _impl(args or {})
