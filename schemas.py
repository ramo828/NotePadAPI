from pydantic import BaseModel, ConfigDict
from typing import List
from datetime import datetime


class AddNote(BaseModel):
    name:str
    note:str

class Note(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id:int
    name:str
    note:str
    created_at:datetime

class ResponseMessage(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    status:str
    status_code:int
    description:str
    notes:List[Note] | None





