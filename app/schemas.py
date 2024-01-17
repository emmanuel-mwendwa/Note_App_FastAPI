from pydantic import BaseModel, EmailStr

from datetime import datetime

class NoteIn(BaseModel):
    title: str
    content: str


class NoteOut(NoteIn):
    
    created_at: datetime


class UserIn(BaseModel):
    email: EmailStr
    password: str


class UserOut(BaseModel):
    email: EmailStr
    created_at: datetime

