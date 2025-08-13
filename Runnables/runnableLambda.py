from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence,RunnableParallel,RunnablePassthrough,RunnableLambda
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers   import StrOutputParser

load_dotenv()

model = ChatOpenAI()
parser = StrOutputParser()

prompt1 = PromptTemplate(
    template = """ Create a joke about {Topic}""",
    input_variables=['Topic']
)

prompt2 = PromptTemplate(
    template = """ Explaint the  {text}""",
    input_variables=['text']
)

jokeGenerator = RunnableSequence(prompt1,model,parser)


passthorughChain = RunnableParallel(
    {
        'joke': RunnablePassthrough(),
        'joke length':RunnableLambda(lambda x: len(x))
    }
)

finalChain = RunnableSequence(jokeGenerator,passthorughChain)
result2 = finalChain.invoke({'Topic' : 'ML'})

print(result2)

