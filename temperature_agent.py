import os
from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
from langchain.tools import tool
from langchain_core.messages import HumanMessage

load_dotenv()

# Setup model
model = ChatOpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1",
    model="openrouter/free",
    temperature=0.1,
)

# Create tool
@tool
def convert_temperature(value: float, from_unit: str, to_unit: str) -> float:
    """Convert temperature between Celsius and Fahrenheit."""
    if from_unit.lower() == "celsius" and to_unit.lower() == "fahrenheit":
        return (value * 9/5) + 32
    elif from_unit.lower() == "fahrenheit" and to_unit.lower() == "celsius":
        return (value - 32) * 5/9
    return value

# Create agent
agent = create_agent(
    model=model,
    system_prompt="You convert temperatures. Always use the convert_temperature tool.",
    tools=[convert_temperature]
)

# Test it
response = agent.invoke({
    "messages": [HumanMessage(content="What is 32°F in Celsius?")]
})
print(response["messages"][-1].content)