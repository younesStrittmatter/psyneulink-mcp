"""Curated tools for navigating the inner structure of nested PNL compositions.

PsyNeuLink lets you wire one Composition into another (any ``Composition``
can act as a node inside another Composition), and several library
classes exploit this — ``EMComposition`` for episodic memory,
``AutodiffComposition`` for backprop-trainable subgraphs, etc. To wire
a projection INTO a specific inner node of a nested Composition, PNL's
own canonical models (see ``psyneulink/library/models/``) use
``composition.nodes[<inner_node_name>]`` to grab a handle and pass it
as ``receiver=`` to ``MappingProjection`` / ``add_projection``:

    em = pnl.EMComposition(name='EM', memory_template=[...], fields={...})
    pnl.MappingProjection(
        sender=context_layer,
        receiver=em.nodes[context_layer.name + ' [QUERY]'],
        matrix=pnl.IDENTITY_MATRIX,
    )

Without these introspection tools the LLM agent has no way to construct
that ``em.nodes[name]`` handle through the MCP, even after reading a
description that mentions the pattern. So we expose the lookup itself
as a small set of curated tools — they're general (work on any nested
Composition, any Mechanism with multiple ports), so we don't have to
add EM-specific or composition-class-specific code paths as new
library compositions land upstream.

Three shapes:

* ``get_composition_node(composition, node_name)`` — the inner-node
  lookup. Returns a fresh handle the agent can pass anywhere a node
  handle is expected.
* ``list_composition_nodes(composition)`` — the discovery counterpart;
  returns the inner-node names + types so the agent can see what's
  available before calling ``get_composition_node``.
* ``get_input_port(node, port)`` / ``get_output_port(node, port)`` —
  port-level addressing for non-primary ports of a Mechanism (or of an
  inner node fetched via ``get_composition_node``). Accept either a
  port name or a 0-based integer index.

All four register the resolved object back into the handle registry
and return a handle payload, so they compose cleanly with the rest
of the tool surface.
"""

from __future__ import annotations

from typing import Any

from ... import handles
from ...feedback import captured_tool


def _resolve_inner_node(composition_obj: Any, node_name: str) -> Any:
    """Look up ``node_name`` inside ``composition_obj.nodes``.

    PNL's ``Composition.nodes`` is a ``NodeRoleList`` that supports both
    integer indexing and dict-like name lookup. We try the dict-like
    path first (the common case) and fall back to scanning by name
    so we get a useful error if the name is missing.

    Raises a ValueError on miss with a list of available names — that
    error string flows back to the LLM as the tool_result, so the next
    attempt can pick the right name without a separate ``list_*`` call.
    """
    nodes = getattr(composition_obj, "nodes", None)
    if nodes is None:
        raise ValueError(
            f"object of type {type(composition_obj).__name__} has no .nodes "
            f"attribute (is it really a Composition?)"
        )
    try:
        return nodes[node_name]
    except (KeyError, TypeError):
        pass
    # Fall back to a name scan so the error message can list candidates.
    available = []
    try:
        for n in nodes:
            name = getattr(n, "name", None)
            if name is None:
                continue
            available.append(name)
            if name == node_name:
                return n
    except TypeError:
        pass
    raise ValueError(
        f"no inner node named {node_name!r}; available: {available}"
    )


def _resolve_port(
    owner: Any,
    port_spec: str | int,
    *,
    side: str,
) -> Any:
    """Look up ``side``-Port ``port_spec`` on ``owner``.

    ``side`` is ``"input"`` or ``"output"``. ``port_spec`` is either a
    port name (string) or a 0-based integer index. Raises ValueError
    with a list of candidate port names on miss.
    """
    attr = "input_ports" if side == "input" else "output_ports"
    ports = getattr(owner, attr, None)
    if ports is None:
        raise ValueError(
            f"object of type {type(owner).__name__} has no .{attr} "
            f"(it isn't a Mechanism / inner node)"
        )
    if isinstance(port_spec, int):
        try:
            return ports[port_spec]
        except (IndexError, TypeError) as exc:
            raise ValueError(
                f".{attr}[{port_spec}] out of range; got {len(list(ports))} ports"
            ) from exc
    # Name lookup — PNL's *_ports container also supports name keys, but
    # falling back to a scan gives us a useful error on miss.
    try:
        return ports[port_spec]
    except (KeyError, TypeError):
        pass
    available = []
    for p in ports:
        name = getattr(p, "name", None)
        if name is None:
            continue
        available.append(name)
        if name == port_spec:
            return p
    raise ValueError(
        f"no {side} port named {port_spec!r}; available: {available}"
    )


def register(mcp: Any) -> None:
    @captured_tool(mcp, layer="curated")
    def get_composition_node(composition: str, node_name: str) -> dict[str, Any]:
        """Return a handle to a named inner node of a nested Composition.

        WHEN TO CALL: when you need to wire INTO or OUT OF a specific
        inner node of a Composition that's used as a node in another
        Composition. This is the standard pattern for nested
        Compositions — ``EMComposition``, ``AutodiffComposition``,
        ``GRUComposition``, plain nested ``Composition`` — every one of
        them lets you address the constituent nodes by name via
        ``composition.nodes[name]``, and PNL's own canonical models
        (``psyneulink/library/models/``) use exactly this pattern.

        After this call you have a handle to the inner node that you
        can pass as ``sender=`` or ``receiver=`` to ``add_projection``,
        or as ``sender=`` / ``receiver=`` to a ``MappingProjection``,
        the same way you'd pass any top-level Mechanism handle.

        Use ``list_composition_nodes`` first if you don't already know
        the inner-node names (the naming convention is composition-
        class-specific — e.g. ``EMComposition`` appends ``" [QUERY]"``,
        ``" [VALUE]"``, ``" [RETRIEVED]"`` suffixes to each field name).

        Args:
            composition: Handle of the outer Composition (the one
                containing the inner node).
            node_name: Name of the inner node to fetch.

        Returns:
            ``{"handle": ..., "type": ..., "name": ..., "repr": ...}``
            for the inner node, registered in the handle registry so
            it works anywhere a node handle is expected. On miss, the
            tool raises with a list of available node names so the
            next attempt can pick the right one without needing
            another tool call first.
        """
        comp = handles.resolve_handle(composition)
        node = _resolve_inner_node(comp, node_name)
        payload = handles.register_handle(node)
        handles.record_call(
            "get_composition_node",
            {"composition": composition, "node_name": node_name},
            result_handle=payload.get("handle") if isinstance(payload, dict) else None,
            tool_layer="curated",
        )
        return payload

    @captured_tool(mcp, layer="curated")
    def list_composition_nodes(composition: str) -> dict[str, Any]:
        """List the inner nodes of a (possibly nested) Composition.

        WHEN TO CALL: before ``get_composition_node`` when you don't
        know the inner-node names of a nested Composition you just
        created (e.g. you built an ``EMComposition`` and need the
        names of its query / value / retrieved nodes for wiring).

        Args:
            composition: Handle of the Composition whose inner nodes
                you want to list.

        Returns:
            ``{"composition": <input_handle>, "nodes": [{"name": ...,
            "type": ..., "repr": ...}, ...]}``. The list is in the
            order PNL exposes ``composition.nodes`` (which mirrors
            insertion order for plain Compositions and class-defined
            order for special compositions like ``EMComposition``).
            Returns an empty list when the Composition has no nodes
            yet (rather than raising).
        """
        comp = handles.resolve_handle(composition)
        nodes_attr = getattr(comp, "nodes", None)
        if nodes_attr is None:
            raise ValueError(
                f"object of type {type(comp).__name__} has no .nodes "
                f"(is it really a Composition?)"
            )
        listing: list[dict[str, Any]] = []
        for n in nodes_attr:
            listing.append(
                {
                    "name": getattr(n, "name", None) or "?",
                    "type": type(n).__name__,
                    "repr": repr(n),
                }
            )
        return {"composition": composition, "nodes": listing}

    @captured_tool(mcp, layer="curated")
    def get_input_port(node: str, port: str) -> dict[str, Any]:
        """Return a handle to a specific InputPort of a Mechanism / node.

        WHEN TO CALL: when ``add_projection`` needs to target a
        non-primary InputPort of a Mechanism (the primary one is
        addressed implicitly when you pass a Mechanism handle as
        ``receiver=``). ``port`` is either the port's name (e.g.
        ``"FIELD_1_INPUT"``) or its 0-based integer index passed as a
        string (e.g. ``"1"``). The returned handle plugs straight into
        ``add_projection(receiver=<this handle>)``.

        For an inner node of a nested Composition, fetch the inner
        node first via ``get_composition_node`` and pass that handle
        as ``node`` here.

        Args:
            node: Handle of the owning Mechanism (top-level or
                fetched via ``get_composition_node``).
            port: Either the port name as a string, or the 0-based
                integer index — also as a string (e.g. ``"0"``,
                ``"1"``). Accepting strings only keeps the JSON-
                Schema simple; we parse the integer form internally.

        Returns:
            Handle payload for the InputPort. On miss, raises with
            the list of available port names so the next attempt
            can pick the right one.
        """
        owner = handles.resolve_handle(node)
        port_spec = _coerce_port_spec(port)
        port_obj = _resolve_port(owner, port_spec, side="input")
        payload = handles.register_handle(port_obj)
        handles.record_call(
            "get_input_port",
            {"node": node, "port": port},
            result_handle=payload.get("handle") if isinstance(payload, dict) else None,
            tool_layer="curated",
        )
        return payload

    @captured_tool(mcp, layer="curated")
    def get_output_port(node: str, port: str) -> dict[str, Any]:
        """Return a handle to a specific OutputPort of a Mechanism / node.

        WHEN TO CALL: when ``add_projection`` needs to source from a
        non-primary OutputPort. The primary OutputPort is addressed
        implicitly when you pass a Mechanism handle as ``sender=``;
        for any other port (e.g. an ``EMComposition`` inner node's
        ``RETRIEVED_FIELD_<n>`` output) fetch the port handle here
        and pass it as ``sender=``.

        See ``get_input_port`` for the args/return shape — symmetric.
        """
        owner = handles.resolve_handle(node)
        port_spec = _coerce_port_spec(port)
        port_obj = _resolve_port(owner, port_spec, side="output")
        payload = handles.register_handle(port_obj)
        handles.record_call(
            "get_output_port",
            {"node": node, "port": port},
            result_handle=payload.get("handle") if isinstance(payload, dict) else None,
            tool_layer="curated",
        )
        return payload


def _coerce_port_spec(port: str) -> str | int:
    """Parse the ``port`` arg as an int when it looks like one, else as a name.

    The MCP schema is string-only for simplicity; this lets the agent
    pass ``"1"`` for integer indexing without us needing a union type
    in the JSON Schema (which would push the agent toward thinking the
    schema is more complex than it is).
    """
    s = port.strip()
    if s.isdigit() or (s.startswith("-") and s[1:].isdigit()):
        return int(s)
    return s
