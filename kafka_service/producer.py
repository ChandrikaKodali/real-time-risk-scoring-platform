import os
import json

from kafka import KafkaProducer


def serialize_transaction(value):
    return json.dumps(value).encode("utf-8")


def send_transaction(transaction):
    try:
        producer = KafkaProducer(
            bootstrap_servers=os.getenv(
                "KAFKA_BOOTSTRAP_SERVERS",
                "localhost:9092"
            ),
            value_serializer=serialize_transaction
        )

        producer.send("risk-events", transaction)
        producer.flush()
        producer.close()

        return True

    except Exception as e:
        print(f"Kafka unavailable: {e}")
        return False