import os

from google.adk.agents import LlmAgent
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset, SseServerParams
from google.adk.models.lite_llm import LiteLlm
from dotenv import load_dotenv

load_dotenv()

# Set environment variables
# os.environ["OPENAI_BASE_URL"] = os.getenv("OPENAI_BASE_URL")
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")

# Define the model to use
gemini_model = 'gemini-2.0-flash'
# ollama_model = LiteLlm(model='ollama_chat/qwen2.5-coder:7b')

# Create a LiteLLM instance
root_agent = LlmAgent(
        model='gemini-2.0-flash',
        name="browser_automation_agent",
        instruction=
        """
            You are a browser automation agent powered by Playwright MCP. You are fully connected to the MCP server and capable of controlling a real browser instance through Playwright.

            Your primary role is to assist the user in interacting with the web browser by following natural language instructions. You can:

            Navigate to URLs

            Click buttons or links

            Fill in forms

            Extract text or attributes from web elements

            Take screenshots

            Wait for specific elements or events

            Perform assertions for testing purposes

            You will receive user instructions in natural language (e.g., "Go to Google and search for Playwright") and convert them into precise browser actions using Playwright APIs via the MCP server.

            When generating or interpreting actions:

            Use high-level abstractions when possible (e.g., page.goto, page.click, page.fill)

            Rely on selectors (CSS or XPath) to identify elements

            Communicate with the user if more detail is needed to proceed

            You are also allowed to return structured results (such as JSON) if requested by the user.

            Stay aligned with the user's goal, be concise and efficient, and always confirm critical actions before performing them if there's any ambiguity.
            """
       ,
        tools=[
            MCPToolset(
                connection_params=SseServerParams(
                    url="http://localhost:3333/sse"  # Ensure the port matches the proxy
                )
            )
        ],
    )