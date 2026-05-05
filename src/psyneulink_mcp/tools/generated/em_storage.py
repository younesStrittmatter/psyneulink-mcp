"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '82b40d5504b05a1ef673963784f1840444dafb9afca132a7c4d0173be0e2eaf7'
__pnl_qualname__ = 'psyneulink.EMStorage'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_em_storage'
TOOL_DESCRIPTION = 'Call this tool to create an EMStorage learning function that writes a 1-D entry vector into a memory matrix with configurable probability and decay. Use it when configuring the storage component of an EMComposition or EMStorageMechanism — it returns a 2-D memory matrix with the new entry written into the row or column with the lowest norm (or a specified location).\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "axis": {\n      "default": 0,\n      "description": "Axis of memory_matrix along which entries are stored. 0 = columns (each entry is a column), 1 = rows (each entry is a row).",\n      "type": "integer"\n    },\n    "decay_rate": {\n      "default": 0,\n      "description": "Multiplicative decay applied to all existing entries in memory_matrix before writing the new entry. 0.0 means no decay; 1.0 means no decay; values < 1 attenuate existing memories.",\n      "type": "number"\n    },\n    "default_variable": {\n      "description": "1-D array defining the shape of the entry to be stored. Must be 1-D; defaults to [0].",\n      "items": {\n        "type": "number"\n      },\n      "type": "array"\n    },\n    "name": {\n      "description": "Name for this EMStorage function instance.",\n      "type": "string"\n    },\n    "params": {\n      "description": "Optional parameter dictionary overriding constructor arguments. Rarely needed directly.",\n      "type": "object"\n    },\n    "seed": {\n      "description": "Seed for the internal random state used to evaluate storage_prob. Omit for non-deterministic behavior.",\n      "type": "integer"\n    },\n    "storage_location": {\n      "description": "Index of the row or column (determined by axis) at which the new entry is written, replacing the existing one. If omitted, the weakest entry (lowest L2 norm) is replaced.",\n      "type": "integer"\n    },\n    "storage_prob": {\n      "default": 1,\n      "description": "Probability [0, 1] that the entry is actually stored on each call. Set below 1.0 to add stochastic storage.",\n      "type": "number"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\n- storage_prob must be in [0, 1]; values outside this range raise a validation error.\n- axis is structural (read-only after construction) and must be 0 or 1; any other value raises FunctionError at runtime.\n- When storage_prob < 1.0 and the random draw fails, the memory_matrix is returned unchanged — no entry is stored that call.\n- decay_rate multiplies the entire matrix before writing the new entry; a value of 0.0 means no decay (not "decay everything to zero").\n- During initialization, no entry is actually written to memory_matrix to avoid contaminating it — this is intentional and silent.\n- memory_matrix is passed at call time through the params dict by EMStorageMechanism/EMComposition; you do not set it here.\n- default_variable must be strictly 1-D; passing a 2-D array raises ComponentError.\n- This function is typically constructed automatically inside EMStorageMechanism rather than instantiated directly by an agent.'
TOOL_PARAMETERS = { 'properties': { 'axis': { 'default': 0,
                            'description': 'Axis of memory_matrix along which entries '
                                           'are stored. 0 = columns (each entry is a '
                                           'column), 1 = rows (each entry is a row).',
                            'type': 'integer'},
                  'decay_rate': { 'default': 0,
                                  'description': 'Multiplicative decay applied to all '
                                                 'existing entries in memory_matrix '
                                                 'before writing the new entry. 0.0 '
                                                 'means no decay; 1.0 means no decay; '
                                                 'values < 1 attenuate existing '
                                                 'memories.',
                                  'type': 'number'},
                  'default_variable': { 'description': '1-D array defining the shape '
                                                       'of the entry to be stored. '
                                                       'Must be 1-D; defaults to [0].',
                                        'items': {'type': 'number'},
                                        'type': 'array'},
                  'name': { 'description': 'Name for this EMStorage function instance.',
                            'type': 'string'},
                  'params': { 'description': 'Optional parameter dictionary overriding '
                                             'constructor arguments. Rarely needed '
                                             'directly.',
                              'type': 'object'},
                  'seed': { 'description': 'Seed for the internal random state used to '
                                           'evaluate storage_prob. Omit for '
                                           'non-deterministic behavior.',
                            'type': 'integer'},
                  'storage_location': { 'description': 'Index of the row or column '
                                                       '(determined by axis) at which '
                                                       'the new entry is written, '
                                                       'replacing the existing one. If '
                                                       'omitted, the weakest entry '
                                                       '(lowest L2 norm) is replaced.',
                                        'type': 'integer'},
                  'storage_prob': { 'default': 1,
                                    'description': 'Probability [0, 1] that the entry '
                                                   'is actually stored on each call. '
                                                   'Set below 1.0 to add stochastic '
                                                   'storage.',
                                    'type': 'number'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = '- storage_prob must be in [0, 1]; values outside this range raise a validation error.\n- axis is structural (read-only after construction) and must be 0 or 1; any other value raises FunctionError at runtime.\n- When storage_prob < 1.0 and the random draw fails, the memory_matrix is returned unchanged — no entry is stored that call.\n- decay_rate multiplies the entire matrix before writing the new entry; a value of 0.0 means no decay (not "decay everything to zero").\n- During initialization, no entry is actually written to memory_matrix to avoid contaminating it — this is intentional and silent.\n- memory_matrix is passed at call time through the params dict by EMStorageMechanism/EMComposition; you do not set it here.\n- default_variable must be strictly 1-D; passing a 2-D array raises ComponentError.\n- This function is typically constructed automatically inside EMStorageMechanism rather than instantiated directly by an agent.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.EMStorage
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
    def create_em_storage(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to create an EMStorage learning function that writes a 1-D entry vector into a memory matrix with configurable probability and decay.'
        return _impl(args or {})
