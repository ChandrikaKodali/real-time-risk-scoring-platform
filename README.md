# Real-Time Risk Scoring & Transaction Anomaly Detection Platform

A real-time financial transaction risk scoring platform built using Python, Kafka, PostgreSQL, Redis, FastAPI, Docker, Kubernetes, and Airflow.

## Project Overview

The platform receives financial transaction events and calculates a risk score based on transaction amount, failed attempts, and transaction frequency.

The system is designed using an event-driven architecture where transaction events can be processed asynchronously through Kafka.

## Architecture

Transaction
     |
     v
FastAPI
     |
     v
Kafka
     |
     v
Risk Scoring Engine
     |
     +------------+
     |            |
     v            v
PostgreSQL      Redis
     |
     v
Risk Monitoring

## Technologies Used

- Python 3.12
- FastAPI
- Apache Kafka
- PostgreSQL
- Redis
- SQLAlchemy
- Docker
- Kubernetes
- Apache Airflow
- Pytest
- REST API

## Risk Scoring Logic

The risk score is calculated using multiple transaction signals.

### High Transaction Amount

Transactions above 50,000 receive:

`+40 risk points`

### High Transaction Frequency

Five or more transactions within one minute receive:

`+30 risk points`

### Multiple Failed Attempts

Three or more failed attempts receive:

`+20 risk points`

### Risk Levels

| Risk Score | Risk Level |
|------------|------------|
| 0 - 39     | LOW        |
| 40 - 69    | MEDIUM     |
| 70 - 100   | HIGH       |

## API Endpoints

### Health Check

```http
GET /