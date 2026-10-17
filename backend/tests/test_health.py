from unittest.mock import MagicMock

from fastapi.testclient import TestClient
from sqlalchemy.exc import OperationalError

from app.database import get_db
from app.main import app

client = TestClient(app)


def test_health_returns_ok_when_database_responds():
    # Troca a sessão real por uma falsa: o teste não precisa de um Postgres rodando.
    app.dependency_overrides[get_db] = lambda: MagicMock()
    try:
        response = client.get("/health")
    finally:
        app.dependency_overrides.clear()

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_health_returns_503_when_database_is_down():
    broken_db = MagicMock()
    broken_db.execute.side_effect = OperationalError("SELECT 1", {}, Exception("sem conexão"))
    app.dependency_overrides[get_db] = lambda: broken_db
    try:
        response = client.get("/health")
    finally:
        app.dependency_overrides.clear()

    assert response.status_code == 503
