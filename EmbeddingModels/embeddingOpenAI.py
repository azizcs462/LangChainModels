from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

#single sentence Embedding
embedding = OpenAIEmbeddings(model='text-embedding-3-large',dimensions=32)

result = embedding.embed_query('What is the Capital of India?')

print(str(result))

#Multiple Sentence Embedding

documents = ['India','China','America']

results = embedding.embed_documents(documents)



print(str(results))







