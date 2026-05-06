"""Resolve PNL symbols from a seed file (or default to the bundled models).

Four directives are supported in ``generator/seeds.txt``:

* ``import-walk: <module>`` — walk every ``.py`` file in the module's
  package directory; for each ``Import`` / ``ImportFrom`` node, resolve
  imported names against the live ``psyneulink`` module. This is the
  default — it captures "what the canonical examples actually use."
* ``symbol: <qualname>`` — include the named symbol regardless.
* ``package: <module>`` — include every public class/function in the
  named package. Wide; use sparingly.
* ``method: <class_qualname>.<method_name>`` — include a single method
  defined on a class. The generator emits a tool whose ``_impl`` pops a
  ``composition`` (or other instance) handle from kwargs, resolves it,
  and dispatches to ``instance.<method_name>(**rest)``. Use for PNL
  surfaces that aren't constructors (``Composition.add_node`` etc.).

All results are deduped by qualname and sorted, so generator runs are
diff-friendly.
"""

from __future__ import annotations

import ast
import hashlib
import importlib
import inspect
from collections.abc import Iterable
from dataclasses import dataclass
from pathlib import Path
from typing import Literal

PNL_MODULE = "psyneulink"
DEFAULT_SEED_DIRECTIVE_TARGET = "psyneulink.library.models"


@dataclass(frozen=True)
class SymbolMeta:
    """One PNL symbol slated for tool generation.

    ``source_sha256`` lets the orchestrator skip regenerating a tool
    when the upstream source hasn't changed.

    For ``kind == "method"``, ``qualname`` includes the owning class:
    e.g. ``psyneulink.Composition.add_projection``. The class qualname
    is exposed via :attr:`class_qualname`; ``short_name`` is just the
    method name (the last segment).

    Parent metadata
    ---------------

    For ``kind == "class"``, :attr:`parent_short_names` carries PNL's
    actual class MRO (excluding ``object`` and non-PNL bases) in the
    order ``inspect.getmro`` returns. :attr:`parent_docstrings` maps
    each parent short name to the first paragraph of its docstring,
    truncated to keep regen prompts compact. :attr:`parent_source_sha256s`
    is the per-parent source-SHA used for cascade invalidation in
    :func:`orchestrator._should_skip` — when a parent's source changes
    its child's compressed description should be regenerated even if
    the child's own source hasn't moved. Empty for non-class symbols.
    """

    qualname: str
    kind: Literal["class", "function", "method"]
    source: str
    docstring: str | None
    module: str
    source_sha256: str
    parent_short_names: tuple[str, ...] = ()
    parent_docstrings: tuple[tuple[str, str], ...] = ()
    parent_source_sha256s: tuple[tuple[str, str], ...] = ()

    @property
    def short_name(self) -> str:
        return self.qualname.rsplit(".", 1)[-1]

    @property
    def class_qualname(self) -> str | None:
        """Qualname of the class that owns this method (method kind only)."""
        if self.kind != "method":
            return None
        parent, _, _ = self.qualname.rpartition(".")
        return parent or None

    @property
    def class_short_name(self) -> str | None:
        """Short name of the owning class (method kind only)."""
        parent = self.class_qualname
        if parent is None:
            return None
        return parent.rsplit(".", 1)[-1]

    @property
    def parent_docstrings_dict(self) -> dict[str, str]:
        """Convenience: parent short name → first-paragraph docstring."""
        return dict(self.parent_docstrings)

    @property
    def parent_source_sha256s_dict(self) -> dict[str, str]:
        """Convenience: parent short name → source SHA for cascade checks."""
        return dict(self.parent_source_sha256s)


@dataclass(frozen=True)
class SeedDirective:
    """One non-comment line from ``seeds.txt``."""

    kind: Literal["import-walk", "symbol", "package", "method"]
    target: str


# --------------------------------------------------------------------------- #
# seeds.txt parser                                                            #
# --------------------------------------------------------------------------- #


def parse_seeds_file(path: Path) -> list[SeedDirective]:
    """Read ``seeds.txt``. Blank lines and ``#`` comments are skipped.

    Each non-comment line must match ``<kind>: <target>`` where kind is
    one of ``import-walk``, ``symbol``, ``package``. Anything else
    raises :class:`ValueError` with the offending line number.
    """
    if not path.exists():
        return []
    directives: list[SeedDirective] = []
    for lineno, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        if ":" not in line:
            raise ValueError(
                f"{path}:{lineno}: missing ':' in seed directive {line!r}"
            )
        kind_raw, _, target_raw = line.partition(":")
        kind = kind_raw.strip()
        target = target_raw.strip()
        if kind not in {"import-walk", "symbol", "package", "method"}:
            raise ValueError(
                f"{path}:{lineno}: unknown seed directive kind {kind!r}; "
                "expected one of import-walk, symbol, package, method"
            )
        if not target:
            raise ValueError(f"{path}:{lineno}: empty target in seed directive")
        directives.append(SeedDirective(kind=kind, target=target))  # type: ignore[arg-type]
    return directives


def default_seed_directives() -> list[SeedDirective]:
    """Fallback when no ``seeds.txt`` exists: walk the bundled models."""
    return [SeedDirective(kind="import-walk", target=DEFAULT_SEED_DIRECTIVE_TARGET)]


# --------------------------------------------------------------------------- #
# directive dispatch                                                          #
# --------------------------------------------------------------------------- #


def discover_from_directives(
    directives: Iterable[SeedDirective],
) -> list[SymbolMeta]:
    """Run every directive and return a deduped, sorted symbol list."""
    qualnames: set[str] = set()
    method_qualnames: set[str] = set()
    for d in directives:
        if d.kind == "import-walk":
            qualnames.update(_qualnames_from_import_walk(d.target))
        elif d.kind == "symbol":
            qualnames.add(d.target)
        elif d.kind == "package":
            qualnames.update(_qualnames_from_package(d.target))
        elif d.kind == "method":
            method_qualnames.add(d.target)

    symbols: list[SymbolMeta] = []
    # ``method`` qualnames need a different resolver because the parent
    # of the last segment is a class, not a module — ``importlib`` will
    # refuse to import ``psyneulink.Composition`` as a module.
    for qualname in sorted(method_qualnames):
        meta = _resolve_method_qualname(qualname)
        if meta is not None:
            symbols.append(meta)
    for qualname in sorted(qualnames):
        meta = _resolve_qualname(qualname)
        if meta is not None:
            symbols.append(meta)
    # Re-sort across both kinds for diff-friendly output (matches the
    # pre-method-support behaviour for class+function seeds).
    symbols.sort(key=lambda s: (s.qualname, s.kind))
    return symbols


def discover_seed_symbols(seeds_file: Path | None = None) -> list[SymbolMeta]:
    """Top-level entry: load ``seeds_file`` or fall back to the default."""
    directives = (
        parse_seeds_file(seeds_file) if seeds_file and seeds_file.exists() else []
    )
    if not directives:
        directives = default_seed_directives()
    return discover_from_directives(directives)


# --------------------------------------------------------------------------- #
# import-walk                                                                 #
# --------------------------------------------------------------------------- #


def iter_seed_module_files(seed_module_qualname: str) -> list[Path]:
    """Sorted list of ``.py`` files in the package, dunders excluded."""
    pkg = importlib.import_module(seed_module_qualname)
    pkg_file = getattr(pkg, "__file__", None)
    if pkg_file is None:
        return []
    pkg_dir = Path(pkg_file).parent
    if not pkg_dir.is_dir():
        return []
    return sorted(
        p
        for p in pkg_dir.iterdir()
        if p.suffix == ".py" and not p.name.startswith("__")
    )


def _qualnames_from_import_walk(seed_module_qualname: str) -> set[str]:
    """PsyNeuLink symbols used by any .py file in the package.

    Catches three idioms:

    * ``from psyneulink import X, Y`` — directly listed names.
    * ``from psyneulink.<sub> import X`` — directly listed names.
    * ``import psyneulink [as alias]`` followed by ``alias.X`` attribute
      access. This is the dominant pattern in the bundled models, so
      missing it returns zero seed symbols on a real PNL install.
    """
    qualnames: set[str] = set()
    for py_file in iter_seed_module_files(seed_module_qualname):
        try:
            tree = ast.parse(py_file.read_text(encoding="utf-8"), filename=str(py_file))
        except (OSError, SyntaxError):
            continue

        pnl_bindings: set[str] = set()

        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom):
                if not node.module:
                    continue
                if node.module != PNL_MODULE and not node.module.startswith(
                    PNL_MODULE + "."
                ):
                    continue
                for alias in node.names:
                    if alias.name == "*" or alias.name.startswith("_"):
                        continue
                    qualnames.add(f"{PNL_MODULE}.{alias.name}")
            elif isinstance(node, ast.Import):
                for alias in node.names:
                    if alias.name != PNL_MODULE and not alias.name.startswith(
                        PNL_MODULE + "."
                    ):
                        continue
                    pnl_bindings.add(alias.asname or alias.name.split(".", 1)[0])

        if pnl_bindings:
            for node in ast.walk(tree):
                if not isinstance(node, ast.Attribute):
                    continue
                base = node.value
                if not isinstance(base, ast.Name):
                    continue
                if base.id not in pnl_bindings:
                    continue
                if node.attr.startswith("_"):
                    continue
                qualnames.add(f"{PNL_MODULE}.{node.attr}")
    return qualnames


# --------------------------------------------------------------------------- #
# package walk                                                                #
# --------------------------------------------------------------------------- #


def _qualnames_from_package(package_qualname: str) -> set[str]:
    """Every public class/function on the live module object.

    Filters silently:

    * Names starting with ``_`` (private-by-convention).
    * Exception / Warning subclasses — these are raised by the library,
      not constructed by an agent. Surfacing them as MCP tools wastes
      LLM regen budget and produces nonsensical "create FooError"
      descriptions.
    """
    try:
        module = importlib.import_module(package_qualname)
    except ImportError:
        return set()
    qualnames: set[str] = set()
    for name in dir(module):
        if name.startswith("_"):
            continue
        try:
            obj = getattr(module, name)
        except AttributeError:
            continue
        if inspect.isclass(obj):
            if issubclass(obj, BaseException):
                continue
            qualnames.add(f"{package_qualname}.{name}")
        elif inspect.isfunction(obj):
            qualnames.add(f"{package_qualname}.{name}")
    return qualnames


# --------------------------------------------------------------------------- #
# resolution                                                                  #
# --------------------------------------------------------------------------- #


def _resolve_qualname(qualname: str) -> SymbolMeta | None:
    """Resolve ``pkg.attr`` to a :class:`SymbolMeta`; return None on failure.

    "Failure" includes: import error on the package, missing attribute,
    non-class / non-function object, or :func:`inspect.getsource` raising
    (which it does for C-implemented callables).
    """
    if "." not in qualname:
        return None
    package_qualname, _, attr = qualname.rpartition(".")
    try:
        package = importlib.import_module(package_qualname)
    except ImportError:
        return None
    try:
        obj = getattr(package, attr)
    except AttributeError:
        return None

    if inspect.isclass(obj):
        # Exceptions / Warnings are raised, not constructed by the agent.
        # Silently skip so wide directives like ``package: psyneulink``
        # don't burn LLM regen budget on `*Error` classes.
        if issubclass(obj, BaseException):
            return None
        kind: Literal["class", "function"] = "class"
    elif inspect.isfunction(obj) or inspect.isbuiltin(obj):
        kind = "function"
    else:
        return None

    try:
        source = inspect.getsource(obj)
    except (OSError, TypeError):
        return None

    parent_short_names: tuple[str, ...] = ()
    parent_docstrings: tuple[tuple[str, str], ...] = ()
    parent_source_sha256s: tuple[tuple[str, str], ...] = ()
    if kind == "class" and inspect.isclass(obj):
        parent_short_names, parent_docstrings, parent_source_sha256s = (
            _collect_parent_metadata(obj)
        )

    return SymbolMeta(
        qualname=qualname,
        kind=kind,
        source=source,
        docstring=inspect.getdoc(obj),
        module=getattr(obj, "__module__", package_qualname),
        source_sha256=hashlib.sha256(source.encode("utf-8")).hexdigest(),
        parent_short_names=parent_short_names,
        parent_docstrings=parent_docstrings,
        parent_source_sha256s=parent_source_sha256s,
    )


# Maximum chars to keep from a parent class's docstring when including it
# in a regen prompt — first paragraph is usually enough to ground the LLM,
# and a paragraph cap keeps prompts predictable. Bumped up from "first
# sentence" because some PNL base classes have multi-sentence first
# paragraphs that reference important parameters.
_PARENT_DOCSTRING_CHAR_CAP = 800


def _first_paragraph(text: str | None, *, cap: int = _PARENT_DOCSTRING_CHAR_CAP) -> str:
    """Return the first non-empty paragraph of ``text`` (capped to ``cap`` chars).

    "Paragraph" = lines up to the first blank line. Falls back to the
    full text when there's no blank line. Empty input → empty string.
    """
    if not text:
        return ""
    lines: list[str] = []
    for raw in text.splitlines():
        if not raw.strip():
            if lines:
                break
            continue
        lines.append(raw)
    paragraph = "\n".join(lines).strip()
    if len(paragraph) > cap:
        return paragraph[: cap - 1].rstrip() + "…"
    return paragraph


def _collect_parent_metadata(
    cls: type,
) -> tuple[tuple[str, ...], tuple[tuple[str, str], ...], tuple[tuple[str, str], ...]]:
    """Walk PNL's MRO for ``cls`` and collect parent docstrings + SHAs.

    Returns ``(parent_short_names, parent_docstrings, parent_sha_pairs)``.
    Each tuple is in MRO order (immediate parent first), filtered to PNL
    classes only — non-PNL framework bases don't help the regen LLM.

    The SHA pairs let :func:`orchestrator._should_skip` cascade-invalidate
    a child when a parent's source changes. Parents whose source can't be
    read (C-implemented descriptors, dynamically-built classes) are kept
    in ``parent_short_names`` (so the prompt still mentions them) but
    omitted from ``parent_sha_pairs`` (we have nothing to compare).
    """
    short_names: list[str] = []
    docstrings: list[tuple[str, str]] = []
    sha_pairs: list[tuple[str, str]] = []
    for parent in cls.__mro__[1:]:
        if parent is object:
            continue
        parent_module = getattr(parent, "__module__", "") or ""
        if not parent_module.startswith("psyneulink"):
            continue
        parent_short = parent.__name__
        short_names.append(parent_short)
        doc = _first_paragraph(inspect.getdoc(parent))
        if doc:
            docstrings.append((parent_short, doc))
        try:
            parent_source = inspect.getsource(parent)
        except (OSError, TypeError):
            continue
        sha_pairs.append(
            (parent_short, hashlib.sha256(parent_source.encode("utf-8")).hexdigest())
        )
    return tuple(short_names), tuple(docstrings), tuple(sha_pairs)


def _resolve_method_qualname(qualname: str) -> SymbolMeta | None:
    """Resolve ``pkg.ClassName.method_name`` to a method-kind :class:`SymbolMeta`.

    Returns ``None`` when:
    * the parent qualname doesn't resolve to a class,
    * the named attribute is missing or isn't a function/descriptor,
    * the source can't be read (C-implemented descriptors etc.).
    """
    class_qualname, _, method_name = qualname.rpartition(".")
    if not class_qualname or not method_name:
        return None
    class_meta = _resolve_qualname(class_qualname)
    if class_meta is None or class_meta.kind != "class":
        return None
    try:
        package = importlib.import_module(
            class_qualname.rpartition(".")[0]
        )
        cls = getattr(package, class_meta.short_name)
    except (ImportError, AttributeError):
        return None
    method = inspect.getattr_static(cls, method_name, None)
    if method is None:
        return None
    # Unwrap descriptors that wrap the underlying function (classmethod,
    # staticmethod). For an ordinary instance method, the static lookup
    # already returns the function object.
    if isinstance(method, (classmethod, staticmethod)):
        method = method.__func__
    if not (inspect.isfunction(method) or inspect.ismethod(method)):
        return None
    try:
        source = inspect.getsource(method)
    except (OSError, TypeError):
        return None
    return SymbolMeta(
        qualname=qualname,
        kind="method",
        source=source,
        docstring=inspect.getdoc(method),
        module=getattr(method, "__module__", class_meta.module),
        source_sha256=hashlib.sha256(source.encode("utf-8")).hexdigest(),
    )
