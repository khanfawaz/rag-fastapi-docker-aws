# 🚀 RAG FastAPI Docker AWS

A production-grade Retrieval-Augmented Generation (RAG) system powered by **LangChain**, **ChromaDB** and **Groq**. **FastAPI** provides a clean API layer for external access. The system is containerized with **Docker** and deployable on **AWS**, offering a scalable and modular foundation for enterprise-level GenAI applications.

![GitHub last commit](https://img.shields.io/github/last-commit/khanfawaz/rag-fastapi-docker-aws)
![Python](https://img.shields.io/badge/Python-3.10+-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![LangChain](https://img.shields.io/badge/LangChain-Enabled-orange)

---

## 🔧 Project Features

* 🧠 **LLM Integration** (Groq using LLaMA3-70B)
* 🔍 **Hybrid RAG Pipeline** (ChromaDB-powered vectorstore)
* ⚡ **FastAPI API Server** (Modular, scalable, async)
* 🛆 **Dockerized** for containerized deployment
* ☁️ **AWS-ready** deployment blueprint
* 🔐 **Secure `.env`-based secret management**
* 📊 **Clean project structure** for rapid development

---

## 🧱 Project Structure

```text
rag-fastapi-docker-aws/
├── app/
│   ├── main.py               # FastAPI app with /query endpoint
│   ├── rag_pipeline.py       # Core RAG logic
│   ├── utils.py              # Text splitter, file reader, etc.
│   ├── vector_store.py       # Chroma DB setup and search
│   └── config.py             # Load env vars and API keys
│
├── data/                     # Uploaded source documents
├── chroma_db/                # Persisted vector DB
│
├── .env                      # Secret API keys (e.g., GROQ_API_KEY)
├── Dockerfile                # Build the production image
├── requirements.txt          # Python dependencies
├── docker-compose.yml        # (optional) Multi-container setup
├── AWS_KEY_PAIR.pem          # SSH key for EC2 (not checked into Git)
├── .github/workflows/        # GitHub Actions CI/CD workflows
├── README.md                 # You are here
└── .dockerignore             # Avoid copying large/unnecessary files
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
GROQ_API_KEY=groq_api_key_here
```

---

## Deployment Checklist

Task                                  Status

RAG pipeline working locally            ✅

FastAPI API implemented                 ✅

Dockerfile created                      ✅

Tested locally with Docker              ✅

Docker image pushed to DockerHub        ✅

EC2 instance running with open ports    ✅

Docker installed on EC2                 ✅

Image pulled on EC2                     ✅

.env created and mounted                ✅

RAG API accessible via public IP        ✅

---

## 🤝 Contributing

All feedback are welcome!

---

## 📞 License

This project is licensed under the MIT License. See `LICENSE` for details.
