import csv
import random
from datetime import datetime, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parent
random.seed(42)

COUNTRIES = ["USA", "CAN", "GBR"]
METHODS = ["CARD", "ACH", "WALLET"]
PROCESSORS = ["GW_A", "GW_B", "GW_C"]
STATUSES = ["SETTLED", "SETTLED", "SETTLED", "DECLINED", "AUTHORIZED"]
EVENTS = ["ACCOUNT_CREATED", "LOGIN", "PAYMENT_STARTED", "PAYMENT_COMPLETED", "LOAN_APPLICATION_STARTED", "LOAN_APPLICATION_SUBMITTED", "LOAN_APPROVED", "LOAN_ACCEPTED", "FEATURE_VIEWED", "NOTIFICATION_CLICKED"]

def generate(customers=1000, payments=10000, events=20000):
    customer_ids = [f"C{i:07d}" for i in range(1, customers+1)]
    now = datetime(2026, 1, 1)
    with (ROOT/"customers.csv").open("w", newline="") as f:
        w=csv.writer(f); w.writerow(["customer_id","email","country","created_at","risk_segment"])
        for cid in customer_ids:
            w.writerow([cid, f"{cid.lower()}@example.com", random.choice(COUNTRIES), now.isoformat(), random.choice(["LOW","MEDIUM","HIGH"])])
    with (ROOT/"payments.csv").open("w", newline="") as f:
        w=csv.writer(f); w.writerow(["payment_id","customer_id","amount","currency","payment_method","processor","status","decline_reason","created_at","settled_at"])
        for i in range(1,payments+1):
            created = now + timedelta(minutes=random.randint(0, 60*24*30))
            status = random.choice(STATUSES)
            settled = created + timedelta(minutes=random.randint(1,120)) if status=="SETTLED" else ""
            reason = random.choice(["ISSUER_DECLINE","INSUFFICIENT_FUNDS","NETWORK_ERROR",""]) if status=="DECLINED" else ""
            w.writerow([f"P{i:08d}", random.choice(customer_ids), round(random.uniform(5,5000),2), "USD", random.choice(METHODS), random.choice(PROCESSORS), status, reason, created.isoformat(), settled.isoformat() if settled else ""])
    with (ROOT/"product_events.csv").open("w", newline="") as f:
        w=csv.writer(f); w.writerow(["event_id","customer_id","session_id","event_name","feature","experiment_id","variant","event_ts"])
        for i in range(1,events+1):
            event = random.choice(EVENTS)
            exp = "EXP_PAYMENT_REMINDER" if random.random()<0.35 else ""
            variant = random.choice(["CONTROL","TREATMENT"]) if exp else ""
            w.writerow([f"E{i:09d}", random.choice(customer_ids), f"S{random.randint(1,6000):07d}", event, random.choice(["AUTO_PAY","CREDIT_INSIGHTS","BUDGETING",""]), exp, variant, (now+timedelta(minutes=random.randint(0,60*24*30))).isoformat()])

if __name__ == "__main__":
    generate()
    print("Synthetic fintech datasets generated")
