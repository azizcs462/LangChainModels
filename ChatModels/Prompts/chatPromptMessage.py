from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv()


model = OpenAI()
template = ChatPromptTemplate([
    ('system','You are a good {domain} assistant'),
    ('human','Tell me about {topic}')
])

prompt = template.invoke({'domain':'cricket','topic':'Dusra'})

print(prompt)

