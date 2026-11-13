from dataclasses import dataclass
from typing import Iterable

@dataclass
class PaymentRecord:
    payment_id: str
    customer_id: str
    amount: float
    status: str
    settled_at: str | None = None

class DataQualityError(ValueError):
    pass

def validate_payment(record: PaymentRecord) -> None:
    if not record.payment_id or not record.customer_id:
        raise DataQualityError("payment_id and customer_id are required")
    if record.amount <= 0:
        raise DataQualityError("amount must be positive")
    if record.status == "SETTLED" and not record.settled_at:
        raise DataQualityError("settled payment requires settled_at")

def reconcile(source_total: float, ledger_total: float, tolerance: float = 0.01) -> bool:
    return abs(source_total - ledger_total) <= tolerance

def duplicate_ids(records: Iterable[PaymentRecord]) -> set[str]:
    seen, duplicates = set(), set()
    for record in records:
        if record.payment_id in seen:
            duplicates.add(record.payment_id)
        seen.add(record.payment_id)
    return duplicates
