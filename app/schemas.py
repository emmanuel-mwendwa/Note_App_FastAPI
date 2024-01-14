from pydantic import BaseModel

class NoteOut(BaseModel):
    title: str
    content: str


class UserOut(BaseModel):
    email: str