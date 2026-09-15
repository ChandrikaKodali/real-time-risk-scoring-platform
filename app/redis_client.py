import os
import json
import redis


redis_client = redis.Redis(
    host=os.getenv("REDIS_HOST", "localhost"),
    port=int(os.getenv("REDIS_PORT", "6379")),
    decode_responses=True
)


def set_risk(transaction_id, risk_data):
    redis_client.set(
        transaction_id,
        json.dumps(risk_data)
    )


def get_risk(transaction_id):
    data = redis_client.get(transaction_id)

    if data:
        return json.loads(data)

    return None