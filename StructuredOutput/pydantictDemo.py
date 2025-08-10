from typing import Optional,Literal
from pydantic import BaseModel,Field,EmailStr

from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from datetime import date


import warnings
warnings.filterwarnings("ignore")

load_dotenv()

model = ChatOpenAI()

class Review(BaseModel):
    key_themes: list[str] = Field( description="List of key themes")
    summary: str = Field(description='Give the summary for review')
    sentiment: Literal['pos','neg'] = Field(description='Give the sentiment')
    pros: Optional[list[str]] = Field(default=None,description = 'Give pros')
    cons: Optional[list[str]] = Field(default=None,description = 'Give pros')
    name: Optional[str] = Field(default=None,description='Name of Reviwer')
    event_date: str = Field(default=None,description='Give the date of Review')



structureModel = model.with_structured_output(Review)

result = structureModel.invoke("""Reviewed in India on 10 June 2025
Colour: Volcanic Red
I’ve been thinking of getting the scrambler x for quite some time now. Finally made a decision to go with the scrambler after going for a test drive on both the speed 400 and scrambler. Really liked the tall riding position, awesome suspension and the power. Sachin from khiviraj Triumph Mekhri circle branch was very knowledgeable and helpful in making my bike purchase seamless. I got the cushioned seat, windshield and various other accessories to make it more convenient. As someone who’s been using the thunderbird 350 for years, riding this bike feels like a big upgrade!""")

print(result)







