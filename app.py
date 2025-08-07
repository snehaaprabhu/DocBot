
import streamlit as st
from document_utils import load_and_chunk_docs
from embed_store import get_vector_store
from query_engine import answer_query

st.set_page_config(page_title="DocBot", layout="wide")
st.title("🤖 DocBot – Ask Your Docs")

uploaded_files = st.file_uploader("Upload PDF, TXT or CSV files", type=["pdf", "txt", "csv"], accept_multiple_files=True)
query = st.text_input("Ask a question about your documents:")

if uploaded_files and query:
    with st.spinner("Processing documents and fetching answer..."):
        chunks = load_and_chunk_docs(uploaded_files)
        vectordb = get_vector_store(chunks)
        response = answer_query(query, vectordb)
        st.success("Answer ready!")
        st.write(response)
