import json
import os
from kafka import KafkaConsumer
from event_processor import Event, EventProcessor

processor = EventProcessor()
consumer = KafkaConsumer(
    "payment-events",
    bootstrap_servers=os.getenv("KAFKA_BOOTSTRAP_SERVERS", "localhost:29092"),
    value_deserializer=lambda b: json.loads(b.decode("utf-8")),
    group_id="payment-intelligence",
    enable_auto_commit=False,
)

for msg in consumer:
    payload = msg.value
    event = Event(
        event_id=payload["payment_id"],
        customer_id=payload["customer_id"],
        event_type=payload["status"],
        ts_epoch=0,
        amount=float(payload["amount"]),
    )
    if processor.process(event):
        consumer.commit()
