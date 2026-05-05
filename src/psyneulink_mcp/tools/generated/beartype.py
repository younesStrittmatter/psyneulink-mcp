"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '931c0d2027ddad89523c10bde3b2ca1525509deb30df4ba2a19c175e733d0cbd'
__pnl_qualname__ = 'psyneulink.core.components.functions.nonstateful.distributionfunctions.beartype'
__pnl_kind__ = 'function'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'beartype'
TOOL_DESCRIPTION = 'Do not call this tool for PsyNeuLink modeling tasks. This is the `beartype` runtime type-checking decorator re-exported through PsyNeuLink\'s namespace — a meta-programming utility, not a neural modeling primitive. It is only relevant if you need to programmatically apply O(1) runtime type-checking to a Python callable or class, or obtain a pre-configured beartype decorator for a specific configuration.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "conf": {\n      "additionalProperties": false,\n      "description": "Beartype configuration as a plain dict of BeartypeConf keyword arguments (e.g., {\\"is_debug\\": true}). Defaults to the standard O(1) configuration. Most callers should omit this.",\n      "properties": {\n        "is_debug": {\n          "description": "If true, emit generated type-checking wrapper source to stdout.",\n          "type": "boolean"\n        },\n        "is_pep484_tower": {\n          "description": "If true, enforce PEP 484 numeric tower (int <= float <= complex).",\n          "type": "boolean"\n        }\n      },\n      "type": "object"\n    },\n    "obj": {\n      "description": "Fully-qualified name or string reference of the pure-Python callable or class to decorate with runtime type-checking. Omit to enter configuration mode, which returns a cached private decorator rather than decorating an object.",\n      "type": "string"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\nThis symbol is beartype._decor.decorcache.beartype re-exported under PsyNeuLink\'s distribution functions namespace — it is not a PsyNeuLink component. Passing a live Python callable through MCP JSON is not possible; obj is represented as a string but the host cannot resolve it to a callable at runtime, so decoration mode is effectively unavailable to LLM agents. If Python optimizations are active (python -O), the decorator silently becomes a no-op. Configuration mode (obj omitted, conf provided) returns a cached private decorator object, not a modeling result.'
TOOL_PARAMETERS = { 'properties': { 'conf': { 'additionalProperties': False,
                            'description': 'Beartype configuration as a plain dict of '
                                           'BeartypeConf keyword arguments (e.g., '
                                           '{"is_debug": true}). Defaults to the '
                                           'standard O(1) configuration. Most callers '
                                           'should omit this.',
                            'properties': { 'is_debug': { 'description': 'If true, '
                                                                         'emit '
                                                                         'generated '
                                                                         'type-checking '
                                                                         'wrapper '
                                                                         'source to '
                                                                         'stdout.',
                                                          'type': 'boolean'},
                                            'is_pep484_tower': { 'description': 'If '
                                                                                'true, '
                                                                                'enforce '
                                                                                'PEP '
                                                                                '484 '
                                                                                'numeric '
                                                                                'tower '
                                                                                '(int '
                                                                                '<= '
                                                                                'float '
                                                                                '<= '
                                                                                'complex).',
                                                                 'type': 'boolean'}},
                            'type': 'object'},
                  'obj': { 'description': 'Fully-qualified name or string reference of '
                                          'the pure-Python callable or class to '
                                          'decorate with runtime type-checking. Omit '
                                          'to enter configuration mode, which returns '
                                          'a cached private decorator rather than '
                                          'decorating an object.',
                           'type': 'string'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = "This symbol is beartype._decor.decorcache.beartype re-exported under PsyNeuLink's distribution functions namespace — it is not a PsyNeuLink component. Passing a live Python callable through MCP JSON is not possible; obj is represented as a string but the host cannot resolve it to a callable at runtime, so decoration mode is effectively unavailable to LLM agents. If Python optimizations are active (python -O), the decorator silently becomes a no-op. Configuration mode (obj omitted, conf provided) returns a cached private decorator object, not a modeling result."


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.beartype
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
    def beartype(args: dict[str, Any] | None = None) -> Any:
        'Do not call this tool for PsyNeuLink modeling tasks.'
        return _impl(args or {})
