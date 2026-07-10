import asyncio
import os
from agent_framework import Agent
from agent_framework.openai import OpenAIChatCompletionClient
from dotenv import load_dotenv


async def agente001():
    chat_client = OpenAIChatCompletionClient(
        model="openai/gpt-4o-mini",
        api_key= os.environ.get("OPENROUTER_API_KEY"),
        base_url="https://openrouter.ai/api/v1",
    )

    agent = Agent(
        name="AgenteTeste001",
        client=chat_client,
        instructions="Você é um agente de teste que responde perguntas simples.",
    )

    resposta = await agent.run(
        "Qual é a capital da França?",
        options={"temperature": 0.7, "max_tokens": 2000},
    )
    print("Resposta do agente:", resposta)

if __name__ == "__main__":
    load_dotenv()
    asyncio.run(agente001())