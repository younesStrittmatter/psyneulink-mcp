"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = 'd5c783e5aefd873ed16351885ebc7b8591aedb75997c926f6ea5fe6bea094696'
__pnl_qualname__ = 'psyneulink.PNLJSONEncoder'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_pnljson_encoder'
TOOL_DESCRIPTION = 'Call this tool when you need a JSON encoder instance capable of serializing PsyNeuLink-specific objects (Components, numpy arrays, enums, MDF objects, etc.) that would otherwise fail standard JSON serialization. Returns a configured PNLJSONEncoder instance; pass it as the `cls` argument to `json.dumps()` or call `.encode(obj)` on it directly to convert PNL component summaries (`_dict_summary` output) into JSON-safe representations.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "allow_nan": {\n      "default": true,\n      "description": "If true, NaN/Infinity are serialized as JavaScript literals (non-standard JSON).",\n      "type": "boolean"\n    },\n    "check_circular": {\n      "default": true,\n      "description": "If true, circular references raise ValueError instead of causing infinite recursion.",\n      "type": "boolean"\n    },\n    "ensure_ascii": {\n      "default": true,\n      "description": "If true, non-ASCII characters are escaped in output; set false to allow Unicode passthrough.",\n      "type": "boolean"\n    },\n    "indent": {\n      "default": null,\n      "description": "Number of spaces for pretty-printing indentation. Omit for compact output.",\n      "type": "integer"\n    },\n    "skipkeys": {\n      "default": false,\n      "description": "If true, keys that are not basic types are skipped instead of raising TypeError.",\n      "type": "boolean"\n    },\n    "sort_keys": {\n      "default": false,\n      "description": "If true, dictionary keys are sorted in the output.",\n      "type": "boolean"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\nPNLJSONEncoder is a utility encoder, not a standalone transformation tool — it must be used with json.dumps(obj, cls=PNLJSONEncoder) or instance.encode(obj) to actually serialize anything. The MCP tool instantiates the encoder; it does not serialize any object on its own. The `separators` JSONEncoder parameter is omitted here as it is rarely needed and cannot be cleanly expressed as a JSON array of exactly two strings. numpy.ndarray objects are converted to lists (or scalars via .item() if list() raises); Components are reduced to their .name string; enums and functions become str(). Objects unknown to all handlers fall back to str() rather than raising.'
TOOL_PARAMETERS = { 'properties': { 'allow_nan': { 'default': True,
                                 'description': 'If true, NaN/Infinity are serialized '
                                                'as JavaScript literals (non-standard '
                                                'JSON).',
                                 'type': 'boolean'},
                  'check_circular': { 'default': True,
                                      'description': 'If true, circular references '
                                                     'raise ValueError instead of '
                                                     'causing infinite recursion.',
                                      'type': 'boolean'},
                  'ensure_ascii': { 'default': True,
                                    'description': 'If true, non-ASCII characters are '
                                                   'escaped in output; set false to '
                                                   'allow Unicode passthrough.',
                                    'type': 'boolean'},
                  'indent': { 'default': None,
                              'description': 'Number of spaces for pretty-printing '
                                             'indentation. Omit for compact output.',
                              'type': 'integer'},
                  'skipkeys': { 'default': False,
                                'description': 'If true, keys that are not basic types '
                                               'are skipped instead of raising '
                                               'TypeError.',
                                'type': 'boolean'},
                  'sort_keys': { 'default': False,
                                 'description': 'If true, dictionary keys are sorted '
                                                'in the output.',
                                 'type': 'boolean'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = 'PNLJSONEncoder is a utility encoder, not a standalone transformation tool — it must be used with json.dumps(obj, cls=PNLJSONEncoder) or instance.encode(obj) to actually serialize anything. The MCP tool instantiates the encoder; it does not serialize any object on its own. The `separators` JSONEncoder parameter is omitted here as it is rarely needed and cannot be cleanly expressed as a JSON array of exactly two strings. numpy.ndarray objects are converted to lists (or scalars via .item() if list() raises); Components are reduced to their .name string; enums and functions become str(). Objects unknown to all handlers fall back to str() rather than raising.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.PNLJSONEncoder
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
    def create_pnljson_encoder(args: dict[str, Any] | None = None) -> Any:
        'Call this tool when you need a JSON encoder instance capable of serializing PsyNeuLink-specific objects (Components, numpy arrays, enums, MDF objects, etc.) that would otherwise fail standard JSON serialization.'
        return _impl(args or {})
