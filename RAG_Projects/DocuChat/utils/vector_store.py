from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
import os

class VectorStoreManager:
    def __init__(self):
        self.embeddings = OpenAIEmbeddings()
    
    def create_vector_store(self, documents):
        """Create FAISS vector store from documents"""
        try:
            vector_store = FAISS.from_documents(
                documents=documents,
                embedding=self.embeddings
            )
            return vector_store
        except Exception as e:
            raise Exception(f"Error creating vector store: {str(e)}")
    
    def similarity_search(self, vector_store, query, k=3):
        """Perform similarity search on vector store"""
        try:
            relevant_docs = vector_store.similarity_search(query, k=k)
            return relevant_docs
        except Exception as e:
            raise Exception(f"Error performing similarity search: {str(e)}")
    
    def save_vector_store(self, vector_store, path):
        """Save vector store to local disk"""
        try:
            vector_store.save_local(path)
        except Exception as e:
            raise Exception(f"Error saving vector store: {str(e)}")
    
    def load_vector_store(self, path):
        """Load vector store from local disk"""
        try:
            vector_store = FAISS.load_local(path, self.embeddings)
            return vector_store
        except Exception as e:
            raise Exception(f"Error loading vector store: {str(e)}")
