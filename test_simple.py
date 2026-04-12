import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

# Load .env file
load_dotenv()

# Initialize OpenRouter
llm = ChatOpenAI(
    openai_api_key=os.getenv("OPENROUTER_API_KEY"),
    openai_api_base="https://openrouter.ai/api/v1",
    model_name="openrouter/free",
)

# Test the connection
response = llm.invoke("Say 'Hello from my hackathon agent!'")
print(response.content)
