from langchain_openai import ChatOpenAI
from langchain.output_parsers import StructuredOutputParser,ResponseSchema
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel,Field
from dotenv import load_dotenv 

load_dotenv()

model = ChatOpenAI()

class Person(BaseModel):
    name: str = Field(description='Name of person')
    age: int = Field(gt=18,description='Age of the Person')
    city: str = Field(description='Place of the person')


parser = PydanticOutputParser(pydantic_object=Person)

template = PromptTemplate(
    template = 'Select name,age,city of random person  from  {place} {format_instruction}',
    input_variables=['place'],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)


chain = template | model | parser

result = chain.invoke({'place':'Turkey'})

print(result)
