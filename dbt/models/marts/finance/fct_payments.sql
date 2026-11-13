{{ config(materialized='incremental', unique_key='payment_id') }}
select * from {{ ref('int_payment_lifecycle') }}
{% if is_incremental() %}
where created_at > (select coalesce(max(created_at), '1900-01-01') from {{ this }})
{% endif %}
