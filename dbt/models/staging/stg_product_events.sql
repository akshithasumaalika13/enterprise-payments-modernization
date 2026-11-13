select
  event_id, customer_id, session_id, upper(event_name) as event_name,
  feature, experiment_id, variant, event_ts
from {{ source('raw', 'product_events') }}
