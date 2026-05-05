"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = 'a0fdc55058ae4ebb8dae9aad4ff7a4cffa949254f721ccb4c983267bfc11aa3d'
__pnl_qualname__ = 'psyneulink.LinearCombination'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_linear_combination'
TOOL_DESCRIPTION = 'Call this tool to create a LinearCombination function that element-wise combines multiple numeric arrays via sum, product, or cross-entropy, with optional per-array weighting and exponentiation before combining and global scale/offset applied after. Use it when assigning a combining function to a Mechanism or Projection that needs to merge multiple input arrays into one output array of the same length.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "default_variable": {\n      "description": "Template for the arrays to be combined. If 1d, the function simply applies scale and offset (no combination). If 2d, all sub-arrays must have the same length.",\n      "items": {},\n      "type": "array"\n    },\n    "exponents": {\n      "description": "Exponents applied to each array in variable. If 1d, each element exponentiates the corresponding array; if 2d, element-wise exponentiation. Shape must match variable. Applied before weights in the Python backend.",\n      "items": {},\n      "type": "array"\n    },\n    "name": {\n      "description": "Optional name for the function instance. If omitted, FunctionRegistry assigns a default.",\n      "type": "string"\n    },\n    "offset": {\n      "default": 0,\n      "description": "Scalar added to the scaled result. Default is 0.0 (no offset). Can also be an array for element-wise offset, but must match the shape of the combined result.",\n      "type": "number"\n    },\n    "operation": {\n      "default": "sum",\n      "description": "How to combine the (weighted/exponentiated) arrays: \'sum\' for element-wise sum (default), \'product\' for Hadamard product, \'cross-entropy\' for v1*log(v2) (Python backend only; not supported in LLVM or AutodiffComposition).",\n      "enum": [\n        "sum",\n        "product",\n        "cross-entropy"\n      ],\n      "type": "string"\n    },\n    "scale": {\n      "default": 1,\n      "description": "Scalar multiplier applied to the combined result before adding offset. Default is 1.0 (no scaling). Can also be an array for element-wise (Hadamard) scaling, but must match the shape of the combined result.",\n      "type": "number"\n    },\n    "weights": {\n      "description": "Multipliers applied to each array in variable before combining. If 1d, each element scales the corresponding array; if 2d, Hadamard (element-wise) product with each array. Shape must match variable. Applied after exponents in the Python backend (despite docstring saying otherwise).",\n      "items": {},\n      "type": "array"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\n- The source code applies exponents FIRST, then weights — but the Attributes docstring states the opposite ("weights are applied before any exponentiation"). Trust the source: order is (1) exponentiate, (2) multiply by weights, (3) combine, (4) scale, (5) offset.\n- If variable is 0d or 1d (a single flat array), the combination step is skipped entirely and the result is just `variable * scale + offset`.\n- \'cross-entropy\' operation is only available in the Python (NumPy) backend. It raises FunctionError in the LLVM backend and AutodiffCompositionError in PyTorch/AutodiffComposition — do not use it in those contexts.\n- scale and offset default to 1.0 and 0.0 respectively at runtime; passing None is equivalent to these defaults.\n- weights and exponents shapes must exactly match the shape of variable at execution time, even though they are not validated during initialization (only during execution).\n- All arrays in a 2d variable must be the same length; mismatched lengths raise FunctionError at initialization.\n- scale and offset JSON Schema is typed as number for simplicity; PsyNeuLink also accepts np.ndarray for Hadamard modulation — pass those as arrays if needed, but note that array scale/offset must match variable shape.'
TOOL_PARAMETERS = { 'properties': { 'default_variable': { 'description': 'Template for the arrays to be '
                                                       'combined. If 1d, the function '
                                                       'simply applies scale and '
                                                       'offset (no combination). If '
                                                       '2d, all sub-arrays must have '
                                                       'the same length.',
                                        'items': {},
                                        'type': 'array'},
                  'exponents': { 'description': 'Exponents applied to each array in '
                                                'variable. If 1d, each element '
                                                'exponentiates the corresponding '
                                                'array; if 2d, element-wise '
                                                'exponentiation. Shape must match '
                                                'variable. Applied before weights in '
                                                'the Python backend.',
                                 'items': {},
                                 'type': 'array'},
                  'name': { 'description': 'Optional name for the function instance. '
                                           'If omitted, FunctionRegistry assigns a '
                                           'default.',
                            'type': 'string'},
                  'offset': { 'default': 0,
                              'description': 'Scalar added to the scaled result. '
                                             'Default is 0.0 (no offset). Can also be '
                                             'an array for element-wise offset, but '
                                             'must match the shape of the combined '
                                             'result.',
                              'type': 'number'},
                  'operation': { 'default': 'sum',
                                 'description': 'How to combine the '
                                                '(weighted/exponentiated) arrays: '
                                                "'sum' for element-wise sum (default), "
                                                "'product' for Hadamard product, "
                                                "'cross-entropy' for v1*log(v2) "
                                                '(Python backend only; not supported '
                                                'in LLVM or AutodiffComposition).',
                                 'enum': ['sum', 'product', 'cross-entropy'],
                                 'type': 'string'},
                  'scale': { 'default': 1,
                             'description': 'Scalar multiplier applied to the combined '
                                            'result before adding offset. Default is '
                                            '1.0 (no scaling). Can also be an array '
                                            'for element-wise (Hadamard) scaling, but '
                                            'must match the shape of the combined '
                                            'result.',
                             'type': 'number'},
                  'weights': { 'description': 'Multipliers applied to each array in '
                                              'variable before combining. If 1d, each '
                                              'element scales the corresponding array; '
                                              'if 2d, Hadamard (element-wise) product '
                                              'with each array. Shape must match '
                                              'variable. Applied after exponents in '
                                              'the Python backend (despite docstring '
                                              'saying otherwise).',
                               'items': {},
                               'type': 'array'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = '- The source code applies exponents FIRST, then weights — but the Attributes docstring states the opposite ("weights are applied before any exponentiation"). Trust the source: order is (1) exponentiate, (2) multiply by weights, (3) combine, (4) scale, (5) offset.\n- If variable is 0d or 1d (a single flat array), the combination step is skipped entirely and the result is just `variable * scale + offset`.\n- \'cross-entropy\' operation is only available in the Python (NumPy) backend. It raises FunctionError in the LLVM backend and AutodiffCompositionError in PyTorch/AutodiffComposition — do not use it in those contexts.\n- scale and offset default to 1.0 and 0.0 respectively at runtime; passing None is equivalent to these defaults.\n- weights and exponents shapes must exactly match the shape of variable at execution time, even though they are not validated during initialization (only during execution).\n- All arrays in a 2d variable must be the same length; mismatched lengths raise FunctionError at initialization.\n- scale and offset JSON Schema is typed as number for simplicity; PsyNeuLink also accepts np.ndarray for Hadamard modulation — pass those as arrays if needed, but note that array scale/offset must match variable shape.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.LinearCombination
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
    def create_linear_combination(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to create a LinearCombination function that element-wise combines multiple numeric arrays via sum, product, or cross-entropy, with optional per-array weighting and exponentiation before combining and global scale/offset applied after.'
        return _impl(args or {})
