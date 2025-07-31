"""pytest configuration and shared fixtures."""

import os
import sys
from pathlib import Path

import pytest
from fastapi.testclient import TestClient

# Test environment setup
os.environ["DATABASE_URL"] = "sqlite+pysqlite:///:memory:"
os.environ["POSTGRES_USER"] = "test_user"
os.environ["POSTGRES_PASSWORD"] = "test_password"
os.environ["POSTGRES_HOST"] = "localhost"
os.environ["POSTGRES_DB"] = "test_db"

sys.path.append(str(Path(__file__).resolve().parent.parent))

from app.core.database import Base, engine
from app.main import app

# Import models so SQLAlchemy registers tables correctly even if unused
from app.user import models  # noqa: F401

Base.metadata.create_all(bind=engine)
# Use a module-level singleton instead of creating a new client per fixture
_client = TestClient(app)


@pytest.fixture()
def client() -> TestClient:
    """
    Provide a FastAPI test client.
    """
    return _client
