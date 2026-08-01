import logging
import os

from dotenv import load_dotenv
from google.adk.agents import LlmAgent
from google.adk.a2a.utils.agent_to_a2a import to_a2a
from google.adk.tools.mcp_tool.mcp_toolset import McpToolset
from google.adk.tools.mcp_tool.mcp_session_manager import StreamableHTTPConnectionParams

logger = logging.getLogger(__name__)
logging.basicConfig(format="[%(levelname)s]: %(message)s", level=logging.INFO)

load_dotenv()

SYSTEM_INSTRUCTION = (
    "You are a specialized assistant for multiplication and division of 2 integers. "
    "Your sole purpose is to use the 'multiply' and 'divide' tool to answer questions about multiplication or division of 2 integers. "
    "If the user asks about anything other than multiplication or division, "
    "politely state that you cannot help with that topic and can only assist with multiplication or division of two integers. "
    "Do not attempt to answer unrelated questions or use tools for other purposes."
)

logger.info("--- 🔧 Loading MCP tools from MCP Server... ---")
logger.info("--- 🤖 Creating ADK Advanced Math Agent... ---")

root_agent = LlmAgent(
    model="gemini-2.5-flash",
    name="adk_advanced_math_agent",
    description="An agent that can help with multiplication and division of two integers",
    instruction=SYSTEM_INSTRUCTION,
    tools=[
        McpToolset(
            connection_params=StreamableHTTPConnectionParams(
                url=os.getenv("MCP_SERVER_URL", "https://advanced-math-mcp-server-v102-869928330868.us-central1.run.app:8080/mcp")
            )
        )
    ],
)