from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_root():
    r = client.get("/")
    assert r.status_code == 200
    assert r.json() == {"message": "API is running"}

def test_create_item_success():
    r = client.post(
        "/items/",
        json={"name": "Apple", "price": 2.5}
    )
    assert r.status_code == 200
    assert r.json()["item"]["name"] == "Apple"
    assert r.json()["item"]["price"] == 2.5

def test_create_item_validation_error():
    r = client.post(
        "/items/",
        json={"name": "A", "price": -1}
    )
    assert r.status_code == 422

def test_create_item_negative_price_fails():
    response = client.post(
        "/items/",
        json={"name": "Apple", "price": -1}
    )

    assert response.status_code == 422
