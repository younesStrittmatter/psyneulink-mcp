"""Render a generated tool module from a :class:`SymbolMeta` + :class:`ToolSpec`.

The generated Python is committed to ``src/psyneulink_mcp/tools/generated/``
and reviewed before merge. The template is the single source of truth
for: import set, ``__source_sha256__`` / ``__pnl_qualname__`` /
``__generated_by__`` markers, MCP registration shape, and the
class-vs-function impl branch.

The first regen wires every generated tool to ``**kwargs: Any`` because
FastMCP derives its input schema from the function signature and
attaching an explicit JSON Schema requires deeper plumbing. The LLM's
schema is captured in ``TOOL_PARAMETERS`` (module metadata) AND embedded
in the ``TOOL_DESCRIPTION`` text, so an LLM consumer reading the tool
description still sees the full schema.
"""

from __future__ import annotations

import json
import keyword
import pprint
import re
from typing import Any

from .adapters.base import ToolSpec
from .introspection import SymbolMeta

_SNAKE1 = re.compile(r"(.)([A-Z][a-z]+)")
_SNAKE2 = re.compile(r"([a-z0-9])([A-Z])")


def snake_case(name: str) -> str:
    """``LinearCombination`` -> ``linear_combination``;
    ``LCAMechanism`` -> ``lca_mechanism`` (treats all-caps runs as one word).
    """
    s = _SNAKE1.sub(r"\1_\2", name)
    s = _SNAKE2.sub(r"\1_\2", s).lower()
    s = re.sub(r"[^0-9a-z_]+", "_", s).strip("_")
    return s or "tool"


def tool_name_for(symbol: SymbolMeta) -> str:
    """Tool name an MCP client sees.

    Classes get a ``create_`` prefix because the underlying call is
    ``cls(**kwargs)`` — naming it ``create_transfer_mechanism`` reads
    better to an LLM consumer than just ``transfer_mechanism``.
    Functions and methods keep their snake-cased name. (Methods use the
    bare PNL method name on purpose — agents already know
    ``add_node`` / ``add_projection`` and the LLM-consumer descriptions
    spell out which class the call binds to.)
    """
    base = snake_case(symbol.short_name)
    if keyword.iskeyword(base):
        base = f"{base}_"
    if symbol.kind == "class":
        return f"create_{base}"
    return base


def module_filename_for(symbol: SymbolMeta) -> str:
    """Filename inside ``tools/generated/`` for this symbol.

    Methods are namespaced by their owning class so two same-named
    methods on different classes don't collide on the filesystem
    (e.g. ``Composition.add_node`` and a hypothetical
    ``Pathway.add_node`` both become valid module stems).
    """
    return f"{module_stem_for(symbol)}.py"


def module_stem_for(symbol: SymbolMeta) -> str:
    """Importable stem of the generated module (filename without ``.py``)."""
    if symbol.kind == "method" and symbol.class_short_name:
        return f"{snake_case(symbol.class_short_name)}_{snake_case(symbol.short_name)}"
    return snake_case(symbol.short_name)


def render_module(
    symbol: SymbolMeta,
    spec: ToolSpec,
    *,
    generated_by: str,
) -> str:
    """Return the full Python source for the generated tool module."""
    tool_name = tool_name_for(symbol)
    description_raw = (spec.get("description") or "").strip()
    parameters = spec.get("parameters") or {}
    notes = (spec.get("notes") or "").strip()

    # Embed the JSON-Schema parameters into the human-visible description so
    # an LLM consumer sees the schema even though FastMCP uses **kwargs.
    description_with_schema = _description_with_schema(
        description_raw, parameters, notes
    )

    parameters_literal = pprint.pformat(parameters, sort_dicts=True, width=88, indent=2)

    docstring_first_line = _first_sentence(description_raw) or tool_name

    if symbol.kind == "method":
        impl_lines = _render_method_impl(symbol)
    else:
        impl_lines = _render_constructor_impl(symbol)

    lines = [
        '"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""',
        "",
        "from __future__ import annotations",
        "",
        "import json",
        "from typing import Any",
        "",
        "import psyneulink as pnl",
        "",
        "from psyneulink_mcp import handles",
        "from psyneulink_mcp.feedback import captured_tool",
    ]
    if symbol.kind == "method":
        lines.append("from psyneulink_mcp import method_helpers")
    lines += [
        "",
        f"__source_sha256__ = {symbol.source_sha256!r}",
        f"__pnl_qualname__ = {symbol.qualname!r}",
        f"__pnl_kind__ = {symbol.kind!r}",
        f"__generated_by__ = {generated_by!r}",
        "",
        f"TOOL_NAME = {tool_name!r}",
        f"TOOL_DESCRIPTION = {description_with_schema!r}",
        f"TOOL_PARAMETERS = {parameters_literal}",
        f"TOOL_NOTES = {notes!r}",
        "",
        "",
        *impl_lines,
        "",
        "",
        "def register(mcp: Any) -> None:",
        '    @captured_tool(mcp, layer="generated", name=TOOL_NAME, description=TOOL_DESCRIPTION)',
        # FastMCP derives an MCP `inputSchema` from the function signature.
        # `**kwargs` would surface as a single required `kwargs` arg
        # rather than passing through the LLM's chosen parameters, so
        # we declare an explicit `args: dict` parameter that the impl
        # then unpacks. The real per-symbol schema lives in
        # TOOL_PARAMETERS / TOOL_DESCRIPTION for the LLM consumer.
        f"    def {tool_name}(args: dict[str, Any] | None = None) -> Any:",
        f"        {docstring_first_line!r}",
        "        return _impl(args or {})",
        "",
    ]
    return "\n".join(lines)


def _render_constructor_impl(symbol: SymbolMeta) -> list[str]:
    """``_impl`` body for class / function symbols.

    Single shape for both classes and module-level callables: build the
    result, then either return it as-is (JSON-friendly) or stash it in
    the handles registry and return a handle payload. Classes never
    produce JSON-serialisable results in practice, but the unified branch
    keeps the template smaller and also handles factory functions whose
    return type isn't known statically.

    The pre-resolution ``kwargs`` dict (handle strings still verbatim) is
    what the session journal wants — ``resolve_in`` mutates the dict's
    values in place, so we record_call with the original kwargs and rely
    on ``handles.record_call`` to deep-copy before stashing.
    """
    return [
        "def _impl(kwargs: dict[str, Any]) -> Any:",
        f"    target = pnl.{symbol.short_name}",
        "    resolved = handles.resolve_in(kwargs)",
        "    result = target(**resolved)",
        "    try:",
        "        json.dumps(result)",
        "    except (TypeError, ValueError):",
        "        payload = handles.register_handle(result)",
        "        handles.record_call(",
        "            TOOL_NAME,",
        "            kwargs,",
        "            result_handle=payload.get('handle') if isinstance(payload, dict) else None,",
        '            tool_layer="generated",',
        "        )",
        "        return payload",
        '    handles.record_call(TOOL_NAME, kwargs, result_handle=None, tool_layer="generated")',
        "    return result",
    ]


def _render_method_impl(symbol: SymbolMeta) -> list[str]:
    """``_impl`` body for method symbols.

    Methods bind to a live PNL object — the agent passes the bound
    instance as a kwarg (``composition`` for ``Composition.add_*``,
    matching the ``_scan_for_composition_handle`` convention the UI
    relies on). The shared helper at :mod:`psyneulink_mcp.method_helpers`
    pops the instance handle, resolves remaining kwargs, dispatches the
    call, bumps the composition revision counter, and journals the call
    with ``tool_layer="generated"``.

    Per-method special cases (``add_projection``'s defensive
    sender/receiver pre-add and DuplicateProjectionError swallow) live
    in the helper too — keeping them out of the template means a regen
    can't accidentally drop them.
    """
    cls_name = symbol.class_short_name or ""
    method_name = symbol.short_name
    return [
        "def _impl(kwargs: dict[str, Any]) -> Any:",
        f"    cls = pnl.{cls_name}",
        "    return method_helpers.call_method_tool(",
        "        owner_cls=cls,",
        f"        method_name={method_name!r},",
        "        kwargs=kwargs,",
        "        tool_name=TOOL_NAME,",
        "    )",
    ]


def render_init(stems: list[str]) -> str:
    """Render the ``tools/generated/__init__.py`` index module."""
    sorted_stems = sorted(set(stems))
    lines = [
        '"""Auto-generated index. Do not edit by hand.',
        "",
        "Rewritten by scripts/generate_tools.py on every successful run.",
        "On a fresh clone (no regen yet) the modules tuple is empty and",
        "register_all is a safe no-op.",
        '"""',
        "",
        "from __future__ import annotations",
        "",
        "from typing import Any",
        "",
    ]
    if sorted_stems:
        lines.append(f"from . import {', '.join(sorted_stems)}")
        lines.append("")
        lines.append(f"ALL = ({', '.join(sorted_stems)},)")
    else:
        lines.append("ALL: tuple[Any, ...] = ()")
    lines += [
        "",
        "",
        "def register_all(mcp: Any) -> None:",
        '    """Register every generated tool module with ``mcp``."""',
        "    for module in ALL:",
        "        module.register(mcp)",
        "",
    ]
    return "\n".join(lines)


# --------------------------------------------------------------------------- #
# helpers                                                                     #
# --------------------------------------------------------------------------- #


def _description_with_schema(
    description: str, parameters: dict[str, Any], notes: str
) -> str:
    """Compose the user-visible description used for MCP registration.

    Includes the JSON Schema and notes inline so an LLM agent sees them
    in the tool listing even though FastMCP can't validate against them
    yet (see module docstring).
    """
    parts: list[str] = []
    if description:
        parts.append(description.strip())
    if parameters:
        parts.append("")
        parts.append("Parameters (JSON Schema):")
        parts.append(json.dumps(parameters, indent=2, sort_keys=True))
    if notes:
        parts.append("")
        parts.append("Notes:")
        parts.append(notes.strip())
    return "\n".join(parts)


_SENTENCE_END = re.compile(r"[.!?](?:\s|$)")


def _first_sentence(text: str) -> str:
    """First sentence of a description, for use as the function docstring."""
    if not text:
        return ""
    match = _SENTENCE_END.search(text)
    if match is None:
        return text.strip().splitlines()[0]
    return text[: match.end()].strip()
