"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '0fe9c4fc943a8a7216618d2a4fae7829c9898760e7ed57c968a3b298a39311a7'
__pnl_qualname__ = 'psyneulink.core.components.projections.pathway.mappingprojection.ProxyProjection'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_proxy_projection'
TOOL_DESCRIPTION = 'Call this tool only when you need to create a proxy MappingProjection that stands in for a real projection crossing a nested Composition boundary (i.e., a projection to/from the input_CIM or output_CIM of a nested Composition). This is an internal PsyNeuLink construct — do not use it as a general-purpose MappingProjection; prefer the `mapping_projection` tool for ordinary connections. Returns a ProxyProjection object linked to the original projection via `_proxy`.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "learnable": {\n      "default": true,\n      "description": "Whether the matrix parameter can be modified by learning. Defaults to True; set False to permanently block learning on this projection.",\n      "type": "boolean"\n    },\n    "learning_rate": {\n      "description": "Projection-specific learning rate. SharedParameter \\u2014 its effective value is inherited from the proxy_for projection. Raises an error if learnable is False and a numeric value is assigned.",\n      "type": "number"\n    },\n    "matrix": {\n      "description": "Matrix specification: a keyword string (e.g., \'IDENTITY_MATRIX\', \'FULL_CONNECTIVITY_MATRIX\'), a JSON-encoded list/array, or a function name. Defaults to DEFAULT_MATRIX.",\n      "type": "string"\n    },\n    "name": {\n      "description": "Name for the ProxyProjection. Auto-generated from sender/receiver names if omitted.",\n      "type": "string"\n    },\n    "proxy_for": {\n      "description": "Name of the existing Projection object that this ProxyProjection stands in for (the real projection crossing the nested Composition boundary). Required.",\n      "type": "string"\n    },\n    "receiver": {\n      "description": "Name of the InputPort or Mechanism that is the destination of this proxy projection\'s output. If omitted, deferred initialization applies.",\n      "type": "string"\n    },\n    "sender": {\n      "description": "Name of the OutputPort or Mechanism that is the source of this proxy projection\'s input. If omitted, deferred initialization applies.",\n      "type": "string"\n    }\n  },\n  "required": [\n    "proxy_for"\n  ],\n  "type": "object"\n}\n\nNotes:\nProxyProjection is an internal PsyNeuLink implementation detail for nested Composition boundaries — agents almost never need to instantiate it directly; PsyNeuLink creates proxies automatically when add_node/add_projection involves nested Compositions. The `proxy_for` argument must be an existing live Projection object (passed by name); the constructor stores a weakref and sets `proxy_for._proxy = self`. The `learning_rate` parameter is a SharedParameter that delegates to the proxied projection — setting it independently on the ProxyProjection has no effect unless the proxied projection\'s value changes. Assigning learning_rate when learnable=False raises an error.'
TOOL_PARAMETERS = { 'properties': { 'learnable': { 'default': True,
                                 'description': 'Whether the matrix parameter can be '
                                                'modified by learning. Defaults to '
                                                'True; set False to permanently block '
                                                'learning on this projection.',
                                 'type': 'boolean'},
                  'learning_rate': { 'description': 'Projection-specific learning '
                                                    'rate. SharedParameter — its '
                                                    'effective value is inherited from '
                                                    'the proxy_for projection. Raises '
                                                    'an error if learnable is False '
                                                    'and a numeric value is assigned.',
                                     'type': 'number'},
                  'matrix': { 'description': 'Matrix specification: a keyword string '
                                             "(e.g., 'IDENTITY_MATRIX', "
                                             "'FULL_CONNECTIVITY_MATRIX'), a "
                                             'JSON-encoded list/array, or a function '
                                             'name. Defaults to DEFAULT_MATRIX.',
                              'type': 'string'},
                  'name': { 'description': 'Name for the ProxyProjection. '
                                           'Auto-generated from sender/receiver names '
                                           'if omitted.',
                            'type': 'string'},
                  'proxy_for': { 'description': 'Name of the existing Projection '
                                                'object that this ProxyProjection '
                                                'stands in for (the real projection '
                                                'crossing the nested Composition '
                                                'boundary). Required.',
                                 'type': 'string'},
                  'receiver': { 'description': 'Name of the InputPort or Mechanism '
                                               'that is the destination of this proxy '
                                               "projection's output. If omitted, "
                                               'deferred initialization applies.',
                                'type': 'string'},
                  'sender': { 'description': 'Name of the OutputPort or Mechanism that '
                                             "is the source of this proxy projection's "
                                             'input. If omitted, deferred '
                                             'initialization applies.',
                              'type': 'string'}},
  'required': ['proxy_for'],
  'type': 'object'}
TOOL_NOTES = "ProxyProjection is an internal PsyNeuLink implementation detail for nested Composition boundaries — agents almost never need to instantiate it directly; PsyNeuLink creates proxies automatically when add_node/add_projection involves nested Compositions. The `proxy_for` argument must be an existing live Projection object (passed by name); the constructor stores a weakref and sets `proxy_for._proxy = self`. The `learning_rate` parameter is a SharedParameter that delegates to the proxied projection — setting it independently on the ProxyProjection has no effect unless the proxied projection's value changes. Assigning learning_rate when learnable=False raises an error."


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.ProxyProjection
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
    def create_proxy_projection(args: dict[str, Any] | None = None) -> Any:
        'Call this tool only when you need to create a proxy MappingProjection that stands in for a real projection crossing a nested Composition boundary (i.e., a projection to/from the input_CIM or output_CIM of a nested Composition).'
        return _impl(args or {})
