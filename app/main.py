from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel

from kafka_service.producer import send_transaction
from app.redis_client import get_risk


app = FastAPI(title="Real-Time Risk Scoring Platform")


class TransactionRequest(BaseModel):
    transaction_id: str
    user_id: str
    amount: float
    failed_attempts: int = 0
    transactions_last_minute: int = 0


@app.get("/")
def home():
    return {
        "message": "Risk Scoring API is running"
    }


@app.get("/login")
def login_page():
    return FileResponse("app/templates/login.html")


@app.post("/risk-score")
def send_risk_event(transaction: TransactionRequest):

    transaction_data = transaction.model_dump()

    send_transaction(transaction_data)

    return {
        "message": "Transaction sent for risk processing",
        "transaction_id": transaction.transaction_id
    }


@app.get("/risk/{transaction_id}")
def get_risk_score(transaction_id: str):

    risk = get_risk(transaction_id)

    if risk is None:
        return {
            "message": "Risk result not available yet"
        }

    return {
        "transaction_id": transaction_id,
        **risk
    }