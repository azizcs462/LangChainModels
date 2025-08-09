from langchain_core.messages import HumanMessage,AIMessage,SystemMessage
from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder

#chat template

template = ChatPromptTemplate([
    ('system','You are good assistant'),
    MessagesPlaceholder(variable_name='chatHistory'),
    ('human','{query}')
])

# load chat history
chat_history = []
with open ('chatHistory.txt') as f:
    chat_history.extend(f.readlines())


#chat prompt

prompt = template.invoke({'chatHistory':chat_history,'query':'where is my refund'})

print(prompt)