select *
from {{ ref('stg_payments') }}
where status in ('DECLINED','REVERSED') or amount >= 10000
