from langchain_openai import ChatOpenAI
from langchain.output_parsers import StructuredOutputParser,ResponseSchema
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv 

load_dotenv()

model = ChatOpenAI()

schema = [
    ResponseSchema(name = 'fact1',description = 'fact1 about the player'),
    ResponseSchema(name = 'fact2',description = 'fact2 about the player'),
    ResponseSchema(name = 'fact3',description = 'fact3 about the player'),

]

parser = StructuredOutputParser.from_response_schemas(schema)


template = PromptTemplate(
    template = """ Give 5 facts about {player} {format_instruction}""",
    input_variables=['player'],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)


chain = template | model | parser

result = chain.invoke({'player':'Messi'})

print(result)
