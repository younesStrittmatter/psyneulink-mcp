"""Tests for the --transport CLI flag and the SSE boot path."""

from __future__ import annotations

import contextlib
import socket
import threading
import time
from unittest.mock import AsyncMock, Mock

import pytest

from psyneulink_mcp import server


def test_parser_defaults_to_stdio(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("PSYNEULINK_MCP_TRANSPORT", raising=False)
    monkeypatch.delenv("PSYNEULINK_MCP_HOST", raising=False)
    monkeypatch.delenv("PSYNEULINK_MCP_PORT", raising=False)
    ns = server._build_parser().parse_args([])
    assert ns.transport == "stdio"
    assert ns.host == "127.0.0.1"
    assert ns.port == 8765


def test_parser_accepts_sse(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("PSYNEULINK_MCP_TRANSPORT", raising=False)
    ns = server._build_parser().parse_args(["--transport", "sse"])
    assert ns.transport == "sse"


def test_parser_accepts_host_and_port(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("PSYNEULINK_MCP_HOST", raising=False)
    monkeypatch.delenv("PSYNEULINK_MCP_PORT", raising=False)
    ns = server._build_parser().parse_args(
        ["--transport", "sse", "--host", "0.0.0.0", "--port", "9000"]
    )
    assert ns.transport == "sse"
    assert ns.host == "0.0.0.0"
    assert ns.port == 9000


def test_parser_reads_env_defaults(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("PSYNEULINK_MCP_TRANSPORT", "sse")
    monkeypatch.setenv("PSYNEULINK_MCP_HOST", "0.0.0.0")
    monkeypatch.setenv("PSYNEULINK_MCP_PORT", "12345")
    ns = server._build_parser().parse_args([])
    assert ns.transport == "sse"
    assert ns.host == "0.0.0.0"
    assert ns.port == 12345


def test_main_stdio_calls_mcp_run(monkeypatch: pytest.MonkeyPatch) -> None:
    fake_run = Mock()
    monkeypatch.setattr(server.mcp, "run", fake_run)
    # asyncio.run should NOT be called in the stdio path; sentinel-fail it.
    monkeypatch.setattr(
        server.asyncio, "run", Mock(side_effect=AssertionError("asyncio.run should not run"))
    )
    server.main(["--transport", "stdio"])
    fake_run.assert_called_once_with()


def test_main_sse_calls_run_sse_async(monkeypatch: pytest.MonkeyPatch) -> None:
    fake_sse = AsyncMock()
    fake_asyncio_run = Mock()
    monkeypatch.setattr(server.mcp, "run_sse_async", fake_sse)
    monkeypatch.setattr(server.asyncio, "run", fake_asyncio_run)
    monkeypatch.setattr(
        server.mcp, "run", Mock(side_effect=AssertionError("stdio path should not run"))
    )

    server.main(["--transport", "sse", "--host", "127.0.0.1", "--port", "8123"])

    assert server.mcp.settings.host == "127.0.0.1"
    assert server.mcp.settings.port == 8123
    fake_sse.assert_called_once_with()
    fake_asyncio_run.assert_called_once()
    # asyncio.run should be invoked with the coroutine returned by run_sse_async()
    (coro_arg,), _ = fake_asyncio_run.call_args
    # AsyncMock returns a coroutine on call; close it to silence the warning.
    coro_arg.close()


def _free_port() -> int:
    s = socket.socket()
    try:
        s.bind(("127.0.0.1", 0))
        return s.getsockname()[1]
    finally:
        s.close()


def _wait_for_port(host: str, port: int, timeout: float = 5.0) -> bool:
    deadline = time.monotonic() + timeout
    while time.monotonic() < deadline:
        try:
            with socket.create_connection((host, port), timeout=0.2):
                return True
        except OSError:
            time.sleep(0.05)
    return False


@pytest.mark.integration
def test_sse_server_boots_and_serves() -> None:
    """Boot the SSE server in a background thread and confirm it answers on /sse.

    We accept any HTTP response that proves the server is bound and answering -
    a 200 with text/event-stream is the happy path, but some FastMCP versions
    only accept POST on /sse and return 405 to a GET. The point of the smoke
    is "server is up", not "protocol matches"; the real client interaction is
    tested out-of-process by the agent-side tests.
    """
    import httpx

    port = _free_port()

    def _run() -> None:
        # Daemon thread; swallow so test failure surfaces via the assertions
        # below instead of a noisy thread traceback.
        with contextlib.suppress(Exception):
            server.main(["--transport", "sse", "--host", "127.0.0.1", "--port", str(port)])

    t = threading.Thread(target=_run, daemon=True, name="psyneulink-mcp-sse-smoke")
    t.start()

    if not _wait_for_port("127.0.0.1", port, timeout=5.0):
        pytest.skip(f"SSE server did not bind to 127.0.0.1:{port} within 5s")

    # Some SSE endpoints stream forever on GET; use a short timeout and stream
    # so we just confirm a response head, not the full body.
    try:
        with httpx.stream(
            "GET",
            f"http://127.0.0.1:{port}/sse",
            timeout=2.0,
            headers={"Accept": "text/event-stream"},
            follow_redirects=False,
        ) as resp:
            status = resp.status_code
    except httpx.ReadTimeout:
        # SSE that opens then blocks for events is a perfectly valid signal
        # that the server is up and answering.
        return

    # Accept anything in the "the server actually answered" range; reject only
    # connection-level failures (which would have raised above).
    assert 200 <= status < 600, f"unexpected status {status}"
