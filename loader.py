# loader.py
#import PyPDF2
import pypdf as PyPDF2
from langchain.docstore.document import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter

def load_and_split(pdf_path):
    # 1) Read all pages into one big string
    text = ""
    with open(pdf_path, "rb") as f:
        reader = PyPDF2.PdfReader(f)
        for page in reader.pages:
            text += page.extract_text() or ""
    # 2) Wrap in a single Document
    docs = [Document(page_content=text, metadata={})]
    # 3) Split into chunks as before
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
    return splitter.split_documents(docs)
