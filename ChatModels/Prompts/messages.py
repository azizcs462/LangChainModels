from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage,AIMessage,SystemMessage
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

messages = [
    SystemMessage(content='You are a good assistant'),
    HumanMessage(content='Tell me about Dhoni')
]

response = model.invoke(messages)

messages.append(AIMessage(response.content))

print(messages)