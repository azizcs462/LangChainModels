from typing import Optional,Literal
from pydantic import BaseModel,Field,EmailStr

from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from datetime import date
import warnings
warnings.filterwarnings("ignore")

load_dotenv()

model = ChatOpenAI()

ReviewJson = {
    "title": "Review",
    "type": "object",
    "properties": {
        "review_id": {"type": "string"},
        "reviewer": {
            "type": "object",
            "properties": {
                "name": {"type": "string"},
                "user_id": {"type": "string"},
                "location": {"type": "string"}
            },
            "required": ["name", "user_id", "location"]
        },
        "product": {
            "type": "object",
            "properties": {
                "product_id": {"type": "string"},
                "name": {"type": "string"},
                "category": {"type": "string"}
            },
            "required": ["product_id", "name", "category"]
        },
        "review_details": {
            "type": "object",
            "properties": {
                "rating": {"type": "number"},
                "title": {"type": "string"},
                "text": {"type": "string"},
                "pros": {
                    "type": "array",
                    "items": {"type": "string"}
                },
                "cons": {
                    "type": "array",
                    "items": {"type": "string"}
                },
                "date": {"type": "string", "format": "date"}
            },
            "required": ["rating", "title", "text", "date"]
        },
        "sentiment_analysis": {
            "type": "object",
            "properties": {
                "overall_sentiment": {
                    "type": "string",
                    "enum": ["positive", "neutral", "negative"]
                },
                "aspects": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "aspect": {"type": "string"},
                            "sentiment": {
                                "type": "string",
                                "enum": ["positive", "neutral", "negative"]
                            },
                            "evidence": {"type": "string"}
                        },
                        "required": ["aspect", "sentiment"]
                    }
                }
            },
            "required": ["overall_sentiment", "aspects"]
        },
        "metadata": {
            "type": "object",
            "properties": {
                "helpful_votes": {"type": "integer"},
                "verified_purchase": {"type": "boolean"},
                "language": {"type": "string"}
            },
            "required": ["helpful_votes", "verified_purchase"]
        }
    },
    "required": [
        "review_id",
        "reviewer",
        "product",
        "review_details",
        "sentiment_analysis",
        "metadata"
    ]
}


print(type(ReviewJson))


structureModel = model.with_structured_output(ReviewJson)

result = structureModel.invoke("""Reviewed in India on 10 June 2025
Colour: Volcanic Red
I’ve been thinking of getting the scrambler x for quite some time now. Finally made a decision to go with the scrambler after going for a test drive on both the speed 400 and scrambler. Really liked the tall riding position, awesome suspension and the power. Sachin from khiviraj Triumph Mekhri circle branch was very knowledgeable and helpful in making my bike purchase seamless. I got the cushioned seat, windshield and various other accessories to make it more convenient. As someone who’s been using the thunderbird 350 for years, riding this bike feels like a big upgrade!""")

print(result)



