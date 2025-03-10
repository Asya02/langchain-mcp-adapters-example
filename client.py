# Create server parameters for stdio connection
import asyncio
import os

from dotenv import find_dotenv, load_dotenv
from langchain_gigachat.chat_models.gigachat import GigaChat
from langchain_mcp_adapters.tools import load_mcp_tools
from langgraph.prebuilt import create_react_agent
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

load_dotenv(find_dotenv())

# model = ChatOpenAI(model="gpt-4o-mini")

# giga_user = os.environ.get("giga_user")
# giga_password = os.environ.get("giga_password")

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
    server_params = StdioServerParameters(
        # command="python",
        command="uv",
        args=["run", "math_server.py"],
    )

    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            # Initialize the connection
            await session.initialize()

            # Get tools
            tools = await load_mcp_tools(session)

            # Create and run the agent
            agent = create_react_agent(model, tools)

            agent_response = await agent.ainvoke({"messages": [{"role": "user", "content": "what's (3 + 5) x 12?"}]})
            print(agent_response['messages'][-1].content)

# Run the main function
asyncio.run(main())
