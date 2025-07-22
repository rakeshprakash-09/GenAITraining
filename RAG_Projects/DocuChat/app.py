import streamlit as st
import os
from dotenv import load_dotenv
from utils.document_processor import DocumentProcessor
from utils.vector_store import VectorStoreManager
from utils.web_search import WebSearchFallback
from langchain_openai import ChatOpenAI
import tempfile

# Load environment variables
load_dotenv()

# Initialize session state
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []
if 'vector_store' not in st.session_state:
    st.session_state.vector_store = None
if 'documents_loaded' not in st.session_state:
    st.session_state.documents_loaded = False

st.set_page_config(
    page_title="DocuChat",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 DocuChat")
st.markdown("Upload your documents and chat with them using AI!")

# Sidebar for document upload
with st.sidebar:
    st.header("\U0001F4C1 Document Upload")
    uploaded_files = st.file_uploader(
        "Choose PDF or DOC files",
        type=['pdf', 'doc', 'docx'],
        accept_multiple_files=True
    )
    
    if uploaded_files and st.button("Process Documents"):
        if not os.getenv('OPENAI_API_KEY'):
            st.error("❌ OpenAI API key not found. Please check your .env file.")
            st.stop()
        
        with st.spinner("Processing documents..."):
            try:
                # Initialize processors
                doc_processor = DocumentProcessor()
                vector_manager = VectorStoreManager()
                
                # Process uploaded files
                all_documents = []
                processed_files = []
                failed_files = []
                
                for uploaded_file in uploaded_files:
                    try:
                        st.write(f"Processing: {uploaded_file.name}")
                        
                        # Validate file name
                        if not uploaded_file.name or len(uploaded_file.name.strip()) == 0:
                            failed_files.append(("Unknown file", "Empty filename"))
                            continue
                        
                        # Check file size
                        if uploaded_file.size == 0:
                            failed_files.append((uploaded_file.name, "Empty file"))
                            continue
                        
                        if uploaded_file.size > 50 * 1024 * 1024:  # 50MB limit
                            failed_files.append((uploaded_file.name, "File too large (>50MB)"))
                            continue
                        
                        # Get file extension safely
                        name_parts = uploaded_file.name.split('.')
                        if len(name_parts) < 2:
                            failed_files.append((uploaded_file.name, "No file extension"))
                            continue
                        
                        file_extension = name_parts[-1].lower()
                        
                        if file_extension not in ['pdf', 'doc', 'docx']:
                            failed_files.append((uploaded_file.name, f"Unsupported file type: {file_extension}"))
                            continue
                        
                        # Create temporary file with proper extension
                        with tempfile.NamedTemporaryFile(delete=False, suffix=f".{file_extension}") as tmp_file:
                            tmp_file.write(uploaded_file.getvalue())
                            tmp_file_path = tmp_file.name
                        
                        try:
                            # Process document
                            documents = doc_processor.process_document(tmp_file_path)
                            all_documents.extend(documents)
                            processed_files.append((uploaded_file.name, len(documents)))
                            
                        finally:
                            # Always clean up temporary file
                            try:
                                os.unlink(tmp_file_path)
                            except Exception as cleanup_error:
                                st.warning(f"Could not clean up temporary file: {cleanup_error}")
                    
                    except Exception as file_error:
                        failed_files.append((uploaded_file.name, str(file_error)))
                        continue
                
                # Show processing results
                if processed_files:
                    st.success(f"✅ Successfully processed {len(processed_files)} file(s):")
                    for filename, chunk_count in processed_files:
                        st.write(f"  • {filename}: {chunk_count} chunks")
                
                if failed_files:
                    st.error(f"❌ Failed to process {len(failed_files)} file(s):")
                    for filename, error in failed_files:
                        st.write(f"  • {filename}: {error}")
                
                if all_documents:
                    # Create vector store
                    st.session_state.vector_store = vector_manager.create_vector_store(all_documents)
                    st.session_state.documents_loaded = True
                    
                    st.success(f"🎉 Created vector database with {len(all_documents)} document chunks!")
                else:
                    st.error("❌ No documents could be processed successfully.")
                
            except Exception as e:
                st.error(f"❌ Unexpected error during document processing: {str(e)}")
                import traceback
                st.code(traceback.format_exc())


# Main chat interface
if st.session_state.documents_loaded:
    st.header("💬 Chat with Your Documents")
    
    # Display chat history
    for message in st.session_state.chat_history:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
            if "source" in message:
                st.info(f"Source: {message['source']}")
    
    # Chat input
    if prompt := st.chat_input("Ask a question about your documents..."):
        # Add user message to chat history
        st.session_state.chat_history.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
        
        # Generate response
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                try:
                    # Initialize components
                    vector_manager = VectorStoreManager()
                    web_search = WebSearchFallback()
                    llm = ChatOpenAI(temperature=0.7, model="gpt-3.5-turbo")
                    
                    # Retrieve relevant documents
                    relevant_docs = vector_manager.similarity_search(
                        st.session_state.vector_store, 
                        prompt, 
                        k=3
                    )
                    
                    if relevant_docs:
                        # Create context from retrieved documents
                        context = "\n\n".join([doc.page_content for doc in relevant_docs])
                        
                        # Generate answer using retrieved context
                        response = llm.invoke(f"""
                        Based on the following context from the uploaded documents, answer the user's question.
                        If the context doesn't contain enough information to answer the question, say so clearly.
                        
                        Context: {context}
                        
                        Question: {prompt}
                        
                        Answer:
                        """)
                        
                        initial_answer = response.content
                        
                        # Check answer quality
                        quality_score = web_search.assess_answer_quality(initial_answer, prompt)
                        
                        if quality_score >= 0.7:  # Good quality threshold
                            st.markdown(initial_answer)
                            st.session_state.chat_history.append({
                                "role": "assistant", 
                                "content": initial_answer,
                                "source": "Document Database"
                            })
                        else:
                            # Fallback to web search
                            st.warning("⚠️ The answer from your documents seems incomplete. Searching the web for additional information...")
                            
                            web_answer = web_search.search_web(prompt)
                            
                            if web_answer:
                                combined_response = f"""
                                **Document-based answer:** {initial_answer}
                                
                                **Additional information from web search:**
                                {web_answer}
                                
                                ---
                                *Note: Web search was performed because the document-based answer was incomplete or of low quality.*
                                """
                                st.markdown(combined_response)
                                st.session_state.chat_history.append({
                                    "role": "assistant", 
                                    "content": combined_response,
                                    "source": "Documents + Web Search"
                                })
                            else:
                                st.markdown(initial_answer)
                                st.warning("Web search failed. Showing document-based answer only.")
                                st.session_state.chat_history.append({
                                    "role": "assistant", 
                                    "content": initial_answer,
                                    "source": "Document Database (Web search failed)"
                                })
                    
                    else:
                        # No relevant documents found, use web search
                        st.warning("No relevant information found in uploaded documents. Searching the web...")
                        web_answer = web_search.search_web(prompt)
                        
                        if web_answer:
                            response = f"""
                            I couldn't find relevant information in your uploaded documents for this question.
                            
                            **Web search result:**
                            {web_answer}
                            
                            ---
                            *Note: This answer is from web search as no relevant information was found in your documents.*
                            """
                            st.markdown(response)
                            st.session_state.chat_history.append({
                                "role": "assistant", 
                                "content": response,
                                "source": "Web Search Only"
                            })
                        else:
                            error_msg = "I couldn't find relevant information in your documents or on the web."
                            st.markdown(error_msg)
                            st.session_state.chat_history.append({
                                "role": "assistant", 
                                "content": error_msg,
                                "source": "No Results"
                            })
                
                except Exception as e:
                    st.error(f"❌ Error generating response: {str(e)}")

else:
    st.info("👆 Please upload and process documents first to start chatting!")

# Footer
st.markdown("---")
st.markdown("Built with Streamlit, LangChain, FAISS, and OpenAI")
