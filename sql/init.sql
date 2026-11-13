CREATE TABLE IF NOT EXISTS customers (
    customer_id VARCHAR(32) PRIMARY KEY,
    email VARCHAR(255) NOT NULL,
    country VARCHAR(3) NOT NULL,
    created_at TIMESTAMP NOT NULL,
    risk_segment VARCHAR(16) NOT NULL
);

CREATE TABLE IF NOT EXISTS payments (
    payment_id VARCHAR(32) PRIMARY KEY,
    customer_id VARCHAR(32) REFERENCES customers(customer_id),
    amount NUMERIC(14,2) NOT NULL CHECK (amount > 0),
    currency VARCHAR(3) NOT NULL,
    payment_method VARCHAR(24) NOT NULL,
    processor VARCHAR(32) NOT NULL,
    status VARCHAR(24) NOT NULL,
    decline_reason VARCHAR(64),
    created_at TIMESTAMP NOT NULL,
    settled_at TIMESTAMP
);

CREATE TABLE IF NOT EXISTS ledger_entries (
    ledger_entry_id VARCHAR(32) PRIMARY KEY,
    payment_id VARCHAR(32) REFERENCES payments(payment_id),
    account_code VARCHAR(32) NOT NULL,
    debit NUMERIC(14,2) DEFAULT 0,
    credit NUMERIC(14,2) DEFAULT 0,
    posted_at TIMESTAMP NOT NULL
);

CREATE TABLE IF NOT EXISTS product_events (
    event_id VARCHAR(32) PRIMARY KEY,
    customer_id VARCHAR(32) REFERENCES customers(customer_id),
    session_id VARCHAR(32) NOT NULL,
    event_name VARCHAR(64) NOT NULL,
    feature VARCHAR(64),
    experiment_id VARCHAR(64),
    variant VARCHAR(16),
    event_ts TIMESTAMP NOT NULL
);
