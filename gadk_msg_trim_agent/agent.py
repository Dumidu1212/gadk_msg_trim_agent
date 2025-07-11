from google.adk.agents import Agent

from gadk_msg_trim_agent.prompt import ROOT_AGENT_INSTRUCTION
from gadk_msg_trim_agent.tools import count_characters

root_agent = Agent(
    name="gadk_msg_trim_agent",
    model="gemini-2.0-flash",
    description="A bot that shortens messages while maintaining their core meaning",
    instruction=ROOT_AGENT_INSTRUCTION,
    tools=[count_characters],
)