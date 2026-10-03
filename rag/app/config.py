import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://fomorag:fomorag_dev_password@localhost:5435/fomo_rag",
)

# Optional API key for securing support endpoints
SUPPORT_API_KEY = os.getenv("SUPPORT_API_KEY", "")

# RAG / support assistant — 100% free stack, no credit card required anywhere
GROQ_API_KEY = os.getenv("GROQ_API_KEY", "")

# Local embedding model, runs on your own CPU via sentence-transformers. Free, no API key.
RAG_EMBEDDING_MODEL = os.getenv("RAG_EMBEDDING_MODEL", "all-MiniLM-L6-v2")
RAG_EMBEDDING_DIM = 384  # all-MiniLM-L6-v2 produces 384-dimensional vectors

# Groq generation model — free tier, no credit card. OpenAI-compatible API.
RAG_GENERATION_MODEL = os.getenv("RAG_GENERATION_MODEL", "llama-3.3-70b-versatile")

RAG_TOP_K = int(os.getenv("RAG_TOP_K", "5"))
RAG_MIN_SIMILARITY = float(os.getenv("RAG_MIN_SIMILARITY", "0.3"))

# Frontend origin allowed to call this API. "*" is fine for local development.
CORS_ALLOWED_ORIGINS = os.getenv("CORS_ALLOWED_ORIGINS", "*")
