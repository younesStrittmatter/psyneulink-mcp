"""Auto-generated index. Do not edit by hand.

Rewritten by scripts/generate_tools.py on every successful run.
On a fresh clone (no regen yet) the modules tuple is empty and
register_all is a safe no-op.
"""

from __future__ import annotations

from typing import Any

from . import composition, convert_to_np_array, lc_control_mechanism, lca_mechanism, linear, logistic, mapping_projection, normal_dist, objective_mechanism, pathway, processing_mechanism, recurrent_transfer_mechanism, stability, threshold, time_scale, transfer_mechanism

ALL = (composition, convert_to_np_array, lc_control_mechanism, lca_mechanism, linear, logistic, mapping_projection, normal_dist, objective_mechanism, pathway, processing_mechanism, recurrent_transfer_mechanism, stability, threshold, time_scale, transfer_mechanism,)


def register_all(mcp: Any) -> None:
    """Register every generated tool module with ``mcp``."""
    for module in ALL:
        module.register(mcp)
