from mcp.server.fastmcp import FastMCP

# Create the MCP server named "Math"
mcp = FastMCP("Math")

@mcp.tool()
def add(a: float, b: float) -> float:
    """Add two numbers together. Use for addition operations."""
    return a + b

@mcp.tool()
def multiply(a: float, b: float) -> float:
    """Multiply two numbers together. Use for multiplication operations."""
    return a * b

if __name__ == "__main__":
    # Run the server using Stdio transport (default)
    mcp.run()
