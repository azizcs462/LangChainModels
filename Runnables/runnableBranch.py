from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence,RunnableParallel,RunnablePassthrough,RunnableLambda,RunnableBranch
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers   import StrOutputParser

load_dotenv()

model = ChatOpenAI()
parser = StrOutputParser()

prompt1 = PromptTemplate(
    template = """ Write Detail Report for  {topic}""",
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template = """ write summary less than 100 words for {text}""",
    input_variables=['text']
)



Runnabl1 = RunnableSequence(prompt1,model,parser)
Runnabl2 = RunnableSequence(prompt2,model,parser)







runnableBranch = RunnableBranch(
    (lambda x:len(x)>500,Runnabl2),
    RunnablePassthrough()

)

finalChain = RunnableSequence(Runnabl1,runnableBranch)


result2 = finalChain.invoke({'topic' : 'AI'})

print(result2)

