"""Run manually whenever fomo_kb.md changes:
    python -m app.rag.ingest
Idempotent: re-running upserts by kb_id rather than duplicating rows."""

from pathlib import Path
from app.db.database import SessionLocal
from app.models.kb_article import KBArticle
from app.rag.parser import parse_kb_file
from app.rag.llm_client import embed_texts

KB_FILE = Path(__file__).parent / "data" / "fomo_kb.md"
BATCH_SIZE = 20  # keeps each embedding request well under API payload limits


def run():
    articles = parse_kb_file(KB_FILE)
    print(f"Parsed {len(articles)} articles from {KB_FILE.name}")

    db = SessionLocal()
    try:
        for i in range(0, len(articles), BATCH_SIZE):
            batch = articles[i : i + BATCH_SIZE]
            # Embed title + applies_to + body together — richer signal for retrieval
            # than the body alone, since many questions echo the title's phrasing.
            texts = [f"{a.title}\n{a.applies_to}\n{a.body}" for a in batch]
            vectors = embed_texts(texts)

            for article, vector in zip(batch, vectors):
                existing = db.query(KBArticle).filter_by(kb_id=article.kb_id).first()
                if existing:
                    existing.title = article.title
                    existing.applies_to = article.applies_to
                    existing.body = article.body
                    existing.related_ids = article.related_ids
                    existing.embedding = vector
                else:
                    db.add(
                        KBArticle(
                            kb_id=article.kb_id,
                            title=article.title,
                            applies_to=article.applies_to,
                            body=article.body,
                            related_ids=article.related_ids,
                            embedding=vector,
                        )
                    )
            db.commit()
            print(f"  embedded {min(i + BATCH_SIZE, len(articles))}/{len(articles)}")
    finally:
        db.close()

    print("Done.")


if __name__ == "__main__":
    run()
