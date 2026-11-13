import pytest
from data_quality.checks import PaymentRecord, validate_payment, reconcile, duplicate_ids, DataQualityError

def test_quality_controls():
    good = PaymentRecord("P1","C1",100,"SETTLED","2026-01-01")
    validate_payment(good)
    with pytest.raises(DataQualityError):
        validate_payment(PaymentRecord("P2","C2",-1,"DECLINED"))
    assert reconcile(100.0,100.0)
    assert duplicate_ids([good, good]) == {"P1"}
