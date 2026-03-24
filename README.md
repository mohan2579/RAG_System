# 📚 RAG System (Retrieval-Augmented Generation)

This project implements a basic **Retrieval-Augmented Generation (RAG)** pipeline using LangChain, ChromaDB, and Ollama.

It allows users to:

* Index documents
* Perform semantic search
* Generate answers using retrieved context

---

## 🚀 Features

* Document loading and chunking
* Embedding generation using Ollama
* Vector storage using ChromaDB
* Semantic similarity search
* Context-aware answer generation using LLM (phi3)

---

## 📂 Project Structure

```
.
├── data/
│   └── college_notes.txt
├── chroma_db/              # Generated after indexing
├── index1.py               # Creates vector database
├── query.py                # Query + retrieval + generation
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```
git clone <your-repo-url>
cd <your-project-folder>
```

---

### 2. Create Virtual Environment (Recommended)

```
python -m venv venv
```

Activate it:

**Windows:**

```
venv\Scripts\activate
```

**Mac/Linux:**

```
source venv/bin/activate
```

---

### 3. Install Dependencies

```
pip install -r requirements.txt
```

---

### 4. Install and Run Ollama

Download Ollama from:
👉 https://ollama.com

Pull required models:

```
ollama pull phi3
ollama pull nomic-embed-text
```

---

## 📊 Step 1: Index the Documents

Run:

```
python index1.py
```

### What it does:

* Loads `college_notes.txt`
* Splits into chunks
* Converts to embeddings
* Stores in ChromaDB (`./chroma_db`)

---

## 🔍 Step 2: Query the System

Run:

```
python query.py
```

Then enter a question like:

```
What is cosine similarity?
```

---

## 🧠 How It Works

### Indexing Phase (`index1.py`)

1. Load document
2. Split into chunks
3. Generate embeddings
4. Store in vector database

### Query Phase (`query.py`)

1. Take user input
2. Convert query into embedding
3. Retrieve top relevant chunks
4. Pass context to LLM (phi3)
5. Generate final answer

---

## ⚠️ Limitations

* Uses only dense retrieval (semantic search)
* No ranking optimization
* No hybrid search (keyword + semantic)
* Depends on quality of input documents

---

## 🔮 Future Improvements

* Add Hybrid Search (BM25 + embeddings)
* Add reranking
* Add metadata filtering
* Build UI (Streamlit / React)
* Support multiple documents

---

## 📦 Dependencies

* LangChain
* ChromaDB
* Ollama
* Python

---

## 🧑‍💻 Author

Your Name

---

## 📌 Note

This project is for learning purposes and demonstrates the core concepts of RAG systems:

* Embeddings
* Vector databases
* Retrieval
* Context-based generation
