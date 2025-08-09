from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate,load_prompt
load_dotenv()

st.header('Research Tool')

model = ChatOpenAI(model = 'gpt-4')

#Static Promt: User Can write anything 
user_input = st.text_input('Enter Your Prompt')

if st.button('Click Here'):
    response = model.invoke(user_input)
    st.write(response.content)


#Dynamic Prompt: Limited 


st.header('Player Research')



player_input =   st.selectbox("Select Player",['Messi','Ronaldo','Virat','Sachin','Neymar','Rohit'])

category_input = st.selectbox('Category',['Popularity','Income','World Cup','Achievements'])

template = load_prompt('/Users/tarique/Documents/Github/LangChainModels/template.json')


prompt = template.invoke({'player_input':player_input,'category_input':category_input})

if st.button('Player Search'):
    result = model.invoke(prompt)
    st.write(result.content)



