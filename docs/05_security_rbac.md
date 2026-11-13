# Security & RBAC

| Role | Finance | Product | Risk | Platform |
|---|---:|---:|---:|---:|
| ADMIN | Yes | Yes | Yes | Yes |
| DATA_ENGINEER | Yes | Yes | Yes | Yes |
| FINANCE_ANALYST | Yes | No | No | No |
| PRODUCT_ANALYST | No | Yes | No | No |
| RISK_ANALYST | No | No | Yes | No |

Security design includes JWT at the API layer, AWS IAM for infrastructure, Snowflake RBAC, secrets management, masking of sensitive fields, and audit logging.
