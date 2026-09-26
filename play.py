from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.agents import AgentExecutor, create_react_agent
from tools.system_time_tool import check_system_time
from react_template_2 import get_react_prompt_template
from langchain_community.llms import Ollama

# load environment variables
load_dotenv()

# Choose the LLM to use
#llm = ChatOpenAI(model="gpt-4")
#llm = ChatOpenAI(model="gpt-3.5-turbo")
# Use ollama
llm = Ollama(model="codellama:70b")

# set my message
query = "What's the current time in Rio?"

# set the tools
tools = [check_system_time]

# Get the react prompt template
prompt_template = get_react_prompt_template()

# set the tools
tools = [check_system_time]

# Get the react prompt template
prompt_template = get_react_prompt_template()

# Construct the ReAct agent
agent = create_react_agent(llm, tools, prompt_template)

# Create an agent executor by passing in the agent and tools
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# Set the recipe, this would of course be looked up using RAG
recipe = """here is a recipe for getting the time in new york:
Question: What's the current time in New York (you are in London) just show the time in New York and not the date?
Thought:
I need to check the current system time. New York is generally 5 hours behind London, but this can change due to daylight saving time. Therefore, I will first find out the current time in London and then make the necessary adjustments to find the time in New York.
Action: check_system_time
Action Input: '%Y-%m-%d %H:%M:%S'
Observation: '2024-04-07 00:58:00'
Thought:
The current system time is 00:58:00 on 2024-04-07. Since New York is 5 hours behind London and daylight saving time is not in effect, I will subtract 5 hours from the current London time to find the current time in New York.
Final Answer: 19:58:00
"""

# Get the current time
agent_executor.invoke({"input": query, "recipe":recipe})