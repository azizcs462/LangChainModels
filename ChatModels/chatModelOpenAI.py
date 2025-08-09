from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model='gpt-4',temperature=0)

result = model.invoke('Create a document list 2 sentences for each  Virat,Rohit,Bumrah,Dhoni')

print(result.content)

