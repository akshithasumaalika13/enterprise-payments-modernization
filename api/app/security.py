import os
import jwt
from fastapi import Header, HTTPException
from .models import Role

SECRET = os.getenv("JWT_SECRET", "change-me")
PERMISSIONS = {
    Role.ADMIN: {"finance", "product", "risk", "platform"},
    Role.DATA_ENGINEER: {"platform", "finance", "product", "risk"},
    Role.FINANCE_ANALYST: {"finance"},
    Role.PRODUCT_ANALYST: {"product"},
    Role.RISK_ANALYST: {"risk"},
}

def create_token(subject: str, role: Role) -> str:
    return jwt.encode({"sub": subject, "role": role.value}, SECRET, algorithm="HS256")

def require_scope(scope: str):
    def dependency(authorization: str = Header(default="")) -> dict:
        if not authorization.startswith("Bearer "):
            raise HTTPException(status_code=401, detail="Missing bearer token")
        token = authorization.split(" ", 1)[1]
        try:
            payload = jwt.decode(token, SECRET, algorithms=["HS256"])
            role = Role(payload["role"])
        except Exception as exc:
            raise HTTPException(status_code=401, detail="Invalid token") from exc
        if scope not in PERMISSIONS.get(role, set()):
            raise HTTPException(status_code=403, detail="Insufficient role")
        return payload
    return dependency
