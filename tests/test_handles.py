"""Unit tests for the handles registry."""

from __future__ import annotations

import pytest

from psyneulink_mcp import handles


@pytest.fixture(autouse=True)
def _reset_registry():
    handles.clear_handles()
    yield
    handles.clear_handles()


class _Dummy:
    def __init__(self, name: str = "dummy") -> None:
        self.name = name

    def __repr__(self) -> str:
        return f"<Dummy {self.name}>"


def test_register_returns_well_formed_payload():
    payload = handles.register_handle(_Dummy("a"))
    assert handles.is_handle_string(payload["handle"])
    assert payload["type"] == "_Dummy"
    assert payload["name"] == "a"
    assert payload["repr"] == "<Dummy a>"


def test_register_none_returns_none():
    assert handles.register_handle(None) is None


def test_resolve_roundtrip():
    obj = _Dummy("b")
    payload = handles.register_handle(obj)
    assert handles.resolve_handle(payload["handle"]) is obj


def test_resolve_unknown_raises():
    with pytest.raises(KeyError):
        handles.resolve_handle("h_deadbeefcafe")


def test_resolve_in_walks_nested_structures():
    obj_a = _Dummy("a")
    obj_b = _Dummy("b")
    h_a = handles.register_handle(obj_a)["handle"]
    h_b = handles.register_handle(obj_b)["handle"]

    nested = {
        "single": h_a,
        "in_list": [h_a, "literal", 7],
        "in_dict": {"x": h_b, "y": "untouched"},
        "deep": [{"k": [h_a]}],
    }
    out = handles.resolve_in(nested)

    assert out["single"] is obj_a
    assert out["in_list"][0] is obj_a
    assert out["in_list"][1] == "literal"
    assert out["in_list"][2] == 7
    assert out["in_dict"]["x"] is obj_b
    assert out["in_dict"]["y"] == "untouched"
    assert out["deep"][0]["k"][0] is obj_a


def test_resolve_in_passthrough_for_non_handle_strings():
    assert handles.resolve_in("h_not_hex_at_all") == "h_not_hex_at_all"
    assert handles.resolve_in("h_123") == "h_123"  # too short
    assert handles.resolve_in("hello") == "hello"


def test_list_and_describe():
    obj = _Dummy("c")
    h = handles.register_handle(obj)["handle"]
    rows = handles.list_handles()
    assert any(r["handle"] == h and r["name"] == "c" for r in rows)
    assert handles.describe_handle(h)["repr"] == "<Dummy c>"


def test_clear_handles_returns_count():
    handles.register_handle(_Dummy("x"))
    handles.register_handle(_Dummy("y"))
    assert handles.clear_handles() == 2
    assert handles.list_handles() == []
