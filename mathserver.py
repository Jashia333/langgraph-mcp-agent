# %%
from mcp.server.fastmcp import FastMCP
import mcp

# %%
mcp_server=FastMCP("math")

# %%
@mcp_server.tool()
def add(a:int,b:int)-> int:
    """ add the two numbers 

    """
    return a+b

# %%
@mcp_server.tool()
def multiply(a:int,b:int)-> int:
    """ multiply two numbers

    """
    return a*b

# %%
if __name__=="__main__":
    mcp_server.run(transport="stdio")


