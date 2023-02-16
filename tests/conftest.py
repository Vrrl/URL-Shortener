import pytest

from fastapi.testclient import TestClient

from src.web.server import app


@pytest.fixture(scope="session")
def client():
    yield TestClient(app=app)
