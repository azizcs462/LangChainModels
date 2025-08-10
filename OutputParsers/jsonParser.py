from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser,JsonOutputParser
from dotenv import load_dotenv


load_dotenv()

model = ChatOpenAI(temperature=0)
parser = JsonOutputParser()



template = PromptTemplate(
    template=""" Create some random item   {format_instruction}""",
    input_variables=[],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)







# prompt = template.format()

# result = model.invoke(prompt)
# final_result = parser.parse(result.content)
# print(final_result)

chain = template | model | parser

result = chain.invoke({})
print(result)
