from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.agents import AgentExecutor, create_react_agent
from tools.system_time_tool import check_system_time
from react_template import get_react_prompt_template

# load environment variables
load_dotenv()

# Choose the LLM to use
llm = ChatOpenAI(model="gpt-4")

# set my message
query = "What's the current time in New York (you are in London) just show the time in New York and not the date?"

# set the tools
tools = [check_system_time]

# Get the react prompt template
prompt_template = get_react_prompt_template()

# Construct the ReAct agent
agent = create_react_agent(llm, tools, prompt_template)

# Create an agent executor by passing in the agent and tools
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# Get the current time
agent_executor.invoke({"input": query})