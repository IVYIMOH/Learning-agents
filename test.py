
import os
from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage

# Load environment variables from .env file
load_dotenv()

# Configure OpenRouter model
model = ChatOpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1",
    model="openrouter/free",  # Different model than before
    temperature=0.7,
    max_tokens=1000,
    default_headers={
        "HTTP-Referer": "http://localhost:8000",
        "X-Title": "My Hackathon Agent",
    }
)

# Create agent with system prompt
agent = create_agent(
    model=model,
    system_prompt="You are a helpful AI assistant that provides clear and concise answers."
)

# Test the agent
response = agent.invoke({"messages": [HumanMessage("What is machine learning?")]})
print(response["messages"][-1].content)
