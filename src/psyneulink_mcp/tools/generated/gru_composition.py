"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '03d8867ff42661ecaaaea784f81e42fb9eb9d343be6063cd91be5fe20bf51ff8'
__pnl_qualname__ = 'psyneulink.GRUComposition'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_gru_composition'
TOOL_DESCRIPTION = 'Call this tool to instantiate a GRUComposition — a single-layer gated recurrent unit (GRU) network built on AutodiffComposition. Use it when you need a recurrent sequence model with reset and update gating that can be trained via PyTorch backprop and then run in PsyNeuLink. The result is a fully wired Composition with input, hidden, output, reset, update, and new nodes already connected; you cannot add or remove nodes/projections after construction.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "bias": {\n      "default": false,\n      "description": "Whether to include learnable bias vectors. When False (default), bias_* attributes/nodes do not exist and cannot be referenced.",\n      "type": "boolean"\n    },\n    "enable_learning": {\n      "default": true,\n      "description": "Whether learning is enabled. Only ExecutionMode.PyTorch is supported for learning.",\n      "type": "boolean"\n    },\n    "hidden_size": {\n      "default": 1,\n      "description": "Length of the hidden state vector; determines the size of hidden_layer_node and all internal nodes.",\n      "type": "integer"\n    },\n    "input_size": {\n      "default": 1,\n      "description": "Length of the input vector; determines the size of input_node.",\n      "type": "integer"\n    },\n    "learning_rate": {\n      "default": 0.001,\n      "description": "Default learning rate for all learnable parameters not individually specified in optimizer_params.",\n      "type": "number"\n    },\n    "name": {\n      "default": "GRU Composition",\n      "description": "Name for the GRUComposition instance.",\n      "type": "string"\n    },\n    "optimizer_params": {\n      "additionalProperties": {},\n      "description": "Dict of per-parameter optimizer settings. Use string keys INPUT_TO_HIDDEN or HIDDEN_TO_HIDDEN for weight groups; do NOT specify individual input-to-hidden or hidden-to-hidden projections by name (raises GRUCompositionError). Bias keys are only valid when bias=True.",\n      "type": "object"\n    },\n    "seed": {\n      "description": "Random seed for weight initialization.",\n      "type": "integer"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\n- Nodes and projections cannot be added or removed after construction; attempting to call add_node() or add_projection() from user code raises CompositionError.\n- Learning only works with ExecutionMode.PyTorch; if execution_mode is omitted in learn(), a warning is issued and PyTorch mode is used automatically.\n- bias=False by default — bias_ir, bias_iu, bias_in, bias_hr, bias_hu, bias_hn attributes and their corresponding *_node attributes do not exist unless bias=True; accessing them when bias=False will raise an AttributeError.\n- optimizer_params must not specify individual input-to-hidden (wts_in, wts_iu, wts_ir) or hidden-to-hidden (wts_hn, wts_hr, wts_hu) projections by name; use the group keys INPUT_TO_HIDDEN and HIDDEN_TO_HIDDEN instead.\n- input_size and hidden_size must be plain Python ints; passing numpy arrays or floats will fail validation.\n- Learnable projections are: wts_in, wts_iu, wts_ir, wts_hn, wts_hr, wts_hu (and all bias projections if bias=True). wts_nh, wts_hh, wts_ho are fixed identity/pass-through projections.\n- The composition exposes PsyNeuLink elements only; PyTorch-specific internals live in pytorch_representation (a PytorchGRUCompositionWrapper).\n- At the Python level the GRU is single-layer only; num_layers, batch_first, dropout, and bidirectional are not currently exposed.'
TOOL_PARAMETERS = { 'properties': { 'bias': { 'default': False,
                            'description': 'Whether to include learnable bias vectors. '
                                           'When False (default), bias_* '
                                           'attributes/nodes do not exist and cannot '
                                           'be referenced.',
                            'type': 'boolean'},
                  'enable_learning': { 'default': True,
                                       'description': 'Whether learning is enabled. '
                                                      'Only ExecutionMode.PyTorch is '
                                                      'supported for learning.',
                                       'type': 'boolean'},
                  'hidden_size': { 'default': 1,
                                   'description': 'Length of the hidden state vector; '
                                                  'determines the size of '
                                                  'hidden_layer_node and all internal '
                                                  'nodes.',
                                   'type': 'integer'},
                  'input_size': { 'default': 1,
                                  'description': 'Length of the input vector; '
                                                 'determines the size of input_node.',
                                  'type': 'integer'},
                  'learning_rate': { 'default': 0.001,
                                     'description': 'Default learning rate for all '
                                                    'learnable parameters not '
                                                    'individually specified in '
                                                    'optimizer_params.',
                                     'type': 'number'},
                  'name': { 'default': 'GRU Composition',
                            'description': 'Name for the GRUComposition instance.',
                            'type': 'string'},
                  'optimizer_params': { 'additionalProperties': {},
                                        'description': 'Dict of per-parameter '
                                                       'optimizer settings. Use string '
                                                       'keys INPUT_TO_HIDDEN or '
                                                       'HIDDEN_TO_HIDDEN for weight '
                                                       'groups; do NOT specify '
                                                       'individual input-to-hidden or '
                                                       'hidden-to-hidden projections '
                                                       'by name (raises '
                                                       'GRUCompositionError). Bias '
                                                       'keys are only valid when '
                                                       'bias=True.',
                                        'type': 'object'},
                  'seed': { 'description': 'Random seed for weight initialization.',
                            'type': 'integer'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = '- Nodes and projections cannot be added or removed after construction; attempting to call add_node() or add_projection() from user code raises CompositionError.\n- Learning only works with ExecutionMode.PyTorch; if execution_mode is omitted in learn(), a warning is issued and PyTorch mode is used automatically.\n- bias=False by default — bias_ir, bias_iu, bias_in, bias_hr, bias_hu, bias_hn attributes and their corresponding *_node attributes do not exist unless bias=True; accessing them when bias=False will raise an AttributeError.\n- optimizer_params must not specify individual input-to-hidden (wts_in, wts_iu, wts_ir) or hidden-to-hidden (wts_hn, wts_hr, wts_hu) projections by name; use the group keys INPUT_TO_HIDDEN and HIDDEN_TO_HIDDEN instead.\n- input_size and hidden_size must be plain Python ints; passing numpy arrays or floats will fail validation.\n- Learnable projections are: wts_in, wts_iu, wts_ir, wts_hn, wts_hr, wts_hu (and all bias projections if bias=True). wts_nh, wts_hh, wts_ho are fixed identity/pass-through projections.\n- The composition exposes PsyNeuLink elements only; PyTorch-specific internals live in pytorch_representation (a PytorchGRUCompositionWrapper).\n- At the Python level the GRU is single-layer only; num_layers, batch_first, dropout, and bidirectional are not currently exposed.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.GRUComposition
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
    def create_gru_composition(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to instantiate a GRUComposition — a single-layer gated recurrent unit (GRU) network built on AutodiffComposition.'
        return _impl(args or {})
