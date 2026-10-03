import pytest
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from fastapi.testclient import TestClient

from app.db.base import Base
from app.models.kb_article import KBArticle  # noqa: F401
from app.main import app
from app.db.database import get_db

TEST_DATABASE_URL = "postgresql://fomorag:fomorag_dev_password@localhost:5435/fomo_rag_test"


@pytest.fixture(scope="session", autouse=True)
def _create_test_database():
    # Connect to default database to create fomo_rag_test if missing
    admin_engine = create_engine(
        "postgresql://fomorag:fomorag_dev_password@localhost:5435/fomo_rag",
        isolation_level="AUTOCOMMIT",
    )
    with admin_engine.connect() as conn:
        exists = conn.execute(
            text("SELECT 1 FROM pg_database WHERE datname = 'fomo_rag_test'")
        ).scalar()
        if not exists:
            conn.execute(text("CREATE DATABASE fomo_rag_test"))
    admin_engine.dispose()

    test_engine = create_engine(TEST_DATABASE_URL)
    with test_engine.connect() as conn:
        conn.execute(text("CREATE EXTENSION IF NOT EXISTS vector"))
        conn.commit()
    Base.metadata.create_all(bind=test_engine)
    test_engine.dispose()
    yield


@pytest.fixture()
def db_session():
    engine = create_engine(TEST_DATABASE_URL)
    TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    session = TestingSessionLocal()
    try:
        yield session
    finally:
        session.query(KBArticle).delete()
        session.commit()
        session.close()
        engine.dispose()


@pytest.fixture()
def client(db_session):
    def _override_get_db():
        try:
            yield db_session
        finally:
            pass

    app.dependency_overrides[get_db] = _override_get_db
    with TestClient(app) as c:
        yield c
    app.dependency_overrides.clear()
