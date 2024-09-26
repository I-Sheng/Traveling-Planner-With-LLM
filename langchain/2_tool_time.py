# Docs: https://python.langchain.com/v0.1/docs/modules/tools/custom_tools/

# Import necessary libraries
from langchain import hub
from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain.pydantic_v1 import BaseModel, Field
from langchain_core.tools import StructuredTool, Tool
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import json
import os

load_dotenv()

current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, "data", "sitesData.json")

with open(file_path, "r") as json_file:
    data = json.load(json_file)


# Functions for the tools
def getTimeSpent(name: str) -> list:
    """Concatenates two strings."""
    if name not in data:
        return data['average']
    return data[name]["time_spent"]



# Pydantic model for tool arguments
class GetTimeSpentArgs(BaseModel):
    name: str = Field(description="Name of the site")


# Create tools using the Tool and StructuredTool constructor approach
tools = [
    # Use StructuredTool for more complex functions that require multiple input parameters.
    # StructuredTool allows us to define an input schema using Pydantic, ensuring proper validation and description.
    StructuredTool.from_function(
        func=getTimeSpent,  # Function to execute
        name="GetTimeSpent",  # Name of the tool
        description="Find the time spent for a site or a restaurant.",  # Description of the tool
        args_schema=GetTimeSpentArgs,  # Schema defining the tool's input arguments
    ),
]

# Initialize a ChatOpenAI model
llm = ChatOpenAI(model="gpt-4o")

# Pull the prompt template from the hub
prompt = hub.pull("hwchase17/openai-tools-agent")

# Create the ReAct agent using the create_tool_calling_agent function
agent = create_tool_calling_agent(
    llm=llm,  # Language model to use
    tools=tools,  # List of tools available to the agent
    prompt=prompt,  # Prompt template to guide the agent's responses
)

# Create the agent executor
agent_executor = AgentExecutor.from_agent_and_tools(
    agent=agent,  # The agent to execute
    tools=tools,  # List of tools available to the agent
    verbose=True,  # Enable verbose logging
    handle_parsing_errors=True,  # Handle parsing errors gracefully
)

# Test the agent with sample queries
response = agent_executor.invoke({"input": "嘉義公園七虎戲水區停留時間"})
print("Response for '嘉義公園七虎戲水區停留時間':", response)

