from langchain_community.document_loaders import PyPDFLoader, UnstructuredWordDocumentLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import tempfile
import os
import streamlit as st

def load_docs(uploaded_files):
    raw_docs = []
    
    for file in uploaded_files:
        # Create temporary file with proper extension
        file_extension = file.name.split('.')[-1].lower()
        
        with tempfile.NamedTemporaryFile(delete=False, suffix=f".{file_extension}") as tmp_file:
            # Write the uploaded file content to temporary file
            tmp_file.write(file.getvalue())
            tmp_file_path = tmp_file.name
        
        try:
            # Load based on file type
            if file.type == "application/pdf" or file_extension == "pdf":
                loader = PyPDFLoader(tmp_file_path)
                docs = loader.load()
                # Add source metadata
                for doc in docs:
                    doc.metadata['source'] = file.name
                raw_docs.extend(docs)
                
            elif (file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document" 
                  or file_extension in ["docx", "doc"]):
                loader = UnstructuredWordDocumentLoader(tmp_file_path)
                docs = loader.load()
                # Add source metadata
                for doc in docs:
                    doc.metadata['source'] = file.name
                raw_docs.extend(docs)
            else:
                st.warning(f"Unsupported file type: {file.name}")
                
        except Exception as e:
            st.error(f"Error loading {file.name}: {str(e)}")
        finally:
            # Clean up temporary file
            try:
                os.unlink(tmp_file_path)
            except:
                pass  # Ignore cleanup errors
    
    if not raw_docs:
        raise ValueError("No documents were successfully loaded")
    
    # Chunk documents for embeddings
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=150,
        length_function=len,
    )
    
    chunks = splitter.split_documents(raw_docs)
    
    # Ensure each chunk has source information
    for chunk in chunks:
        if 'source' not in chunk.metadata:
            chunk.metadata['source'] = 'Unknown'
    
    return chunks
