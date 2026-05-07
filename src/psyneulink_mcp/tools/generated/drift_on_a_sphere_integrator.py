"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import psyneulink as pnl

from psyneulink_mcp import handles
from psyneulink_mcp.feedback import captured_tool

__source_sha256__ = 'e1fac85c4630b6ae2852fa07700431b619a6aa55eac9a133a8a8e5bbb8ff8e95'
__pnl_qualname__ = 'psyneulink.DriftOnASphereIntegrator'
__pnl_kind__ = 'class'
__pnl_parents__ = ['IntegratorFunction',
 'StatefulFunction',
 'Function_Base',
 'Function',
 'ShellClass',
 'Component',
 'MDFSerializable']
__pnl_parent_sha256s__ = {'Component': 'b878afca9fca90ac1a952605ca8d39a37f25ebebf1411a7f545b9c48a3eaeec3',
 'Function': '49ff0535055d97328c0f76806a53021714e2f8577d138152b75b7e15fcaab2e3',
 'Function_Base': '9b4c0d2feb23147f7d25af3ae03decf546fdb1f2e8be53abb8d8168801d60afa',
 'IntegratorFunction': '8a17d1e7ef745b7ec20cf5925290acde573cbabda2806b3a7aa26ce0cc966916',
 'MDFSerializable': 'caad6059e8ef158be1269a23127f13da3733824c3585f9b4d6e3a63de82f65da',
 'ShellClass': 'adc23754ebeb0c55bdde1324622b33a509116703503508ee7e7de181a8afeee6',
 'StatefulFunction': 'b49d4a3b9b27486e488e3eb62eb3a9313fc20a2170b37eebb6b79b803fa7dedb'}
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_drift_on_a_sphere_integrator'
TOOL_DESCRIPTION = 'Create a PsyNeuLink DriftOnASphereIntegrator function: a stateful integrator whose state is a unit vector evolving on the sphere S^(dimension-1), with drift and isotropic/anisotropic noise applied in the tangent space and mapped back to the sphere via the exponential map. Beyond IntegratorFunction, this adds three input interpretations (scalar drift along a parallel-transported direction, tangent-space displacement of length dimension-1, or target point of length dimension) selected via input_space, plus the dimension parameter and Cartesian-or-hyperspherical initializer. Returns a function handle suitable for assigning to a Mechanism (e.g. as the function of a ProcessingMechanism producing a temporal-context vector).\n\nParameters (JSON Schema):\n{\n  "additionalProperties": false,\n  "properties": {\n    "default_variable": {\n      "description": "Template shape for the drift input. MUST be length dimension-1 (tangent template) or length dimension (target template, requires input_space=\'target\'). A length-1 array is NOT accepted here even though scalar drift is supported at call time; omit this field for scalar drift mode.",\n      "items": {\n        "type": "number"\n      },\n      "type": "array"\n    },\n    "dimension": {\n      "default": 3,\n      "description": "Ambient dimension d of the embedding R^d; the state lives on S^(d-1). Must be >= 2.",\n      "minimum": 2,\n      "type": "integer"\n    },\n    "initializer": {\n      "description": "Starting point on the sphere. MUST be length dimension (Cartesian, will be normalized to unit length) OR length dimension-1 (hyperspherical angles in radians). Must NOT be the zero vector. If omitted, defaults to e_0 = [1, 0, ..., 0].",\n      "items": {\n        "type": "number"\n      },\n      "type": "array"\n    },\n    "input_space": {\n      "default": "auto",\n      "description": "How a vector input to the function is interpreted at runtime. \'tangent\' = length dimension-1 tangent displacement; \'target\' = length dimension point on the sphere (geodesic step toward it); \'auto\' picks by length and warns once when length-d is treated as a target. Scalar inputs always mean drift along the persistent drift_dir regardless of this setting.",\n      "enum": [\n        "auto",\n        "tangent",\n        "target"\n      ],\n      "type": "string"\n    },\n    "name": {\n      "description": "Optional name for this function instance.",\n      "type": "string"\n    },\n    "noise": {\n      "default": 0,\n      "description": "Diffusion coefficient. Scalar = isotropic noise on the sphere. Array MUST have length dimension-1 (anisotropic noise in tangent coords); other array lengths raise FunctionError.",\n      "oneOf": [\n        {\n          "type": "number"\n        },\n        {\n          "items": {\n            "type": "number"\n          },\n          "type": "array"\n        }\n      ]\n    },\n    "offset": {\n      "default": 0,\n      "description": "Additive drift term, projected into the tangent space at each step.",\n      "oneOf": [\n        {\n          "type": "number"\n        },\n        {\n          "items": {\n            "type": "number"\n          },\n          "type": "array"\n        }\n      ]\n    },\n    "rate": {\n      "default": 1,\n      "description": "Multiplies the drift input. Scales angular velocity (scalar mode), tangent step size (tangent mode), or fraction of geodesic distance per step (target mode; 1.0 reaches target in one step).",\n      "oneOf": [\n        {\n          "type": "number"\n        },\n        {\n          "items": {\n            "type": "number"\n          },\n          "type": "array"\n        }\n      ]\n    },\n    "seed": {\n      "description": "Seed for the internal RNG used by the diffusion term.",\n      "type": "integer"\n    },\n    "time_step_size": {\n      "default": 1,\n      "description": "Integration step dt. Drift scales as dt and noise as sqrt(dt).",\n      "exclusiveMinimum": 0,\n      "type": "number"\n    }\n  },\n  "required": [\n    "dimension"\n  ],\n  "type": "object"\n}\n\nNotes:\nDimensional gotchas — most reported failures come from getting these wrong:\n\n- `initializer` length is `dimension` (Cartesian, gets normalized) OR `dimension - 1` (hyperspherical angles). NOT length 1, NOT a scalar, NOT the zero vector. Examples for dimension=25: 25 nonzero floats (e.g. small random values), or 24 angles. To pick a safe Cartesian default, use a unit basis vector like [1.0, 0.0, ..., 0.0] of length `dimension`.\n- `default_variable` must be length `dimension - 1` (tangent template) or `dimension` (target template, with input_space=\'target\'). A length-1 array is rejected even though the runtime function accepts scalar drift; just omit `default_variable` to use scalar drift mode.\n- `noise` as an array must be exactly length `dimension - 1`; any other length raises FunctionError.\n\nBehavioral notes:\n\n- The state stored in `previous_value` is always a unit vector; the function output is the new unit vector after one integration step.\n- Scalar drift uses a persistent `drift_dir` (a random tangent unit vector, parallel-transported each step). It is not user-settable through this tool; if you need a specific direction, supply a tangent-space `default_variable` of length dimension-1 instead.\n- In target mode with rate=1.0 and time_step_size=1.0 the system reaches the target in one step; 0<rate<1 moves only partway along the geodesic.\n- `dimension` is read-only after construction.'
TOOL_PARAMETERS = { 'additionalProperties': False,
  'properties': { 'default_variable': { 'description': 'Template shape for the drift '
                                                       'input. MUST be length '
                                                       'dimension-1 (tangent template) '
                                                       'or length dimension (target '
                                                       'template, requires '
                                                       "input_space='target'). A "
                                                       'length-1 array is NOT accepted '
                                                       'here even though scalar drift '
                                                       'is supported at call time; '
                                                       'omit this field for scalar '
                                                       'drift mode.',
                                        'items': {'type': 'number'},
                                        'type': 'array'},
                  'dimension': { 'default': 3,
                                 'description': 'Ambient dimension d of the embedding '
                                                'R^d; the state lives on S^(d-1). Must '
                                                'be >= 2.',
                                 'minimum': 2,
                                 'type': 'integer'},
                  'initializer': { 'description': 'Starting point on the sphere. MUST '
                                                  'be length dimension (Cartesian, '
                                                  'will be normalized to unit length) '
                                                  'OR length dimension-1 '
                                                  '(hyperspherical angles in radians). '
                                                  'Must NOT be the zero vector. If '
                                                  'omitted, defaults to e_0 = [1, 0, '
                                                  '..., 0].',
                                   'items': {'type': 'number'},
                                   'type': 'array'},
                  'input_space': { 'default': 'auto',
                                   'description': 'How a vector input to the function '
                                                  'is interpreted at runtime. '
                                                  "'tangent' = length dimension-1 "
                                                  "tangent displacement; 'target' = "
                                                  'length dimension point on the '
                                                  'sphere (geodesic step toward it); '
                                                  "'auto' picks by length and warns "
                                                  'once when length-d is treated as a '
                                                  'target. Scalar inputs always mean '
                                                  'drift along the persistent '
                                                  'drift_dir regardless of this '
                                                  'setting.',
                                   'enum': ['auto', 'tangent', 'target'],
                                   'type': 'string'},
                  'name': { 'description': 'Optional name for this function instance.',
                            'type': 'string'},
                  'noise': { 'default': 0,
                             'description': 'Diffusion coefficient. Scalar = isotropic '
                                            'noise on the sphere. Array MUST have '
                                            'length dimension-1 (anisotropic noise in '
                                            'tangent coords); other array lengths '
                                            'raise FunctionError.',
                             'oneOf': [ {'type': 'number'},
                                        { 'items': {'type': 'number'},
                                          'type': 'array'}]},
                  'offset': { 'default': 0,
                              'description': 'Additive drift term, projected into the '
                                             'tangent space at each step.',
                              'oneOf': [ {'type': 'number'},
                                         { 'items': {'type': 'number'},
                                           'type': 'array'}]},
                  'rate': { 'default': 1,
                            'description': 'Multiplies the drift input. Scales angular '
                                           'velocity (scalar mode), tangent step size '
                                           '(tangent mode), or fraction of geodesic '
                                           'distance per step (target mode; 1.0 '
                                           'reaches target in one step).',
                            'oneOf': [ {'type': 'number'},
                                       {'items': {'type': 'number'}, 'type': 'array'}]},
                  'seed': { 'description': 'Seed for the internal RNG used by the '
                                           'diffusion term.',
                            'type': 'integer'},
                  'time_step_size': { 'default': 1,
                                      'description': 'Integration step dt. Drift '
                                                     'scales as dt and noise as '
                                                     'sqrt(dt).',
                                      'exclusiveMinimum': 0,
                                      'type': 'number'}},
  'required': ['dimension'],
  'type': 'object'}
TOOL_NOTES = "Dimensional gotchas — most reported failures come from getting these wrong:\n\n- `initializer` length is `dimension` (Cartesian, gets normalized) OR `dimension - 1` (hyperspherical angles). NOT length 1, NOT a scalar, NOT the zero vector. Examples for dimension=25: 25 nonzero floats (e.g. small random values), or 24 angles. To pick a safe Cartesian default, use a unit basis vector like [1.0, 0.0, ..., 0.0] of length `dimension`.\n- `default_variable` must be length `dimension - 1` (tangent template) or `dimension` (target template, with input_space='target'). A length-1 array is rejected even though the runtime function accepts scalar drift; just omit `default_variable` to use scalar drift mode.\n- `noise` as an array must be exactly length `dimension - 1`; any other length raises FunctionError.\n\nBehavioral notes:\n\n- The state stored in `previous_value` is always a unit vector; the function output is the new unit vector after one integration step.\n- Scalar drift uses a persistent `drift_dir` (a random tangent unit vector, parallel-transported each step). It is not user-settable through this tool; if you need a specific direction, supply a tangent-space `default_variable` of length dimension-1 instead.\n- In target mode with rate=1.0 and time_step_size=1.0 the system reaches the target in one step; 0<rate<1 moves only partway along the geodesic.\n- `dimension` is read-only after construction."


def _impl(kwargs: dict[str, Any]) -> Any:
    target = pnl.DriftOnASphereIntegrator
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
    def create_drift_on_a_sphere_integrator(args: dict[str, Any] | None = None) -> Any:
        'Create a PsyNeuLink DriftOnASphereIntegrator function: a stateful integrator whose state is a unit vector evolving on the sphere S^(dimension-1), with drift and isotropic/anisotropic noise applied in the tangent space and mapped back to the sphere via the exponential map.'
        return _impl(args or {})
