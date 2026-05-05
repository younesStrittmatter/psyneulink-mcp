"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '9287b6681622bf41fb60c77dcc2a12d3fc0e58105a75f0031abe515448900d5d'
__pnl_qualname__ = 'psyneulink.ParameterAlias'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_parameter_alias'
TOOL_DESCRIPTION = 'Call this tool to create a named alias for an existing PsyNeuLink Parameter object — use it when you need the same parameter to be accessible under a second name (e.g., a legacy or shorthand name) without duplicating its state. The result is a ParameterAlias instance that transparently forwards all attribute reads and writes to the source Parameter, except for its own identity fields (name, aliases, source, constructor_argument).\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "name": {\n      "description": "The name for this alias. This is the only identity field that differs from the source Parameter.",\n      "type": "string"\n    },\n    "source": {\n      "description": "The Parameter instance that this alias should point to. All non-identity attribute access is forwarded to this object.",\n      "type": "object"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\nBoth arguments are optional at construction time, but a ParameterAlias without a `source` is essentially inert — attribute delegation will fail at access time. `source` must be a Parameter instance that supports `_register_alias`; passing a plain object is tolerated (the registration step is silently skipped) but is unlikely to be useful. Deep-copying a ParameterAlias produces another ParameterAlias (not a Parameter), which is correct but may surprise code that checks `isinstance(x, Parameter)` exclusively.'
TOOL_PARAMETERS = { 'properties': { 'name': { 'description': 'The name for this alias. This is the only '
                                           'identity field that differs from the '
                                           'source Parameter.',
                            'type': 'string'},
                  'source': { 'description': 'The Parameter instance that this alias '
                                             'should point to. All non-identity '
                                             'attribute access is forwarded to this '
                                             'object.',
                              'type': 'object'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = 'Both arguments are optional at construction time, but a ParameterAlias without a `source` is essentially inert — attribute delegation will fail at access time. `source` must be a Parameter instance that supports `_register_alias`; passing a plain object is tolerated (the registration step is silently skipped) but is unlikely to be useful. Deep-copying a ParameterAlias produces another ParameterAlias (not a Parameter), which is correct but may surprise code that checks `isinstance(x, Parameter)` exclusively.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.ParameterAlias
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
    def create_parameter_alias(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to create a named alias for an existing PsyNeuLink Parameter object — use it when you need the same parameter to be accessible under a second name (e.g., a legacy or shorthand name) without duplicating its state.'
        return _impl(args or {})
