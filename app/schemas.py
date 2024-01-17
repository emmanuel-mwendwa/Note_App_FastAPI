from pydantic import BaseModel, EmailStr

from typing import Optional

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


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[str] = None

