from langchain_community.document_loaders import PyPDFLoader, Docx2txtLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class DocumentProcessor:
    def __init__(self, chunk_size=1000, chunk_overlap=200):
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            length_function=len,
            separators=["\n\n", "\n", " ", ""]
        )
    
    def get_file_extension(self, file_path):
        """Safely extract file extension"""
        try:
            if not file_path or not isinstance(file_path, str):
                raise ValueError("Invalid file path provided")
            
            # Split the file path and get extension
            _, ext = os.path.splitext(file_path)
            
            # Remove the dot and convert to lowercase
            if ext and len(ext) > 1:
                return ext[1:].lower()
            else:
                raise ValueError("No file extension found")
                
        except Exception as e:
            logger.error(f"Error extracting file extension from {file_path}: {str(e)}")
            raise ValueError(f"Could not determine file type for: {file_path}")
    
    def validate_file(self, file_path):
        """Validate file exists and is readable"""
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")
        
        if not os.path.isfile(file_path):
            raise ValueError(f"Path is not a file: {file_path}")
        
        if os.path.getsize(file_path) == 0:
            raise ValueError(f"File is empty: {file_path}")
    
    def process_document(self, file_path):
        """Process a document and return split chunks"""
        try:
            logger.info(f"Processing document: {file_path}")
            
            # Validate file
            self.validate_file(file_path)
            
            # Get file extension safely
            file_extension = self.get_file_extension(file_path)
            logger.info(f"Detected file extension: {file_extension}")
            
            # Choose appropriate loader based on file extension
            if file_extension == 'pdf':
                loader = PyPDFLoader(file_path)
                logger.info("Using PyPDFLoader")
            elif file_extension in ['doc', 'docx']:
                loader = Docx2txtLoader(file_path)
                logger.info("Using Docx2txtLoader")
            else:
                supported_types = ['pdf', 'doc', 'docx']
                raise ValueError(f"Unsupported file type: {file_extension}. Supported types: {supported_types}")
            
            # Load documents
            logger.info("Loading document content...")
            documents = loader.load()
            
            if not documents:
                raise ValueError("No content could be extracted from the document")
            
            logger.info(f"Loaded {len(documents)} document(s)")
            
            # Filter out empty documents
            valid_documents = [doc for doc in documents if doc.page_content.strip()]
            
            if not valid_documents:
                raise ValueError("No valid content found in the document")
            
            logger.info(f"Found {len(valid_documents)} valid document(s) with content")
            
            # Split documents into chunks
            logger.info("Splitting documents into chunks...")
            split_docs = self.text_splitter.split_documents(valid_documents)
            
            if not split_docs:
                raise ValueError("No document chunks were created")
            
            logger.info(f"Created {len(split_docs)} document chunks")
            
            # Log some statistics
            total_chars = sum(len(doc.page_content) for doc in split_docs)
            avg_chunk_size = total_chars / len(split_docs) if split_docs else 0
            logger.info(f"Total characters: {total_chars}, Average chunk size: {avg_chunk_size:.0f}")
            
            return split_docs
            
        except Exception as e:
            logger.error(f"Error processing document {file_path}: {str(e)}")
            raise Exception(f"Error processing document: {str(e)}")
