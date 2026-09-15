def test_redis_risk_data(monkeypatch):
    storage = {}

    def fake_set(key, value):
        storage[key] = value

    def fake_get(key):
        return storage.get(key)

    monkeypatch.setattr("app.redis_client.redis_client.set", fake_set)
    monkeypatch.setattr("app.redis_client.redis_client.get", fake_get)

    from app.redis_client import set_risk, get_risk

    transaction_id = "TEST_REDIS_001"

    risk_data = {
        "risk_score": 70,
        "risk_level": "HIGH",
        "reasons": ["High transaction amount"]
    }

    set_risk(transaction_id, risk_data)

    result = get_risk(transaction_id)

    assert result == risk_data