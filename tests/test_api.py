"""
API tests.

These tests check that the FastAPI endpoint works correctly.
"""

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health_check():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_calculate_add_endpoint():
    response = client.post(
        "/calculate",
        json={"operation": "add", "a": 2, "b": 3},
    )

    assert response.status_code == 200
    assert response.json() == {"result": 5}


def test_calculate_divide_by_zero_endpoint():
    response = client.post(
        "/calculate",
        json={"operation": "divide", "a": 10, "b": 0},
    )

    assert response.status_code == 400
    assert response.json()["detail"] == "Cannot divide by zero"
