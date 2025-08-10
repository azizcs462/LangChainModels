from langchain_openai import ChatOpenAI
from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser,PydanticOutputParser
from langchain.schema.runnable import RunnableParallel,RunnableLambda,RunnableBranch
from dotenv import load_dotenv
from pydantic import BaseModel,Field
from typing import Literal

load_dotenv()

model1 = ChatOpenAI()
parser = StrOutputParser()

class Feedback(BaseModel):
    sentiment:Literal['Negative','Positive']=Field(description='Give the sentiment of the feedback')

parser2 = PydanticOutputParser(pydantic_object=Feedback)

prompt1 = PromptTemplate(
    template = """ Classify the following feedback into positive or negative based on {feedback} {format_instruction}""",
    input_variables=['feedback'],
    partial_variables={'format_instruction':parser2.get_format_instructions()}

)

#Prompt for positive Feedback

prompt2 = PromptTemplate(
    template = "Generate Appropreate response for positive feedback {feedback}",
    input_variables=['feedback']
)

#Prompt for positive Feedback

prompt3 = PromptTemplate(
    template = "Generate Appropreate response for negative feedback {feedback}",
    input_variables=['feedback']
)



classifierChain = prompt1 | model1 | parser2

branchChain = RunnableBranch(

    (lambda x:x.sentiment=='Positive',prompt2 | model1 | parser),
    (lambda x:x.sentiment=='Negative',prompt3 | model1 | parser),
    RunnableLambda(lambda x:'Could not find sentiment')
)

merge = classifierChain | branchChain


print(merge.invoke({'feedback':'THis is a good phone'}))



# prompt1 = PromptTemplate(
#     template = """ Classify the following feedback into positive or negative based on {feedback}""",
#     input_variables=['feedback']

# )




