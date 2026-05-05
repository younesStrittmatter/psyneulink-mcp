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
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_drift_on_a_sphere_integrator'
TOOL_DESCRIPTION = 'Use this tool to create a DriftOnASphereIntegrator when you need geometric Brownian motion on a unit sphere S^(d-1) — e.g., modeling neural population states that evolve on a spherical manifold. Each call to the resulting function advances the state one integration step via the exponential map and returns a unit vector (the new position on the sphere). Choose this over standard integrators when the state space is inherently spherical and you need drift+noise that respects the sphere\'s geometry.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "default_variable": {\n      "description": "Template for the drift input. In tangent/auto mode: length dimension-1 (tangent coords). In target mode: length dimension (target point on sphere). Omit to use zeros of the appropriate shape.",\n      "items": {\n        "type": "number"\n      },\n      "type": "array"\n    },\n    "dimension": {\n      "default": 3,\n      "description": "Ambient embedding dimension; sphere is S^(dimension-1). Must be >= 2.",\n      "type": "integer"\n    },\n    "initializer": {\n      "description": "Starting point. Length dimension = Cartesian coordinates (will be normalized). Length dimension-1 = hyperspherical angles. Defaults to [1, 0, 0, ...] (north pole).",\n      "items": {\n        "type": "number"\n      },\n      "type": "array"\n    },\n    "input_space": {\n      "default": "auto",\n      "description": "Controls how vector drift input is interpreted. \'tangent\': input is length d-1 tangent-space displacement. \'target\': input is length d Cartesian target on sphere (drift is geodesic toward it). \'auto\': infers from input length (d-1 \\u2192 tangent, d \\u2192 target with a one-time warning).",\n      "enum": [\n        "auto",\n        "tangent",\n        "target"\n      ],\n      "type": "string"\n    },\n    "noise": {\n      "default": 0,\n      "description": "Diffusion magnitude. Scalar for isotropic noise; 1D array of length dimension-1 for anisotropic noise in tangent coordinates.",\n      "oneOf": [\n        {\n          "type": "number"\n        },\n        {\n          "items": {\n            "type": "number"\n          },\n          "type": "array"\n        }\n      ]\n    },\n    "offset": {\n      "default": 0,\n      "description": "Additive drift term projected into tangent space.",\n      "oneOf": [\n        {\n          "type": "number"\n        },\n        {\n          "items": {\n            "type": "number"\n          },\n          "type": "array"\n        }\n      ]\n    },\n    "params": {\n      "description": "Optional parameter override dictionary passed to PsyNeuLink.",\n      "type": "object"\n    },\n    "rate": {\n      "default": 1,\n      "description": "Scales the drift. In scalar mode: angular velocity multiplier. In tangent mode: scales the angular step. In target mode: fraction of remaining geodesic distance per step (1.0 = reach target in one step with dt=1.0).",\n      "oneOf": [\n        {\n          "type": "number"\n        },\n        {\n          "items": {\n            "type": "number"\n          },\n          "type": "array"\n        }\n      ]\n    },\n    "seed": {\n      "description": "Integer seed for the internal random number generator. Omit for non-reproducible noise.",\n      "type": "integer"\n    },\n    "time_step_size": {\n      "default": 1,\n      "description": "Integration time step dt. Drift scales as dt; noise scales as sqrt(dt).",\n      "type": "number"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\n- `input_space` is not listed in the class signature but is accepted as a kwarg and controls tangent vs. target drift mode — set it explicitly to avoid the auto-detection RuntimeWarning.\n- In target mode with rate=1.0 and time_step_size=1.0, the integrator reaches the target in exactly one step; use 0 < rate < 1 for gradual movement.\n- `noise` array length must be dimension-1 (tangent coords), NOT dimension — passing an array of length dimension raises FunctionError.\n- `initializer` of length dimension is treated as Cartesian (normalized); length dimension-1 is treated as hyperspherical angles, not Cartesian.\n- The drift direction (`drift_dir`) for scalar inputs is initialized randomly and parallel-transported each step; results are not reproducible without `seed`.\n- `dimension` is read-only after construction; to change dimension, create a new instance.\n- `offset` is described as additive but is projected into tangent space — it does not shift the output in Euclidean space.\n- Scalar drift input scales the persistent drift direction vector, not the angle directly; the effective rotation magnitude is rate * |variable| * dt radians.'
TOOL_PARAMETERS = { 'properties': { 'default_variable': { 'description': 'Template for the drift input. '
                                                       'In tangent/auto mode: length '
                                                       'dimension-1 (tangent coords). '
                                                       'In target mode: length '
                                                       'dimension (target point on '
                                                       'sphere). Omit to use zeros of '
                                                       'the appropriate shape.',
                                        'items': {'type': 'number'},
                                        'type': 'array'},
                  'dimension': { 'default': 3,
                                 'description': 'Ambient embedding dimension; sphere '
                                                'is S^(dimension-1). Must be >= 2.',
                                 'type': 'integer'},
                  'initializer': { 'description': 'Starting point. Length dimension = '
                                                  'Cartesian coordinates (will be '
                                                  'normalized). Length dimension-1 = '
                                                  'hyperspherical angles. Defaults to '
                                                  '[1, 0, 0, ...] (north pole).',
                                   'items': {'type': 'number'},
                                   'type': 'array'},
                  'input_space': { 'default': 'auto',
                                   'description': 'Controls how vector drift input is '
                                                  "interpreted. 'tangent': input is "
                                                  'length d-1 tangent-space '
                                                  "displacement. 'target': input is "
                                                  'length d Cartesian target on sphere '
                                                  '(drift is geodesic toward it). '
                                                  "'auto': infers from input length "
                                                  '(d-1 → tangent, d → target with a '
                                                  'one-time warning).',
                                   'enum': ['auto', 'tangent', 'target'],
                                   'type': 'string'},
                  'noise': { 'default': 0,
                             'description': 'Diffusion magnitude. Scalar for isotropic '
                                            'noise; 1D array of length dimension-1 for '
                                            'anisotropic noise in tangent coordinates.',
                             'oneOf': [ {'type': 'number'},
                                        { 'items': {'type': 'number'},
                                          'type': 'array'}]},
                  'offset': { 'default': 0,
                              'description': 'Additive drift term projected into '
                                             'tangent space.',
                              'oneOf': [ {'type': 'number'},
                                         { 'items': {'type': 'number'},
                                           'type': 'array'}]},
                  'params': { 'description': 'Optional parameter override dictionary '
                                             'passed to PsyNeuLink.',
                              'type': 'object'},
                  'rate': { 'default': 1,
                            'description': 'Scales the drift. In scalar mode: angular '
                                           'velocity multiplier. In tangent mode: '
                                           'scales the angular step. In target mode: '
                                           'fraction of remaining geodesic distance '
                                           'per step (1.0 = reach target in one step '
                                           'with dt=1.0).',
                            'oneOf': [ {'type': 'number'},
                                       {'items': {'type': 'number'}, 'type': 'array'}]},
                  'seed': { 'description': 'Integer seed for the internal random '
                                           'number generator. Omit for '
                                           'non-reproducible noise.',
                            'type': 'integer'},
                  'time_step_size': { 'default': 1,
                                      'description': 'Integration time step dt. Drift '
                                                     'scales as dt; noise scales as '
                                                     'sqrt(dt).',
                                      'type': 'number'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = '- `input_space` is not listed in the class signature but is accepted as a kwarg and controls tangent vs. target drift mode — set it explicitly to avoid the auto-detection RuntimeWarning.\n- In target mode with rate=1.0 and time_step_size=1.0, the integrator reaches the target in exactly one step; use 0 < rate < 1 for gradual movement.\n- `noise` array length must be dimension-1 (tangent coords), NOT dimension — passing an array of length dimension raises FunctionError.\n- `initializer` of length dimension is treated as Cartesian (normalized); length dimension-1 is treated as hyperspherical angles, not Cartesian.\n- The drift direction (`drift_dir`) for scalar inputs is initialized randomly and parallel-transported each step; results are not reproducible without `seed`.\n- `dimension` is read-only after construction; to change dimension, create a new instance.\n- `offset` is described as additive but is projected into tangent space — it does not shift the output in Euclidean space.\n- Scalar drift input scales the persistent drift direction vector, not the angle directly; the effective rotation magnitude is rate * |variable| * dt radians.'


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
        'Use this tool to create a DriftOnASphereIntegrator when you need geometric Brownian motion on a unit sphere S^(d-1) — e.g., modeling neural population states that evolve on a spherical manifold.'
        return _impl(args or {})
