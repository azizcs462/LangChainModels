from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.runnables import RunnableParallel,RunnableSequence
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers   import StrOutputParser

load_dotenv()

model = ChatOpenAI()
parser = StrOutputParser()

prompt1 = PromptTemplate(
    template = """ Create a  tweet about  {topic}""",
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template = """ Create a linkdin post about {topic}""",
    input_variables=['topic']
)

parallelChain = RunnableParallel(
    {
        'tweetpost':RunnableSequence(prompt1,model,parser),
        'lpost':RunnableSequence(prompt2,model,parser)

    }
)

result2 = parallelChain.invoke({'topic' : 'ML'})

print(result2)

