# 🚀 RAG FastAPI Docker AWS

A **production-ready** Retrieval-Augmented Generation (RAG) system built with **FastAPI**, **LangChain**, and **Groq**. This project supports seamless deployment with **Docker** and **AWS**, making it a robust foundation for enterprise-grade GenAI applications.

![GitHub last commit](https://img.shields.io/github/last-commit/khanfawaz/rag-fastapi-docker-aws)
![Python](https://img.shields.io/badge/Python-3.10+-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![LangChain](https://img.shields.io/badge/LangChain-Enabled-orange)

---

## 🔧 Features

* 🧠 **LLM Integration** (Groq using LLaMA3-70B)
* 🔍 **Hybrid RAG Pipeline** (ChromaDB-powered vectorstore)
* ⚡ **FastAPI API Server** (Modular, scalable, async)
* 🛆 **Dockerized** for containerized deployment
* ☁️ **AWS-ready** deployment blueprint
* 🔐 **Secure `.env`-based secret management**
* 📊 **Clean project structure** for rapid development

---

## 📁 Project Structure

```text
RAG FastAPI Docker AWS/
├── chroma_db/               # Vector DB directory
├── data/                    # Documents to ingest (PDF, DOCX, etc.)
├── main.py                  # FastAPI app
├── rag_utils.py             # Ingestion, chunking, embedding helpers
├── .env                     # Contains GROQ_API_KEY
├── .gitignore               # Prevents secrets and venv from being committed
├── Dockerfile               # Container specification
├── requirements.txt         # All dependencies
├── README.md                # You're reading this
└── venv/                    # Local Python environment (ignored)
```

---

## 🛆 Docker Build & Run

```bash
# 1. Build the Docker image
docker build -t groq-rag-app .

# 2. Run the container with env + volume mounts
docker run -it --rm \
  -p 8000:8000 \
  --env-file .env \
  -v "$(pwd)/data:/app/data" \
  -v "$(pwd)/chroma_db:/app/chroma_db" \
  groq-rag-app
```

> 💡 Use `^` instead of `\` for Windows PowerShell.

---

## ⚙️ How It Works

### 🔄 Ingest

`GET /ingest` — Reads all documents in `/data` and populates `ChromaDB`.

### 💬 Query

`POST /query` — Accepts a user query, retrieves relevant chunks from vectorstore, and returns Groq LLM response.

**Example JSON payload:**

```json
{
  "query": "What are AI agents?"
}
```

---

## 📄 Push to DockerHub

```bash
# 1. Login to DockerHub
docker login

# 2. Tag your image
docker tag groq-rag-app khanfawaz/groq-rag-app:latest

# 3. Push to DockerHub
docker push khanfawaz/groq-rag-app:latest
```

---

## 📥 Pull & Run (For Others)

```bash
docker pull khanfawaz/groq-rag-app:latest

docker run -it --rm \
  -p 8000:8000 \
  --env-file .env \
  -v "$(pwd)/data:/app/data" \
  -v "$(pwd)/chroma_db:/app/chroma_db" \
  khanfawaz/groq-rag-app:latest
```

---

## 🔐 .env File Example

```env
GROQ_API_KEY=your_groq_api_key_here
```

> ⚠️ **Never commit `.env` files.** Your API keys are sensitive. Always use `.gitignore`.

---

## ✅ Status

* [x] Phase 1: Groq LLM API Setup
* [x] Phase 2: FastAPI Backend
* [x] Phase 3: Document Ingestion & Chunking
* [x] Phase 4: Vector DB (Chroma)
* [x] Phase 5: Query Endpoint with RAG
* [x] Phase 6: Dockerization
* [ ] Phase 7: AWS EC2 Deployment

---

## 🤝 Contributing

PRs and feedback are welcome! Feel free to fork and build on this.

---

## 📞 License

This project is licensed under the MIT License. See `LICENSE` for details.
