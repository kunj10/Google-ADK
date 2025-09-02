from google.adk.agents import Agent
from google.adk.tools import google_search
from datetime import datetime


def get_current_time() -> dict:
  """
  Get the current time in the format YYYY-MM-DD HH:MM:SS
  """
  return {
    "current_time" : datetime.now().strftime("%Y-%m-%d %H:%M:%S")
  }
  

root_agent = Agent(
  name = "tool_agent",
  model = "gemini-2.0-flash",
  description="tool-agent",
  instruction = """
  You are helpful assistant that use following tools : google_search
  """,
  tools = [google_search],
  #tools = [get_current_time],
)