from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI

# load environment variables
load_dotenv()

# Choose the LLM to use
llm = ChatOpenAI(model="gpt-4")

# set my message
query = "Who is Katy Perry?"

# set the messages
messages = [
    SystemMessage(content="You're a helpful assistant"),
    HumanMessage(content=query),
]

# execute
result = llm.invoke(messages)

# print out the result
print(result)