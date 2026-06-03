from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

# Load dataset
loader = TextLoader("datasets/skills.txt")
documents = loader.load()

# Split documents into chunks
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=200,
    chunk_overlap=20
)

docs = text_splitter.split_documents(documents)

# Create embedding model
embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Store embeddings in ChromaDB
vector_db = Chroma.from_documents(
    documents=docs,
    embedding=embedding_model,
    persist_directory="vector_db"
)

print("Embeddings stored successfully!")