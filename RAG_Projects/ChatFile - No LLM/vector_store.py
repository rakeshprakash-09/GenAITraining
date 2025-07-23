from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings

# Use local embeddings instead of OpenAI
EMBEDDER = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

def build_faiss_index(chunks):
    """Build FAISS index from document chunks"""
    return FAISS.from_documents(chunks, EMBEDDER)

def get_retriever(index, k=5, search_type="similarity"):
    """Convert FAISS index to retriever"""
    return index.as_retriever(
        search_kwargs={
            "k": k,
            "search_type": search_type
        }
    )
