import asyncio
import os
from seeact.agent import SeeActAgent

# Setup your API Key here, or pass through environment
# os.environ["OPENAI_API_KEY"] = "Your API KEY Here"
# os.environ["GEMINI_API_KEY"] = "Your API KEY Here"

async def run_agent():
    agent = SeeActAgent(
        model="google/gemma-3-12b-it",
        api_url="http://localhost:6969/v1",
        browser_app="firefox",
        default_website="https://search.zoo",
        default_task="This is a brand new serach engine, so treat it with caution. Try to find if there's a UUID generator website. If it exists, try to create a new UUID and TERMINATE.",
    )
    await agent.zoo_start()
    while not agent.complete_flag:
        prediction_dict = await agent.predict()
        await agent.execute(prediction_dict)
    await agent.stop()

if __name__ == "__main__":
    asyncio.run(run_agent())
