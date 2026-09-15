FROM secure-payment-engine-api:latest

WORKDIR /app

COPY app ./app
COPY kafka_service ./kafka_service

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]