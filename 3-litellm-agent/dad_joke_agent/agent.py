from google.adk.agents import Agent
import os
import random
from google.adk.models.lite_llm import LiteLlm


model = LiteLlm(
  model="huggingface/HuggingFaceTB/SmolLM3-3B",
  api_key=os.getenv("HUGGINGFACEHUB_API_TOKEN"),
  messages=[{ "content": "Hello, how are you?","role": "user"}],
  stream=True,
)
 
root_agent = Agent(
  name = "dad_joke_agent",
  model = model,
  description="dad_joke_agent",
  instruction = """
  You are helpful assistant that tells me dad jokes
  """,

)