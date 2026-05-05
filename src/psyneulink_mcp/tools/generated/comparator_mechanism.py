"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = 'f5b5f0212ccb22afb99f5a2cb43eb521fa1f945d7171aaefa15ec635da73cd1f'
__pnl_qualname__ = 'psyneulink.ComparatorMechanism'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_comparator_mechanism'
TOOL_DESCRIPTION = 'Call this tool to create a ComparatorMechanism that computes the difference (or other comparison) between two values in a PsyNeuLink composition — typically to measure prediction error, compare network output to a target, or drive learning. Returns a mechanism whose OUTCOME output port holds the element-wise comparison result; additional output ports SUM, SSE, and MSE are available for scalar loss aggregation.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "function": {\n      "description": "Function used to compare sample and target. Defaults to LinearCombination(weights=[[-1],[1]]), which computes element-wise (target - sample). Can be any TransformFunction or a Python callable accepting a 2D array with two rows and returning a 1D array.",\n      "type": "string"\n    },\n    "input_ports": {\n      "description": "List of exactly two InputPort specifications (names, dicts, or values) for the SAMPLE and TARGET inputs respectively. Defaults to [\'SAMPLE\', \'TARGET\']. Override to rename ports or specify explicit variable shapes.",\n      "items": {\n        "type": "string"\n      },\n      "type": "array"\n    },\n    "name": {\n      "description": "Optional string name for the mechanism instance.",\n      "type": "string"\n    },\n    "output_ports": {\n      "description": "List of output port names to include. Default is [\'OUTCOME\']. Standard options also include \'SUM\' (sum of comparison array), \'SSE\' (sum of squared errors), \'MSE\' (mean squared error).",\n      "items": {\n        "type": "string"\n      },\n      "type": "array"\n    },\n    "sample": {\n      "description": "Name or reference to the OutputPort or Mechanism whose value is the \'predicted\' or \'actual\' value being compared. Must have the same shape as target.",\n      "type": "string"\n    },\n    "target": {\n      "description": "Name or reference to the OutputPort or Mechanism whose value is the \'desired\' or \'ground truth\' value. Must have the same shape as sample.",\n      "type": "string"\n    }\n  },\n  "required": [\n    "sample",\n    "target"\n  ],\n  "type": "object"\n}\n\nNotes:\n- Both sample and target must refer to values of identical length/shape; a ComparatorMechanismError is raised otherwise.\n- The default function is LinearCombination(weights=[[-1],[1]]), which produces (target − sample) element-wise — NOT absolute difference or MSE. For scalar loss use the SSE or MSE output ports.\n- In a Composition, PsyNeuLink automatically requires projections to both the SAMPLE and TARGET InputPorts; both must be connected or composition validation will fail.\n- input_ports must be exactly two items if specified; any other count raises an error.\n- The OUTCOME output port value is a 1D array (same length as sample/target), not a scalar. Use the SUM/SSE/MSE output ports when a scalar is needed downstream.\n- sample and target are parsed at construction time via _parse_port_spec; passing a Mechanism name string will work only if the Mechanism is already instantiated in scope.'
TOOL_PARAMETERS = { 'properties': { 'function': { 'description': 'Function used to compare sample and '
                                               'target. Defaults to '
                                               'LinearCombination(weights=[[-1],[1]]), '
                                               'which computes element-wise (target - '
                                               'sample). Can be any TransformFunction '
                                               'or a Python callable accepting a 2D '
                                               'array with two rows and returning a 1D '
                                               'array.',
                                'type': 'string'},
                  'input_ports': { 'description': 'List of exactly two InputPort '
                                                  'specifications (names, dicts, or '
                                                  'values) for the SAMPLE and TARGET '
                                                  'inputs respectively. Defaults to '
                                                  "['SAMPLE', 'TARGET']. Override to "
                                                  'rename ports or specify explicit '
                                                  'variable shapes.',
                                   'items': {'type': 'string'},
                                   'type': 'array'},
                  'name': { 'description': 'Optional string name for the mechanism '
                                           'instance.',
                            'type': 'string'},
                  'output_ports': { 'description': 'List of output port names to '
                                                   "include. Default is ['OUTCOME']. "
                                                   'Standard options also include '
                                                   "'SUM' (sum of comparison array), "
                                                   "'SSE' (sum of squared errors), "
                                                   "'MSE' (mean squared error).",
                                    'items': {'type': 'string'},
                                    'type': 'array'},
                  'sample': { 'description': 'Name or reference to the OutputPort or '
                                             "Mechanism whose value is the 'predicted' "
                                             "or 'actual' value being compared. Must "
                                             'have the same shape as target.',
                              'type': 'string'},
                  'target': { 'description': 'Name or reference to the OutputPort or '
                                             "Mechanism whose value is the 'desired' "
                                             "or 'ground truth' value. Must have the "
                                             'same shape as sample.',
                              'type': 'string'}},
  'required': ['sample', 'target'],
  'type': 'object'}
TOOL_NOTES = '- Both sample and target must refer to values of identical length/shape; a ComparatorMechanismError is raised otherwise.\n- The default function is LinearCombination(weights=[[-1],[1]]), which produces (target − sample) element-wise — NOT absolute difference or MSE. For scalar loss use the SSE or MSE output ports.\n- In a Composition, PsyNeuLink automatically requires projections to both the SAMPLE and TARGET InputPorts; both must be connected or composition validation will fail.\n- input_ports must be exactly two items if specified; any other count raises an error.\n- The OUTCOME output port value is a 1D array (same length as sample/target), not a scalar. Use the SUM/SSE/MSE output ports when a scalar is needed downstream.\n- sample and target are parsed at construction time via _parse_port_spec; passing a Mechanism name string will work only if the Mechanism is already instantiated in scope.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.ComparatorMechanism
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
    def create_comparator_mechanism(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to create a ComparatorMechanism that computes the difference (or other comparison) between two values in a PsyNeuLink composition — typically to measure prediction error, compare network output to a target, or drive learning.'
        return _impl(args or {})
