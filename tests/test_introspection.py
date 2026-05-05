"""Unit tests for :mod:`psyneulink_mcp.generator.introspection`.

Most assertions exercise the parser + dispatch logic with synthetic
modules so the test suite stays fast. A small "live" test against
``psyneulink.library.models`` confirms the seven canonical model files
are still on disk and the import-walk yields a non-empty, well-typed
symbol set.
"""

from __future__ import annotations

import sys
import textwrap
import types
from pathlib import Path

import pytest

from psyneulink_mcp.generator import introspection
from psyneulink_mcp.generator.introspection import (
    DEFAULT_SEED_DIRECTIVE_TARGET,
    SeedDirective,
    SymbolMeta,
    default_seed_directives,
    discover_from_directives,
    discover_seed_symbols,
    iter_seed_module_files,
    parse_seeds_file,
)


# --------------------------------------------------------------------------- #
# parse_seeds_file                                                            #
# --------------------------------------------------------------------------- #


def test_parse_seeds_file_handles_three_directives(tmp_path: Path) -> None:
    seeds = tmp_path / "seeds.txt"
    seeds.write_text(
        textwrap.dedent(
            """
            # comment
            import-walk: psyneulink.library.models

            symbol: psyneulink.TransferMechanism
            package: psyneulink.core.components.functions
            """
        ).strip()
        + "\n"
    )
    directives = parse_seeds_file(seeds)
    assert directives == [
        SeedDirective("import-walk", "psyneulink.library.models"),
        SeedDirective("symbol", "psyneulink.TransferMechanism"),
        SeedDirective("package", "psyneulink.core.components.functions"),
    ]


def test_parse_seeds_file_returns_empty_when_missing(tmp_path: Path) -> None:
    assert parse_seeds_file(tmp_path / "nope.txt") == []


def test_parse_seeds_file_skips_blank_and_comment_lines(tmp_path: Path) -> None:
    seeds = tmp_path / "seeds.txt"
    seeds.write_text("\n\n# comment only file\n\n")
    assert parse_seeds_file(seeds) == []


def test_parse_seeds_file_rejects_bad_kind(tmp_path: Path) -> None:
    seeds = tmp_path / "seeds.txt"
    seeds.write_text("garbage: psyneulink.X\n")
    with pytest.raises(ValueError, match="unknown seed directive kind"):
        parse_seeds_file(seeds)


def test_parse_seeds_file_rejects_missing_colon(tmp_path: Path) -> None:
    seeds = tmp_path / "seeds.txt"
    seeds.write_text("import-walk psyneulink.library.models\n")
    with pytest.raises(ValueError, match="missing ':'"):
        parse_seeds_file(seeds)


def test_parse_seeds_file_rejects_empty_target(tmp_path: Path) -> None:
    seeds = tmp_path / "seeds.txt"
    seeds.write_text("symbol:\n")
    with pytest.raises(ValueError, match="empty target"):
        parse_seeds_file(seeds)


# --------------------------------------------------------------------------- #
# default_seed_directives + repo-tracked seeds.txt                            #
# --------------------------------------------------------------------------- #


def test_default_seed_directives_targets_bundled_models() -> None:
    assert default_seed_directives() == [
        SeedDirective("import-walk", DEFAULT_SEED_DIRECTIVE_TARGET)
    ]


def test_repo_seeds_file_parses() -> None:
    """The repo-tracked seeds.txt must always be valid."""
    seeds = Path(__file__).resolve().parents[1] / "generator" / "seeds.txt"
    assert seeds.exists(), "generator/seeds.txt missing from the repo"
    directives = parse_seeds_file(seeds)
    assert any(
        d.kind == "import-walk" and d.target == DEFAULT_SEED_DIRECTIVE_TARGET
        for d in directives
    )


# --------------------------------------------------------------------------- #
# iter_seed_module_files (the spy hook)                                       #
# --------------------------------------------------------------------------- #


def test_iter_seed_module_files_lists_all_seven_pnl_models() -> None:
    """The canonical seven library.models files must always be present.

    PNL's `devel` branch grows new bundled models over time (e.g.
    Giallanza2024 landed after this test was first written), so we
    assert a SUPERSET rather than equality — new additions don't
    break the assertion, but a regression that drops one of the
    canonical seven still does.
    """
    files = iter_seed_module_files(DEFAULT_SEED_DIRECTIVE_TARGET)
    names = {p.name for p in files}
    canonical = {
        "Botvinick_conflict_monitoring_model.py",
        "Cohen_Huston1994.py",
        "Cohen_Huston1994_horse_race.py",
        "GilzenratModel.py",
        "Kalanthroff_PCTC_2018.py",
        "MontagueDayanSejnowski96.py",
        "Nieuwenhuis2005Model.py",
    }
    missing = canonical - names
    assert not missing, (
        f"library.models is missing canonical model file(s) "
        f"from PNL devel: {sorted(missing)}"
    )


# --------------------------------------------------------------------------- #
# discover_from_directives — synthetic modules                                #
# --------------------------------------------------------------------------- #


# Module-level fixture classes/functions — declared here so
# `inspect.getsource` can resolve them (the tests reassign ``__module__``
# to a synthetic name, but the source lookup still uses ``__file__``,
# which has to be a real file on disk).


class FxPublic:
    """Public class doc."""

    def __init__(self) -> None: ...


class FxAlpha:
    """alpha."""


class FxBeta:
    """beta."""


def fx_func() -> None:
    """fx func doc."""


def _make_fake_package(monkeypatch: pytest.MonkeyPatch, name: str) -> types.ModuleType:
    """Register a synthetic package under ``name``.

    Sets ``__file__`` to *this* test module so ``inspect.getsource`` can
    resolve attached classes whose ``__module__`` we reassign.
    """
    module = types.ModuleType(name)
    module.__file__ = __file__
    monkeypatch.setitem(sys.modules, name, module)
    return module


def _retag(obj: object, module_name: str) -> object:
    try:
        obj.__module__ = module_name  # type: ignore[attr-defined]
    except (AttributeError, TypeError):
        pass
    return obj


def test_discover_from_directives_symbol_directive(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    pkg = _make_fake_package(monkeypatch, "fake_pnl_a")
    pkg.Public = _retag(FxPublic, "fake_pnl_a")

    symbols = discover_from_directives([SeedDirective("symbol", "fake_pnl_a.Public")])
    assert [s.qualname for s in symbols] == ["fake_pnl_a.Public"]
    assert symbols[0].kind == "class"
    assert "Public class doc." in (symbols[0].docstring or "")
    assert symbols[0].source_sha256
    assert symbols[0].short_name == "Public"


def test_discover_from_directives_package_directive(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    pkg = _make_fake_package(monkeypatch, "fake_pnl_b")

    pkg.Beta = _retag(FxBeta, "fake_pnl_b")
    pkg.Alpha = _retag(FxAlpha, "fake_pnl_b")
    pkg.func = _retag(fx_func, "fake_pnl_b")
    pkg._private = FxBeta

    qualnames = [
        s.qualname
        for s in discover_from_directives([SeedDirective("package", "fake_pnl_b")])
    ]
    assert qualnames == sorted(qualnames)
    assert "fake_pnl_b.Alpha" in qualnames
    assert "fake_pnl_b.Beta" in qualnames
    assert "fake_pnl_b.func" in qualnames
    assert not any("private" in q for q in qualnames)


def test_discover_from_directives_dedupes_across_directives(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    pkg = _make_fake_package(monkeypatch, "fake_pnl_c")
    pkg.Public = _retag(FxPublic, "fake_pnl_c")

    symbols = discover_from_directives(
        [
            SeedDirective("symbol", "fake_pnl_c.Public"),
            SeedDirective("symbol", "fake_pnl_c.Public"),
            SeedDirective("package", "fake_pnl_c"),
        ]
    )
    assert [s.qualname for s in symbols] == ["fake_pnl_c.Public"]


def test_discover_from_directives_skips_unresolvable_symbol(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    _make_fake_package(monkeypatch, "fake_pnl_d")
    symbols = discover_from_directives(
        [SeedDirective("symbol", "fake_pnl_d.DoesNotExist")]
    )
    assert symbols == []


# Module-level Exception fixture — declared at top level so
# `inspect.getsource` can resolve it (mirroring the existing `Fx*`
# fixtures above; see `_retag` for why __module__ is rebound).
class FxBoomError(Exception):
    """Synthetic Exception subclass used to assert it gets filtered out."""


def test_discover_from_directives_skips_exception_subclasses_via_package(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """Wide ``package:`` directives must NOT pull in BaseException subclasses.

    Exception classes are raised by the wrapped library, not constructed
    by an agent. Surfacing them as MCP tools wastes regen budget and
    produces "create FooError" descriptions that confuse LLM consumers.
    The filter sits in introspection so all callers benefit.
    """
    pkg = _make_fake_package(monkeypatch, "fake_pnl_e")
    pkg.Real = _retag(FxAlpha, "fake_pnl_e")
    pkg.Boom = _retag(FxBoomError, "fake_pnl_e")

    qualnames = [
        s.qualname
        for s in discover_from_directives([SeedDirective("package", "fake_pnl_e")])
    ]
    assert "fake_pnl_e.Real" in qualnames
    assert "fake_pnl_e.Boom" not in qualnames


def test_discover_from_directives_skips_exception_subclasses_via_symbol(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """Same filter applies to direct ``symbol:`` directives.

    A user who writes ``symbol: fake.SomeError`` in seeds.txt almost
    certainly didn't mean to: the resolver silently drops it so the
    seed list stays diff-friendly without a noisy warning every regen.
    """
    pkg = _make_fake_package(monkeypatch, "fake_pnl_f")
    pkg.Boom = _retag(FxBoomError, "fake_pnl_f")

    symbols = discover_from_directives([SeedDirective("symbol", "fake_pnl_f.Boom")])
    assert symbols == []


# --------------------------------------------------------------------------- #
# Live PNL pass                                                               #
# --------------------------------------------------------------------------- #


def test_discover_seed_symbols_live_psyneulink_returns_well_typed_list() -> None:
    """The default seed (import-walk on `psyneulink.library.models`) should
    return a non-empty, deduped, sorted list whose qualnames all resolve."""
    import psyneulink

    symbols = discover_seed_symbols()
    assert symbols, "import-walk yielded zero symbols"

    qualnames = [s.qualname for s in symbols]
    assert qualnames == sorted(qualnames)
    assert len(qualnames) == len(set(qualnames))

    for s in symbols:
        assert s.qualname.startswith("psyneulink.")
        assert s.kind in {"class", "function", "method"}
        assert s.source
        assert len(s.source_sha256) == 64
        # ``method`` symbols expose the method via the owning class, not
        # via the ``psyneulink`` top-level — so we only check
        # top-level attribute presence for class/function kinds.
        if s.kind in {"class", "function"}:
            assert getattr(psyneulink, s.short_name, None) is not None
        else:
            owner = getattr(psyneulink, s.class_short_name or "", None)
            assert owner is not None
            assert getattr(owner, s.short_name, None) is not None


def test_discover_seed_symbols_uses_repo_seeds_file_when_provided(
    tmp_path: Path,
) -> None:
    """Pointing at an empty seeds.txt should fall back to the default."""
    seeds = tmp_path / "seeds.txt"
    seeds.write_text("# only comments\n")
    symbols_default = discover_seed_symbols(seeds_file=None)
    symbols_empty_file = discover_seed_symbols(seeds_file=seeds)
    assert {s.qualname for s in symbols_default} == {
        s.qualname for s in symbols_empty_file
    }
