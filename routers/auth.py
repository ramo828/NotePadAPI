from fastapi import APIRouter, Depends
from datetime import datetime, timedelta
from security import SECRET_KEY, ALGORITHM
from jose import jwt

router = APIRouter(prefix="/auth", tags=["auth"])


@router.get("/login")
async def login():
    payload = {
        "user_id":1,
        "role":"admin",
        "exp":datetime.now()+timedelta(minutes=60)
    }
    token = jwt.encode(payload, key=SECRET_KEY, algorithm=ALGORITHM)
    return {
        "key_type":"Bearer",
        "key":token
    }