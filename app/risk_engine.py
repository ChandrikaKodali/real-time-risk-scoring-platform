def calculate_risk(amount, failed_attempts, transactions_last_minute):
    score = 0
    reasons = []

    # High transaction amount
    if amount > 50000:
        score += 40
        reasons.append("High transaction amount")

    # Multiple transactions in a short time
    if transactions_last_minute >= 5:
        score += 30
        reasons.append("Too many transactions in one minute")

    # Failed attempts
    if failed_attempts >= 3:
        score += 20
        reasons.append("Multiple failed attempts")

    # Keep score between 0 and 100
    score = min(score, 100)

    if score >= 70:
        level = "HIGH"
    elif score >= 40:
        level = "MEDIUM"
    else:
        level = "LOW"

    return {
        "risk_score": score,
        "risk_level": level,
        "reasons": reasons
    }