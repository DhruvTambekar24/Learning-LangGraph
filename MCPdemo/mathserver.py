from mcp.server.fastmcp import FastMCP

mcp=FastMCP(
    name="MathServer"
)
@mcp.tool()
def add(a: int, b: int) -> int:
    """ _summary_
    Add two numbers.
    """
    return a + b

@mcp.tool()
def subtract(a: int, b: int) -> int:
    """ _summary_
    Subtract two numbers.
    """
    return a - b

@mcp.tool()
def multiply(a: int, b: int) -> int:
    """ _summary_
    Multiply two numbers.
    """
    return a * b

@mcp.tool()
def divide(a: int, b: int) -> int:
    """ _summary_
    Divide two numbers.
    """
    return a / b

#The transport="stdio" argument tells the server to:
#Use standard input/output (stdin and stdout) to receive and respond to tool function calls
#This is useful for testing and development, but not recommended for production

if __name__ == "__main__":
    mcp.run(transport="stdio")