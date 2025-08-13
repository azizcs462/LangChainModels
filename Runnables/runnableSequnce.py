from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers   import StrOutputParser

load_dotenv()

model = ChatOpenAI()
parser = StrOutputParser()

prompt1 = PromptTemplate(
    template = """ Create a joke from {Topic}""",
    input_variables=['Topic']
)

prompt2 = PromptTemplate(
    template = """ Explaint the  {joke}""",
    input_variables=['joke']
)



sequenceChain = RunnableSequence(prompt1,model,parser,prompt2,model,parser)

result2 = sequenceChain.invoke({'Topic' : 'ML'})

print(result2)

