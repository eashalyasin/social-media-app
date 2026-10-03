import re
from dataclasses import dataclass
from pathlib import Path


@dataclass
class ParsedArticle:
    kb_id: str
    title: str
    applies_to: str
    body: str
    related_ids: list[str]


ARTICLE_SPLIT = re.compile(r"^##\s+(KB-\d{3})\s+—\s+(.+)$", re.MULTILINE)
APPLIES_TO = re.compile(r"^Applies to:\s*(.+)$", re.MULTILINE)
RELATED = re.compile(r"^Related:\s*(.+)$", re.MULTILINE)
KB_ID_TOKEN = re.compile(r"KB-\d{3}")


def parse_kb_file(path: Path) -> list[ParsedArticle]:
    text = path.read_text(encoding="utf-8")
    matches = list(ARTICLE_SPLIT.finditer(text))
    if not matches:
        raise ValueError(f"No '## KB-XXX — Title' headings found in {path}")

    articles = []
    for i, m in enumerate(matches):
        kb_id, title = m.group(1), m.group(2).strip()
        start = m.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        section = text[start:end]

        applies_match = APPLIES_TO.search(section)
        related_match = RELATED.search(section)

        if not applies_match:
            raise ValueError(f"{kb_id} has no 'Applies to:' line")

        applies_to = applies_match.group(1).strip()
        related_ids = KB_ID_TOKEN.findall(related_match.group(1)) if related_match else []

        # Body = everything between "Applies to:" and "Related:" (or end of section)
        body_start = applies_match.end()
        body_end = related_match.start() if related_match else len(section)
        body = section[body_start:body_end].strip()

        if not body:
            raise ValueError(f"{kb_id} has an empty body")

        articles.append(
            ParsedArticle(
                kb_id=kb_id,
                title=title,
                applies_to=applies_to,
                body=body,
                related_ids=related_ids,
            )
        )

    return articles
