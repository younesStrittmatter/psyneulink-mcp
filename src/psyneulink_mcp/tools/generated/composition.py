"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '82e486b9b09ff0cde5e71602e6f5b2d26ee05fc304b26675dbbf2c8dd497f0cd'
__pnl_qualname__ = 'psyneulink.Composition'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_composition'
TOOL_DESCRIPTION = 'Call this tool to instantiate a PsyNeuLink Composition — the top-level container that wires together Mechanisms and Projections into an executable cognitive/neural model. Use it when you need a new empty or pre-populated Composition; the result is the Composition object itself, which can subsequently be run via `.run()` or trained via `.learn()`. Specify structure upfront via `pathways` (most common), `nodes`, and/or `projections`, or build incrementally after construction with `add_node`/`add_linear_processing_pathway`.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "allow_probes": {\n      "default": true,\n      "description": "Whether OUTPUT nodes of nested Compositions may be used as probes (intermediate value monitors) by outer Compositions. Pass \'CONTROL\' string to delegate control to the controller.",\n      "type": "boolean"\n    },\n    "controller": {\n      "description": "Python object reference (OptimizationControlMechanism or subclass) that controls parameter values. Pass as a pre-constructed Python object; this field accepts a string name/handle. Required if enable_controller=True.",\n      "type": "string"\n    },\n    "controller_mode": {\n      "default": "after",\n      "description": "Whether controller executes before or after the Composition\'s processing nodes each trial.",\n      "enum": [\n        "before",\n        "after"\n      ],\n      "type": "string"\n    },\n    "controller_time_scale": {\n      "default": "TRIAL",\n      "description": "TimeScale granularity at which the controller is invoked.",\n      "enum": [\n        "TIME_STEP",\n        "PASS",\n        "TRIAL",\n        "RUN"\n      ],\n      "type": "string"\n    },\n    "enable_controller": {\n      "description": "Explicitly enable or disable the controller. If omitted, controller is enabled automatically when one is assigned.",\n      "type": "boolean"\n    },\n    "enable_learning": {\n      "default": true,\n      "description": "Whether learning is enabled globally. Does not add learning components; they must be added separately or via AutodiffComposition.",\n      "type": "boolean"\n    },\n    "include_probes_in_output": {\n      "default": false,\n      "description": "Whether probe values are included in the Composition\'s output. Automatically set to True when nested Compositions are present.",\n      "type": "boolean"\n    },\n    "learning_rate": {\n      "description": "Global learning rate. True default is 0.05 (constructor signature shows None but Parameters class sets 0.05). Overrides per-LearningMechanism rates unless a dict is provided.",\n      "oneOf": [\n        {\n          "minimum": 0,\n          "type": "number"\n        },\n        {\n          "description": "Dict mapping learning components to individual rates.",\n          "type": "object"\n        }\n      ]\n    },\n    "minibatch_size": {\n      "default": 1,\n      "description": "Number of trials per minibatch for learning. Only relevant when learning is enabled.",\n      "minimum": 1,\n      "type": "integer"\n    },\n    "name": {\n      "description": "Name for the Composition. Auto-generated if omitted (e.g., \'Composition-0\').",\n      "type": "string"\n    },\n    "nodes": {\n      "description": "Mechanisms or nested Compositions to add as SINGLETON nodes (no automatic projections). Use when not specifying full pathways.",\n      "type": "array"\n    },\n    "optimizations_per_minibatch": {\n      "default": 1,\n      "description": "Number of weight-update passes per minibatch. Only relevant when learning is enabled.",\n      "minimum": 1,\n      "type": "integer"\n    },\n    "pathways": {\n      "description": "One or more processing pathways. Flat list = single pathway; list of lists = parallel pathways. Each pathway element may be a Mechanism, Projection, or (node, projection, node) tuple. Sets at a position create parallel branches that merge downstream.",\n      "type": "array"\n    },\n    "projections": {\n      "description": "MappingProjection objects to add explicitly. Usually inferred from pathways; specify here only when adding projections outside a pathway.",\n      "type": "array"\n    },\n    "retain_old_simulation_data": {\n      "default": false,\n      "description": "Whether simulation data from controller evaluation trials is retained after each trial. Set True for debugging; False (default) discards simulation results to save memory.",\n      "type": "boolean"\n    },\n    "show_graph_attributes": {\n      "description": "Dict of display attributes passed to show_graph(). Controls visual rendering only; no effect on execution.",\n      "type": "object"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\n- `learning_rate` true operative default is **0.05**, not None — the constructor signature is misleading; the `Parameters` inner class sets `Parameter(.05)`.\n- `pathways` parsing rules are non-obvious: a flat list is treated as a **single** pathway (elements are nodes/projections in sequence); a list of lists creates **parallel** pathways; doubly-nested lists collapse into a single pathway; triply-nested raises an error.\n- `nodes` adds each element as a **SINGLETON** — no projections are created automatically. Mix with `pathways` only if you know what roles will be assigned.\n- `controller` must be a Python object (OptimizationControlMechanism or subclass), not a string literal. JSON Schema cannot represent object references; the string type here is a proxy — pass the actual Python handle at call time.\n- Nested Compositions as nodes force `include_probes_in_output=True` automatically regardless of the kwarg.\n- `allow_probes` also accepts the string `\'CONTROL\'` to delegate probe authorization to the controller; the boolean schema is a simplification.\n- Adding nodes or projections after construction (via `add_node`, `add_projection`, `add_linear_processing_pathway`) triggers a full graph re-analysis — roles, INPUT/OUTPUT designation, and learning components are reassigned.\n- `termination_processing` (dict mapping TimeScale → Condition) is available as an extra kwarg via `**param_defaults` and is commonly needed for custom stopping criteria; it does not appear in the schema above.'
TOOL_PARAMETERS = { 'properties': { 'allow_probes': { 'default': True,
                                    'description': 'Whether OUTPUT nodes of nested '
                                                   'Compositions may be used as probes '
                                                   '(intermediate value monitors) by '
                                                   "outer Compositions. Pass 'CONTROL' "
                                                   'string to delegate control to the '
                                                   'controller.',
                                    'type': 'boolean'},
                  'controller': { 'description': 'Python object reference '
                                                 '(OptimizationControlMechanism or '
                                                 'subclass) that controls parameter '
                                                 'values. Pass as a pre-constructed '
                                                 'Python object; this field accepts a '
                                                 'string name/handle. Required if '
                                                 'enable_controller=True.',
                                  'type': 'string'},
                  'controller_mode': { 'default': 'after',
                                       'description': 'Whether controller executes '
                                                      'before or after the '
                                                      "Composition's processing nodes "
                                                      'each trial.',
                                       'enum': ['before', 'after'],
                                       'type': 'string'},
                  'controller_time_scale': { 'default': 'TRIAL',
                                             'description': 'TimeScale granularity at '
                                                            'which the controller is '
                                                            'invoked.',
                                             'enum': [ 'TIME_STEP',
                                                       'PASS',
                                                       'TRIAL',
                                                       'RUN'],
                                             'type': 'string'},
                  'enable_controller': { 'description': 'Explicitly enable or disable '
                                                        'the controller. If omitted, '
                                                        'controller is enabled '
                                                        'automatically when one is '
                                                        'assigned.',
                                         'type': 'boolean'},
                  'enable_learning': { 'default': True,
                                       'description': 'Whether learning is enabled '
                                                      'globally. Does not add learning '
                                                      'components; they must be added '
                                                      'separately or via '
                                                      'AutodiffComposition.',
                                       'type': 'boolean'},
                  'include_probes_in_output': { 'default': False,
                                                'description': 'Whether probe values '
                                                               'are included in the '
                                                               "Composition's output. "
                                                               'Automatically set to '
                                                               'True when nested '
                                                               'Compositions are '
                                                               'present.',
                                                'type': 'boolean'},
                  'learning_rate': { 'description': 'Global learning rate. True '
                                                    'default is 0.05 (constructor '
                                                    'signature shows None but '
                                                    'Parameters class sets 0.05). '
                                                    'Overrides per-LearningMechanism '
                                                    'rates unless a dict is provided.',
                                     'oneOf': [ {'minimum': 0, 'type': 'number'},
                                                { 'description': 'Dict mapping '
                                                                 'learning components '
                                                                 'to individual rates.',
                                                  'type': 'object'}]},
                  'minibatch_size': { 'default': 1,
                                      'description': 'Number of trials per minibatch '
                                                     'for learning. Only relevant when '
                                                     'learning is enabled.',
                                      'minimum': 1,
                                      'type': 'integer'},
                  'name': { 'description': 'Name for the Composition. Auto-generated '
                                           "if omitted (e.g., 'Composition-0').",
                            'type': 'string'},
                  'nodes': { 'description': 'Mechanisms or nested Compositions to add '
                                            'as SINGLETON nodes (no automatic '
                                            'projections). Use when not specifying '
                                            'full pathways.',
                             'type': 'array'},
                  'optimizations_per_minibatch': { 'default': 1,
                                                   'description': 'Number of '
                                                                  'weight-update '
                                                                  'passes per '
                                                                  'minibatch. Only '
                                                                  'relevant when '
                                                                  'learning is '
                                                                  'enabled.',
                                                   'minimum': 1,
                                                   'type': 'integer'},
                  'pathways': { 'description': 'One or more processing pathways. Flat '
                                               'list = single pathway; list of lists = '
                                               'parallel pathways. Each pathway '
                                               'element may be a Mechanism, '
                                               'Projection, or (node, projection, '
                                               'node) tuple. Sets at a position create '
                                               'parallel branches that merge '
                                               'downstream.',
                                'type': 'array'},
                  'projections': { 'description': 'MappingProjection objects to add '
                                                  'explicitly. Usually inferred from '
                                                  'pathways; specify here only when '
                                                  'adding projections outside a '
                                                  'pathway.',
                                   'type': 'array'},
                  'retain_old_simulation_data': { 'default': False,
                                                  'description': 'Whether simulation '
                                                                 'data from controller '
                                                                 'evaluation trials is '
                                                                 'retained after each '
                                                                 'trial. Set True for '
                                                                 'debugging; False '
                                                                 '(default) discards '
                                                                 'simulation results '
                                                                 'to save memory.',
                                                  'type': 'boolean'},
                  'show_graph_attributes': { 'description': 'Dict of display '
                                                            'attributes passed to '
                                                            'show_graph(). Controls '
                                                            'visual rendering only; no '
                                                            'effect on execution.',
                                             'type': 'object'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = "- `learning_rate` true operative default is **0.05**, not None — the constructor signature is misleading; the `Parameters` inner class sets `Parameter(.05)`.\n- `pathways` parsing rules are non-obvious: a flat list is treated as a **single** pathway (elements are nodes/projections in sequence); a list of lists creates **parallel** pathways; doubly-nested lists collapse into a single pathway; triply-nested raises an error.\n- `nodes` adds each element as a **SINGLETON** — no projections are created automatically. Mix with `pathways` only if you know what roles will be assigned.\n- `controller` must be a Python object (OptimizationControlMechanism or subclass), not a string literal. JSON Schema cannot represent object references; the string type here is a proxy — pass the actual Python handle at call time.\n- Nested Compositions as nodes force `include_probes_in_output=True` automatically regardless of the kwarg.\n- `allow_probes` also accepts the string `'CONTROL'` to delegate probe authorization to the controller; the boolean schema is a simplification.\n- Adding nodes or projections after construction (via `add_node`, `add_projection`, `add_linear_processing_pathway`) triggers a full graph re-analysis — roles, INPUT/OUTPUT designation, and learning components are reassigned.\n- `termination_processing` (dict mapping TimeScale → Condition) is available as an extra kwarg via `**param_defaults` and is commonly needed for custom stopping criteria; it does not appear in the schema above."


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
        'Call this tool to instantiate a PsyNeuLink Composition — the top-level container that wires together Mechanisms and Projections into an executable cognitive/neural model.'
        return _impl(args or {})
