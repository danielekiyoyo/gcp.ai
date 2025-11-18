import os
# from kaggle_secrets import UserSecretsClient
from google.adk.agents import Agent
from google.adk.models.google_llm import Gemini
from google.adk.runners import InMemoryRunner
from google.adk.tools import google_search
from google.genai import types

from adk.models import GeminiModel

# Configure Gemini model
model = GeminiModel(
    api_key="your_api_key_here",
    model_name="gemini-1.5-pro",
    temperature=0.7,
    max_tokens=1024
)

try:
    # GOOGLE_API_KEY = UserSecretsClient().get_secret("GOOGLE_API_KEY")
    os.environ["GOOGLE_API_KEY"] = "DE GOOGLE_API_KEY"
    # os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY
    print("✅ Gemini API key setup complete.")
except Exception as e:
    print(
        f"🔑 Authentication Error: Please make sure you have added 'GOOGLE_API_KEY' to your Kaggle secrets. Details: {e}"
    )


print("✅ ADK components imported successfully.")