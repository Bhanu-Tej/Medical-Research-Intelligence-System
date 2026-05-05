# 🩺 Medical Research Intelligence System

An end-to-end Medical RAG (Retrieval-Augmented Generation) platform built using FastAPI, ChromaDB, Ollama, Llama 3, and Streamlit.

This system allows users to upload multiple medical research papers, perform semantic search across documents, and generate grounded AI-powered responses with source citations.

---

# 🚀 Features

✅ Multi-document PDF ingestion
✅ Semantic medical search
✅ ChromaDB persistent vector database
✅ Conversational AI memory
✅ Source-grounded AI responses
✅ Streamlit frontend UI
✅ FastAPI backend APIs
✅ Local Llama 3 inference using Ollama
✅ Retrieval-Augmented Generation (RAG) pipeline
✅ Explainable AI with source references

---

# 🏗️ System Architecture

```text
Frontend (Streamlit)
        ↓
FastAPI Backend
        ↓
Embedding Generation
        ↓
ChromaDB Vector Database
        ↓
Semantic Retrieval
        ↓
Llama3 via Ollama
        ↓
Grounded AI Response
```

---

# 🧠 How It Works

1. Users upload medical research PDFs.
2. PDFs are processed and cleaned.
3. Text is split into semantic chunks.
4. Embeddings are generated using Sentence Transformers.
5. Chunks are stored in ChromaDB.
6. User questions are converted into embeddings.
7. Relevant chunks are retrieved from vector DB.
8. Llama 3 generates grounded responses using retrieved medical context.
9. Sources are displayed for explainability.

---

# 🛠️ Tech Stack

## Backend

* FastAPI
* Python

## Vector Database

* ChromaDB

## LLM

* Ollama
* Llama 3

## Embeddings

* Sentence Transformers

## Frontend

* Streamlit

## AI Concepts

* Retrieval-Augmented Generation (RAG)
* Semantic Search
* Conversational Memory
* Vector Embeddings

---

# 📂 Project Structure

```text
Medical-Research-Intelligence-System/
│
├── backend/
├── frontend/
├── datasets/
├── README.md
└── .gitignore
```

---

# ⚙️ Installation & Setup

## Clone Repository

```bash
git clone YOUR_GITHUB_REPO_URL
```

---

## Navigate to Backend

```bash
cd backend
```

---

## Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\\Scripts\\activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🦙 Install Ollama

Download and install Ollama:

[Ollama Official Website](https://ollama.com?utm_source=chatgpt.com)

Pull Llama 3 model:

```bash
ollama pull llama3:8b
```

---

# 🚀 Run Backend

Inside backend folder:

```bash
uvicorn app.main:app --reload
```

Backend runs at:

```text
http://127.0.0.1:8000
```

Swagger Docs:

```text
http://127.0.0.1:8000/docs
```

---

# 🎨 Run Frontend

Open second terminal:

```bash
cd frontend
```

Run:

```bash
streamlit run app.py
```

Frontend runs at:

```text
http://localhost:8501
```

---

# 🧪 Example Questions

* What is Parkinson’s disease?
* Compare diabetes and hypertension.
* What are the symptoms of Alzheimer’s disease?
* Explain cancer immunotherapy.
* What treatments are discussed for hypertension?

---

# 📚 Key Concepts Demonstrated

* Retrieval-Augmented Generation (RAG)
* Vector Databases
* Embedding Pipelines
* Semantic Search
* Conversational AI
* AI Backend Engineering
* Local LLM Deployment
* Explainable AI Systems

---

# 🔥 Future Improvements

* Hybrid Search
* GraphRAG
* Authentication
* Cloud Deployment
* Medical Image Understanding
* Advanced Re-ranking
* Docker Support

---

# 👨‍💻 Author

## Bhanu Tej

Built as a hands-on Generative AI engineering project focused on real-world Medical AI system design.
