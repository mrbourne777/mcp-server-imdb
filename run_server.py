#!/usr/bin/env python3
"""
Entry point for running the FM-DB MCP Server
"""

from src.fm_db_server.server import mcp

if __name__ == "__main__":
    mcp.run()
