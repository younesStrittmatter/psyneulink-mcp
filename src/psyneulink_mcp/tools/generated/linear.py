"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = 'b37a9a3a746dcd09d3a00b9e7b14948d4b3bc4811b7c3e03b834d9ef21c6c2c1'
__pnl_qualname__ = 'psyneulink.Linear'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_linear'
TOOL_DESCRIPTION = 'Use this tool to create a PsyNeuLink Linear transfer function that applies the transform `scale * (slope * variable + intercept) + offset`. Call it when you need a parameterized linear mapping for a Mechanism\'s function — for example, to scale activations, shift baselines, or compose a gain+bias transform. The result is a Linear Function object that can be assigned to a Mechanism\'s `function` argument.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "intercept": {\n      "default": 0,\n      "description": "Additive bias applied to the input variable after multiplying by slope.",\n      "type": "number"\n    },\n    "name": {\n      "description": "Optional name for this Function instance. Defaults to a registry-generated name.",\n      "type": "string"\n    },\n    "offset": {\n      "default": 0,\n      "description": "Additive shift applied after scale. Displaces the entire linear output.",\n      "type": "number"\n    },\n    "scale": {\n      "default": 1,\n      "description": "Multiplier applied to the result of slope*variable+intercept. Amplifies the entire linear output.",\n      "type": "number"\n    },\n    "slope": {\n      "default": 1,\n      "description": "Multiplicative gain applied to the input variable before adding intercept.",\n      "type": "number"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\nAll four parameters default to values that implement the identity function (slope=1, intercept=0, scale=1, offset=0); PsyNeuLink may silently replace a default-parameter Linear with the Identity Function during compilation. scale and offset are NOT equivalent to slope and intercept: slope and intercept transform the variable first, then scale multiplies the intermediate result and offset shifts it — so scale*slope is the effective gain, not just slope. The derivative method returns scale*slope, not slope alone. default_variable is omitted from the schema because it is inferred from the owning Mechanism at runtime; only pass it if you need an explicit shape template.'
TOOL_PARAMETERS = { 'properties': { 'intercept': { 'default': 0,
                                 'description': 'Additive bias applied to the input '
                                                'variable after multiplying by slope.',
                                 'type': 'number'},
                  'name': { 'description': 'Optional name for this Function instance. '
                                           'Defaults to a registry-generated name.',
                            'type': 'string'},
                  'offset': { 'default': 0,
                              'description': 'Additive shift applied after scale. '
                                             'Displaces the entire linear output.',
                              'type': 'number'},
                  'scale': { 'default': 1,
                             'description': 'Multiplier applied to the result of '
                                            'slope*variable+intercept. Amplifies the '
                                            'entire linear output.',
                             'type': 'number'},
                  'slope': { 'default': 1,
                             'description': 'Multiplicative gain applied to the input '
                                            'variable before adding intercept.',
                             'type': 'number'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = 'All four parameters default to values that implement the identity function (slope=1, intercept=0, scale=1, offset=0); PsyNeuLink may silently replace a default-parameter Linear with the Identity Function during compilation. scale and offset are NOT equivalent to slope and intercept: slope and intercept transform the variable first, then scale multiplies the intermediate result and offset shifts it — so scale*slope is the effective gain, not just slope. The derivative method returns scale*slope, not slope alone. default_variable is omitted from the schema because it is inferred from the owning Mechanism at runtime; only pass it if you need an explicit shape template.'


def _impl(**kwargs: Any) -> Any:
    target = pnl.Linear
    instance = target(**kwargs)
    return repr(instance)


def register(mcp: Any) -> None:
    @captured_tool(mcp, layer="generated", name=TOOL_NAME, description=TOOL_DESCRIPTION)
    def create_linear(**kwargs: Any) -> Any:
        'Use this tool to create a PsyNeuLink Linear transfer function that applies the transform `scale * (slope * variable + intercept) + offset`.'
        return _impl(**kwargs)
