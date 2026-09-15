from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_home():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["message"] == "Risk Scoring API is running"


def test_risk_score(monkeypatch):
    def fake_send_transaction(transaction):
        return None

    monkeypatch.setattr(
        "app.main.send_transaction",
        fake_send_transaction
    )

    response = client.post(
        "/risk-score",
        json={
            "transaction_id": "TEST001",
            "user_id": "USER001",
            "amount": 1000,
            "failed_attempts": 0,
            "transactions_last_minute": 1
        }
    )

    assert response.status_code == 200
    assert response.json()["transaction_id"] == "TEST001"