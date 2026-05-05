"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '5e08bb8849a3fa6b7afd40159c8be0d4d30e0eddb2a626c2d86c4ff86592b72d'
__pnl_qualname__ = 'psyneulink.PytorchGRUCompositionWrapper'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_pytorch_gru_composition_wrapper'
TOOL_DESCRIPTION = 'Call this tool only when you need to manually instantiate a low-level PyTorch wrapper around a GRUComposition — for example, to inspect or manipulate the GRU module\'s weight tensors, projection wrappers, or forward pass outside normal execution. Under typical use, GRUComposition creates this wrapper automatically when running in PyTorch/learning mode; call this directly only for advanced debugging or custom training loops. Returns a PytorchGRUCompositionWrapper instance whose `torch_gru`, `gru_pytorch_node`, and `projections_map` attributes expose the underlying PyTorch GRU module and its PNL projection wrappers.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "composition": {\n      "description": "The GRUComposition instance to wrap. Must be a fully constructed GRUComposition with gru_mech, input_node, output_node, and all weight projections (wts_ir, wts_iu, etc.) already initialized.",\n      "type": "object"\n    },\n    "context": {\n      "default": null,\n      "description": "PsyNeuLink execution Context. If null, a default context is used. Needed when integrating with an existing PNL execution.",\n      "type": "object"\n    },\n    "device": {\n      "description": "PyTorch device string on which to place tensors, e.g. \'cpu\' or \'cuda:0\'.",\n      "type": "string"\n    },\n    "dtype": {\n      "default": null,\n      "description": "PyTorch dtype string for weight tensors, e.g. \'float64\' or \'float32\'. Defaults to torch.float64 if omitted. Must match the dtype expected by the surrounding training loop.",\n      "type": "string"\n    },\n    "outer_creator": {\n      "default": null,\n      "description": "The outer PytorchCompositionWrapper that is creating this wrapper when GRUComposition is nested inside another Composition. Pass null (None) when GRUComposition is run standalone.",\n      "type": "object"\n    }\n  },\n  "required": [\n    "composition",\n    "device"\n  ],\n  "type": "object"\n}\n\nNotes:\n- `subclass_components` is intentionally excluded from the schema — it is populated internally by `__init__` and passing it externally will conflict with the wrapper\'s own initialization logic.\n- `base_context` is also excluded; its default `Context(execution_id=None)` is correct for all normal use cases.\n- Default compute dtype is `torch.float64` (not float32). If you pass `dtype=\'float32\'`, all weight tensors and numpy conversions will use float32, which may affect learning precision.\n- `copy_weights_to_torch_gru()` is called automatically during `__init__` unless `context.source == ContextFlags.SHOW_GRAPH`; initial PNL projection weights are synced to the Pytorch GRU module at construction time.\n- When GRUComposition is nested, `composition.pytorch_representation` is set to this wrapper only if it was previously None — do not rely on this attribute if the composition has already been wrapped.\n- `dtype` here is a torch dtype object in the source, but since the MCP layer will call the constructor with string kwargs, pass a standard torch dtype name; the host template is responsible for converting it.'
TOOL_PARAMETERS = { 'properties': { 'composition': { 'description': 'The GRUComposition instance to '
                                                  'wrap. Must be a fully constructed '
                                                  'GRUComposition with gru_mech, '
                                                  'input_node, output_node, and all '
                                                  'weight projections (wts_ir, wts_iu, '
                                                  'etc.) already initialized.',
                                   'type': 'object'},
                  'context': { 'default': None,
                               'description': 'PsyNeuLink execution Context. If null, '
                                              'a default context is used. Needed when '
                                              'integrating with an existing PNL '
                                              'execution.',
                               'type': 'object'},
                  'device': { 'description': 'PyTorch device string on which to place '
                                             "tensors, e.g. 'cpu' or 'cuda:0'.",
                              'type': 'string'},
                  'dtype': { 'default': None,
                             'description': 'PyTorch dtype string for weight tensors, '
                                            "e.g. 'float64' or 'float32'. Defaults to "
                                            'torch.float64 if omitted. Must match the '
                                            'dtype expected by the surrounding '
                                            'training loop.',
                             'type': 'string'},
                  'outer_creator': { 'default': None,
                                     'description': 'The outer '
                                                    'PytorchCompositionWrapper that is '
                                                    'creating this wrapper when '
                                                    'GRUComposition is nested inside '
                                                    'another Composition. Pass null '
                                                    '(None) when GRUComposition is run '
                                                    'standalone.',
                                     'type': 'object'}},
  'required': ['composition', 'device'],
  'type': 'object'}
TOOL_NOTES = "- `subclass_components` is intentionally excluded from the schema — it is populated internally by `__init__` and passing it externally will conflict with the wrapper's own initialization logic.\n- `base_context` is also excluded; its default `Context(execution_id=None)` is correct for all normal use cases.\n- Default compute dtype is `torch.float64` (not float32). If you pass `dtype='float32'`, all weight tensors and numpy conversions will use float32, which may affect learning precision.\n- `copy_weights_to_torch_gru()` is called automatically during `__init__` unless `context.source == ContextFlags.SHOW_GRAPH`; initial PNL projection weights are synced to the Pytorch GRU module at construction time.\n- When GRUComposition is nested, `composition.pytorch_representation` is set to this wrapper only if it was previously None — do not rely on this attribute if the composition has already been wrapped.\n- `dtype` here is a torch dtype object in the source, but since the MCP layer will call the constructor with string kwargs, pass a standard torch dtype name; the host template is responsible for converting it."


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.PytorchGRUCompositionWrapper
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
    def create_pytorch_gru_composition_wrapper(args: dict[str, Any] | None = None) -> Any:
        "Call this tool only when you need to manually instantiate a low-level PyTorch wrapper around a GRUComposition — for example, to inspect or manipulate the GRU module's weight tensors, projection wrappers, or forward pass outside normal execution."
        return _impl(args or {})
