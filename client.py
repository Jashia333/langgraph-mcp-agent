from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
from langchain_groq import ChatGroq

import asyncio
import os

from dotenv import load_dotenv
load_dotenv()


async def main():

    llm_client=MultiServerMCPClient(
        {
            "math":{
                "command":"python",
                "args":["mathserver.py"], # absolute pathm
                "transport":"stdio",
            },
            "weather":{
                "url" : "http://127.0.0.1:8000/mcp", # /mcp to pull up all the mcp servers
                "transport":"streamable_http"
            }
        }
    )


    os.environ["GROQ_API_KEY"]=os.getenv("GROQ_API_KEY")

    tools=await llm_client.get_tools()
    #print("Available tools:", tools)
    model = ChatGroq(model="llama3-8b-8192", api_key=os.getenv("GROQ_API_KEY"))

    agent=create_react_agent(
        model,
        tools
    )

    response=await agent.ainvoke(
        {"messages":[
            {
            "role":"user",
            "content":"what is 5*5"
            }
        ]
        }
    )

    print("the response ",response["messages"][-1].content)


asyncio.run(main())