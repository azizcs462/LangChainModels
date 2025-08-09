from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()

embedding = OpenAIEmbeddings(model='text-embedding-3-large',dimensions=300)

documents = [
"Virat Kohli is considered one of the best batsmen in the world. He has been the captain of the Indian cricket team since 2013.",

"Rohit Sharma is known for his aggressive batting style and is often referred to as the 'Hitman' of Indian cricket. He holds the record for the highest individual score in One Day Internationals.",

"Jasprit Bumrah is a right-arm fast bowler, known for his unique bowling action and ability to bowl yorkers at will. He made his debut for the Indian cricket team in 2016 and has since become a key player in the team's bowling lineup.",

"Mahendra Singh Dhoni, popularly known as MS Dhoni, is one of the most successful captains in the history of Indian cricket. He is known for his calm demeanor on the field and his exceptional skills as a wicket-keeper."
]

query = 'Tell me about Sharma Kohli'

doc_embedding = embedding.embed_documents(documents)

query_embedding = embedding.embed_query(query)

scores = cosine_similarity([query_embedding],doc_embedding)[0]

index,score = sorted(list(enumerate(scores)),key = lambda x:x[1])[-1]

print(documents[index],score)

