from app.risk_engine import calculate_risk


def test_low_risk():
    result = calculate_risk(1000, 0, 1)
    assert result["risk_score"] == 0
    assert result["risk_level"] == "LOW"


def test_medium_risk():
    result = calculate_risk(60000, 0, 0)
    assert result["risk_score"] == 40
    assert result["risk_level"] == "MEDIUM"


def test_high_risk():
    result = calculate_risk(80000, 1, 6)
    assert result["risk_score"] == 70
    assert result["risk_level"] == "HIGH"


def test_multiple_failed_attempts():
    result = calculate_risk(1000, 3, 0)
    assert result["risk_score"] == 20
    assert result["risk_level"] == "LOW"
