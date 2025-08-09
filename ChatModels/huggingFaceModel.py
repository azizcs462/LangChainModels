from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv

load_dotenv()




llm = HuggingFaceEndpoint(
    repo_id='openai/gpt-oss-120b',
    task='text-generation',  # ✅ correct task for this model
)

model = ChatHuggingFace(llm=llm)

result = model.invoke("Create a document list 2 sentences for each  Virat,Rohit,Bumrah,Dhoni")
print(result.content)
