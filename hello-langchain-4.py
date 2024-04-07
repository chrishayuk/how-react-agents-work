from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from tools.system_time_tool import check_system_time
from react_template import get_react_prompt_template
from langchain_core.output_parsers import StrOutputParser

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

# execute
output_parser = StrOutputParser()
chain = prompt_template | llm | output_parser
result = chain.invoke({"input": query, "tools":"", "tool_names": "", "agent_scratchpad": ""})

# print out the result
print(result)