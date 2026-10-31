from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok", "service": "controle-acesso-api"}

def test_create_and_list_visitor():
    payload = {"nome": "Maria Santos", "documento": "98765432100", "unidade": "Bloco B - Ap 12"}
    response = client.post("/api/v1/visitors", json=payload)
    assert response.status_code == 201
    data = response.json()
    assert data["nome"] == "Maria Santos"
    assert "id" in data

    list_res = client.get("/api/v1/visitors")
    assert list_res.status_code == 200
    assert len(list_res.json()) > 0