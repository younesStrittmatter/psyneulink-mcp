"""Re-template every already-generated tool module without calling the LLM.

Used when only ``template.render_module`` has changed (impl shape, import
list, registration boilerplate) and the LLM-produced metadata
(``TOOL_DESCRIPTION``, ``TOOL_PARAMETERS``, ``TOOL_NOTES``) on disk is
still correct. Avoids the cost and nondeterminism of a full regen.

Strategy: read each module on disk, AST-extract the metadata constants
literally, reconstruct a stub :class:`SymbolMeta` plus the original
:class:`ToolSpec`, then call :func:`render_module`.

Limitation: ``SymbolMeta.kind`` is inferred from the existing
``TOOL_NAME`` (``create_*`` ⇒ class, otherwise function). That keeps
the regenerated tool name byte-identical, which is the only place
``kind`` is consulted by the template.
"""

from __future__ import annotations

import ast
from pathlib import Path
from typing import Any

from .adapters.base import ToolSpec
from .introspection import SymbolMeta
from .template import render_module

_REQUIRED_CONSTANTS = (
    "__source_sha256__",
    "__pnl_qualname__",
    "__generated_by__",
    "TOOL_NAME",
    "TOOL_DESCRIPTION",
    "TOOL_PARAMETERS",
    "TOOL_NOTES",
)
# ``__pnl_kind__`` is optional for backward compatibility with modules
# generated before method support landed. When present it pins the kind
# verbatim; when absent, the legacy ``create_*``-vs-everything-else
# heuristic is used (those modules are class- or function-kind by
# definition — no method module ever existed without ``__pnl_kind__``).
_OPTIONAL_CONSTANTS = (
    "__pnl_kind__",
    # Phase 3: hierarchy metadata. Older modules don't have these; the
    # rerender path tolerates the absence and rewrites them as empty.
    "__pnl_parents__",
    "__pnl_parent_sha256s__",
)


class RerenderError(RuntimeError):
    """Raised when a module on disk doesn't have the expected metadata."""


def _extract_constants(source: str, path: Path) -> dict[str, Any]:
    tree = ast.parse(source, filename=str(path))
    out: dict[str, Any] = {}
    wanted = set(_REQUIRED_CONSTANTS) | set(_OPTIONAL_CONSTANTS)
    for node in tree.body:
        if not isinstance(node, ast.Assign) or len(node.targets) != 1:
            continue
        target = node.targets[0]
        if not isinstance(target, ast.Name):
            continue
        if target.id not in wanted:
            continue
        try:
            out[target.id] = ast.literal_eval(node.value)
        except ValueError as exc:
            raise RerenderError(
                f"{path}: could not literal-eval constant {target.id}: {exc}"
            ) from exc
    missing = sorted(set(_REQUIRED_CONSTANTS) - out.keys())
    if missing:
        raise RerenderError(
            f"{path}: missing required constants: {missing}"
        )
    return out


def _strip_schema_augmentation(description_with_schema: str) -> str:
    """Recover the raw description string from the augmented one.

    ``template._description_with_schema`` joins the raw description with
    the JSON Schema and notes via two markers. Splitting on the first
    one we encounter recovers the original.
    """
    text = description_with_schema
    for marker in ("\n\nParameters (JSON Schema):", "\n\nNotes:"):
        if marker in text:
            text = text.split(marker, 1)[0]
            break
    return text.strip()


def rerender_path(path: Path) -> Path:
    """Rewrite *path* using the current template; return the same path."""
    source = path.read_text(encoding="utf-8")
    constants = _extract_constants(source, path)

    qualname: str = constants["__pnl_qualname__"]
    tool_name: str = constants["TOOL_NAME"]

    explicit_kind = constants.get("__pnl_kind__")
    if explicit_kind in {"class", "function", "method"}:
        kind = explicit_kind
    else:
        kind = "class" if tool_name.startswith("create_") else "function"

    if kind == "method":
        # ``psyneulink.Composition.add_projection`` → module is
        # ``psyneulink``; the class qualname (``...Composition``) is
        # captured implicitly via SymbolMeta.class_qualname.
        module_qualname = qualname.split(".", 1)[0]
    else:
        module_qualname = (
            qualname.rsplit(".", 1)[0] if "." in qualname else qualname
        )

    parents_raw = constants.get("__pnl_parents__") or []
    parent_short_names: tuple[str, ...] = tuple(
        str(p) for p in parents_raw if isinstance(p, str)
    )
    parent_shas_raw = constants.get("__pnl_parent_sha256s__") or {}
    parent_source_sha256s: tuple[tuple[str, str], ...] = ()
    if isinstance(parent_shas_raw, dict):
        parent_source_sha256s = tuple(
            (str(k), str(v))
            for k, v in parent_shas_raw.items()
            if isinstance(k, str) and isinstance(v, str)
        )
    symbol = SymbolMeta(
        qualname=qualname,
        kind=kind,  # type: ignore[arg-type]
        source="",  # not consulted by render_module
        docstring=None,
        module=module_qualname,
        source_sha256=constants["__source_sha256__"],
        parent_short_names=parent_short_names,
        # parent_docstrings isn't recorded in the on-disk module (it
        # lives in the regen prompt only), so the rerender path leaves
        # it empty — that's fine, render_module doesn't read it.
        parent_docstrings=(),
        parent_source_sha256s=parent_source_sha256s,
    )

    parameters: dict[str, Any] = constants["TOOL_PARAMETERS"] or {}
    notes: str = constants["TOOL_NOTES"] or ""
    description_raw = _strip_schema_augmentation(constants["TOOL_DESCRIPTION"])

    spec: ToolSpec = {
        "description": description_raw,
        "parameters": parameters,
        "notes": notes,
    }

    rendered = render_module(
        symbol, spec, generated_by=constants["__generated_by__"]
    )
    text = rendered if rendered.endswith("\n") else rendered + "\n"
    path.write_text(text, encoding="utf-8")
    return path


def rerender_directory(generated_dir: Path) -> tuple[list[Path], list[tuple[Path, str]]]:
    """Rewrite every ``*.py`` in *generated_dir* (excluding ``__init__.py``).

    Returns ``(written, failures)`` where ``failures`` is a list of
    ``(path, error_message)`` pairs.
    """
    written: list[Path] = []
    failures: list[tuple[Path, str]] = []
    if not generated_dir.is_dir():
        return written, failures
    for path in sorted(generated_dir.iterdir()):
        if path.suffix != ".py" or path.name.startswith("__"):
            continue
        try:
            rerender_path(path)
        except (RerenderError, OSError, ValueError) as exc:
            failures.append((path, str(exc)))
            continue
        written.append(path)
    return written, failures


__all__ = ["rerender_path", "rerender_directory", "RerenderError"]
