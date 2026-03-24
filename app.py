import streamlit as st
import os
import time
import shutil
from langchain_groq import ChatGroq
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import PyPDFLoader
from langchain_classic.chains.combine_documents import create_stuff_documents_chain
from langchain_classic.chains import create_retrieval_chain

from dotenv import load_dotenv
load_dotenv()

# --- Page Config ---
st.set_page_config(page_title="AI Doc Insight", layout="wide")
st.title("RAG - Semantic Doc Explorer ⏱️💡📄 ")
st.markdown("---")

# --- Sidebar for Settings & Upload ---
with st.sidebar:
    st.header("Settings")
    api_key = st.text_input("Enter Groq API Key", type="password", value=os.getenv("GROQ_API_KEY"))
    
    st.divider()
    st.header("Upload Center")
    uploaded_files = st.file_uploader("Drop your PDFs here", type="pdf", accept_multiple_files=True)
    
    if st.button("🚀 Process & Embed"):
        if uploaded_files:
            with st.status("Analyzing documents...", expanded=True) as status:
                st.write("Creating temporary storage...")
                if os.path.exists("temp_pdf"):
                    shutil.rmtree("temp_pdf")
                os.makedirs("temp_pdf")

                all_docs = []
                for file in uploaded_files:
                    st.write(f"Reading {file.name}...")
                    temp_path = os.path.join("temp_pdf", file.name)
                    with open(temp_path, "wb") as f:
                        f.write(file.getbuffer())
                    loader = PyPDFLoader(temp_path)
                    all_docs.extend(loader.load())

                st.write("Splitting text into chunks...")
                text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
                final_docs = text_splitter.split_documents(all_docs)

                st.write("Generating Vector Embeddings...")
                st.session_state.embeddings = OpenAIEmbeddings()
                st.session_state.vectors = FAISS.from_documents(final_docs, st.session_state.embeddings)
                
                status.update(label="System Ready!", state="complete", expanded=False)
                st.success("Database initialized!")
        else:
            st.error("Please upload files first.")

    if st.button("🗑️ Clear Database"):
        st.session_state.pop("vectors", None)
        st.rerun()

# --- Main Chat Interface ---
if "vectors" in st.session_state:
    user_prompt = st.chat_input("Ask a question about your documents...")

    if user_prompt:
        # Display user message
        with st.chat_message("user"):
            st.markdown(user_prompt)

        # Generate response
        with st.chat_message("assistant"):
            with st.spinner("Searching documents..."):
                llm = ChatGroq(groq_api_key=api_key, model_name="llama-3.1-8b-instant")
                prompt = ChatPromptTemplate.from_template(
                    "Answer based on context only:\n<context>{context}</context>\nQuestion:{input}"
                )
                
                doc_chain = create_stuff_documents_chain(llm, prompt)
                retriever = st.session_state.vectors.as_retriever()
                retrieval_chain = create_retrieval_chain(retriever, doc_chain)
                
                start_time = time.perf_counter()
                response = retrieval_chain.invoke({'input': user_prompt})
                end_time = time.perf_counter()

                st.markdown(response['answer'])
                st.caption(f"⚡ Response generated in {end_time - start_time:.2f} seconds")

                # Interactive Citations
                with st.expander("🔍 View Source References"):
                    for i, doc in enumerate(response['context']):
                        source_name = os.path.basename(doc.metadata.get('source', 'Unknown'))
                        page_num = doc.metadata.get('page', 'N/A')
                        st.markdown(f"**Source {i+1}:** {source_name} (Page {page_num})")
                        st.info(doc.page_content)
else:
    st.info("👋 Welcome! Please upload your documents in the sidebar and click **Process** to begin.")