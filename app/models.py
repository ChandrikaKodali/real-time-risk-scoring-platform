from sqlalchemy import Column, Integer, String, Float
from app.database import Base


class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String, nullable=False)
    amount = Column(Float, nullable=False)
    failed_attempts = Column(Integer, default=0)
    transactions_last_minute = Column(Integer, default=0)
    risk_score = Column(Integer, nullable=False)
    risk_level = Column(String, nullable=False)
    reasons = Column(String, nullable=True)