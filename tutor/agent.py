from google.adk.agents import Agent
from google.adk.tools.agent_tool import AgentTool
from google.adk.tools import google_search
from google.adk.runners import Runner
from google.adk.memory import InMemoryMemoryService
from google.adk.sessions import Session
from google.adk.tools.langchain_tool import LangchainTool
from .tools import python_tool

session_service=InMemoryMemoryService()

APP_NAME="Tutor"
USER_ID="user-1"
SESSION_ID="session-1"

session=Session(
    app_name=APP_NAME,
    user_id=USER_ID,
    id=SESSION_ID
)

from dotenv import load_dotenv
load_dotenv("./.env")

history_tutor_agent=Agent(
    name="history_tutor_agent",
    model="gemini-2.0-flash-001",
    description="You are a History teacher.",
    instruction="You are an expert and friendly History teaching assistant. You have access to the following tool(s) to answer user queries:" \
    "TOOL(S):" \
    "   - google_search_tool : search the web for information\n\n" \
    "Return the answer in bullet points, if possible.",
    tools=[google_search],
)

math_tutor_agent=Agent(
    name="math_tutor_agent",
    model="gemini-2.0-flash-001",
    description="You are a Math teacher.",
    instruction="You are an expert and friendly Math teaching assistant." \
    "break down each and every aspect of the problem into smaller solvable units and solve them,"
    "then compile them to get the final result." \
    "return your answer in a coherent format with formulae,equations etc."
)

computer_Science_tutor_agent=Agent(
    name="computer_Science_tutor_agent",
    model="gemini-2.0-flash-001",
    description="You are a Computer Science teacher.",
    instruction="You are an expert and friendly Computer science teaching assistant" \
    "with access to some tools, use them wisely to solve the problem apointed by the user." \
    "TOOL(S):" \
    "   - python_tool : Use for executing python code and outputting the result using the print() statement",
    tools=[LangchainTool(python_tool,name="python_tool")]
)

tutor=Agent(
    name="root_agent",
    model="gemini-2.0-flash-001",
    description="You are a Head teacher.",
    instruction="You are an expert and friendly Computer science teaching assistant." \
    "You have access to the following tool(s):" \
    "   - history_tutor_agent : Use to retrieve histrical data and answer questions related to any historical events or people." \
    "   - math_tutor_agent : Use to solve mathematical problems." \
    "   - computer_science_tutor_agent : Use to generate python code for any given problem and execute scripts to get their output.",
    # sub_agents=[history_tutor_agent,math_tutor_agent,computer_Science_tutor_agent]
    tools=[AgentTool(history_tutor_agent),AgentTool(math_tutor_agent),AgentTool(computer_Science_tutor_agent)]
)

root_agent=tutor

runner=Runner(
    app_name=APP_NAME,
    session_service=session,
    agent=root_agent,
)