"""change embedding column to vector(384) for local embeddings

Revision ID: 97b051b4e060
Revises: 02bdddb25551
Create Date: 2026-08-13 13:49:27.318217

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '97b051b4e060'
down_revision: Union[str, None] = '02bdddb25551'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql
from pgvector.sqlalchemy import Vector  # <--- ADD THIS IMPORT

# LEAVE revision AND down_revision UNTOUCHED!
# revision: str = '...'
# down_revision: Union[str, None] = '...'


def upgrade() -> None:
    op.drop_table("kb_articles")
    op.create_table(
        "kb_articles",
        sa.Column("id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("kb_id", sa.String(length=16), nullable=False),
        sa.Column("title", sa.String(length=500), nullable=False),
        sa.Column("applies_to", sa.String(length=500), nullable=False),
        sa.Column("body", sa.Text(), nullable=False),
        sa.Column("related_ids", postgresql.ARRAY(sa.String(length=16)), nullable=False),
        sa.Column("embedding", Vector(384), nullable=True),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("updated_at", sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("kb_id"),
    )
    op.create_index(op.f("ix_kb_articles_kb_id"), "kb_articles", ["kb_id"], unique=True)


def downgrade() -> None:
    op.drop_index(op.f("ix_kb_articles_kb_id"), table_name="kb_articles")
    op.drop_table("kb_articles")