"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '216b828fe306c49eaec2babb8733dbbd63d515f752a42e1ec5082020b1b6b939'
__pnl_qualname__ = 'psyneulink.AutodiffComposition'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_autodiff_composition'
TOOL_DESCRIPTION = 'Call this tool to create an AutodiffComposition — a Composition subclass that trains neural network models using PyTorch backpropagation. Use it when you need gradient-based learning (e.g., training a feedforward network with SGD or Adam). The result is an AutodiffComposition object; after creation, add nodes/projections and call `.learn()` to train, or `.run()` to execute without learning.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "device": {\n      "description": "Device on which the PyTorch model runs. If omitted, defaults to \'cuda\' if available, then \'mps\', otherwise \'cpu\'.",\n      "enum": [\n        "cpu",\n        "cuda",\n        "mps"\n      ],\n      "type": "string"\n    },\n    "enable_learning": {\n      "default": true,\n      "description": "Whether the AutodiffComposition enables learning when .learn() is called. Set to False to disable learning without removing the composition.",\n      "type": "boolean"\n    },\n    "full_sequence_mode": {\n      "default": false,\n      "description": "If True, each element of an input sequence is processed in a separate time step. Only needed when there are sequential dependencies between mechanisms. Do NOT use with GRU composition wrappers.",\n      "type": "boolean"\n    },\n    "learning_rate": {\n      "default": 0.001,\n      "description": "Default learning rate passed to the optimizer, applied to all learnable MappingProjections that don\'t have a projection-specific rate. Overridden by learning_rate specified in the .learn() call.",\n      "type": "number"\n    },\n    "loss_spec": {\n      "default": "MSE",\n      "description": "Loss function for training. Use Loss enum string values (e.g., \'MSE\' for mean squared error). Defaults to \'MSE\'.",\n      "enum": [\n        "MSE",\n        "SSE",\n        "CROSS_ENTROPY",\n        "BINARY_CROSS_ENTROPY",\n        "L1",\n        "NLL",\n        "POISSON_NLL",\n        "KL_DIV"\n      ],\n      "type": "string"\n    },\n    "name": {\n      "description": "Name for the AutodiffComposition. Defaults to \'autodiff_composition\'.",\n      "type": "string"\n    },\n    "optimizer_type": {\n      "default": "sgd",\n      "description": "Optimizer used during training. Must be \'sgd\' (Stochastic Gradient Descent) or \'adam\'.",\n      "enum": [\n        "sgd",\n        "adam"\n      ],\n      "type": "string"\n    },\n    "retain_torch_losses": {\n      "default": "MINIBATCH",\n      "description": "Granularity at which per-update losses are tracked and stored in torch_losses.",\n      "enum": [\n        "OPTIMIZATION_STEP",\n        "MINIBATCH",\n        "EPOCH",\n        "RUN"\n      ],\n      "type": "string"\n    },\n    "retain_torch_targets": {\n      "default": "MINIBATCH",\n      "description": "Granularity at which training targets are tracked and stored in torch_targets.",\n      "enum": [\n        "OPTIMIZATION_STEP",\n        "TRIAL",\n        "MINIBATCH",\n        "EPOCH",\n        "RUN"\n      ],\n      "type": "string"\n    },\n    "retain_torch_trained_outputs": {\n      "default": "MINIBATCH",\n      "description": "Granularity at which PyTorch model outputs are tracked and stored in torch_trained_outputs.",\n      "enum": [\n        "OPTIMIZATION_STEP",\n        "MINIBATCH",\n        "EPOCH",\n        "RUN"\n      ],\n      "type": "string"\n    },\n    "synch_node_values_with_torch": {\n      "default": "RUN",\n      "description": "When to copy PyTorch node outputs to PsyNeuLink node value attributes.",\n      "enum": [\n        "OPTIMIZATION_STEP",\n        "MINIBATCH",\n        "EPOCH",\n        "RUN"\n      ],\n      "type": "string"\n    },\n    "synch_node_variables_with_torch": {\n      "description": "When to copy current PyTorch node inputs to PsyNeuLink node variable attributes. Primarily useful for debugging/inspection. Defaults to None (no syncing).",\n      "enum": [\n        "OPTIMIZATION_STEP",\n        "TRIAL",\n        "MINIBATCH",\n        "EPOCH",\n        "RUN"\n      ],\n      "type": "string"\n    },\n    "synch_projection_matrices_with_torch": {\n      "default": "RUN",\n      "description": "When to copy PyTorch weight parameters back to PsyNeuLink MappingProjection matrices. More frequent syncing increases PNL accuracy but slows performance.",\n      "enum": [\n        "OPTIMIZATION_STEP",\n        "MINIBATCH",\n        "EPOCH",\n        "RUN"\n      ],\n      "type": "string"\n    },\n    "synch_results_with_torch": {\n      "default": "RUN",\n      "description": "When to copy PyTorch model outputs to the AutodiffComposition\'s results attribute. Note: OPTIMIZATION_STEP is not valid here.",\n      "enum": [\n        "TRIAL",\n        "MINIBATCH",\n        "EPOCH",\n        "RUN"\n      ],\n      "type": "string"\n    },\n    "weight_decay": {\n      "default": 0,\n      "description": "L2 regularization penalty applied by the optimizer to discourage large weights.",\n      "type": "number"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\n- PyTorch must be installed (`pip install torch`) for learning; without it, `learn()` with ExecutionMode.PyTorch raises an error.\n- `execution_mode` is NOT a constructor argument — it is passed to `.learn()` or `.run()`. The default for `.learn()` is `ExecutionMode.PyTorch` (with a one-time warning if not specified).\n- After constructing, you must add nodes and projections (e.g., via `add_node`, `add_projection`, or `add_linear_processing_pathway`) before calling `.learn()`.\n- `learn()` auto-infers backpropagation pathways from INPUT→OUTPUT node paths on first call; no manual pathway setup required.\n- Nested Compositions within an AutodiffComposition require `ExecutionMode.PyTorch`; Python mode raises an error.\n- If `minibatch_size > 1`, `retain_torch_trained_outputs`, `retain_torch_losses`, and `retain_torch_targets` cannot be `OPTIMIZATION_STEP` or `TRIAL` — use `MINIBATCH` or coarser.\n- `synch_results_with_torch` does NOT accept `OPTIMIZATION_STEP` (will raise a validation error).\n- `synch_node_variables_with_torch` defaults to None (no copying); this is intentional — PNL uses lazy evaluation so syncing variables is generally not useful except for debugging.\n- The `loss_spec` parameter accepts a Loss enum string; a callable PyTorch loss function can also be passed directly (not representable in this schema — pass the string name for standard losses).\n- Weight saving/loading via `.save()` and `.load()` uses PyTorch state_dict format.\n- `learning_rate` can also be a dict mapping projection names to rates (not representable as `number` here); for projection-specific rates, call `.learn(learning_rate={...})` directly.'
TOOL_PARAMETERS = { 'properties': { 'device': { 'description': 'Device on which the PyTorch model runs. '
                                             "If omitted, defaults to 'cuda' if "
                                             "available, then 'mps', otherwise 'cpu'.",
                              'enum': ['cpu', 'cuda', 'mps'],
                              'type': 'string'},
                  'enable_learning': { 'default': True,
                                       'description': 'Whether the AutodiffComposition '
                                                      'enables learning when .learn() '
                                                      'is called. Set to False to '
                                                      'disable learning without '
                                                      'removing the composition.',
                                       'type': 'boolean'},
                  'full_sequence_mode': { 'default': False,
                                          'description': 'If True, each element of an '
                                                         'input sequence is processed '
                                                         'in a separate time step. '
                                                         'Only needed when there are '
                                                         'sequential dependencies '
                                                         'between mechanisms. Do NOT '
                                                         'use with GRU composition '
                                                         'wrappers.',
                                          'type': 'boolean'},
                  'learning_rate': { 'default': 0.001,
                                     'description': 'Default learning rate passed to '
                                                    'the optimizer, applied to all '
                                                    'learnable MappingProjections that '
                                                    "don't have a projection-specific "
                                                    'rate. Overridden by learning_rate '
                                                    'specified in the .learn() call.',
                                     'type': 'number'},
                  'loss_spec': { 'default': 'MSE',
                                 'description': 'Loss function for training. Use Loss '
                                                "enum string values (e.g., 'MSE' for "
                                                'mean squared error). Defaults to '
                                                "'MSE'.",
                                 'enum': [ 'MSE',
                                           'SSE',
                                           'CROSS_ENTROPY',
                                           'BINARY_CROSS_ENTROPY',
                                           'L1',
                                           'NLL',
                                           'POISSON_NLL',
                                           'KL_DIV'],
                                 'type': 'string'},
                  'name': { 'description': 'Name for the AutodiffComposition. Defaults '
                                           "to 'autodiff_composition'.",
                            'type': 'string'},
                  'optimizer_type': { 'default': 'sgd',
                                      'description': 'Optimizer used during training. '
                                                     "Must be 'sgd' (Stochastic "
                                                     "Gradient Descent) or 'adam'.",
                                      'enum': ['sgd', 'adam'],
                                      'type': 'string'},
                  'retain_torch_losses': { 'default': 'MINIBATCH',
                                           'description': 'Granularity at which '
                                                          'per-update losses are '
                                                          'tracked and stored in '
                                                          'torch_losses.',
                                           'enum': [ 'OPTIMIZATION_STEP',
                                                     'MINIBATCH',
                                                     'EPOCH',
                                                     'RUN'],
                                           'type': 'string'},
                  'retain_torch_targets': { 'default': 'MINIBATCH',
                                            'description': 'Granularity at which '
                                                           'training targets are '
                                                           'tracked and stored in '
                                                           'torch_targets.',
                                            'enum': [ 'OPTIMIZATION_STEP',
                                                      'TRIAL',
                                                      'MINIBATCH',
                                                      'EPOCH',
                                                      'RUN'],
                                            'type': 'string'},
                  'retain_torch_trained_outputs': { 'default': 'MINIBATCH',
                                                    'description': 'Granularity at '
                                                                   'which PyTorch '
                                                                   'model outputs are '
                                                                   'tracked and stored '
                                                                   'in '
                                                                   'torch_trained_outputs.',
                                                    'enum': [ 'OPTIMIZATION_STEP',
                                                              'MINIBATCH',
                                                              'EPOCH',
                                                              'RUN'],
                                                    'type': 'string'},
                  'synch_node_values_with_torch': { 'default': 'RUN',
                                                    'description': 'When to copy '
                                                                   'PyTorch node '
                                                                   'outputs to '
                                                                   'PsyNeuLink node '
                                                                   'value attributes.',
                                                    'enum': [ 'OPTIMIZATION_STEP',
                                                              'MINIBATCH',
                                                              'EPOCH',
                                                              'RUN'],
                                                    'type': 'string'},
                  'synch_node_variables_with_torch': { 'description': 'When to copy '
                                                                      'current PyTorch '
                                                                      'node inputs to '
                                                                      'PsyNeuLink node '
                                                                      'variable '
                                                                      'attributes. '
                                                                      'Primarily '
                                                                      'useful for '
                                                                      'debugging/inspection. '
                                                                      'Defaults to '
                                                                      'None (no '
                                                                      'syncing).',
                                                       'enum': [ 'OPTIMIZATION_STEP',
                                                                 'TRIAL',
                                                                 'MINIBATCH',
                                                                 'EPOCH',
                                                                 'RUN'],
                                                       'type': 'string'},
                  'synch_projection_matrices_with_torch': { 'default': 'RUN',
                                                            'description': 'When to '
                                                                           'copy '
                                                                           'PyTorch '
                                                                           'weight '
                                                                           'parameters '
                                                                           'back to '
                                                                           'PsyNeuLink '
                                                                           'MappingProjection '
                                                                           'matrices. '
                                                                           'More '
                                                                           'frequent '
                                                                           'syncing '
                                                                           'increases '
                                                                           'PNL '
                                                                           'accuracy '
                                                                           'but slows '
                                                                           'performance.',
                                                            'enum': [ 'OPTIMIZATION_STEP',
                                                                      'MINIBATCH',
                                                                      'EPOCH',
                                                                      'RUN'],
                                                            'type': 'string'},
                  'synch_results_with_torch': { 'default': 'RUN',
                                                'description': 'When to copy PyTorch '
                                                               'model outputs to the '
                                                               "AutodiffComposition's "
                                                               'results attribute. '
                                                               'Note: '
                                                               'OPTIMIZATION_STEP is '
                                                               'not valid here.',
                                                'enum': [ 'TRIAL',
                                                          'MINIBATCH',
                                                          'EPOCH',
                                                          'RUN'],
                                                'type': 'string'},
                  'weight_decay': { 'default': 0,
                                    'description': 'L2 regularization penalty applied '
                                                   'by the optimizer to discourage '
                                                   'large weights.',
                                    'type': 'number'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = '- PyTorch must be installed (`pip install torch`) for learning; without it, `learn()` with ExecutionMode.PyTorch raises an error.\n- `execution_mode` is NOT a constructor argument — it is passed to `.learn()` or `.run()`. The default for `.learn()` is `ExecutionMode.PyTorch` (with a one-time warning if not specified).\n- After constructing, you must add nodes and projections (e.g., via `add_node`, `add_projection`, or `add_linear_processing_pathway`) before calling `.learn()`.\n- `learn()` auto-infers backpropagation pathways from INPUT→OUTPUT node paths on first call; no manual pathway setup required.\n- Nested Compositions within an AutodiffComposition require `ExecutionMode.PyTorch`; Python mode raises an error.\n- If `minibatch_size > 1`, `retain_torch_trained_outputs`, `retain_torch_losses`, and `retain_torch_targets` cannot be `OPTIMIZATION_STEP` or `TRIAL` — use `MINIBATCH` or coarser.\n- `synch_results_with_torch` does NOT accept `OPTIMIZATION_STEP` (will raise a validation error).\n- `synch_node_variables_with_torch` defaults to None (no copying); this is intentional — PNL uses lazy evaluation so syncing variables is generally not useful except for debugging.\n- The `loss_spec` parameter accepts a Loss enum string; a callable PyTorch loss function can also be passed directly (not representable in this schema — pass the string name for standard losses).\n- Weight saving/loading via `.save()` and `.load()` uses PyTorch state_dict format.\n- `learning_rate` can also be a dict mapping projection names to rates (not representable as `number` here); for projection-specific rates, call `.learn(learning_rate={...})` directly.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.AutodiffComposition
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
    def create_autodiff_composition(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to create an AutodiffComposition — a Composition subclass that trains neural network models using PyTorch backpropagation.'
        return _impl(args or {})
