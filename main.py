from fastapi import FastAPI, Request
from pydantic import BaseModel
from groq import Groq
from dotenv import load_dotenv
import os

# Load environment
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

# Setup Groq client
client = Groq(api_key=api_key)

# FastAPI app
app = FastAPI()

from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import logging
import traceback

# Enable CORS and full logging
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Configure logging
logging.basicConfig(level=logging.DEBUG)

# Health check
@app.get("/")
def health_check():
    return {"status": "Groq FastAPI app is running ✅"}

# Request model
class QueryRequest(BaseModel):
    query: str

# Chat endpoint
@app.post("/query")
async def chat(request: QueryRequest):
    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "user", "content": request.query}
        ],
        temperature=1,
        max_completion_tokens=1024,
        top_p=1,
        stream=False,
    )
    return {"response": completion.choices[0].message.content}

# Load utility
from rag_utils import get_api_key
print(f"🔑 Using API Key: {get_api_key()[:10]}...")  # Only show partial key

# Ingest endpoint with full error reporting
from rag_utils import ingest_documents

@app.get("/ingest")
def ingest():
    try:
        result = ingest_documents()
        return {"status": "Ingestion complete ✅", "documents": result}
    except Exception as e:
        traceback_str = traceback.format_exc()
        print("🔥 Exception during ingestion:\n", traceback_str)
        return JSONResponse(
            status_code=500,
            content={"error": str(e), "trace": traceback_str}
        )
