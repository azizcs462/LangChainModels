from langchain_openai import ChatOpenAI
from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id='openai/gpt-oss-120b',
    task='text-generation',  # ✅ correct task for this model
)

model1 = ChatHuggingFace(llm=llm)
model2 = ChatOpenAI()
parser = StrOutputParser()

prompt1 = PromptTemplate(
    template=""" Generate Notes from {text}""",
    input_variables=['text']
)

prompt2 = PromptTemplate(
    template=""" Generate 5 Quiz from {text}""",
    input_variables=['text']
)

prompt3 = PromptTemplate(
    template=""" Merge {Notes} and {Quiz}""",
    input_variables=['Notes','Quiz']
)

parallelChain = RunnableParallel({
    'Notes': prompt1 | model1 | parser,
    'Quiz': prompt2 | model2 | parser
})


mergeChain = prompt3 | model1 | parser

chain = parallelChain  | mergeChain

text = """
Support Vector Machine (SVM) Algorithm
Last Updated : 07 Aug, 2025
Support Vector Machine (SVM) is a supervised machine learning algorithm used for classification and regression tasks. It tries to find the best boundary known as hyperplane that separates different classes in the data. It is useful when you want to do binary classification like spam vs. not spam or cat vs. dog.

The main goal of SVM is to maximize the margin between the two classes. The larger the margin the better the model performs on new and unseen data.

Key Concepts of Support Vector Machine
Hyperplane: A decision boundary separating different classes in feature space and is represented by the equation wx + b = 0 in linear classification.
Support Vectors: The closest data points to the hyperplane, crucial for determining the hyperplane and margin in SVM.
Margin: The distance between the hyperplane and the support vectors. SVM aims to maximize this margin for better classification performance.
Kernel: A function that maps data to a higher-dimensional space enabling SVM to handle non-linearly separable data.
Hard Margin: A maximum-margin hyperplane that perfectly separates the data without misclassifications.
Soft Margin: Allows some misclassifications by introducing slack variables, balancing margin maximization and misclassification penalties when data is not perfectly separable.
C: A regularization term balancing margin maximization and misclassification penalties. A higher C value forces stricter penalty for misclassifications.
Hinge Loss: A loss function penalizing misclassified points or margin violations and is combined with regularization in SVM.
Dual Problem: Involves solving for Lagrange multipliers associated with support vectors, facilitating the kernel trick and efficient computation.
How does Support Vector Machine Algorithm Work?
The key idea behind the SVM algorithm is to find the hyperplane that best separates two classes by maximizing the margin between them. This margin is the distance from the hyperplane to the nearest data points (support vectors) on each side.
"""

result = chain.invoke({'text':text})
print(result)


chain.get_graph().print_ascii()






