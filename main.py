# import asyncio
# from agents import Agent, Runner, function_tool, OpenAIChatCompletionsModel
# from openai import AsyncOpenAI
# from agents.tracing import set_tracing_disabled

# set_tracing_disabled(True)

# model = OpenAIChatCompletionsModel(
#     model="minimax-m2.5:cloud",
#     openai_client=AsyncOpenAI(api_key="ollama", base_url="http://localhost:11434/v1"),
# )
# # # Point the client to your local Ollama instance
# # ollama_client = AsyncOpenAI(
# #     base_url="http://localhost:11434/v1",
# #     api_key="ollama",  # required by the SDK, but Ollama ignores it
# # )

# history_agent = Agent(
#     # name="History Tutor",
#     # instructions="You answer history questions clearly and concisely",
#     # model=OpenAIChatCompletionsModel(
#     model=model,  # or any model you've pulled in Ollama
#     name="History Tutor",
#     instructions="You answer history question clearly and concisely",
# )


# async def main():
#     query = "Who built Badshahi Masjid in Lahore, Pakistan?"
#     result = Runner.run(history_agent, query)


# asyncio.run(main)


import asyncio
from agents import Agent, Runner, OpenAIChatCompletionsModel
from openai import AsyncOpenAI
from agents.tracing import set_tracing_disabled

# Disable tracing (optional)
set_tracing_disabled(True)

# -------------------------------
# 1. Model (Minimax via Ollama/OpenAI-compatible endpoint)
# -------------------------------
model = OpenAIChatCompletionsModel(
    model="minimax-m2.5:cloud",
    openai_client=AsyncOpenAI(
        api_key="ollama",  # required but ignored by Ollama
        base_url="http://localhost:11434/v1",
    ),
)

# -------------------------------
# 2. Agent
# -------------------------------
history_agent = Agent(
    name="History Tutor",
    instructions="You answer history questions clearly and concisely.",
    model=model,
)


# -------------------------------
# 3. Run
# -------------------------------
async def main():
    query = "Who built Badshahi Masjid in Lahore, Pakistan?"

    # ✅ FIX: add await
    result = await Runner.run(history_agent, query)

    # ✅ FIX: print output
    print("\n✅ Answer:\n")
    print(result.final_output)


# -------------------------------
# 4. Execute
# -------------------------------
asyncio.run(main())
