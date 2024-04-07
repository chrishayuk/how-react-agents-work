from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.agents import AgentExecutor, create_react_agent
from langchain import hub
from tools.system_time_tool import check_system_time

# load environment variables
load_dotenv()

# Choose the LLM to use
llm = ChatOpenAI(model="gpt-4")

# set my message
query = "What is the current time?"

# Get the react prompt template
prompt_template = hub.pull("hwchase17/react")

# set the tools
tools = [check_system_time]

# Construct the ReAct agent
agent = create_react_agent(llm, tools, prompt_template)

# Create an agent executor by passing in the agent and tools
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# Get the current time
agent_executor.invoke({"input": query})