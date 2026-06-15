from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings


embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


def create_vector_db():

    loader = TextLoader("datasets/skills.txt")

    documents = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=200,
        chunk_overlap=20
    )

    docs = text_splitter.split_documents(documents)

    vector_db = Chroma.from_documents(
        documents=docs,
        embedding=embedding_model,
        persist_directory="vector_db"
    )

    return vector_db


def load_vector_db():

    return Chroma(
        persist_directory="vector_db",
        embedding_function=embedding_model
    )


def search_documents(query):

    vector_db = load_vector_db()

    results = vector_db.similarity_search(
        query,
        k=3
    )

    return [
        doc.page_content
        for doc in results
    ]