from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.schemas.support import SupportRequest, SupportResponse
from app.rag.retrieval import retrieve_relevant_articles
from app.rag.llm_client import generate_answer

router = APIRouter(prefix="/support", tags=["support"])

FALLBACK_ANSWER = (
    "I'm sorry, but I couldn't find any relevant information in the FOMO knowledge base "
    "to answer your question. Please contact human support for further assistance."
)

@router.post("/ask", response_model=SupportResponse)
def ask_support(payload: SupportRequest, db: Session = Depends(get_db)):
    question = payload.question.strip()
    if not question:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Question cannot be empty.",
        )

    articles = retrieve_relevant_articles(db, question, top_k=3)

    if not articles:
        return SupportResponse(answer=FALLBACK_ANSWER, sources=[])

    sources = [a.kb_id for a in articles]
    answer = generate_answer(question, articles)

    return SupportResponse(answer=answer, sources=sources)
