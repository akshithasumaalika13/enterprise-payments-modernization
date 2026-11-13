from checks import PaymentRecord, validate_payment, reconcile

sample = PaymentRecord("P100", "C10", 125.0, "SETTLED", "2026-01-01T10:00:00")
validate_payment(sample)
assert reconcile(1000.0, 1000.0)
print("Data-quality controls passed")
