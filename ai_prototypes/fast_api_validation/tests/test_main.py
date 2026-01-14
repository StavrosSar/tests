from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

#test that app starts (smoke test)
def test_root():
    r = client.get("/")
    assert r.status_code == 200
    assert r.json() == {"message": "API is running"}

#valid input test
def test_create_item_success():
    r = client.post(
        "/items/",
        #a simple comment
        json={"name": "Apple", "price": 2.5}
    )
    assert r.status_code == 200
    assert r.json()["item"]["name"] == "Apple"
    assert r.json()["item"]["price"] == 2.5

#negative price test
def test_create_item_validation_error_negative_price():
    r = client.post(
        "/items/",
        json={"name": "Apple", "price": -1}
    )
    assert r.status_code == 422

#missing price test
def test_create_item_missing_price_returns_422():
    r = client.post("/items/", json={"name": "Apple"})
    assert r.status_code == 422

#item too short test
def test_create_item_name_too_short_returns_422():
    r = client.post("/items/", json={"name": "A", "price": 1.0})
    assert r.status_code == 422
