"""Curated tools for composing and running PsyNeuLink models.

These tools are the bridge between the per-class generated tools (which
each create a single PNL object and return a handle) and an actual
runnable model. The agent's loop is meant to look like:

1. ``create_transfer_mechanism(...)`` → handle ``h_a``
2. ``create_transfer_mechanism(...)`` → handle ``h_b``
3. ``create_composition(...)``       → handle ``h_c``
4. ``add_linear_pathway(composition=h_c, nodes=[h_a, h_b])``
5. ``run_composition(composition=h_c, inputs={h_a: [[1, 2, 3]]})``

We intentionally keep the surface narrow:

* ``add_node`` / ``add_linear_pathway`` / ``add_projection`` cover the
  topologies an MVP modeling session needs.
* ``run_composition`` is the one execution entry point.
* ``list_handles`` / ``describe_handle`` exist so the agent can recover
  from confusion mid-session.

Anything more advanced (controllers, learning, custom schedulers) is
deliberately out of scope until the MVP loop is proven.
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


def _node_summary(composition: Any) -> list[str]:
    return [getattr(node, "name", repr(node)) for node in composition.nodes]


def register(mcp: Any) -> None:
    @captured_tool(mcp, layer="curated")
    def add_node(composition: str, node: str) -> dict[str, Any]:
        """Add a single Mechanism (or sub-Composition) to a Composition.

        WHEN TO CALL: when wiring a model that doesn't fit a single
        linear pathway, or when adding an isolated mechanism whose
        projections you'll specify with ``add_projection``.

        Args:
            composition: Handle returned by ``create_composition``.
            node: Handle for the Mechanism / Composition to add.

        Returns:
            ``{"composition": <handle>, "added": <handle>,
            "nodes": [name, ...]}`` listing every node in the
            composition after the add.
        """
        comp = handles.resolve_handle(composition)
        n = handles.resolve_handle(node)
        comp.add_node(n)
        return {
            "composition": composition,
            "added": node,
            "nodes": _node_summary(comp),
        }

    @captured_tool(mcp, layer="curated")
    def add_linear_pathway(
        composition: str, nodes: list[str]
    ) -> dict[str, Any]:
        """Add an ordered chain of nodes connected by default MappingProjections.

        WHEN TO CALL: feed-forward chains like
        ``input -> hidden -> output``. PNL inserts a default
        identity-ish MappingProjection between each consecutive pair.

        Args:
            composition: Handle returned by ``create_composition``.
            nodes: Ordered list of Mechanism handles. The first entry
                becomes an INPUT node of the composition; the last
                becomes an OUTPUT node.

        Returns:
            ``{"composition": <handle>, "pathway": [<handle>, ...],
            "nodes": [name, ...]}``.
        """
        if not nodes:
            raise ValueError("add_linear_pathway requires at least one node")
        comp = handles.resolve_handle(composition)
        objs = [handles.resolve_handle(h) for h in nodes]
        comp.add_linear_processing_pathway(objs)
        return {
            "composition": composition,
            "pathway": list(nodes),
            "nodes": _node_summary(comp),
        }

    @captured_tool(mcp, layer="curated")
    def add_projection(
        composition: str,
        sender: str,
        receiver: str,
        matrix: Any = None,
    ) -> dict[str, Any]:
        """Add an explicit MappingProjection between two existing nodes.

        WHEN TO CALL: a custom weight matrix is required, or the
        connection pattern isn't a simple linear pathway (e.g.,
        skip connections, recurrent loops, fan-out).

        Args:
            composition: Handle returned by ``create_composition``.
            sender: Handle of the source Mechanism (must already be in
                the composition; if not, it will be added).
            receiver: Handle of the target Mechanism (same rule).
            matrix: Optional weight matrix. Either a 2D list of floats
                or one of PNL's matrix keywords as a string
                (``"IDENTITY_MATRIX"``, ``"FULL_CONNECTIVITY_MATRIX"``,
                ``"RANDOM_CONNECTIVITY_MATRIX"``). ``None`` lets PNL
                pick its default for the given shapes.

        Returns:
            ``{"composition": <handle>, "from": <handle>,
            "to": <handle>}``.
        """
        import psyneulink as pnl  # local to keep server import cheap

        comp = handles.resolve_handle(composition)
        s = handles.resolve_handle(sender)
        r = handles.resolve_handle(receiver)
        kwargs: dict[str, Any] = {"sender": s, "receiver": r}
        if matrix is not None:
            kwargs["matrix"] = matrix
        proj = pnl.MappingProjection(**kwargs)
        comp.add_projection(proj)
        return {
            "composition": composition,
            "from": sender,
            "to": receiver,
        }

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
