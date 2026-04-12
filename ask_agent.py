import os
from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
from langchain.tools import tool
from langchain_core.messages import HumanMessage

load_dotenv()

model = ChatOpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1",
    model="gpt-4o-mini",
    temperature=0.1,
)

@tool
def convert_temperature(value: float, from_unit: str, to_unit: str) -> float:
    """Convert temperature between Celsius and Fahrenheit."""
    if from_unit.lower() == "celsius" and to_unit.lower() == "fahrenheit":
        return (value * 9/5) + 32
    elif from_unit.lower() == "fahrenheit" and to_unit.lower() == "celsius":
        return (value - 32) * 5/9
    return value

agent = create_agent(
    model=model,
    system_prompt="You are a helpful assistant that converts temperatures. Always use the convert_temperature tool.",
    tools=[convert_temperature]
)

# Ask your question here - CHANGE THIS LINE
response = agent.invoke({
    "messages": [HumanMessage(content="What is 32 degrees Fahrenheit in Celsius?")]
})
print(response["messages"][-1].content)
