# @title Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# from google.adk.agents.llm_agent import Agent
from google.adk.agents import Agent, SequentialAgent, ParallelAgent, LoopAgent
from google.adk.models.google_llm import Gemini
from google.adk.runners import InMemoryRunner
from google.adk.tools import AgentTool, FunctionTool, google_search
from google.genai import types

print("✅ ADK components imported successfully.")

try:
    # GOOGLE_API_KEY = UserSecretsClient().get_secret("GOOGLE_API_KEY")
    # os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY
    print("✅ Gemini API key setup complete.")
except Exception as e:
    print(
        f"🔑 Authentication Error: Please make sure you have added 'GOOGLE_API_KEY' to your Kaggle secrets. Details: {e}"
    )

retry_config = types.HttpRetryOptions(
    attempts=5,  # Maximum retry attempts
    exp_base=7,  # Delay multiplier
    initial_delay=1,  # Initial delay before first retry (in seconds)
    http_status_codes=[429, 500, 503, 504]  # Retry on these HTTP errors
)


# Mock tool implementation
def get_current_time(city: str) -> dict:
    """Returns the current time in a specified city."""
    return {"status": "success", "city": city, "time": "10:30 AM"}


def get_favourite_pet(person: str) -> dict:
    """Returns the current time in a specified city."""
    return {"status": "success", "person": person, "pet": "Lion"}


# ---------------------------------------------
# Root Coordinator: Orchestrates the workflow by calling the sub-agents as tools.
# ---------------------------------------------
root_agent = Agent(
    name='de_simple_agent',
    # model='gemini-2.5-flash',
    model=Gemini(
        model="gemini-2.5-flash",
        retry_options=retry_config
    ),
    description="A simple agent that tells the current time in a specified city., can tell the favourite pet for a "
                "person and can answer general questions.",
    instruction="You are a helpful assistant that tells the current time in cities, can tell the favourite pet for a "
                "person and can answer general questions. Use the 'get_current_time' tool for telling the current "
                "time. Use 'get_favourite_pet' tool for deciding eth favourite pet. Use Google Search for any other "
                "current info or if unsure.",
    # google_search is a pre-built tool which allows the agent to perform Google searches.
    # tools=[get_current_time, get_favourite_pet, google_search],
    tools=[get_current_time, get_favourite_pet],
)

print("✅ Simple Agent defined.")


# runner = InMemoryRunner(agent=root_agent)
# print("✅ Runner created.")

# response = await runner.run_debug(
#     "What is Agent Development Kit from Google? What languages is the SDK available in?"
# )
