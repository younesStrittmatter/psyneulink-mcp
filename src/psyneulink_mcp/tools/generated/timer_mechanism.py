"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '53409d532fb7abc3a4644e3399f8c8f71e57711e4fbe0d45b2adde46718e1e36'
__pnl_qualname__ = 'psyneulink.TimerMechanism'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_timer_mechanism'
TOOL_DESCRIPTION = 'Call this tool to create a TimerMechanism — a countdown/timer node that advances a value from `start` toward `end` over a shaped trajectory, stopping when either the accumulated input reaches `duration` or the trajectory output reaches `end`. The result is a configured TimerMechanism object whose `finished` attribute becomes True once the stopping condition is met, at which point its output freezes at the terminal value.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "duration": {\n      "default": 1,\n      "description": "Accumulated input value (variable) at which the timer stops and sets finished=True. Distinct from \'end\': duration gates on the integrator\'s cumulative input, end gates on the trajectory output. Default 1.",\n      "type": "number"\n    },\n    "end": {\n      "default": 1,\n      "description": "Trajectory output value at which the timer stops advancing. Default 1.",\n      "type": "number"\n    },\n    "increment": {\n      "default": 0.01,\n      "description": "Amount added to previous_value each execution when no external input is provided; mapped to the rate of the integrator function. Default in Parameters class is 0.01 (docstring says 1 \\u2014 use 0.01 for reliable behavior).",\n      "type": "number"\n    },\n    "input_shapes": {\n      "default": 1,\n      "description": "Size of the input/output vector. If start/end/duration are arrays they must match this length. Default 1.",\n      "type": "integer"\n    },\n    "name": {\n      "description": "Optional name for the mechanism.",\n      "type": "string"\n    },\n    "reset_default": {\n      "default": 0,\n      "description": "Default value used for the reset parameter at runtime. Non-zero triggers a reset to start. Default 0.",\n      "type": "number"\n    },\n    "start": {\n      "default": 0,\n      "description": "Starting value of the timer\'s output trajectory. Passed as the \'initial\' parameter of the trajectory function. Default 0.",\n      "type": "number"\n    },\n    "trajectory": {\n      "default": "LinearTimer",\n      "description": "Name of the TimerFunction that shapes the output trajectory. Must be one of the supported TimerFunction subclasses (e.g., \'LinearTimer\', \'ExponentialTimer\'). Default \'LinearTimer\'.",\n      "type": "string"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\n1. **increment default discrepancy**: the docstring advertises default 1 but the Parameters class sets it to 0.01; trust the Parameters class (0.01).\n2. **trajectory must be a TimerFunction**: passing an arbitrary TransferFunction will raise a validation error. Only TimerFunction subclasses (e.g., LinearTimer, ExponentialTimer) are accepted.\n3. **Two distinct stopping conditions**: `duration` stops the integrator when the cumulative *input* reaches that value; `end` stops advancement when the *trajectory output* reaches that value. Both are checked and both default to 1.\n4. **finished freezes output**: once `finished=True`, every subsequent execution returns the same terminal value without further integration.\n5. **runtime reset**: the `reset` attribute (not a constructor arg) is a runtime parameter — passing a non-zero value during execution triggers `reset()`, restoring the timer to `start` and clearing `finished`.\n6. **trajectory is passed as a class/instance, not a string**: in the actual PNL call the trajectory value should be the class object (e.g., `LinearTimer`) or an instance, not a string. The schema uses string for agent convenience; the host template must resolve it.'
TOOL_PARAMETERS = { 'properties': { 'duration': { 'default': 1,
                                'description': 'Accumulated input value (variable) at '
                                               'which the timer stops and sets '
                                               "finished=True. Distinct from 'end': "
                                               "duration gates on the integrator's "
                                               'cumulative input, end gates on the '
                                               'trajectory output. Default 1.',
                                'type': 'number'},
                  'end': { 'default': 1,
                           'description': 'Trajectory output value at which the timer '
                                          'stops advancing. Default 1.',
                           'type': 'number'},
                  'increment': { 'default': 0.01,
                                 'description': 'Amount added to previous_value each '
                                                'execution when no external input is '
                                                'provided; mapped to the rate of the '
                                                'integrator function. Default in '
                                                'Parameters class is 0.01 (docstring '
                                                'says 1 — use 0.01 for reliable '
                                                'behavior).',
                                 'type': 'number'},
                  'input_shapes': { 'default': 1,
                                    'description': 'Size of the input/output vector. '
                                                   'If start/end/duration are arrays '
                                                   'they must match this length. '
                                                   'Default 1.',
                                    'type': 'integer'},
                  'name': { 'description': 'Optional name for the mechanism.',
                            'type': 'string'},
                  'reset_default': { 'default': 0,
                                     'description': 'Default value used for the reset '
                                                    'parameter at runtime. Non-zero '
                                                    'triggers a reset to start. '
                                                    'Default 0.',
                                     'type': 'number'},
                  'start': { 'default': 0,
                             'description': "Starting value of the timer's output "
                                            "trajectory. Passed as the 'initial' "
                                            'parameter of the trajectory function. '
                                            'Default 0.',
                             'type': 'number'},
                  'trajectory': { 'default': 'LinearTimer',
                                  'description': 'Name of the TimerFunction that '
                                                 'shapes the output trajectory. Must '
                                                 'be one of the supported '
                                                 'TimerFunction subclasses (e.g., '
                                                 "'LinearTimer', 'ExponentialTimer'). "
                                                 "Default 'LinearTimer'.",
                                  'type': 'string'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = '1. **increment default discrepancy**: the docstring advertises default 1 but the Parameters class sets it to 0.01; trust the Parameters class (0.01).\n2. **trajectory must be a TimerFunction**: passing an arbitrary TransferFunction will raise a validation error. Only TimerFunction subclasses (e.g., LinearTimer, ExponentialTimer) are accepted.\n3. **Two distinct stopping conditions**: `duration` stops the integrator when the cumulative *input* reaches that value; `end` stops advancement when the *trajectory output* reaches that value. Both are checked and both default to 1.\n4. **finished freezes output**: once `finished=True`, every subsequent execution returns the same terminal value without further integration.\n5. **runtime reset**: the `reset` attribute (not a constructor arg) is a runtime parameter — passing a non-zero value during execution triggers `reset()`, restoring the timer to `start` and clearing `finished`.\n6. **trajectory is passed as a class/instance, not a string**: in the actual PNL call the trajectory value should be the class object (e.g., `LinearTimer`) or an instance, not a string. The schema uses string for agent convenience; the host template must resolve it.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.TimerMechanism
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
    def create_timer_mechanism(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to create a TimerMechanism — a countdown/timer node that advances a value from `start` toward `end` over a shaped trajectory, stopping when either the accumulated input reaches `duration` or the trajectory output reaches `end`.'
        return _impl(args or {})
