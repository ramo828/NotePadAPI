from database import AsyncSession
from models import NotePad
from sqlalchemy import select
from schemas import AddNote

async def get_notes(db:AsyncSession, table:NotePad):
    query = await db.execute(select(table))
    notes = query.scalars().all()
    return notes

async def add_notes(db:AsyncSession, table:NotePad):
    db.add(table)
    await db.commit()

async def delete_note(db:AsyncSession, table:NotePad, id:int):
    query = await db.execute(select(table).where(table.id == id))

    await db.delete(query.scalar_one_or_none())
    await db.commit()

async def update_note(db:AsyncSession, table:NotePad, update_data:AddNote, id:int):
    query = await db.execute(select(table).where(table.id == id))
    note = query.scalar_one_or_none()
    if note:
        note.name = update_data.name
        note.note = update_data.note
    await db.commit()
