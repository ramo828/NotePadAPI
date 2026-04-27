from jose import jwt, JWTError
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi import Depends, HTTPException

SECRET_KEY = "productive-key"
ALGORITHM = "HS256"

security = HTTPBearer()

def verify_token(verify:HTTPAuthorizationCredentials = Depends(security)):
    token = verify.credentials
    try:
        payload = jwt.decode(token, key=SECRET_KEY, algorithms=ALGORITHM)
        return payload
    except JWTError:
        raise HTTPException(
            status_code=403,
            detail="Auth Error"
        )