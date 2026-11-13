import pytest
from api.app.models import PaymentEvent

def test_payment_amount_must_be_positive():
    with pytest.raises(Exception):
        PaymentEvent(
            payment_id="P1", customer_id="C1", amount=-1,
            currency="USD", payment_method="CARD", processor="GW_A",
            status="DECLINED", created_at="2026-01-01T00:00:00"
        )
