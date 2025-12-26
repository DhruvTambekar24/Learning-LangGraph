from mcp.server.fastmcp import FastMCP
mcp=FastMCP(
    name="WeatherServer"
)

@mcp.tool()
def get_weather(location: str) -> str:
    """ _summary_
    Get weather information for a given location.
    """
    return f"Weather for {location} is sunny."

if __name__ == "__main__":
    mcp.run(transport="streamable-http")