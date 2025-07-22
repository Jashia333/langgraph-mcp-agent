from mcp.server.fastmcp import FastMCP

weather_server=FastMCP("weather")

@weather_server.tool()
async def get_weather(a:str)->str:
    """
    this gets the weather location
    """
    return "its really hot in new jersey"

if __name__=="__main__":
    weather_server.run(transport="streamable-http")