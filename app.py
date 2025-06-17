import streamlit as st
from loader import load_and_split
from indexer import build_faiss_index
from llm import load_llm
from qa_chain import make_qa_chain
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings

st.set_page_config(page_title="AskMyDocs", layout="wide")

st.markdown("""
    <h1 style='text-align: center;'>📄 AskMyDocs</h1>
    <p style='text-align: center; font-size:18px;'>Chat with your PDF documents. Upload. Ask. Understand.</p>
""", unsafe_allow_html=True)

st.sidebar.title("🛠️ How to use AskMyDocs")
st.sidebar.markdown("""
1. Upload a PDF file.
2. Ask a question about its content.
3. Get instant answers.

ℹ️ Works offline, no internet required!
""")

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    uploaded = st.file_uploader("Upload a PDF", type="pdf")

if uploaded:
    with open("temp.pdf", "wb") as f:
        f.write(uploaded.read())

    chunks = load_and_split("temp.pdf")

    if not chunks:
        st.error(
            "⚠️ No text could be extracted from that PDF. "
            "Please upload a document containing selectable text."
        )
        st.stop()

    try:
        embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
        vectorstore = FAISS.load_local("faiss_index", embeddings)
    except Exception:
        vectorstore = build_faiss_index(chunks)

    llm = load_llm()
    qa = make_qa_chain(vectorstore, llm)

    query = st.text_input("Ask a question:")
    if query:
        with st.spinner("🤖 Analyzing your document..."):
            if "how many lines" in query.lower():
                all_text = " ".join([chunk.page_content for chunk in chunks])
                line_count = len(all_text.strip().splitlines())
                answer = f"The document contains approximately {line_count} lines."
            else:
                answer = qa.run(query)

        st.markdown("#### ✅ Answer:", unsafe_allow_html=True)
        st.markdown(f"""
        <div style='background-color:#2b2b2b;padding:10px;border-radius:8px;color:#eee;'>
            {answer}
        </div>
        """, unsafe_allow_html=True)

