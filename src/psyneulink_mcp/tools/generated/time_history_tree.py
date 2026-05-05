"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '8d3fd8706476bd43e53c847cf46c707201eefabbcf231af846ffc80436783a53'
__pnl_qualname__ = 'psyneulink.TimeHistoryTree'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_time_history_tree'
TOOL_DESCRIPTION = 'Call this tool to instantiate a TimeHistoryTree when you need a hierarchical time-tracking structure for a PsyNeuLink simulation — specifically to record how many units of each TimeScale have elapsed and to query counts across nested scopes (e.g., how many PASS intervals occurred in a given ENVIRONMENT_STATE_UPDATE). The result is a tree object whose root represents LIFE-scale time, with children representing successively finer TimeScale intervals down to max_depth.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "enable_current_time": {\n      "default": true,\n      "description": "Whether this tree maintains a current_time and previous_time Time object. Should be True for the root (LIFE-scale) node only; child nodes created internally always use False.",\n      "type": "boolean"\n    },\n    "index": {\n      "default": 0,\n      "description": "Position of this node in its parent\'s children list. Leave at 0 for root nodes.",\n      "type": "integer"\n    },\n    "max_depth": {\n      "default": "ENVIRONMENT_STATE_UPDATE",\n      "description": "The finest-grain TimeScale for which subtrees are created. Finer values (e.g. \'CONSIDERATION_SET_EXECUTION\') enable more precise queries but consume significantly more memory in large simulations.",\n      "enum": [\n        "LIFE",\n        "ENVIRONMENT_SEQUENCE",\n        "ENVIRONMENT_STATE_UPDATE",\n        "PASS",\n        "CONSIDERATION_SET_EXECUTION"\n      ],\n      "type": "string"\n    },\n    "time_scale": {\n      "default": "LIFE",\n      "description": "The TimeScale unit this tree/node represents. Root trees should use \'LIFE\' (default). Non-root trees should match the child_time_scale of their parent.",\n      "enum": [\n        "LIFE",\n        "ENVIRONMENT_SEQUENCE",\n        "ENVIRONMENT_STATE_UPDATE",\n        "PASS",\n        "CONSIDERATION_SET_EXECUTION"\n      ],\n      "type": "string"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\nThe `parent` constructor argument is omitted from the schema — it accepts another TimeHistoryTree instance, which cannot be meaningfully serialized to JSON; child nodes should be created by calling increment_time on the root rather than constructed directly. The docstring\'s TimeScale names (TRIAL, TIME_STEP, PASS) are legacy aliases; the source uses ENVIRONMENT_STATE_UPDATE and CONSIDERATION_SET_EXECUTION — always use the latter names. Setting enable_current_time=True on a non-root node (time_scale != LIFE) is technically allowed but semantically incorrect; only root nodes should track current_time. total_times only contains entries for TimeScales finer than time_scale, so querying the root for LIFE counts will raise an error.'
TOOL_PARAMETERS = { 'properties': { 'enable_current_time': { 'default': True,
                                           'description': 'Whether this tree maintains '
                                                          'a current_time and '
                                                          'previous_time Time object. '
                                                          'Should be True for the root '
                                                          '(LIFE-scale) node only; '
                                                          'child nodes created '
                                                          'internally always use '
                                                          'False.',
                                           'type': 'boolean'},
                  'index': { 'default': 0,
                             'description': "Position of this node in its parent's "
                                            'children list. Leave at 0 for root nodes.',
                             'type': 'integer'},
                  'max_depth': { 'default': 'ENVIRONMENT_STATE_UPDATE',
                                 'description': 'The finest-grain TimeScale for which '
                                                'subtrees are created. Finer values '
                                                "(e.g. 'CONSIDERATION_SET_EXECUTION') "
                                                'enable more precise queries but '
                                                'consume significantly more memory in '
                                                'large simulations.',
                                 'enum': [ 'LIFE',
                                           'ENVIRONMENT_SEQUENCE',
                                           'ENVIRONMENT_STATE_UPDATE',
                                           'PASS',
                                           'CONSIDERATION_SET_EXECUTION'],
                                 'type': 'string'},
                  'time_scale': { 'default': 'LIFE',
                                  'description': 'The TimeScale unit this tree/node '
                                                 'represents. Root trees should use '
                                                 "'LIFE' (default). Non-root trees "
                                                 'should match the child_time_scale of '
                                                 'their parent.',
                                  'enum': [ 'LIFE',
                                            'ENVIRONMENT_SEQUENCE',
                                            'ENVIRONMENT_STATE_UPDATE',
                                            'PASS',
                                            'CONSIDERATION_SET_EXECUTION'],
                                  'type': 'string'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = "The `parent` constructor argument is omitted from the schema — it accepts another TimeHistoryTree instance, which cannot be meaningfully serialized to JSON; child nodes should be created by calling increment_time on the root rather than constructed directly. The docstring's TimeScale names (TRIAL, TIME_STEP, PASS) are legacy aliases; the source uses ENVIRONMENT_STATE_UPDATE and CONSIDERATION_SET_EXECUTION — always use the latter names. Setting enable_current_time=True on a non-root node (time_scale != LIFE) is technically allowed but semantically incorrect; only root nodes should track current_time. total_times only contains entries for TimeScales finer than time_scale, so querying the root for LIFE counts will raise an error."


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.TimeHistoryTree
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
    def create_time_history_tree(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to instantiate a TimeHistoryTree when you need a hierarchical time-tracking structure for a PsyNeuLink simulation — specifically to record how many units of each TimeScale have elapsed and to query counts across nested scopes (e.g., how many PASS intervals occurred in a given ENVIRONMENT_STATE_UPDATE).'
        return _impl(args or {})
