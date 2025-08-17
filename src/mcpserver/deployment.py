from mcp.server.fast import FastMCP

mcp = FastMCP("Deployment")

@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b