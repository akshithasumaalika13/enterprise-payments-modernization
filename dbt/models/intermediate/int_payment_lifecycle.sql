select
  payment_id,
  customer_id,
  amount,
  currency,
  processor,
  status,
  created_at,
  settled_at,
  datediff('minute', created_at, settled_at) as settlement_minutes
from {{ ref('stg_payments') }}
