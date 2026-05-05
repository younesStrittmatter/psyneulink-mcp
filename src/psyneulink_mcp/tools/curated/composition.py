"""Curated execution + introspection tools for PsyNeuLink compositions.

Three of the historically-curated tools (``add_node``,
``add_linear_pathway``, ``add_projection``) moved to the generated
layer once captured failures gave the regen loop enough signal to be
worth iterating on. They now live in ``tools/generated/composition_*.py``
backed by the seed directives in ``generator/seeds.txt`` and the shared
runtime helper at :mod:`psyneulink_mcp.method_helpers`.

What stays curated:

* ``run_composition`` — the one execution entry point. The shape of its
  ``inputs`` argument (``{handle: trial-list-of-lists}``) doesn't map
  cleanly onto a generated method tool, and the result-massaging
  (``output_values`` per node, JSON-friendly result coercion) is
  bespoke enough that the cost of regen-iteration outweighs the
  benefit.
* ``list_handles`` / ``describe_handle`` — purely registry queries that
  exist so the agent can recover from confusion mid-session. No PNL
  surface to introspect.

The agent's loop is meant to look like:

1. ``create_transfer_mechanism(...)`` → handle ``h_a``
2. ``create_transfer_mechanism(...)`` → handle ``h_b``
3. ``create_composition(...)``       → handle ``h_c``
4. ``add_linear_processing_pathway(composition=h_c, pathway=[h_a, h_b])``
5. ``run_composition(composition=h_c, inputs={h_a: [[1, 2, 3]]})``
"""

from __future__ import annotations

import json
from typing import Any

from ... import handles
from ...feedback import captured_tool


def _safe_jsonable(value: Any) -> Any:
    """Best-effort conversion of a PNL run result into a JSON-friendly shape.

    ``Composition.run`` returns a ``numpy.ndarray`` of trial outputs.
    The agent only consumes the value via the tool transport, which is
    JSON, so we coerce here rather than at the call site.
    """
    try:
        json.dumps(value)
        return value
    except (TypeError, ValueError):
        pass
    try:
        return [list(row) for row in value]
    except Exception:
        return repr(value)


def register(mcp: Any) -> None:
    @captured_tool(mcp, layer="curated")
    def run_composition(
        composition: str,
        inputs: dict[str, Any] | None = None,
        num_trials: int | None = None,
    ) -> dict[str, Any]:
        """Execute a Composition.

        WHEN TO CALL: after the composition's nodes and projections are
        wired up. This blocks until the run completes.

        Args:
            composition: Handle returned by ``create_composition``.
            inputs: Mapping of ``{<input_node_handle>: trial_values}``.
                Each ``trial_values`` is a list-of-lists where the
                outer list is trials and the inner list is the
                per-port input vector for that trial. Examples::

                    {h_in: [[1.0, 2.0]]}              # 1 trial, 2-dim input
                    {h_in: [[1], [2], [3]]}           # 3 trials, scalar input

                Pass ``None`` (or omit) for compositions that don't
                need external inputs.
            num_trials: Optional explicit trial count. Usually inferred
                from the inputs.

        Returns:
            ``{"composition": <handle>, "result": ..., "output_values":
            {node_name: [...] }}``. ``result`` is the final trial's
            output (numpy → list); ``output_values`` is the last value
            of each node, useful for inspecting intermediate
            activations.
        """
        handles.record_call(
            "run_composition",
            {
                "composition": composition,
                "inputs": inputs,
                "num_trials": num_trials,
            },
            result_handle=None,
            tool_layer="curated",
        )
        comp = handles.resolve_handle(composition)
        run_kwargs: dict[str, Any] = {}
        if inputs:
            run_kwargs["inputs"] = {
                handles.resolve_handle(handle): values
                for handle, values in inputs.items()
            }
        if num_trials is not None:
            run_kwargs["num_trials"] = num_trials
        result = comp.run(**run_kwargs)

        per_node: dict[str, Any] = {}
        for node in comp.nodes:
            try:
                per_node[node.name] = _safe_jsonable(node.output_values)
            except Exception as exc:  # pragma: no cover — defensive
                per_node[node.name] = f"<unreadable: {exc!r}>"

        return {
            "composition": composition,
            "result": _safe_jsonable(result),
            "output_values": per_node,
        }

    @captured_tool(mcp, layer="curated")
    def list_handles() -> list[dict[str, Any]]:
        """Show every live PNL object created in this session.

        WHEN TO CALL: to recover from confusion about which handles
        exist, or to confirm what was created so far.
        """
        return handles.list_handles()

    @captured_tool(mcp, layer="curated")
    def describe_handle(handle: str) -> dict[str, Any]:
        """Return the type, name, and ``repr`` of a single handle.

        WHEN TO CALL: when ``list_handles`` isn't enough and you need
        to confirm the type of a specific object before passing it
        somewhere.
        """
        return handles.describe_handle(handle)
