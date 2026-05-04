"""Unit tests for the LLM-adapter layer.

The real adapters are exercised by integration tests
(``tests/test_adapters_integration.py``); these tests stay offline.
"""

from __future__ import annotations

import json
import subprocess
import sys
from typing import Any

import pytest

from psyneulink_mcp.generator import adapters
from psyneulink_mcp.generator.adapters import (
    ADAPTERS,
    AdapterError,
    get_adapter,
)
from psyneulink_mcp.generator.adapters.anthropic_api import AnthropicAPIAdapter
from psyneulink_mcp.generator.adapters.base import validate_tool_spec
from psyneulink_mcp.generator.adapters.claude_cli import (
    DEFAULT_MODEL,
    ClaudeCLIAdapter,
    _parse_cli_output,
)

# --------------------------------------------------------------------------- #
# Fixtures                                                                    #
# --------------------------------------------------------------------------- #


SCHEMA: dict[str, Any] = {
    "type": "object",
    "properties": {
        "description": {"type": "string"},
        "parameters": {"type": "object"},
        "notes": {"type": "string"},
    },
    "required": ["description", "parameters", "notes"],
    "additionalProperties": False,
}

VALID_SPEC = {
    "description": "Create a TransferMechanism.",
    "parameters": {"type": "object", "properties": {}, "required": []},
    "notes": "",
}


# --------------------------------------------------------------------------- #
# Registry                                                                    #
# --------------------------------------------------------------------------- #


def test_registry_lists_both_adapters() -> None:
    assert set(ADAPTERS) == {"claude_cli", "anthropic_api"}


def test_get_adapter_default_is_claude_cli(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv(adapters.ENV_LLM_ADAPTER, raising=False)
    assert isinstance(get_adapter(), ClaudeCLIAdapter)


def test_get_adapter_explicit_claude_cli(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv(adapters.ENV_LLM_ADAPTER, "claude_cli")
    assert isinstance(get_adapter(), ClaudeCLIAdapter)


def test_get_adapter_unknown_name_raises(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv(adapters.ENV_LLM_ADAPTER, "totally_made_up")
    with pytest.raises(AdapterError, match="unknown adapter"):
        get_adapter()


# --------------------------------------------------------------------------- #
# ClaudeCLIAdapter                                                            #
# --------------------------------------------------------------------------- #


def test_claude_cli_argv_includes_required_flags() -> None:
    adapter = ClaudeCLIAdapter(cmd="claude", model="sonnet")
    argv = adapter.build_argv(SCHEMA)

    assert argv[0] == "claude"
    assert "--print" in argv
    assert "--no-session-persistence" in argv

    schema_index = argv.index("--json-schema") + 1
    assert json.loads(argv[schema_index]) == SCHEMA

    fmt_index = argv.index("--output-format") + 1
    assert argv[fmt_index] == "json"

    model_index = argv.index("--model") + 1
    assert argv[model_index] == "sonnet"

    assert "--bare" not in argv, "--bare bypasses Claude Max OAuth; do not pass it"


def test_claude_cli_argv_includes_max_budget_when_set() -> None:
    adapter = ClaudeCLIAdapter(cmd="claude", max_budget_usd=2.5)
    argv = adapter.build_argv(SCHEMA)
    assert "--max-budget-usd" in argv
    assert argv[argv.index("--max-budget-usd") + 1] == "2.5"


def test_claude_cli_argv_omits_max_budget_when_unset() -> None:
    adapter = ClaudeCLIAdapter(cmd="claude")
    assert "--max-budget-usd" not in adapter.build_argv(SCHEMA)


def test_claude_cli_default_model_from_env(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("PSYNEULINK_MCP_CLAUDE_MODEL", raising=False)
    adapter = ClaudeCLIAdapter()
    assert adapter.model == DEFAULT_MODEL


def test_claude_cli_env_overrides(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("PSYNEULINK_MCP_CLAUDE_CMD", "/opt/bin/claude")
    monkeypatch.setenv("PSYNEULINK_MCP_CLAUDE_MODEL", "opus")
    monkeypatch.setenv("PSYNEULINK_MCP_CLAUDE_MAX_BUDGET_USD", "5")
    monkeypatch.setenv("PSYNEULINK_MCP_CLAUDE_TIMEOUT_S", "30")

    adapter = ClaudeCLIAdapter()
    assert adapter.cmd == "/opt/bin/claude"
    assert adapter.model == "opus"
    assert adapter.max_budget_usd == 5.0
    assert adapter.timeout_s == 30


def test_claude_cli_generate_pipes_prompt_and_returns_spec(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """End-to-end shape using the wrapper format the live CLI emits when
    --json-schema is set: structured_output holds the parsed object and
    `result` is empty."""
    captured: dict[str, Any] = {}

    def fake_run(argv, *, input, capture_output, text, timeout, check):  # type: ignore[no-untyped-def]
        captured["argv"] = argv
        captured["input"] = input
        captured["timeout"] = timeout
        return subprocess.CompletedProcess(
            args=argv,
            returncode=0,
            stdout=json.dumps(
                {
                    "type": "result",
                    "result": "",
                    "structured_output": VALID_SPEC,
                }
            ),
            stderr="",
        )

    monkeypatch.setattr(subprocess, "run", fake_run)
    monkeypatch.setattr("shutil.which", lambda _cmd: "/usr/bin/claude")

    adapter = ClaudeCLIAdapter(cmd="claude", model="sonnet")
    spec = adapter.generate("hello prompt", schema=SCHEMA)

    assert spec == VALID_SPEC
    assert captured["input"] == "hello prompt"
    assert captured["timeout"] == adapter.timeout_s
    assert captured["argv"][0] == "claude"


def test_claude_cli_generate_raises_when_cli_missing(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr("shutil.which", lambda _cmd: None)
    adapter = ClaudeCLIAdapter(cmd="claude")
    with pytest.raises(AdapterError, match="not found on PATH"):
        adapter.generate("p", schema=SCHEMA)


def test_claude_cli_generate_raises_on_nonzero_exit(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    def fake_run(argv, *, input, capture_output, text, timeout, check):  # type: ignore[no-untyped-def]
        return subprocess.CompletedProcess(
            args=argv, returncode=2, stdout="", stderr="boom"
        )

    monkeypatch.setattr(subprocess, "run", fake_run)
    monkeypatch.setattr("shutil.which", lambda _cmd: "/usr/bin/claude")
    adapter = ClaudeCLIAdapter()
    with pytest.raises(AdapterError, match="exited 2.*boom"):
        adapter.generate("p", schema=SCHEMA)


def test_claude_cli_generate_raises_on_timeout(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    def fake_run(argv, *, input, capture_output, text, timeout, check):  # type: ignore[no-untyped-def]
        raise subprocess.TimeoutExpired(cmd=argv, timeout=timeout)

    monkeypatch.setattr(subprocess, "run", fake_run)
    monkeypatch.setattr("shutil.which", lambda _cmd: "/usr/bin/claude")
    adapter = ClaudeCLIAdapter(timeout_s=1)
    with pytest.raises(AdapterError, match="timed out"):
        adapter.generate("p", schema=SCHEMA)


def test_claude_cli_generate_raises_on_invalid_json(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    def fake_run(argv, *, input, capture_output, text, timeout, check):  # type: ignore[no-untyped-def]
        return subprocess.CompletedProcess(
            args=argv, returncode=0, stdout="not json at all", stderr=""
        )

    monkeypatch.setattr(subprocess, "run", fake_run)
    monkeypatch.setattr("shutil.which", lambda _cmd: "/usr/bin/claude")
    adapter = ClaudeCLIAdapter()
    with pytest.raises(AdapterError, match="could not parse"):
        adapter.generate("p", schema=SCHEMA)


# --------------------------------------------------------------------------- #
# _parse_cli_output                                                           #
# --------------------------------------------------------------------------- #


def test_parse_cli_output_prefers_structured_output() -> None:
    """The live CLI puts schema-validated output here when --json-schema is set."""
    stdout = json.dumps(
        {"type": "result", "result": "", "structured_output": VALID_SPEC}
    )
    assert _parse_cli_output(stdout) == VALID_SPEC


def test_parse_cli_output_handles_string_result() -> None:
    """Legacy fallback: --output-format json without --json-schema."""
    stdout = json.dumps({"type": "result", "result": json.dumps(VALID_SPEC)})
    assert _parse_cli_output(stdout) == VALID_SPEC


def test_parse_cli_output_handles_object_result() -> None:
    stdout = json.dumps({"type": "result", "result": VALID_SPEC})
    assert _parse_cli_output(stdout) == VALID_SPEC


def test_parse_cli_output_handles_bare_object() -> None:
    stdout = json.dumps(VALID_SPEC)
    assert _parse_cli_output(stdout) == VALID_SPEC


def test_parse_cli_output_raises_on_empty() -> None:
    with pytest.raises(AdapterError, match="empty"):
        _parse_cli_output("")


def test_parse_cli_output_raises_on_empty_result_no_structured() -> None:
    """If --json-schema fails to populate structured_output AND result is empty,
    surface a clear error rather than letting json.loads crash on '' input."""
    stdout = json.dumps({"type": "result", "result": ""})
    with pytest.raises(AdapterError, match="empty `result` field"):
        _parse_cli_output(stdout)


# --------------------------------------------------------------------------- #
# validate_tool_spec                                                          #
# --------------------------------------------------------------------------- #


def test_validate_tool_spec_accepts_valid() -> None:
    validate_tool_spec(VALID_SPEC, SCHEMA)


def test_validate_tool_spec_rejects_missing_required() -> None:
    with pytest.raises(AdapterError, match="missing required field"):
        validate_tool_spec({"description": "x", "parameters": {}}, SCHEMA)


def test_validate_tool_spec_rejects_non_dict() -> None:
    with pytest.raises(AdapterError, match="must be a JSON object"):
        validate_tool_spec("not a dict", SCHEMA)


def test_validate_tool_spec_rejects_bad_field_types() -> None:
    bad = {"description": 42, "parameters": {}, "notes": ""}
    with pytest.raises(AdapterError, match="description must be a string"):
        validate_tool_spec(bad, SCHEMA)


# --------------------------------------------------------------------------- #
# AnthropicAPIAdapter                                                         #
# --------------------------------------------------------------------------- #


def test_anthropic_adapter_clear_error_when_sdk_missing(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setitem(sys.modules, "anthropic", None)
    with pytest.raises(AdapterError, match="anthropic SDK not installed"):
        AnthropicAPIAdapter()
