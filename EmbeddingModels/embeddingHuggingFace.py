from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = HuggingFaceEmbeddings(model='sentence-transformers/all-MiniLM-L6-v2')
text = 'delhi is capital of India.'

vector = embedding.embed_query(text)

print(str(vector))