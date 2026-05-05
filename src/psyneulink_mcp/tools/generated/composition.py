"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '91c28065491d04d0a3ded52e935feb2bca686842f405b333d1467186486f72cb'
__pnl_qualname__ = 'psyneulink.Composition'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_composition'
TOOL_DESCRIPTION = 'Call this tool to construct a PsyNeuLink `Composition` — the top-level executable container that wires Mechanisms and Projections into a runnable computational graph. Use it after creating component Mechanisms (e.g., via `transfer_mechanism`, `processing_mechanism`) when you need to assemble them into a network that can be executed with `.run()` or `.learn()`. The tool returns a Composition object whose `output_values` and `results` attributes hold trial-by-trial outputs.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "allow_probes": {\n      "default": true,\n      "description": "If true (default), allows Mechanisms with NodeRole.PROBE to exist in the Composition without raising an error.",\n      "type": "boolean"\n    },\n    "controller": {\n      "description": "An OptimizationControlMechanism (e.g. EVCControlMechanism, OCM) that modulates parameters of the Composition. Omit unless you need adaptive control. When provided, enable_controller is automatically set to True.",\n      "type": "object"\n    },\n    "controller_mode": {\n      "default": "after",\n      "description": "When the controller executes relative to the rest of the Composition each trial. \\"before\\" runs controller before other Mechanisms; \\"after\\" (default) runs it after.",\n      "enum": [\n        "before",\n        "after"\n      ],\n      "type": "string"\n    },\n    "controller_time_scale": {\n      "default": "TRIAL",\n      "description": "Time scale at which the controller executes. Default: \\"TRIAL\\" (once per trial).",\n      "enum": [\n        "TIME_STEP",\n        "PASS",\n        "TRIAL",\n        "RUN"\n      ],\n      "type": "string"\n    },\n    "enable_controller": {\n      "description": "Explicitly enable or disable the controller. Automatically set to True when a controller is provided. Set to False to temporarily disable a controller without removing it.",\n      "type": "boolean"\n    },\n    "enable_learning": {\n      "default": true,\n      "description": "If true (default), learning pathways defined via pathways are activated when .learn() is called. Set to False to disable all learning even if learning pathways are present.",\n      "type": "boolean"\n    },\n    "include_probes_in_output": {\n      "default": false,\n      "description": "If true, Mechanisms with NodeRole.PROBE are included in output_values and results. Always forced True for nested (inner) Compositions.",\n      "type": "boolean"\n    },\n    "learning_rate": {\n      "default": 0.05,\n      "description": "Global learning rate applied to all LearningMechanisms in the Composition. Default: 0.05. Individual LearningProjections may override this.",\n      "type": "number"\n    },\n    "minibatch_size": {\n      "default": 1,\n      "description": "Number of trials per minibatch during .learn(). Default: 1 (online learning). Values > 1 produce minibatch gradient accumulation.",\n      "minimum": 1,\n      "type": "integer"\n    },\n    "name": {\n      "description": "Optional name for this Composition. Defaults to \'Composition-N\'.",\n      "type": "string"\n    },\n    "nodes": {\n      "description": "Additional Mechanisms or Compositions to add as singleton nodes (no auto-created Projections). Use when you want to add nodes that will be connected via explicit projections.",\n      "items": {},\n      "type": "array"\n    },\n    "optimizations_per_minibatch": {\n      "default": 1,\n      "description": "Number of weight-update steps taken per minibatch. Default: 1.",\n      "minimum": 1,\n      "type": "integer"\n    },\n    "pathways": {\n      "description": "Primary way to add Nodes and connections. A flat list [MechA, MechB, ...] creates a linear chain with auto-created MappingProjections. A tuple (pathway_list, LearningFunction) creates a learning pathway. A set at any position creates parallel non-connected nodes.",\n      "items": {},\n      "type": "array"\n    },\n    "projections": {\n      "description": "Additional Projections to add beyond those auto-created by pathways.",\n      "items": {},\n      "type": "array"\n    },\n    "retain_old_simulation_data": {\n      "default": false,\n      "description": "If true, simulation results from controller simulations are retained in simulation_results. Default: false (cleared each trial) to save memory.",\n      "type": "boolean"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\n- `pathways` is the recommended entry point: a flat list `[MechA, MechB, MechC]` automatically inserts MappingProjections between adjacent mechanisms.\n- `learning_rate` default is 0.05 (from the Parameters inner class), not None as the constructor signature implies.\n- `controller_mode` takes lowercase strings "before" or "after" — do not use PNL keyword constants BEFORE/AFTER.\n- `enable_controller` is automatically set True when a controller is provided; you rarely need to set it explicitly.\n- For nested (inner) Compositions, `include_probes_in_output` is always forced True regardless of the argument.\n- A `set` of Mechanisms at a position in a pathways list creates parallel (non-connected) nodes at that point; doubly-nested lists beyond a single level of nesting cause errors.\n- `pathways`, `nodes`, and `projections` accept live PNL Python objects — they cannot be serialized to JSON. Pass the Python objects returned by other create_* tools.\n- `controller_condition` and `prefs` are omitted from this schema because they require live PNL objects; use `report_tool_issue` if you need them.\n- `show_graph_attributes` is omitted; it only affects visualization, not execution.'
TOOL_PARAMETERS = { 'properties': { 'allow_probes': { 'default': True,
                                    'description': 'If true (default), allows '
                                                   'Mechanisms with NodeRole.PROBE to '
                                                   'exist in the Composition without '
                                                   'raising an error.',
                                    'type': 'boolean'},
                  'controller': { 'description': 'An OptimizationControlMechanism '
                                                 '(e.g. EVCControlMechanism, OCM) that '
                                                 'modulates parameters of the '
                                                 'Composition. Omit unless you need '
                                                 'adaptive control. When provided, '
                                                 'enable_controller is automatically '
                                                 'set to True.',
                                  'type': 'object'},
                  'controller_mode': { 'default': 'after',
                                       'description': 'When the controller executes '
                                                      'relative to the rest of the '
                                                      'Composition each trial. '
                                                      '"before" runs controller before '
                                                      'other Mechanisms; "after" '
                                                      '(default) runs it after.',
                                       'enum': ['before', 'after'],
                                       'type': 'string'},
                  'controller_time_scale': { 'default': 'TRIAL',
                                             'description': 'Time scale at which the '
                                                            'controller executes. '
                                                            'Default: "TRIAL" (once '
                                                            'per trial).',
                                             'enum': [ 'TIME_STEP',
                                                       'PASS',
                                                       'TRIAL',
                                                       'RUN'],
                                             'type': 'string'},
                  'enable_controller': { 'description': 'Explicitly enable or disable '
                                                        'the controller. Automatically '
                                                        'set to True when a controller '
                                                        'is provided. Set to False to '
                                                        'temporarily disable a '
                                                        'controller without removing '
                                                        'it.',
                                         'type': 'boolean'},
                  'enable_learning': { 'default': True,
                                       'description': 'If true (default), learning '
                                                      'pathways defined via pathways '
                                                      'are activated when .learn() is '
                                                      'called. Set to False to disable '
                                                      'all learning even if learning '
                                                      'pathways are present.',
                                       'type': 'boolean'},
                  'include_probes_in_output': { 'default': False,
                                                'description': 'If true, Mechanisms '
                                                               'with NodeRole.PROBE '
                                                               'are included in '
                                                               'output_values and '
                                                               'results. Always forced '
                                                               'True for nested '
                                                               '(inner) Compositions.',
                                                'type': 'boolean'},
                  'learning_rate': { 'default': 0.05,
                                     'description': 'Global learning rate applied to '
                                                    'all LearningMechanisms in the '
                                                    'Composition. Default: 0.05. '
                                                    'Individual LearningProjections '
                                                    'may override this.',
                                     'type': 'number'},
                  'minibatch_size': { 'default': 1,
                                      'description': 'Number of trials per minibatch '
                                                     'during .learn(). Default: 1 '
                                                     '(online learning). Values > 1 '
                                                     'produce minibatch gradient '
                                                     'accumulation.',
                                      'minimum': 1,
                                      'type': 'integer'},
                  'name': { 'description': 'Optional name for this Composition. '
                                           "Defaults to 'Composition-N'.",
                            'type': 'string'},
                  'nodes': { 'description': 'Additional Mechanisms or Compositions to '
                                            'add as singleton nodes (no auto-created '
                                            'Projections). Use when you want to add '
                                            'nodes that will be connected via explicit '
                                            'projections.',
                             'items': {},
                             'type': 'array'},
                  'optimizations_per_minibatch': { 'default': 1,
                                                   'description': 'Number of '
                                                                  'weight-update steps '
                                                                  'taken per '
                                                                  'minibatch. Default: '
                                                                  '1.',
                                                   'minimum': 1,
                                                   'type': 'integer'},
                  'pathways': { 'description': 'Primary way to add Nodes and '
                                               'connections. A flat list [MechA, '
                                               'MechB, ...] creates a linear chain '
                                               'with auto-created MappingProjections. '
                                               'A tuple (pathway_list, '
                                               'LearningFunction) creates a learning '
                                               'pathway. A set at any position creates '
                                               'parallel non-connected nodes.',
                                'items': {},
                                'type': 'array'},
                  'projections': { 'description': 'Additional Projections to add '
                                                  'beyond those auto-created by '
                                                  'pathways.',
                                   'items': {},
                                   'type': 'array'},
                  'retain_old_simulation_data': { 'default': False,
                                                  'description': 'If true, simulation '
                                                                 'results from '
                                                                 'controller '
                                                                 'simulations are '
                                                                 'retained in '
                                                                 'simulation_results. '
                                                                 'Default: false '
                                                                 '(cleared each trial) '
                                                                 'to save memory.',
                                                  'type': 'boolean'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = '- `pathways` is the recommended entry point: a flat list `[MechA, MechB, MechC]` automatically inserts MappingProjections between adjacent mechanisms.\n- `learning_rate` default is 0.05 (from the Parameters inner class), not None as the constructor signature implies.\n- `controller_mode` takes lowercase strings "before" or "after" — do not use PNL keyword constants BEFORE/AFTER.\n- `enable_controller` is automatically set True when a controller is provided; you rarely need to set it explicitly.\n- For nested (inner) Compositions, `include_probes_in_output` is always forced True regardless of the argument.\n- A `set` of Mechanisms at a position in a pathways list creates parallel (non-connected) nodes at that point; doubly-nested lists beyond a single level of nesting cause errors.\n- `pathways`, `nodes`, and `projections` accept live PNL Python objects — they cannot be serialized to JSON. Pass the Python objects returned by other create_* tools.\n- `controller_condition` and `prefs` are omitted from this schema because they require live PNL objects; use `report_tool_issue` if you need them.\n- `show_graph_attributes` is omitted; it only affects visualization, not execution.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.Composition
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
    def create_composition(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to construct a PsyNeuLink `Composition` — the top-level executable container that wires Mechanisms and Projections into a runnable computational graph.'
        return _impl(args or {})
