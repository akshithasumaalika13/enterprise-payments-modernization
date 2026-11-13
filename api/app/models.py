from enum import Enum
from typing import Optional
from pydantic import BaseModel, Field

class Role(str, Enum):
    ADMIN = "ADMIN"
    DATA_ENGINEER = "DATA_ENGINEER"
    FINANCE_ANALYST = "FINANCE_ANALYST"
    PRODUCT_ANALYST = "PRODUCT_ANALYST"
    RISK_ANALYST = "RISK_ANALYST"

class ProductEvent(BaseModel):
    event_id: str
    customer_id: str
    session_id: str
    event_name: str
    feature: Optional[str] = None
    experiment_id: Optional[str] = None
    variant: Optional[str] = None
    event_ts: str

class PaymentEvent(BaseModel):
    payment_id: str
    customer_id: str
    amount: float = Field(gt=0)
    currency: str = Field(min_length=3, max_length=3)
    payment_method: str
    processor: str
    status: str
    decline_reason: Optional[str] = None
    created_at: str
    settled_at: Optional[str] = None
