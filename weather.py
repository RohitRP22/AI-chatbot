from mcp.server.fastmcp import FastMCP

mcp = FastMCP("weather")

@mcp.tool()
def get_temperature(city: str) -> float:
    """
    _summary_
    Retrieves the current temperature for a given city.
    """
    # Placeholder implementation, replace with actual API call or logic
    return 25.0
@mcp.tool()
def get_humidity(city: str) -> float:
    """
    _summary_
    Retrieves the current humidity for a given city.
    """
    # Placeholder implementation, replace with actual API call or logic
    return 60.0

if __name__ == "__main__":
    mcp.run(transport="streamable-http")