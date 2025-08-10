from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()
parser = StrOutputParser()


template1 = PromptTemplate(
    template=""" Tell me 5 line paragraph for {topic}""",
    input_variables=['topic']
)

template2 = PromptTemplate(
    template=""" Suggest me headline for  {text}""",
    input_variables=['text']
)

chain = template1 | model | parser | template2 | model | parser

result = chain.invoke({'topic':'politics'})

print(result)

chain.get_graph().print_ascii()
