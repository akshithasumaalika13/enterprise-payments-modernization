select
  experiment_id,
  variant,
  count(distinct customer_id) as users,
  count_if(event_name='PAYMENT_COMPLETED') as conversions,
  conversions / nullif(users,0) as conversion_rate
from {{ ref('stg_product_events') }}
where experiment_id is not null
group by 1,2
