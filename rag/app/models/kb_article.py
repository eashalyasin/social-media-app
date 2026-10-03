import uuid
from datetime import datetime
from sqlalchemy import Column, String, Text, DateTime, ARRAY
from sqlalchemy.dialects.postgresql import UUID
from pgvector.sqlalchemy import Vector

from app.db.base import Base
from app.config import RAG_EMBEDDING_DIM


class KBArticle(Base):
    __tablename__ = "kb_articles"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, nullable=False)

    # e.g. "KB-001" — stable identifier from the source document, never regenerated
    kb_id = Column(String(16), unique=True, nullable=False, index=True)

    title = Column(String(500), nullable=False)
    applies_to = Column(String(500), nullable=False)
    body = Column(Text, nullable=False)
    related_ids = Column(ARRAY(String(16)), nullable=False, default=list)

    embedding = Column(Vector(RAG_EMBEDDING_DIM), nullable=True)

    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

    def __repr__(self):
        return f"<KBArticle(kb_id={self.kb_id}, title={self.title!r})>"
