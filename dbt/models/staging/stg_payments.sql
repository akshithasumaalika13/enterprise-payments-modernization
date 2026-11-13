select
  payment_id,
  customer_id,
  cast(amount as numeric(14,2)) as amount,
  upper(currency) as currency,
  payment_method,
  processor,
  status,
  decline_reason,
  created_at,
  settled_at
from {{ source('raw', 'payments') }}
