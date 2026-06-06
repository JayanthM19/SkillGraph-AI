from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vector_db = Chroma(
    persist_directory="vector_db",
    embedding_function=embedding_model
)

def search_documents(query: str, k: int = 3):
    results = vector_db.similarity_search(query, k=k)

    return [
        {
            "content": result.page_content
        }
        for result in results
    ]