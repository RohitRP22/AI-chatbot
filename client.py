from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
from langchain_groq import ChatGroq

from dotenv import load_dotenv
load_dotenv()

import asyncio

async def main():
    client = MultiServerMCPClient(
        {
            "math": {"command":"python", "args": ["mathserver.py"], "transport": "stdio"},
            "weather": {"url": "http://localhost:8000/mcp", "transport": "streamable_http"}
        }
    )

    import os
    groq_api_key = os.getenv("GROQ_API_KEY")
    if groq_api_key is not None:
        os.environ["GROQ_API_KEY"] = groq_api_key

    tools = await client.get_tools()
    model = ChatGroq(model="qwen/qwen3-32b")
    agent = create_react_agent(
            model,tools
        )
    # print(agent.input_schema.schema())
    
    math_response = await agent.ainvoke({
    "messages": [
        {
        "type": "human",
        "content": "How is the weather in Tokyo?"
        }
    ], 
    "is_last_step": False,
    "remaining_steps": 5
    })

    print(math_response["messages"][-1].content)
    # print("Math Response:", math_response)
    

    # math_response = await agent.ainvoke(
    #     {"message":[{"role": "user", "content": "What is (5 + 3) x 12?"}]})
    
    

    
    # math_response = await agent.ainvoke(
    #     {"messages": [{"role": "user", "content": "What is (5 + 3) x 12?"}]}
    # )
    # print(math_response)
    
asyncio.run(main())

