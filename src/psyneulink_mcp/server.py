"""Entry point for the psyneulink-mcp server."""

from __future__ import annotations

from mcp.server.fastmcp import FastMCP

from .tools.curated import feedback as curated_feedback

mcp = FastMCP("psyneulink-mcp")

curated_feedback.register(mcp)


def main() -> None:
    mcp.run()


if __name__ == "__main__":
    main()
