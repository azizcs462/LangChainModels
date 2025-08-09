from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage,SystemMessage,AIMessage
from dotenv import load_dotenv

load_dotenv()
model = ChatOpenAI(model='gpt-4')

chatHistory = [
    SystemMessage(content='You are good  a assistant')
]



while True:
    user_input = input("You: ")
    chatHistory.append(HumanMessage(content=user_input))
    if user_input == 'exit':
        break
    else:
        response = model.invoke(user_input)
        chatHistory.append(AIMessage(content=(response.content)))
        print('AI: ' ,response.content)

print(chatHistory)        
