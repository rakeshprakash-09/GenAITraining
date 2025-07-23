import streamlit as st
from loader import load_docs
from vector_store import build_faiss_index, get_retriever

st.set_page_config(
    page_title="Document Search & Retrieval",
    page_icon="📄",
    layout="wide"
)

# Initialize session state
if "retriever" not in st.session_state:
    st.session_state.retriever = None
if "document_count" not in st.session_state:
    st.session_state.document_count = 0

st.title("📄 Document Search & Retrieval")
st.write("Upload PDF or Word documents and search through their content using semantic similarity.")

# Sidebar for file upload
st.sidebar.header("📁 Upload Documents")
uploaded_files = st.sidebar.file_uploader(
    "Choose PDF or DOCX files",
    type=["pdf", "docx"],
    accept_multiple_files=True,
    help="Upload one or more PDF or Word documents to search through"
)

# Processing controls
col1, col2 = st.sidebar.columns(2)
search_k = col1.slider("Results to show", 1, 10, 5)
search_type = col2.selectbox("Search type", ["similarity", "mmr"])

if st.sidebar.button("🔄 Process Documents", type="primary") and uploaded_files:
    with st.spinner("Processing documents..."):
        try:
            # Load and chunk documents
            progress_bar = st.progress(0)
            progress_bar.progress(25, "Loading documents...")
            
            docs = load_docs(uploaded_files)
            st.session_state.document_count = len(docs)
            
            progress_bar.progress(50, "Creating embeddings...")
            
            # Build FAISS index
            index = build_faiss_index(docs)
            
            progress_bar.progress(75, "Setting up retriever...")
            
            # Create retriever
            st.session_state.retriever = get_retriever(
                index, 
                k=search_k, 
                search_type=search_type
            )
            
            progress_bar.progress(100, "Complete!")
            progress_bar.empty()
            
            st.sidebar.success(f"✅ Processed {len(uploaded_files)} files into {st.session_state.document_count} chunks")
            
        except Exception as e:
            st.sidebar.error(f"❌ Error processing documents: {str(e)}")

# Main search interface
if st.session_state.retriever is not None:
    st.success(f"📚 Ready to search through {st.session_state.document_count} document chunks")
    
    # Search input
    query = st.text_input(
        "🔍 Enter your search query:",
        placeholder="e.g., What are the main findings in the document?",
        help="Enter keywords or questions to search through your documents"
    )
    
    if query:
        with st.spinner("Searching documents..."):
            try:
                # Use retriever to get relevant documents
                retrieved_docs = st.session_state.retriever.invoke(query)
                
                if retrieved_docs:
                    st.write(f"**Found {len(retrieved_docs)} relevant sections:**")
                    
                    # Display results in expandable sections
                    for i, doc in enumerate(retrieved_docs, 1):
                        with st.expander(f"📖 Result {i} - {doc.metadata.get('source', 'Unknown source')}", expanded=(i==1)):
                            st.write("**Content:**")
                            st.write(doc.page_content)
                            
                            # Show metadata if available
                            if doc.metadata:
                                st.write("**Metadata:**")
                                for key, value in doc.metadata.items():
                                    if key != 'source':  # Already shown in title
                                        st.write(f"- **{key}:** {value}")
                            
                            # Add a separator
                            if i < len(retrieved_docs):
                                st.divider()
                else:
                    st.warning("🔍 No relevant sections found for your query. Try rephrasing or using different keywords.")
                    
            except Exception as e:
                st.error(f"❌ Error during search: {str(e)}")
    
    # Show search tips
    with st.expander("💡 Search Tips"):
        st.write("""
        - **Be specific**: Use specific terms related to your document content
        - **Try synonyms**: If you don't find results, try alternative words
        - **Use questions**: Natural language questions often work well
        - **Adjust results**: Use the sidebar slider to see more or fewer results
        - **Try MMR search**: For more diverse results, select 'mmr' in search type
        """)
        
else:
    st.info("👆 Please upload documents using the sidebar to get started")
    
    # Show example without documents
    st.write("### How it works:")
    st.write("""
    1. **Upload** PDF or Word documents using the sidebar
    2. **Process** the documents to create a searchable index
    3. **Search** through the content using natural language queries
    4. **View** relevant sections from your documents
    """)
