from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

# Load embedding model
embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Load vector database
vector_db = Chroma(
    persist_directory="vector_db",
    embedding_function=embedding_model
)

# User query
query = input("Enter your query: ")

# Semantic search
results = vector_db.similarity_search(query, k=3)

print("\nTop Relevant Results:\n")

for i, result in enumerate(results, start=1):
    print(f"{i}. {result.page_content}\n")