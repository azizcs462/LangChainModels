from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

parser = StrOutputParser()

template = PromptTemplate(
    template = """ Generate 5 lines essay on {topic}""",
    input_variables=['topic']
)

chain = template | model | parser
result = chain.invoke({'topic':'soccer'})

print(result)

chain.get_graph().print_ascii() 