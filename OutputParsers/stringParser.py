from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv


load_dotenv()

model = ChatOpenAI(temperature=0)

template1 = PromptTemplate(
    template=""" Write details for {topic}""",
    input_variables=['topic']
)

template2 = PromptTemplate(
    template=""" Write 5 lines details for {text}""",
    input_variables=['text']
)



 # traditional 

# prompt1 = template1.invoke({'topic':'Champions League'})
# result1 = model.invoke(prompt1)


# prompt2 = template2.invoke({'text':result1.content})

# result2 = model.invoke(prompt2) 


# using parser and chain
parser = StrOutputParser()

chain = template1  | model | parser | template2  | model | parser

result2 = chain.invoke({'topic':'Champions League'})

print(result2)
