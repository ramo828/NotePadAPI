from fastapi import FastAPI, Depends
from database import run_db, init_database, reset_database, AsyncSession
from contextlib import asynccontextmanager
from schemas import ResponseMessage, AddNote
from models import NotePad
from functions import get_notes, add_notes, delete_note, update_note
from datetime import datetime, timedelta
from security import verify_token, SECRET_KEY, ALGORITHM
from jose import jwt


@asynccontextmanager
async def life_span(app:FastAPI):
    await init_database()
    yield

app = FastAPI(lifespan=life_span, title="Note API")


@app.delete("/reset", response_model=ResponseMessage)
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
@app.post("/login")
def login():
    user_data = {
        "user_id": 1,
        "role": "user",
        "exp": datetime.now() + timedelta(minutes=30)
    }

    token = jwt.encode(user_data, SECRET_KEY, algorithm=ALGORITHM)

    return {
        "access_token": token,
        "token_type": "bearer"
    }

@app.get("/", response_model=ResponseMessage)
async def get_index(db:AsyncSession = Depends(run_db)):
    notes = await get_notes(db=db, table=NotePad)
    return ResponseMessage(
        status_code=200,
        description="success",
        notes=notes,
        status="success"
    )


@app.post("/", response_model=ResponseMessage)
async def post_index(data:AddNote, db:AsyncSession = Depends(run_db)):
    note = NotePad(
        name = data.name,
        note = data.note
    )
    await add_notes(db=db, table=note)
    return ResponseMessage(
        status_code=201,
        description="success",
        notes=None,
        status="success"
    )


@app.delete("/{id}", response_model=ResponseMessage)
async def delete_index(id:int, db:AsyncSession = Depends(run_db)):
    await delete_note(db=db, table=NotePad, id=id)
    return ResponseMessage(
        status_code=202,
        description="success",
        notes=None,
        status="success"
    )

@app.put("/{id}", response_model=ResponseMessage)
async def update_index(id:int, data:AddNote, db:AsyncSession=Depends(run_db)):
    await update_note(db=db, table=NotePad, update_data=data, id=id)
    return ResponseMessage(
            status_code=203,
            description="success",
            notes=None,
            status="success"
        )

if __name__ == "__main__":
    from uvicorn import run
    run(app=app, host="0.0.0.0", port=8000)