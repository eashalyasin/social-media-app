from sqlalchemy.orm import Session
from app.models.kb_article import KBArticle
from app.rag.llm_client import embed_text
from app.config import RAG_TOP_K, RAG_MIN_SIMILARITY


def retrieve_relevant_articles(db: Session, question: str) -> list[KBArticle]:
    """Returns up to RAG_TOP_K articles above the similarity threshold, most relevant first.
    Returns an empty list if nothing clears the threshold — callers must handle that
    case explicitly rather than assuming at least one result."""
    query_vector = embed_text(question)

    # pgvector's cosine_distance is 0 (identical) to 2 (opposite); similarity = 1 - distance.
    results = (
        db.query(KBArticle, KBArticle.embedding.cosine_distance(query_vector).label("distance"))
        .order_by("distance")
        .limit(RAG_TOP_K)
        .all()
    )

    return [
        article for article, distance in results
        if (1 - distance) >= RAG_MIN_SIMILARITY
    ]
