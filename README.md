# Enterprise Policy Assistant (RAG System)

A production-grade Retrieval-Augmented Generation (RAG) application that enables intelligent querying across enterprise policies, employee handbooks, and compliance documents.

---

# Features

- Semantic document retrieval
- OpenAI-powered question answering
- FastAPI backend
- Streamlit frontend
- Streaming responses
- Source attribution
- Docker-ready architecture

---

# Demo App

Frontend:
https://YOUR-STREAMLIT-APP.streamlit.app

Backend API:
https://YOUR-RENDER-BACKEND.onrender.com/docs

---

# Tech Stack

- Python
- LangChain
- OpenAI
- ChromaDB / FAISS
- FastAPI
- Streamlit
- Docker

---

# Local Setup

## Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/enterprise-policy-assistant.git

cd enterprise-policy-assistant
```

## Create Virtual Environment

```bash
python3 -m venv venv

source venv/bin/activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Add Environment Variables

Create `.env`

```env
OPENAI_API_KEY=your_key_here
```

---

# Run Backend

```bash
uvicorn src.api:app --host 0.0.0.0 --port 8000
```

---

# Run Frontend

```bash
streamlit run app/streamlit_app.py
```

---

# Security Notes

- `.env` is excluded using `.gitignore`
- API keys are never committed
- Environment variables are managed securely in cloud deployment

---

# Disclaimer

This project is for educational and portfolio purposes only.
All policy documents used are publicly available.

---

# Author

Chinenye Omejieke