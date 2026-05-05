"""Curated persistence tools: ``export_python_script`` + ``load_python_script``.

The chat session lives entirely in this MCP subprocess's RAM (see
``handles.py``). These two tools turn that ephemeral state into (and back
from) a runnable, human-readable Python file — the canonical model
artifact for every front-end of the agent.

Mechanism:

* Every generated tool's ``_impl`` (rendered by ``generator.template``)
  and every composition-mutating curated tool (``composition.py``)
  appends a :class:`handles.JournalEntry` to the per-process session
  journal. The journal preserves handle strings verbatim so the renderer
  has the same call graph the agent intended.
* :func:`export_python_script` walks the journal in order and emits
  ``import psyneulink as pnl`` followed by one statement per entry,
  with handle strings rewritten to readable Python variable names
  derived from each object's PNL ``.name``. Run-composition entries
  go under ``if __name__ == "__main__":`` plus a ``print(comp.results)``.
  A trailing ``# psyneulink-mcp:journal`` block carries the entire
  journal as base64-encoded JSON, which makes :func:`load_python_script`
  symmetric and exec-free in the common case.
* :func:`load_python_script` prefers **replay mode**: read the journal
  block, replay each recorded call through the same MCP tool
  implementations, and rewrite handle strings as new handles get minted.
  Falls back to **exec mode** for hand-written ``.py`` files without a
  journal block — runs the script in an isolated module namespace, then
  introspects globals for PNL objects and registers them. Exec mode
  carries an explicit warning in its return payload because it executes
  arbitrary Python.

The MDF-format tools (``load_mdf_model`` / ``dump_mdf_model``) live in
``plans/mdf-loader.md``; they're deferred behind the heavy
``modeci-mdf`` dependency and not registered here.
"""

from __future__ import annotations

import base64
import importlib
import importlib.util
import json
import re
import sys
import textwrap
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from ... import handles
from ...feedback import captured_tool

# Markers for the trailing journal block. Both must be on their own line,
# starting with ``# `` (Python comment) so a script with a journal block is
# still a valid no-side-effect read.
_JOURNAL_MARKER_BEGIN = "# psyneulink-mcp:journal"
_JOURNAL_MARKER_END = "# psyneulink-mcp:end-journal"

# Curated tool names we know how to render as Composition method calls in
# the exported script. ``run_composition`` is handled separately because
# it goes under the ``if __name__ == "__main__":`` block.
_RENDERABLE_CURATED = {"add_node", "add_linear_pathway", "add_projection"}

_DEFAULT_EXPORT_DIR = Path("~/Documents/psyneulink-models").expanduser()

_SNAKE1 = re.compile(r"(.)([A-Z][a-z]+)")
_SNAKE2 = re.compile(r"([a-z0-9])([A-Z])")


# --------------------------------------------------------------------------- #
# helpers                                                                     #
# --------------------------------------------------------------------------- #


def _snake_case(name: str) -> str:
    """``LinearCombination`` → ``linear_combination``.

    Mirrors :func:`generator.template.snake_case` but vendored here so
    persistence has no cross-package dep on the generator (which exists
    only at build time).
    """
    s = _SNAKE1.sub(r"\1_\2", name)
    s = _SNAKE2.sub(r"\1_\2", s).lower()
    s = re.sub(r"[^0-9a-z_]+", "_", s).strip("_")
    return s or "obj"


def _utc_iso() -> str:
    return (
        datetime.now(timezone.utc)
        .isoformat(timespec="seconds")
        .replace("+00:00", "Z")
    )


def _utc_stamp() -> str:
    """File-name friendly UTC timestamp: ``YYYYMMDD-HHMMSS``."""
    return datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")


def _module_stem_for_tool(tool_name: str) -> str:
    """Map a generated tool's ``TOOL_NAME`` to its on-disk module stem."""
    if tool_name.startswith("create_"):
        return tool_name[len("create_") :]
    return tool_name


def _walk_handle_strings(value: Any, out: set[str]) -> None:
    """Collect every handle string that appears anywhere in ``value``."""
    if isinstance(value, str):
        if handles.is_handle_string(value):
            out.add(value)
    elif isinstance(value, dict):
        for k, v in value.items():
            _walk_handle_strings(k, out)
            _walk_handle_strings(v, out)
    elif isinstance(value, (list, tuple)):
        for item in value:
            _walk_handle_strings(item, out)


def _build_var_map(
    snapshot: list[handles.JournalEntry],
) -> dict[str, str]:
    """Build a stable ``handle → python_variable_name`` map.

    Resolves each producing handle to its live object, snake-cases its
    PNL ``.name``, and suffixes ``_2``, ``_3`` ... on collision so the
    rendered script is always syntactically valid even when two
    mechanisms share a name.
    """
    var_map: dict[str, str] = {}
    used: set[str] = set()
    for entry in snapshot:
        h = entry.result_handle
        if not h or h in var_map:
            continue
        try:
            obj = handles.resolve_handle(h)
            base = _snake_case(getattr(obj, "name", "") or type(obj).__name__)
        except KeyError:
            base = _snake_case(h)
        candidate = base
        suffix = 2
        while candidate in used or _is_python_keyword(candidate):
            candidate = f"{base}_{suffix}"
            suffix += 1
        var_map[h] = candidate
        used.add(candidate)
    return var_map


def _is_python_keyword(name: str) -> bool:
    import keyword

    return keyword.iskeyword(name)


def _render_value(value: Any, var_map: dict[str, str]) -> str:
    """Recursively render *value* as a Python source expression.

    Handle strings present in ``var_map`` are emitted as bare variable
    identifiers (no quotes). Dict keys that are handles get the same
    treatment so ``{h_in: [[1.0]]}`` becomes ``{in_node: [[1.0]]}``.
    Non-handle primitives go through ``repr``. Unknown object types
    fall through to ``repr`` too — the resulting script may not run,
    but it's still readable and the journal block lets reload work.
    """
    if isinstance(value, str):
        if value in var_map:
            return var_map[value]
        return repr(value)
    if isinstance(value, dict):
        items: list[str] = []
        for k, v in value.items():
            if isinstance(k, str) and k in var_map:
                key_src = var_map[k]
            else:
                key_src = repr(k)
            items.append(f"{key_src}: {_render_value(v, var_map)}")
        return "{" + ", ".join(items) + "}"
    if isinstance(value, tuple):
        items = [_render_value(v, var_map) for v in value]
        if len(items) == 1:
            return f"({items[0]},)"
        return "(" + ", ".join(items) + ")"
    if isinstance(value, list):
        items = [_render_value(v, var_map) for v in value]
        return "[" + ", ".join(items) + "]"
    return repr(value)


def _render_kwargs(args: dict[str, Any], var_map: dict[str, str]) -> str:
    """Render an args dict as the inside of a function call: ``a=1, b=x``."""
    return ", ".join(
        f"{name}={_render_value(val, var_map)}" for name, val in args.items()
    )


def _entry_handles(entry: handles.JournalEntry) -> set[str]:
    """Every handle string this entry mentions (in args or result)."""
    found: set[str] = set()
    _walk_handle_strings(entry.args, found)
    if entry.result_handle:
        found.add(entry.result_handle)
    return found


def _filter_for_composition(
    snapshot: list[handles.JournalEntry], composition: str | None
) -> list[handles.JournalEntry]:
    """Return entries that touch *composition* directly or transitively.

    Conservative: walk the dependency closure to a fixed point. An entry
    is included iff it shares any handle with the closure. Starts the
    closure from ``{composition}``; entries that reference the
    composition pull in their args' handles, which then pull in earlier
    creator entries, etc. When ``composition`` is ``None``, returns
    everything.
    """
    if composition is None:
        return snapshot
    needed: set[str] = {composition}
    while True:
        size_before = len(needed)
        for entry in snapshot:
            mentions = _entry_handles(entry)
            if mentions & needed:
                needed |= mentions
        if len(needed) == size_before:
            break
    return [
        entry for entry in snapshot if _entry_handles(entry) & needed
    ]


# --------------------------------------------------------------------------- #
# rendering                                                                   #
# --------------------------------------------------------------------------- #


def _class_name_for(entry: handles.JournalEntry) -> str:
    """Class name to emit for a generated create_* entry.

    Resolves the result handle live and reads ``type(obj).__name__`` so
    the rendered script uses the actual PNL class — robust to symbol
    aliasing in the public ``psyneulink`` namespace.
    """
    if entry.result_handle:
        try:
            obj = handles.resolve_handle(entry.result_handle)
            return type(obj).__name__
        except KeyError:
            pass
    name = entry.tool_name
    if name.startswith("create_"):
        name = name[len("create_") :]
    parts = [p.capitalize() for p in name.split("_")]
    return "".join(parts) or "Unknown"


def _render_generated_create(
    entry: handles.JournalEntry, var_map: dict[str, str]
) -> str | None:
    """Render one ``create_*`` call as ``var = pnl.<Class>(**args)``."""
    if not entry.result_handle or entry.result_handle not in var_map:
        return None
    var = var_map[entry.result_handle]
    cls = _class_name_for(entry)
    kwargs_src = _render_kwargs(entry.args, var_map)
    return f"{var} = pnl.{cls}({kwargs_src})"


def _render_curated_mutation(
    entry: handles.JournalEntry, var_map: dict[str, str]
) -> str | None:
    """Render an ``add_*`` curated entry as a ``Composition`` method call.

    Returns ``None`` for entries we can't render (missing composition
    handle in the var map, unknown tool, etc.). ``add_projection``
    expands to two lines: a ``MappingProjection(...)`` construction and
    the ``comp.add_projection(proj)`` call.
    """
    args = entry.args
    comp_handle = args.get("composition")
    if not isinstance(comp_handle, str) or comp_handle not in var_map:
        return None
    comp_var = var_map[comp_handle]
    name = entry.tool_name

    if name == "add_node":
        node_h = args.get("node")
        node_src = _render_value(node_h, var_map)
        return f"{comp_var}.add_node({node_src})"

    if name == "add_linear_pathway":
        nodes = args.get("nodes") or []
        nodes_src = _render_value(list(nodes), var_map)
        return f"{comp_var}.add_linear_processing_pathway({nodes_src})"

    if name == "add_projection":
        sender_src = _render_value(args.get("sender"), var_map)
        receiver_src = _render_value(args.get("receiver"), var_map)
        matrix = args.get("matrix")
        proj_kwargs = [f"sender={sender_src}", f"receiver={receiver_src}"]
        if matrix is not None:
            proj_kwargs.append(f"matrix={_render_value(matrix, var_map)}")
        proj_var = f"_proj_{comp_var}_{len(var_map)}_{abs(hash(comp_handle)) % 10_000}"
        return (
            f"{proj_var} = pnl.MappingProjection({', '.join(proj_kwargs)})\n"
            f"{comp_var}.add_projection({proj_var})"
        )

    return None


def _render_run(
    entry: handles.JournalEntry, var_map: dict[str, str]
) -> tuple[str, str] | None:
    """Render a ``run_composition`` entry as ``(call_line, comp_var)``.

    The call goes under ``if __name__ == "__main__":`` and is followed
    by a ``print("results:", comp.results)`` so the script demonstrates
    its output when executed standalone.
    """
    args = entry.args
    comp_handle = args.get("composition")
    if not isinstance(comp_handle, str) or comp_handle not in var_map:
        return None
    comp_var = var_map[comp_handle]
    run_kwargs: dict[str, Any] = {}
    if args.get("inputs") is not None:
        run_kwargs["inputs"] = args["inputs"]
    if args.get("num_trials") is not None:
        run_kwargs["num_trials"] = args["num_trials"]
    kwargs_src = _render_kwargs(run_kwargs, var_map)
    call_line = f"{comp_var}.run({kwargs_src})"
    return call_line, comp_var


# --------------------------------------------------------------------------- #
# journal block (base64-encoded JSON, comment-wrapped)                        #
# --------------------------------------------------------------------------- #


def _serialise_journal(snapshot: list[handles.JournalEntry]) -> list[dict[str, Any]]:
    """Convert journal entries to plain dicts, preserving order."""
    return [
        {
            "tool_name": e.tool_name,
            "args": e.args,
            "result_handle": e.result_handle,
            "tool_layer": e.tool_layer,
        }
        for e in snapshot
    ]


def _encode_journal_block(snapshot: list[handles.JournalEntry]) -> str:
    """Encode the journal as a comment-wrapped base64 block.

    The block is bracketed by ``_JOURNAL_MARKER_BEGIN`` / ``_END``
    markers so :func:`_decode_journal_block` can find it without parsing
    the rest of the file.
    """
    payload = json.dumps(_serialise_journal(snapshot), default=repr)
    encoded = base64.b64encode(payload.encode("utf-8")).decode("ascii")
    body_lines = textwrap.wrap(encoded, width=76) or [""]
    commented = "\n".join(f"# {line}" for line in body_lines)
    return f"{_JOURNAL_MARKER_BEGIN}\n{commented}\n{_JOURNAL_MARKER_END}"


def _decode_journal_block(text: str) -> list[dict[str, Any]] | None:
    """Find and decode the journal block in *text*, or return ``None``."""
    begin = text.find(_JOURNAL_MARKER_BEGIN)
    end = text.find(_JOURNAL_MARKER_END)
    if begin == -1 or end == -1 or end <= begin:
        return None
    body = text[begin + len(_JOURNAL_MARKER_BEGIN) : end]
    encoded = "".join(
        line.lstrip("#").strip()
        for line in body.splitlines()
        if line.strip()
    )
    if not encoded:
        return []
    try:
        decoded = base64.b64decode(encoded.encode("ascii")).decode("utf-8")
        return json.loads(decoded)
    except (ValueError, json.JSONDecodeError):
        return None


# --------------------------------------------------------------------------- #
# script renderer                                                             #
# --------------------------------------------------------------------------- #


def _render_script(
    snapshot: list[handles.JournalEntry],
    composition: str | None,
) -> tuple[str, int, int]:
    """Build the full ``.py`` source. Returns ``(text, n_objects, n_ops)``."""
    var_map = _build_var_map(snapshot)
    composition_name = ""
    if composition and composition in var_map:
        composition_name = var_map[composition]

    object_lines: list[str] = []
    mutation_lines: list[str] = []
    run_lines: list[str] = []
    n_objects = 0
    n_operations = 0

    for entry in snapshot:
        if entry.tool_layer == "generated":
            line = _render_generated_create(entry, var_map)
            if line is not None:
                object_lines.append(line)
                n_objects += 1
            continue
        if entry.tool_layer == "curated":
            if entry.tool_name in _RENDERABLE_CURATED:
                line = _render_curated_mutation(entry, var_map)
                if line is not None:
                    mutation_lines.append(line)
                    n_operations += 1
                continue
            if entry.tool_name == "run_composition":
                rendered = _render_run(entry, var_map)
                if rendered is not None:
                    call_line, comp_var = rendered
                    run_lines.append(call_line)
                    run_lines.append(f'print("results:", {comp_var}.results)')
                    n_operations += 1

    handle_summary = ", ".join(sorted(var_map))
    header = textwrap.dedent(
        f'''\
        """Auto-generated by psyneulink-mcp on {_utc_iso()}.

        Reproduces the model built in chat session with handles {{{handle_summary}}}.
        Filtered to composition: {composition_name or "(all)"}
        Run with: python this-file.py
        """
        import psyneulink as pnl
        '''
    )

    parts: list[str] = [header.rstrip(), ""]

    if object_lines:
        parts.append("# --- Object construction ---")
        parts.extend(object_lines)
        parts.append("")

    if mutation_lines:
        parts.append("# --- Composition wiring ---")
        parts.extend(mutation_lines)
        parts.append("")

    parts.append('if __name__ == "__main__":')
    if run_lines:
        for line in run_lines:
            parts.append("    " + line)
    else:
        parts.append("    pass")
    parts.append("")

    parts.append(_encode_journal_block(snapshot))
    parts.append("")

    return "\n".join(parts), n_objects, n_operations


# --------------------------------------------------------------------------- #
# replay / exec helpers                                                       #
# --------------------------------------------------------------------------- #


def _rewrite_handles(value: Any, mapping: dict[str, str]) -> Any:
    """Return a copy of *value* with handle strings remapped."""
    if isinstance(value, str):
        return mapping.get(value, value) if handles.is_handle_string(value) else value
    if isinstance(value, dict):
        out: dict[Any, Any] = {}
        for k, v in value.items():
            new_k = (
                mapping.get(k, k)
                if isinstance(k, str) and handles.is_handle_string(k)
                else k
            )
            out[new_k] = _rewrite_handles(v, mapping)
        return out
    if isinstance(value, list):
        return [_rewrite_handles(item, mapping) for item in value]
    if isinstance(value, tuple):
        return tuple(_rewrite_handles(item, mapping) for item in value)
    return value


def _replay_journal(
    entries: list[dict[str, Any]],
) -> tuple[dict[str, dict[str, Any]], list[str]]:
    """Replay a decoded journal through the live tool implementations.

    Returns ``(handles_by_var, skipped_summaries)``. Each entry's args
    are first rewritten to swap original-session handles for
    just-minted ones; any new handle returned by the tool is folded
    into the rewrite map for subsequent entries. ``run_composition``
    is intentionally skipped — loading should not have side effects.
    """
    from . import composition as curated_composition

    class _CaptureMCP:
        """Minimal MCP-compatible decorator container.

        Used here so we can call the registered curated functions
        through the same ``captured_tool`` wrapper the server uses,
        without needing a real FastMCP instance.
        """

        def __init__(self) -> None:
            self.tools: dict[str, Any] = {}

        def tool(self, **_kwargs: Any):
            def decorator(fn):
                self.tools[fn.__name__] = fn
                return fn

            return decorator

    capture = _CaptureMCP()
    curated_composition.register(capture)

    rewrite: dict[str, str] = {}
    handles_by_var: dict[str, dict[str, Any]] = {}
    skipped: list[str] = []
    var_counter: dict[str, int] = {}

    def _bind(orig_handle: str, payload: dict[str, Any]) -> str:
        """Pick a stable variable name for the new handle and stash it."""
        new_handle = payload["handle"]
        rewrite[orig_handle] = new_handle
        base = _snake_case(payload.get("name") or payload.get("type") or "obj")
        var_counter[base] = var_counter.get(base, 0) + 1
        n = var_counter[base]
        var_name = base if n == 1 else f"{base}_{n}"
        handles_by_var[var_name] = payload
        return var_name

    for entry in entries:
        tool_name = entry.get("tool_name")
        args = entry.get("args") or {}
        layer = entry.get("tool_layer", "generated")
        original_result = entry.get("result_handle")

        if not isinstance(tool_name, str):
            skipped.append(f"missing tool_name in entry: {entry!r}")
            continue

        if tool_name == "run_composition":
            skipped.append(
                "skipped run_composition (loading shouldn't side-effect)"
            )
            continue

        rewritten = _rewrite_handles(args, rewrite)

        try:
            if layer == "generated":
                stem = _module_stem_for_tool(tool_name)
                module = importlib.import_module(
                    f"psyneulink_mcp.tools.generated.{stem}"
                )
                result = module._impl(rewritten)
                if (
                    isinstance(result, dict)
                    and isinstance(result.get("handle"), str)
                    and isinstance(original_result, str)
                ):
                    _bind(original_result, result)
            elif layer == "curated":
                fn = capture.tools.get(tool_name)
                if fn is None:
                    skipped.append(f"unknown curated tool: {tool_name!r}")
                    continue
                fn(**rewritten)
            else:
                skipped.append(f"unknown tool layer: {layer!r}")
        except Exception as exc:  # noqa: BLE001 — report and continue
            skipped.append(f"{tool_name} replay failed: {exc!r}")

    return handles_by_var, skipped


def _exec_module_from_path(path: Path) -> Any:
    """Load *path* as an isolated Python module and return it.

    Uses ``importlib.util`` instead of bare ``exec`` so the script's
    ``__name__`` is the temp module name (not ``"__main__"``); the
    typical ``if __name__ == "__main__":`` guard therefore stays
    inactive during loading. The module name is unique per call so
    repeated loads of the same file don't collide in ``sys.modules``.
    """
    module_name = f"_psyneulink_mcp_loaded_{abs(hash(str(path)))}"
    spec = importlib.util.spec_from_file_location(module_name, str(path))
    if spec is None or spec.loader is None:
        raise ImportError(f"could not load script as module: {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    try:
        spec.loader.exec_module(module)
    except Exception:
        sys.modules.pop(module_name, None)
        raise
    return module


def _register_pnl_objects(module: Any) -> dict[str, dict[str, Any]]:
    """Walk *module*'s globals; register every PNL object as a handle.

    Recognises Mechanisms, Compositions, Functions, and Projections
    (the four base classes the agent will actually pass around).
    Names that start with an underscore are skipped on the assumption
    they're internal helpers in the script.
    """
    import psyneulink as pnl

    pnl_types: tuple[type, ...] = (
        pnl.Mechanism_Base,
        pnl.Composition,
        pnl.Function_Base,
        pnl.Projection_Base,
    )
    out: dict[str, dict[str, Any]] = {}
    for name, value in vars(module).items():
        if name.startswith("_"):
            continue
        if isinstance(value, pnl_types):
            out[name] = handles.register_handle(value)
    return out


# --------------------------------------------------------------------------- #
# registration                                                                #
# --------------------------------------------------------------------------- #


def register(mcp: Any) -> None:
    @captured_tool(mcp, layer="curated")
    def export_python_script(
        composition: str | None = None,
        path: str | None = None,
        dry_run: bool = False,
    ) -> dict[str, Any]:
        """Render the current session as a runnable ``.py`` file.

        WHEN TO CALL: when the user wants to keep, share, edit, or
        version-control the model the agent has built so far. The
        emitted file imports ``psyneulink as pnl``, recreates each
        object the journal recorded, replays composition mutations,
        and runs the recorded ``run_composition`` calls inside an
        ``if __name__ == "__main__":`` block (printing ``results:
        ...``). It also embeds a base64-encoded journal block so
        :func:`load_python_script` can reload it without ``exec``.

        Args:
            composition: Optional handle for a Composition. When set,
                the rendered script is filtered to operations that
                touch that composition (transitively — its constituent
                node creations, projection wiring, etc. are pulled in).
                Omit to dump the entire session.
            path: Optional output path. Must end in ``.py``. Defaults
                to ``~/Documents/psyneulink-models/<name>-<UTC>.py``.
                Parent directories are created as needed. Ignored when
                ``dry_run=True``.
            dry_run: When ``True``, render the script and return its
                ``text`` *without writing anything to disk*. ``path``
                in the result will be ``None``. This is the path
                front-ends use for live preview panes (e.g. the web
                UI's code pane that polls every revision tick) where
                the goal is "show me what export would produce" rather
                than "persist a model artifact". Defaults to ``False``
                so the historical write-to-disk behaviour is preserved.

        Returns:
            ``{"path": <abs str | None>, "text": <full source>,
            "n_objects": <int>, "n_operations": <int>}``.
            ``text`` is included so the agent can preview the script
            without a second tool call. ``path`` is ``None`` in dry-run
            mode.
        """
        snapshot = handles.journal_snapshot()
        filtered = _filter_for_composition(snapshot, composition)

        text, n_objects, n_operations = _render_script(filtered, composition)

        if dry_run:
            return {
                "path": None,
                "text": text,
                "n_objects": n_objects,
                "n_operations": n_operations,
            }

        if path is None:
            comp_label = "session"
            if composition:
                try:
                    obj = handles.resolve_handle(composition)
                    comp_label = _snake_case(getattr(obj, "name", "")) or "session"
                except KeyError:
                    pass
            target = _DEFAULT_EXPORT_DIR / f"{comp_label}-{_utc_stamp()}.py"
        else:
            target = Path(path).expanduser().resolve()

        if target.suffix != ".py":
            raise ValueError(
                f"export_python_script: path must end in .py, got {target!r}"
            )

        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(text, encoding="utf-8")

        return {
            "path": str(target),
            "text": text,
            "n_objects": n_objects,
            "n_operations": n_operations,
        }

    @captured_tool(mcp, layer="curated")
    def load_python_script(path: str) -> dict[str, Any]:
        """Materialise a previously-exported ``.py`` model into this session.

        WHEN TO CALL: when the user points the agent at a ``.py`` file
        produced by :func:`export_python_script` (or hand-written using
        the same shape) and wants the resulting PNL objects available
        as handles for further inspection / mutation / runs.

        Two strategies, tried in order:

        1. **Replay mode** (preferred, no ``exec``): if the file
           contains the trailing ``# psyneulink-mcp:journal`` block,
           decode it and replay each recorded call through the same
           MCP tool implementations. Original-session handle strings
           are rewritten to the freshly-minted ones as objects come
           back. ``run_composition`` entries are skipped (loading
           shouldn't run the model).
        2. **Exec mode** (fallback): for hand-written files without a
           journal block, load the file as an isolated Python module
           via :mod:`importlib.util` (so ``if __name__ == "__main__":``
           stays inert), then walk its globals and register every
           Mechanism / Composition / Function / Projection as a handle.
           **WARNING**: exec mode runs the script as Python — only
           load files you trust.

        Args:
            path: Path to the ``.py`` file. Must exist and end in
                ``.py``.

        Returns:
            ``{"mode": "replay" | "exec",
            "handles": {<var_name>: <handle_payload>, ...},
            "summary": <human str>,
            "skipped": [...]}`` (replay mode) or
            ``{... "warning": "..."}`` (exec mode). The handle payloads
            match :func:`handles.list_handles` entries, so the agent
            can immediately pass them to ``add_*`` / ``run_composition``.
        """
        target = Path(path).expanduser().resolve()
        if not target.exists():
            raise FileNotFoundError(f"load_python_script: no such file: {target}")
        if target.suffix != ".py":
            raise ValueError(
                f"load_python_script: path must end in .py, got {target!r}"
            )

        text = target.read_text(encoding="utf-8")
        decoded = _decode_journal_block(text)

        if decoded is not None and decoded:
            handles_by_var, skipped = _replay_journal(decoded)
            return {
                "mode": "replay",
                "handles": handles_by_var,
                "summary": (
                    f"replayed {len(decoded)} operations from journal in {target}"
                ),
                "skipped": skipped,
            }

        module = _exec_module_from_path(target)
        registered = _register_pnl_objects(module)
        return {
            "mode": "exec",
            "handles": registered,
            "summary": f"loaded {len(registered)} PNL objects from {target} via exec",
            "warning": (
                "exec mode runs the script as Python; only load files you trust"
            ),
        }
