from pydantic import BaseModel

class NoteOut(BaseModel):
    title: str
    content: str