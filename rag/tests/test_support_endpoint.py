from unittest.mock import patch


def test_ask_with_no_relevant_articles_returns_fallback(client, db_session):
    with patch("app.rag.retrieval.embed_text", return_value=[0.0] * 384):
        response = client.post(
            "/api/v1/support/ask",
            json={"question": "What is the airspeed velocity of an unladen swallow?"},
        )
    assert response.status_code == 200
    body = response.json()
    assert body["sources"] == []
    assert "don't have information" in body["answer"].lower()


def test_ask_rejects_empty_question(client):
    response = client.post("/api/v1/support/ask", json={"question": ""})
    assert response.status_code == 422


def test_ask_with_relevant_article_returns_grounded_answer(client, db_session):
    from app.models.kb_article import KBArticle

    db_session.add(
        KBArticle(
            kb_id="KB-034",
            title="Following someone",
            applies_to="Connections",
            body="Following is one-way and instant. Press Follow on a profile.",
            related_ids=[],
            embedding=[1.0] + [0.0] * 383,
        )
    )
    db_session.commit()

    with patch("app.rag.retrieval.embed_text", return_value=[1.0] + [0.0] * 383), patch(
        "app.rag.llm_client.generate_answer", return_value="Press Follow. [KB-034]"
    ):
        response = client.post(
            "/api/v1/support/ask",
            json={"question": "How do I follow someone?"},
        )

    assert response.status_code == 200
    assert response.json()["sources"] == ["KB-034"]
