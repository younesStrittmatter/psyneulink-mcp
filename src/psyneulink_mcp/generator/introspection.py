"""Resolve PNL symbols from a seed file (or default to the bundled models).

Three directives are supported in ``generator/seeds.txt``:

* ``import-walk: <module>`` — walk every ``.py`` file in the module's
  package directory; for each ``Import`` / ``ImportFrom`` node, resolve
  imported names against the live ``psyneulink`` module. This is the
  default — it captures "what the canonical examples actually use."
* ``symbol: <qualname>`` — include the named symbol regardless.
* ``package: <module>`` — include every public class/function in the
  named package. Wide; use sparingly.

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
    """

    qualname: str
    kind: Literal["class", "function"]
    source: str
    docstring: str | None
    module: str
    source_sha256: str

    @property
    def short_name(self) -> str:
        return self.qualname.rsplit(".", 1)[-1]


@dataclass(frozen=True)
class SeedDirective:
    """One non-comment line from ``seeds.txt``."""

    kind: Literal["import-walk", "symbol", "package"]
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
        if kind not in {"import-walk", "symbol", "package"}:
            raise ValueError(
                f"{path}:{lineno}: unknown seed directive kind {kind!r}; "
                "expected one of import-walk, symbol, package"
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
    for d in directives:
        if d.kind == "import-walk":
            qualnames.update(_qualnames_from_import_walk(d.target))
        elif d.kind == "symbol":
            qualnames.add(d.target)
        elif d.kind == "package":
            qualnames.update(_qualnames_from_package(d.target))

    symbols: list[SymbolMeta] = []
    for qualname in sorted(qualnames):
        meta = _resolve_qualname(qualname)
        if meta is not None:
            symbols.append(meta)
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
    """Every public class/function on the live module object."""
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
        if inspect.isclass(obj) or inspect.isfunction(obj):
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
        kind: Literal["class", "function"] = "class"
    elif inspect.isfunction(obj) or inspect.isbuiltin(obj):
        kind = "function"
    else:
        return None

    try:
        source = inspect.getsource(obj)
    except (OSError, TypeError):
        return None

    return SymbolMeta(
        qualname=qualname,
        kind=kind,
        source=source,
        docstring=inspect.getdoc(obj),
        module=getattr(obj, "__module__", package_qualname),
        source_sha256=hashlib.sha256(source.encode("utf-8")).hexdigest(),
    )
