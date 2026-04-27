from security import verify_token
from database import reset_database
from schemas import ResponseMessage
from fastapi import APIRouter, Depends

router = APIRouter(prefix="/admin", tags=["admin"])

@router.delete("/reset", response_model=ResponseMessage)
async def reset_index(user=Depends(verify_token)):
    print(user)
    if(user['role'] == 'admin'):
        await reset_database()
        return ResponseMessage(
            status_code=205,
            description="success",
            notes=None,
            status="success"
        )
    else:
        return ResponseMessage(
            status_code=403,
            description="Admin only",
            notes=None,
            status="error"
        )
