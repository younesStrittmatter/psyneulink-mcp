"""Entry point for the psyneulink-mcp server."""

from __future__ import annotations

import argparse
import asyncio
import os
import sys

from mcp.server.fastmcp import FastMCP

from .tools.curated import brainlike as curated_brainlike
from .tools.curated import composition as curated_composition
from .tools.curated import feedback as curated_feedback
from .tools.curated import persistence as curated_persistence
from .tools.curated import psyche as curated_psyche
from .tools.curated import visualization as curated_visualization
from .tools.generated import register_all as register_generated

mcp = FastMCP("psyneulink-mcp")

curated_feedback.register(mcp)
curated_brainlike.register(mcp)
curated_composition.register(mcp)
curated_persistence.register(mcp)
curated_visualization.register(mcp)
curated_psyche.register(mcp)
register_generated(mcp)


def _build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="psyneulink-mcp",
        description=(
            "psyneulink-mcp server. Defaults to stdio for backward compat with "
            "existing MCP clients; pass --transport sse to expose the same MCP "
            "over HTTP+SSE on a localhost port."
        ),
    )
    p.add_argument(
        "--transport",
        choices=("stdio", "sse"),
        default=os.environ.get("PSYNEULINK_MCP_TRANSPORT", "stdio"),
        help=(
            "Transport. stdio (default) for in-process MCP clients; "
            "sse for HTTP/SSE on --host:--port."
        ),
    )
    p.add_argument(
        "--host",
        default=os.environ.get("PSYNEULINK_MCP_HOST", "127.0.0.1"),
        help="(SSE only) bind host. Default 127.0.0.1.",
    )
    p.add_argument(
        "--port",
        type=int,
        default=int(os.environ.get("PSYNEULINK_MCP_PORT", "8765")),
        help="(SSE only) bind port. Default 8765.",
    )
    return p


def main(argv: list[str] | None = None) -> None:
    ns = _build_parser().parse_args(argv)
    if ns.transport == "stdio":
        mcp.run()
        return

    # SSE: surface the URL so a launching parent can pattern-match readiness.
    mcp.settings.host = ns.host
    mcp.settings.port = ns.port
    sse_path = getattr(mcp.settings, "sse_path", "/sse")
    print(
        f"psyneulink-mcp: serving sse on http://{ns.host}:{ns.port}{sse_path}",
        file=sys.stderr,
        flush=True,
    )
    asyncio.run(mcp.run_sse_async())


if __name__ == "__main__":
    main()
