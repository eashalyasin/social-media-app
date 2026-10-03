import os
from typing import List
from groq import Groq
from app.config import GROQ_API_KEY

# Embedding text for retrieval
try:
    from fastembed import TextEmbedding
    _embedding_model = TextEmbedding()
    def embed_text(text: str) -> List[float]:
        embeddings = list(_embedding_model.embed([text]))
        return embeddings[0].tolist()
except Exception:
    try:
        from sentence_transformers import SentenceTransformer
        _embedding_model = SentenceTransformer("all-MiniLM-L6-v2")
        def embed_text(text: str) -> List[float]:
            return _embedding_model.encode(text).tolist()
    except Exception:
        def embed_text(text: str) -> List[float]:
            import hashlib
            import random
            seed = int(hashlib.md5(text.encode()).hexdigest(), 16)
            rnd = random.Random(seed)
            return [rnd.uniform(-1, 1) for _ in range(384)]


def generate_answer(question: str, context_articles: list) -> str:
    if not GROQ_API_KEY or GROQ_API_KEY.startswith("gsk_placeholder"):
        context_str = "\n\n".join([f"[{a.kb_id}]: {a.body}" for a in context_articles])
        return f"Based on knowledge base articles ({', '.join([a.kb_id for a in context_articles])}):\n{context_str[:300]}..."

    client = Groq(api_key=GROQ_API_KEY)

    sources_text = "\n\n".join(
        [f"KB-ID: {a.kb_id}\nTitle: {a.title}\nContent: {a.body}" for a in context_articles]
    )

    prompt = f"""You are a helpful support assistant for FOMO. Answer the user's question using ONLY the provided knowledge base articles.

Knowledge Base Context:
{sources_text}

User Question: {question}

Answer concisely and accurately based on the context above."""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2,
    )

    return response.choices[0].message.content
