"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '70b0bf2a73a60a45b2fcdf322f680ace5ee737e4b439a39c9ce63c6f427597b0'
__pnl_qualname__ = 'psyneulink.Scheduler'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_scheduler'
TOOL_DESCRIPTION = 'Call this tool to create a Scheduler that controls the order and timing of node execution within a PsyNeuLink Composition or a custom dependency graph, optionally constrained by Conditions. Use it when you need fine-grained control over execution ordering beyond what a Composition\'s built-in scheduler provides — for example, when attaching explicit Conditions, using exact-time scheduling, or scheduling a raw graph without a Composition wrapper.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "composition": {\n      "description": "Name of an existing Composition whose graph_processing dependency structure will be used. Mutually exclusive with \'graph\': provide one or the other, not both.",\n      "type": "string"\n    },\n    "conditions": {\n      "additionalProperties": {},\n      "description": "Mapping of node names to Condition specifications (e.g., {\\"my_node\\": {\\"type\\": \\"EveryNCalls\\", \\"dependency\\": \\"other_node\\", \\"n\\": 2}}). Nodes without explicit Conditions get defaults based on their dependencies.",\n      "type": "object"\n    },\n    "default_absolute_time_unit": {\n      "default": "1ms",\n      "description": "Duration of a single TIME_STEP as a pint-compatible string (e.g., \'1ms\', \'500us\', \'0.1s\'). Only relevant when absolute-time Conditions are used.",\n      "type": "string"\n    },\n    "default_execution_id": {\n      "description": "Identifier for this scheduling context; allows multiple independent schedulings. Defaults to the Composition\'s default_execution_id when a Composition is provided.",\n      "type": "string"\n    },\n    "graph": {\n      "additionalProperties": {\n        "items": {\n          "type": "string"\n        },\n        "type": "array"\n      },\n      "description": "Explicit dependency graph as a dict mapping each node name to the set of node names that project directly to it (i.e., its dependencies). Used when no Composition is provided.",\n      "type": "object"\n    },\n    "mode": {\n      "default": "STANDARD",\n      "description": "STANDARD: default trial-based scheduling. EXACT_TIME: nodes are scheduled at exact time points; required when using absolute-time Conditions.",\n      "enum": [\n        "STANDARD",\n        "EXACT_TIME"\n      ],\n      "type": "string"\n    },\n    "termination_conds": {\n      "additionalProperties": {},\n      "description": "Mapping of TimeScale names (e.g., \\"TRIAL\\", \\"RUN\\") to Condition specs that halt execution at that scale when satisfied.",\n      "type": "object"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\nEither `composition` or `graph` must be provided; if both are omitted, the Scheduler will have an empty graph and no nodes to schedule. When `composition` is given, `graph` is derived automatically from `composition.graph_processing.prune_feedback_edges()` and should not also be specified. Nodes without explicit Conditions in `conditions` receive auto-generated defaults: Always() for root nodes, EveryNCalls(dep, 1) for single-dependency nodes, All(EveryNCalls(dep, 1), ...) for multi-dependency nodes. `default_absolute_time_unit` is ignored unless absolute-time Conditions are present. Use `mode="EXACT_TIME"` only when precise timing synchronization is required; it imposes stricter scheduling rules. The Scheduler\'s `run()` method is a generator — it yields sets of nodes for each consideration step rather than returning all at once.'
TOOL_PARAMETERS = { 'properties': { 'composition': { 'description': 'Name of an existing Composition '
                                                  'whose graph_processing dependency '
                                                  'structure will be used. Mutually '
                                                  "exclusive with 'graph': provide one "
                                                  'or the other, not both.',
                                   'type': 'string'},
                  'conditions': { 'additionalProperties': {},
                                  'description': 'Mapping of node names to Condition '
                                                 'specifications (e.g., {"my_node": '
                                                 '{"type": "EveryNCalls", '
                                                 '"dependency": "other_node", "n": '
                                                 '2}}). Nodes without explicit '
                                                 'Conditions get defaults based on '
                                                 'their dependencies.',
                                  'type': 'object'},
                  'default_absolute_time_unit': { 'default': '1ms',
                                                  'description': 'Duration of a single '
                                                                 'TIME_STEP as a '
                                                                 'pint-compatible '
                                                                 "string (e.g., '1ms', "
                                                                 "'500us', '0.1s'). "
                                                                 'Only relevant when '
                                                                 'absolute-time '
                                                                 'Conditions are used.',
                                                  'type': 'string'},
                  'default_execution_id': { 'description': 'Identifier for this '
                                                           'scheduling context; allows '
                                                           'multiple independent '
                                                           'schedulings. Defaults to '
                                                           "the Composition's "
                                                           'default_execution_id when '
                                                           'a Composition is provided.',
                                            'type': 'string'},
                  'graph': { 'additionalProperties': { 'items': {'type': 'string'},
                                                       'type': 'array'},
                             'description': 'Explicit dependency graph as a dict '
                                            'mapping each node name to the set of node '
                                            'names that project directly to it (i.e., '
                                            'its dependencies). Used when no '
                                            'Composition is provided.',
                             'type': 'object'},
                  'mode': { 'default': 'STANDARD',
                            'description': 'STANDARD: default trial-based scheduling. '
                                           'EXACT_TIME: nodes are scheduled at exact '
                                           'time points; required when using '
                                           'absolute-time Conditions.',
                            'enum': ['STANDARD', 'EXACT_TIME'],
                            'type': 'string'},
                  'termination_conds': { 'additionalProperties': {},
                                         'description': 'Mapping of TimeScale names '
                                                        '(e.g., "TRIAL", "RUN") to '
                                                        'Condition specs that halt '
                                                        'execution at that scale when '
                                                        'satisfied.',
                                         'type': 'object'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = 'Either `composition` or `graph` must be provided; if both are omitted, the Scheduler will have an empty graph and no nodes to schedule. When `composition` is given, `graph` is derived automatically from `composition.graph_processing.prune_feedback_edges()` and should not also be specified. Nodes without explicit Conditions in `conditions` receive auto-generated defaults: Always() for root nodes, EveryNCalls(dep, 1) for single-dependency nodes, All(EveryNCalls(dep, 1), ...) for multi-dependency nodes. `default_absolute_time_unit` is ignored unless absolute-time Conditions are present. Use `mode="EXACT_TIME"` only when precise timing synchronization is required; it imposes stricter scheduling rules. The Scheduler\'s `run()` method is a generator — it yields sets of nodes for each consideration step rather than returning all at once.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.Scheduler
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
    def create_scheduler(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to create a Scheduler that controls the order and timing of node execution within a PsyNeuLink Composition or a custom dependency graph, optionally constrained by Conditions.'
        return _impl(args or {})
