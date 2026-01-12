from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_health():
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json() == {"status": "ok"}

def test_echo_success():
    r = client.post("/echo", json={"message": "hello"})
    assert r.status_code == 200
    assert r.json() == {"message": "hello"}

def test_echo_validation_error():
    # missing required field "message" -> 422
    r = client.post("/echo", json={})
    assert r.status_code == 422
