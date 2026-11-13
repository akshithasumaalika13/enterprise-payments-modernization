import json
import os
from fastapi import Depends, FastAPI
from kafka import KafkaProducer
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST
from starlette.responses import Response
from .models import PaymentEvent, ProductEvent, Role
from .security import require_scope, create_token

app = FastAPI(title="NorthStar Finance & Product Intelligence API", version="1.0.0")
EVENTS = Counter("northstar_events_total", "Events accepted", ["type"])


def producer():
    return KafkaProducer(
        bootstrap_servers=os.getenv("KAFKA_BOOTSTRAP_SERVERS", "localhost:29092"),
        value_serializer=lambda v: json.dumps(v).encode("utf-8"),
    )

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/token")
def token(role: Role = Role.ADMIN):
    return {"access_token": create_token("portfolio-user", role)}

@app.post("/events/product")
def ingest_product_event(event: ProductEvent):
    producer().send("product-events", event.model_dump())
    EVENTS.labels("product").inc()
    return {"accepted": True, "event_id": event.event_id}

@app.post("/events/payment")
def ingest_payment_event(event: PaymentEvent):
    producer().send("payment-events", event.model_dump())
    EVENTS.labels("payment").inc()
    return {"accepted": True, "payment_id": event.payment_id}

@app.get("/finance/reconciliation")
def reconciliation(user=Depends(require_scope("finance"))):
    return {"status": "PASS", "variance": 0.0, "currency": "USD"}

@app.get("/product/funnel")
def funnel(user=Depends(require_scope("product"))):
    return {"started": 100000, "submitted": 68000, "approved": 41000, "accepted": 31000}

@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)
