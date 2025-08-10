from typing import TypedDict,Annotated,Optional,Literal
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import warnings

warnings.filterwarnings("ignore")

load_dotenv()

model = ChatOpenAI()

class Review(TypedDict):
    summary: str
    sentiment: str


structureModel = model.with_structured_output(Review)
result = structureModel.invoke("Isn't it like 6 years late to make a Game of Thrones edition ? The tv show ended that long ago. Deem time flies as it's already 6 years when that ended")

print(result,'here')



class Review1(TypedDict):
    key_themes:Annotated[list[str],'Mention all key themes']
    summary: Annotated[str,'Return the Summary of the Riview']
    sentiment: Annotated[str,'Return the Sentiment of the Riview Negatiove or Positive or Neutral']
    sentiment1:Annotated[Literal['pos','neg'],'Senitment of the review']
    pros: Annotated[Optional[list[str]],'Pros']
    cons: Annotated[Optional[list[str]],'Cons']

structureModel2 = model.with_structured_output(Review1)

result2 = structureModel2.invoke("Isnt it like 6 years late to make a Game of Thrones edition ? The tv show ended that long ago. Deem time flies as it's already 6 years when that ended")

print(result2,'here1')
