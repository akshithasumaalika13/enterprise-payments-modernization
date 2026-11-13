select
  date_trunc('day', event_ts) as event_date,
  count_if(event_name='LOAN_APPLICATION_STARTED') as started,
  count_if(event_name='LOAN_APPLICATION_SUBMITTED') as submitted,
  count_if(event_name='LOAN_APPROVED') as approved,
  count_if(event_name='LOAN_ACCEPTED') as accepted
from {{ ref('stg_product_events') }}
group by 1
