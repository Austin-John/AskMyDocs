# AskMyDocs

**Offline PDF Q\&A Bot** built with Streamlit, LangChain, FAISS & Hugging Face Transformers.

## Features

* Upload any PDF and ask natural‑language questions about its content
* Local embeddings via sentence-transformers + FAISS for fast, private search
* Instruct‑style answers from a local LLM (e.g. Flan‑T5‑Base)
* Special handlers for “structural” queries (e.g. “how many lines?”)
* Dark‑mode‑friendly UI with simple, responsive layout

## Installation

1. **Clone the repo**

   ```bash
   git clone https://github.com/YOUR_USERNAME/askmydocs.git
   cd askmydocs
   ```

2. **Create & activate a virtual environment**

   ```bash
   python3 -m venv venv
   # macOS/Linux
   source venv/bin/activate  
   # Windows
   venv\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

## Usage

```bash
streamlit run app.py
```

* Open your browser to the URL shown (usually `http://localhost:8501`).
* Upload a PDF, type your question, and get instant answers—all offline.

## Project Structure

```
.
├── app.py
├── loader.py
├── indexer.py
├── llm.py
├── qa_chain.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Contributing

Feel free to open issues or submit pull requests for new features, bug‑fixes, or UI improvements!

## License

This project is released under the MIT License.
