import pytest
from pathlib import Path
from app.rag.parser import parse_kb_file

KB_PATH = Path(__file__).resolve().parent.parent / "data" / "fomo_kb.md"


def test_parses_all_84_articles():
    articles = parse_kb_file(KB_PATH)
    assert len(articles) == 84


def test_kb_ids_are_unique():
    articles = parse_kb_file(KB_PATH)
    kb_ids = [a.kb_id for a in articles]
    assert len(kb_ids) == len(set(kb_ids))


def test_first_article_content():
    articles = parse_kb_file(KB_PATH)
    first = articles[0]
    assert first.kb_id == "KB-001"
    assert first.applies_to == "Platform overview"


def test_every_article_has_applies_to_and_nonempty_body():
    articles = parse_kb_file(KB_PATH)
    for a in articles:
        assert a.applies_to != ""
        assert len(a.body) > 0


def test_missing_applies_to_raises(tmp_path):
    bad_file = tmp_path / "bad.md"
    bad_file.write_text(
        "## KB-001 — No applies-to line\n\nJust a body.\n", encoding="utf-8"
    )
    with pytest.raises(ValueError, match="Applies to"):
        parse_kb_file(bad_file)
