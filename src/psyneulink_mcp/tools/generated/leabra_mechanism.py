"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '96e9e9f715ceb5c81273240ed044b50e470f21cee4ea82713f45da53d807a42b'
__pnl_qualname__ = 'psyneulink.LeabraMechanism'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_leabra_mechanism'
TOOL_DESCRIPTION = 'Call this tool to create a LeabraMechanism — a ProcessingMechanism that wraps a Leabra biologically-inspired neural network. Use it when building models that require Leabra-style bidirectional activation and Hebbian/error-driven learning. Returns a LeabraMechanism instance that can be added to a Composition and run like any other mechanism.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "hidden_layers": {\n      "default": 0,\n      "description": "Number of hidden layers in the Leabra network. Ignored if `network` is provided.",\n      "type": "integer"\n    },\n    "hidden_sizes": {\n      "description": "Size of each hidden layer. Can be a single integer (all hidden layers share that size) or a list of integers (one per hidden layer). Defaults to `input_size` if not specified. Ignored if `network` is provided.",\n      "oneOf": [\n        {\n          "type": "integer"\n        },\n        {\n          "items": {\n            "type": "integer"\n          },\n          "type": "array"\n        }\n      ]\n    },\n    "input_size": {\n      "default": 1,\n      "description": "Number of units in the input layer of the Leabra network. Ignored if `network` is provided.",\n      "type": "integer"\n    },\n    "name": {\n      "description": "Name for the LeabraMechanism instance.",\n      "type": "string"\n    },\n    "output_size": {\n      "default": 1,\n      "description": "Number of units in the output layer of the Leabra network. Ignored if `network` is provided.",\n      "type": "integer"\n    },\n    "params": {\n      "description": "Dictionary of parameters to override defaults. Passed to the parent Mechanism class.",\n      "type": "object"\n    },\n    "quarter_size": {\n      "default": 50,\n      "description": "Number of cycles the Leabra network runs each trial. Lower values are faster but may cause output fluctuations and reduce the magnitude of weight changes during learning.",\n      "type": "integer"\n    },\n    "training_flag": {\n      "default": false,\n      "description": "Whether the Leabra network should learn (adjust weights) during execution. Can be changed after initialization. If `network` is provided and this is omitted, the network\'s existing learning rules are preserved.",\n      "type": "boolean"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\n- The `network` parameter (a `leabra.Network` object) is intentionally excluded from the schema: it cannot be serialized to JSON. Agents must build the network via the size/layer parameters instead.\n- When `hidden_layers > 0` and `hidden_sizes` is a list, the list length must equal `hidden_layers`; mismatches will raise an error.\n- `training_flag=False` (not None) is the effective default when building a new network without providing one. Passing `None` only preserves existing learning rules on a pre-supplied `network`.\n- Very low `quarter_size` values (e.g., < 10) can produce noticeably unstable outputs and weak learning signals.\n- The mechanism has two output states: the first is the network output, and the second is used as the training pattern when `training_flag=True`. Wire the second input port to supply target patterns for supervised learning.\n- Leabra requires the optional `leabra` Python package; import will fail if it is not installed.'
TOOL_PARAMETERS = { 'properties': { 'hidden_layers': { 'default': 0,
                                     'description': 'Number of hidden layers in the '
                                                    'Leabra network. Ignored if '
                                                    '`network` is provided.',
                                     'type': 'integer'},
                  'hidden_sizes': { 'description': 'Size of each hidden layer. Can be '
                                                   'a single integer (all hidden '
                                                   'layers share that size) or a list '
                                                   'of integers (one per hidden '
                                                   'layer). Defaults to `input_size` '
                                                   'if not specified. Ignored if '
                                                   '`network` is provided.',
                                    'oneOf': [ {'type': 'integer'},
                                               { 'items': {'type': 'integer'},
                                                 'type': 'array'}]},
                  'input_size': { 'default': 1,
                                  'description': 'Number of units in the input layer '
                                                 'of the Leabra network. Ignored if '
                                                 '`network` is provided.',
                                  'type': 'integer'},
                  'name': { 'description': 'Name for the LeabraMechanism instance.',
                            'type': 'string'},
                  'output_size': { 'default': 1,
                                   'description': 'Number of units in the output layer '
                                                  'of the Leabra network. Ignored if '
                                                  '`network` is provided.',
                                   'type': 'integer'},
                  'params': { 'description': 'Dictionary of parameters to override '
                                             'defaults. Passed to the parent Mechanism '
                                             'class.',
                              'type': 'object'},
                  'quarter_size': { 'default': 50,
                                    'description': 'Number of cycles the Leabra '
                                                   'network runs each trial. Lower '
                                                   'values are faster but may cause '
                                                   'output fluctuations and reduce the '
                                                   'magnitude of weight changes during '
                                                   'learning.',
                                    'type': 'integer'},
                  'training_flag': { 'default': False,
                                     'description': 'Whether the Leabra network should '
                                                    'learn (adjust weights) during '
                                                    'execution. Can be changed after '
                                                    'initialization. If `network` is '
                                                    'provided and this is omitted, the '
                                                    "network's existing learning rules "
                                                    'are preserved.',
                                     'type': 'boolean'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = '- The `network` parameter (a `leabra.Network` object) is intentionally excluded from the schema: it cannot be serialized to JSON. Agents must build the network via the size/layer parameters instead.\n- When `hidden_layers > 0` and `hidden_sizes` is a list, the list length must equal `hidden_layers`; mismatches will raise an error.\n- `training_flag=False` (not None) is the effective default when building a new network without providing one. Passing `None` only preserves existing learning rules on a pre-supplied `network`.\n- Very low `quarter_size` values (e.g., < 10) can produce noticeably unstable outputs and weak learning signals.\n- The mechanism has two output states: the first is the network output, and the second is used as the training pattern when `training_flag=True`. Wire the second input port to supply target patterns for supervised learning.\n- Leabra requires the optional `leabra` Python package; import will fail if it is not installed.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.LeabraMechanism
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
    def create_leabra_mechanism(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to create a LeabraMechanism — a ProcessingMechanism that wraps a Leabra biologically-inspired neural network.'
        return _impl(args or {})
