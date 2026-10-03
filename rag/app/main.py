from fastapi import FastAPI
from app.api.support import router as support_router

app = FastAPI(title="FOMO Support RAG", version="1.0.0")

app.include_router(support_router, prefix="/api/v1")


@app.get("/health")
def health():
    return {"status": "ok"}
