from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate

# load environment variables
load_dotenv()

# Choose the LLM to use
llm = ChatOpenAI(model="gpt-4")

# set my message
query = "Katy Perry"
prompt_template = PromptTemplate.from_template("Who is {input}?")

# execute
output_parser = StrOutputParser()
chain = prompt_template | llm | output_parser
result = chain.invoke({"input": query})

# print out the result
print(result)