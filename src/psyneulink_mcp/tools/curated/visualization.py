"""Curated graph-rendering tools for the UI's graph pane.

Two tools:

* ``render_composition_graph(composition, fmt='png'|'svg'|'dot')`` — renders
  a Composition's graph and returns it as a base64 ``data:`` URL the UI can
  drop straight into an ``<img>`` tag (PNG / SVG) or a code block (raw dot
  source). PNG is the default; SVG keeps the graph crisp at any zoom; the
  ``dot`` format is the underlying graphviz source, useful for debugging
  layout.
* ``get_composition_revision(composition)`` — cheap counter the UI polls
  to decide "do I re-render?". Bumped by every composition-mutating curated
  tool (``add_node``, ``add_linear_pathway``, ``add_projection``); not
  bumped by ``run_composition`` because executing a graph doesn't change
  its topology.

Both tools resolve the ``composition`` arg through the handles registry and
reject handles that don't point at a ``psyneulink.Composition``. The PNG
and SVG paths shell out to graphviz's ``dot`` binary; if that binary isn't
installed we re-raise as a ``RuntimeError`` with the install hint instead
of letting the bare ``graphviz.ExecutableNotFound`` bubble up.
"""

from __future__ import annotations

import base64
from typing import Any

from ... import handles
from ...feedback import captured_tool

_FMT_TO_MIME = {
    "png": "image/png",
    "svg": "image/svg+xml",
    "dot": "text/vnd.graphviz",
}

_INSTALL_HINT = (
    "graphviz `dot` binary not found on PATH. "
    "Install it: `brew install graphviz` (macOS), "
    "`apt install graphviz` (Debian/Ubuntu), "
    "or see https://graphviz.org/download/."
)


def _require_composition(composition: str) -> Any:
    """Resolve ``composition`` and assert it points to a PNL ``Composition``.

    Lazy-imports psyneulink so the server still boots when PNL isn't
    available — and so the import cost only lands on tools that need it.
    """
    import psyneulink as pnl

    obj = handles.resolve_handle(composition)
    if not isinstance(obj, pnl.Composition):
        raise ValueError(
            f"{composition!r} is not a Composition handle "
            f"(resolved to {type(obj).__name__})"
        )
    return obj


def _composition_graphviz(comp: Any) -> Any:
    """Return the ``graphviz.Digraph`` PNL builds for ``comp``.

    ``Composition.show_graph(output_fmt='gv')`` returns a ``Digraph`` in
    every PNL version we support; older versions exposed a ``Source`` via
    ``output_fmt='source'`` which we fall back to defensively.
    """
    try:
        return comp.show_graph(output_fmt="gv")
    except (TypeError, ValueError):
        return comp.show_graph(output_fmt="source")


def register(mcp: Any) -> None:
    """Register graph-visualisation tools on the MCP server."""

    @captured_tool(mcp, layer="curated")
    def render_composition_graph(
        composition: str, fmt: str = "png"
    ) -> dict[str, Any]:
        """Render a Composition's graph and return it as a ``data:`` URL.

        WHEN TO CALL: the UI's graph pane needs a fresh render (the user
        just opened the model, or ``get_composition_revision`` reported a
        new revision), or the agent wants to show the user what the graph
        looks like inline. Cheap to call at any time, but every call shells
        out to graphviz, so the UI should gate this on a revision change.

        Args:
            composition: Handle returned by ``create_composition``.
            fmt: One of ``"png"``, ``"svg"``, ``"dot"``. ``"png"`` is the
                most ``<img>``-friendly default; ``"svg"`` stays crisp at
                any zoom level; ``"dot"`` returns the raw graphviz source
                (useful for debugging layout).

        Returns:
            ``{"composition": <handle>, "revision": <int>, "format": <fmt>,
            "mime": <mime>, "data_url": "data:<mime>;base64,<...>",
            "n_nodes": <int>, "n_projections": <int>}``. The journal entry
            recorded for this call deliberately omits ``data_url`` — base64
            images would balloon exported scripts.

        Errors:
            ``KeyError`` if the handle isn't registered;
            ``ValueError`` if it doesn't resolve to a Composition or ``fmt``
            is unknown; ``RuntimeError`` if graphviz's ``dot`` binary isn't
            installed (PNG / SVG only — ``"dot"`` format never invokes it).
        """
        if fmt not in _FMT_TO_MIME:
            raise ValueError(
                f"render_composition_graph: unknown fmt {fmt!r}; "
                f"expected one of {sorted(_FMT_TO_MIME)}"
            )

        comp = _require_composition(composition)
        gv = _composition_graphviz(comp)

        if fmt == "dot":
            payload_bytes = gv.source.encode("utf-8")
        else:
            try:
                payload_bytes = gv.pipe(format=fmt)
            except Exception as exc:
                import graphviz as _gv

                if isinstance(exc, _gv.ExecutableNotFound):
                    raise RuntimeError(_INSTALL_HINT) from exc
                raise

        mime = _FMT_TO_MIME[fmt]
        b64 = base64.b64encode(payload_bytes).decode("ascii")
        data_url = f"data:{mime};base64,{b64}"

        revision = handles.get_revision(composition)

        # Record a small breadcrumb in the journal — args + revision, but
        # NOT the data_url. The journal feeds export_python_script and an
        # inline base64 image would bloat the exported .py with kilobytes
        # of noise per render.
        handles.record_call(
            "render_composition_graph",
            {"composition": composition, "fmt": fmt},
            result_handle=None,
            tool_layer="curated",
        )

        return {
            "composition": composition,
            "revision": revision,
            "format": fmt,
            "mime": mime,
            "data_url": data_url,
            "n_nodes": len(comp.nodes),
            "n_projections": len(comp.projections),
        }

    @captured_tool(mcp, layer="curated")
    def get_composition_revision(composition: str) -> dict[str, Any]:
        """Return the current revision counter for a Composition handle.

        WHEN TO CALL: a UI's graph pane wants to ask "should I re-render
        the graph yet?" without paying for a full render. The counter
        starts at ``0`` and increments by 1 every time a composition-
        mutating curated tool (``add_node``, ``add_linear_pathway``,
        ``add_projection``) runs to completion. ``run_composition`` does
        NOT bump the counter — running a model isn't a topology change.

        Args:
            composition: Handle returned by ``create_composition``.

        Returns:
            ``{"composition": <handle>, "revision": <int>}``.

        Errors:
            ``KeyError`` if the handle isn't registered;
            ``ValueError`` if it doesn't resolve to a Composition.
        """
        _require_composition(composition)
        handles.record_call(
            "get_composition_revision",
            {"composition": composition},
            result_handle=None,
            tool_layer="curated",
        )
        return {
            "composition": composition,
            "revision": handles.get_revision(composition),
        }
