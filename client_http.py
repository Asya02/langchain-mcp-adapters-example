# Create server parameters for stdio connection
import asyncio
import os

from dotenv import find_dotenv, load_dotenv
from langchain_gigachat.chat_models.gigachat import GigaChat
from langchain_mcp_adapters.tools import load_mcp_tools
from langgraph.prebuilt import create_react_agent
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from langchain_mcp_adapters.client import MultiServerMCPClient

load_dotenv(find_dotenv())

# LLM GigaChat
model = GigaChat(model="GigaChat-Max",
                verify_ssl_certs=False,
                profanity_check=False,
                top_p=0,
                streaming=False,
                max_tokens=8000,
                temperature=1,
                timeout=600)


async def main():
    async with MultiServerMCPClient(
        {
            "math": {
                "url": "http://localhost:8000/sse",
                "transport": "sse",
            }
        }
    ) as client:
        agent = create_react_agent(model, client.get_tools())
        resp = await agent.ainvoke({"messages": "what's (3 + 5) x 12?"})
        print(resp['messages'][-1].content)

# Run the main function
asyncio.run(main())
