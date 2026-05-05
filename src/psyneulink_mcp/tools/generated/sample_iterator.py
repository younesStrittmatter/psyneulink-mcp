"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = '484d1ce57913760cafc5bf30c1bf6483eed4c373c6fe0f548f3610dd7d8ac589'
__pnl_qualname__ = 'psyneulink.SampleIterator'
__pnl_kind__ = 'class'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_sample_iterator'
TOOL_DESCRIPTION = 'Call this tool when you need to create a reusable sampling iterator to feed a sequence of values into a PsyNeuLink operation that accepts an iterator (e.g., GridSearch, ParameterEstimationComposition, or any mechanism that iterates over a sample space). The result is a SampleIterator object whose `next()` yields one sample per call and which raises StopIteration when the sequence is exhausted.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "specification": {\n      "description": "Defines the sample sequence. Pass a JSON array of numbers (e.g. [0.1, 0.5, 1.0]) to iterate over an explicit list; pass an object with \'start\', \'stop\', and \'step\' keys to generate a stepped range (equivalent to SampleSpec(start, stop, step)); pass an object with \'start\', \'stop\', and \'num\' keys to generate evenly-spaced samples between start and stop.",\n      "oneOf": [\n        {\n          "description": "Explicit list of sample values; iterator stops after the last element.",\n          "items": {\n            "type": "number"\n          },\n          "type": "array"\n        },\n        {\n          "description": "Stepped or count-based numeric range, equivalent to SampleSpec(start, stop, step|num).",\n          "properties": {\n            "num": {\n              "description": "Total number of samples to draw. Provide either num or step, not both.",\n              "type": "integer"\n            },\n            "start": {\n              "description": "First value in the sequence.",\n              "type": "number"\n            },\n            "step": {\n              "description": "Increment between successive samples. Provide either step or num, not both.",\n              "type": "number"\n            },\n            "stop": {\n              "description": "Upper bound; iteration stops when the generated value exceeds this.",\n              "type": "number"\n            }\n          },\n          "required": [\n            "start",\n            "stop"\n          ],\n          "type": "object"\n        }\n      ]\n    }\n  },\n  "required": [\n    "specification"\n  ],\n  "type": "object"\n}\n\nNotes:\n- Callable and SampleSpec specifications cannot be passed directly through the MCP JSON boundary; only list-arrays and start/stop/step|num objects are supported here.\n- For the object form, passing both `step` and `num` simultaneously is undefined; use one or the other.\n- The iterator is stateful and single-pass by default; call `reset()` on the returned object to replay from the beginning.\n- For large or infinite sequences, prefer the start/stop/step object form over a large explicit array — the object form generates values on demand without pre-allocating memory.\n- An explicit list stops at the last element; a stepped range stops when the next computed value would exceed `stop`; neither form stops iteration for a callable specification (not supported via JSON).'
TOOL_PARAMETERS = { 'properties': { 'specification': { 'description': 'Defines the sample sequence. Pass '
                                                    'a JSON array of numbers (e.g. '
                                                    '[0.1, 0.5, 1.0]) to iterate over '
                                                    'an explicit list; pass an object '
                                                    "with 'start', 'stop', and 'step' "
                                                    'keys to generate a stepped range '
                                                    '(equivalent to SampleSpec(start, '
                                                    'stop, step)); pass an object with '
                                                    "'start', 'stop', and 'num' keys "
                                                    'to generate evenly-spaced samples '
                                                    'between start and stop.',
                                     'oneOf': [ { 'description': 'Explicit list of '
                                                                 'sample values; '
                                                                 'iterator stops after '
                                                                 'the last element.',
                                                  'items': {'type': 'number'},
                                                  'type': 'array'},
                                                { 'description': 'Stepped or '
                                                                 'count-based numeric '
                                                                 'range, equivalent to '
                                                                 'SampleSpec(start, '
                                                                 'stop, step|num).',
                                                  'properties': { 'num': { 'description': 'Total '
                                                                                          'number '
                                                                                          'of '
                                                                                          'samples '
                                                                                          'to '
                                                                                          'draw. '
                                                                                          'Provide '
                                                                                          'either '
                                                                                          'num '
                                                                                          'or '
                                                                                          'step, '
                                                                                          'not '
                                                                                          'both.',
                                                                           'type': 'integer'},
                                                                  'start': { 'description': 'First '
                                                                                            'value '
                                                                                            'in '
                                                                                            'the '
                                                                                            'sequence.',
                                                                             'type': 'number'},
                                                                  'step': { 'description': 'Increment '
                                                                                           'between '
                                                                                           'successive '
                                                                                           'samples. '
                                                                                           'Provide '
                                                                                           'either '
                                                                                           'step '
                                                                                           'or '
                                                                                           'num, '
                                                                                           'not '
                                                                                           'both.',
                                                                            'type': 'number'},
                                                                  'stop': { 'description': 'Upper '
                                                                                           'bound; '
                                                                                           'iteration '
                                                                                           'stops '
                                                                                           'when '
                                                                                           'the '
                                                                                           'generated '
                                                                                           'value '
                                                                                           'exceeds '
                                                                                           'this.',
                                                                            'type': 'number'}},
                                                  'required': ['start', 'stop'],
                                                  'type': 'object'}]}},
  'required': ['specification'],
  'type': 'object'}
TOOL_NOTES = '- Callable and SampleSpec specifications cannot be passed directly through the MCP JSON boundary; only list-arrays and start/stop/step|num objects are supported here.\n- For the object form, passing both `step` and `num` simultaneously is undefined; use one or the other.\n- The iterator is stateful and single-pass by default; call `reset()` on the returned object to replay from the beginning.\n- For large or infinite sequences, prefer the start/stop/step object form over a large explicit array — the object form generates values on demand without pre-allocating memory.\n- An explicit list stops at the last element; a stepped range stops when the next computed value would exceed `stop`; neither form stops iteration for a callable specification (not supported via JSON).'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.SampleIterator
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
    def create_sample_iterator(args: dict[str, Any] | None = None) -> Any:
        'Call this tool when you need to create a reusable sampling iterator to feed a sequence of values into a PsyNeuLink operation that accepts an iterator (e.g., GridSearch, ParameterEstimationComposition, or any mechanism that iterates over a sample space).'
        return _impl(args or {})
