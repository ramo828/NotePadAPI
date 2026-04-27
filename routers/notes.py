from fastapi import APIRouter, Depends
from database import run_db, reset_database, AsyncSession
from functions import get_notes, add_notes, delete_note, update_note
from schemas import ResponseMessage, AddNote
from models import NotePad


router = APIRouter(prefix="/notes", tags=["notes"])


@router.get("/", response_model=ResponseMessage)
async def get_index(db:AsyncSession = Depends(run_db)):
    notes = await get_notes(db=db, table=NotePad)
    return ResponseMessage(
        status_code=200,
        description="success",
        notes=notes,
        status="success"
    )


@router.post("/", response_model=ResponseMessage)
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


@router.delete("/{id}", response_model=ResponseMessage)
async def delete_index(id:int, db:AsyncSession = Depends(run_db)):
    await delete_note(db=db, table=NotePad, id=id)
    return ResponseMessage(
        status_code=202,
        description="success",
        notes=None,
        status="success"
    )

@router.put("/{id}", response_model=ResponseMessage)
async def update_index(id:int, data:AddNote, db:AsyncSession=Depends(run_db)):
    await update_note(db=db, table=NotePad, update_data=data, id=id)
    return ResponseMessage(
            status_code=203,
            description="success",
            notes=None,
            status="success"
        )
