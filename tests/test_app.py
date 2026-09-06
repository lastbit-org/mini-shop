from litestar.testing import TestClient

from app import app


def test_index() -> None:
    with TestClient(app=app) as client:
        response = client.get("/")

    assert response.status_code == 200
    assert response.text == "Hello, world! Teste"


def test_get_book() -> None:
    with TestClient(app=app) as client:
        response = client.get("/books/42")

    assert response.status_code == 200
    assert response.json() == {"book_id": 42}
