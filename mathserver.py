from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Math")

@mcp.tool()
def add(a: int, b: int) -> int:
    """
    _summary_
    Adds two integers.
    """
    return a + b
@mcp.tool()
def subtract(a: int, b: int) -> int:
    """
    _summary_
    Subtracts the second integer from the first.
    """
    return a - b
@mcp.tool()
def multiply(a: int, b: int) -> int:
    """
    _summary_
    Multiplies two integers.
    """
    return a * b
@mcp.tool()
def divide(a: int, b: int) -> float:
    """
    _summary_
    Divides the first integer by the second.
    Raises an error if the second integer is zero.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

#trasnport = stdio tells the server to use standard input/output for communication
# This is useful for testing or when integrating with other systems that use standard I/O.

if __name__ == "__main__":
    mcp.run(transport="stdio")