import os
import json

from kafka import KafkaConsumer

from app.risk_engine import calculate_risk
from app.database import SessionLocal, Base, engine
from app.models import Transaction
from app.redis_client import set_risk


Base.metadata.create_all(bind=engine)


consumer = KafkaConsumer(
    "risk-events",
    bootstrap_servers=os.getenv(
        "KAFKA_BOOTSTRAP_SERVERS",
        "localhost:9092"
    ),
    group_id="risk-service",
    auto_offset_reset="earliest",
    value_deserializer=lambda value: json.loads(
        value.decode("utf-8")
    )
)


print("Kafka consumer started...")


for message in consumer:
    transaction = message.value

    result = calculate_risk(
        transaction["amount"],
        transaction["failed_attempts"],
        transaction["transactions_last_minute"]
    )

    db = SessionLocal()

    db_transaction = Transaction(
        user_id=transaction["user_id"],
        amount=transaction["amount"],
        failed_attempts=transaction["failed_attempts"],
        transactions_last_minute=transaction["transactions_last_minute"],
        risk_score=result["risk_score"],
        risk_level=result["risk_level"],
        reasons=", ".join(result["reasons"])
    )

    db.add(db_transaction)
    db.commit()

    set_risk(
        transaction["transaction_id"],
        {
            "risk_score": result["risk_score"],
            "risk_level": result["risk_level"],
            "reasons": result["reasons"]
        }
    )

    db.close()

    print(
        f"Processed transaction: "
        f"{transaction['transaction_id']} "
        f"Risk: {result['risk_level']}"
    )