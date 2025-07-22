# DocuChat: LangChain Document Chatbot with FAISS

DocuChat is a Streamlit-based web application that allows you to upload your own documents (PDF, DOC, DOCX) and chat with an AI assistant that answers questions based on the content of those documents. If the documents do not contain enough information, DocuChat can also search the web to supplement its answers.

---

## Features
- **Document Upload:** Supports PDF, DOC, and DOCX files.
- **Document Processing:** Extracts and chunks text from uploaded documents.
- **Vector Search:** Uses FAISS for fast similarity search over document content.
- **AI Chatbot:** Answers questions using OpenAI's GPT models via LangChain.
- **Web Search Fallback:** If document information is insufficient, the app searches the web for additional context.
- **Chat History:** Maintains a history of your conversation with sources indicated.

---

## Setup Instructions

### 1. Clone the Repository
```bash
git clone <repo-url>
cd GenAITraining/RAG_Projects/DocuChat
```

### 2. Install Dependencies
It is recommended to use a virtual environment.
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Set Up Environment Variables
Create a `.env` file in the `DocuChat` directory and add your OpenAI API key:
```
OPENAI_API_KEY=your_openai_api_key_here
```

### 4. Run the Application
```bash
streamlit run app.py
```

---

## Usage
1. Open the app in your browser (Streamlit will provide a local URL).
2. Upload one or more documents using the sidebar.
3. Click **Process Documents** to index your files.
4. Ask questions about your documents in the chat interface.
5. If the answer is not found in your documents, DocuChat will search the web for you.

---

## Technologies Used
- [Streamlit](https://streamlit.io/) - Web UI
- [LangChain](https://python.langchain.com/) - LLM orchestration
- [FAISS](https://github.com/facebookresearch/faiss) - Vector similarity search
- [OpenAI GPT](https://platform.openai.com/) - Language model
- [python-dotenv](https://pypi.org/project/python-dotenv/) - Environment variable management


## License
MIT License