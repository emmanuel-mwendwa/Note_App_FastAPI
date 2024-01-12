from fastapi import FastAPI

from . import models
from .database import engine
from .routers import notes

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(notes.router)


@app.get("/")
def home():
    return {"message": "Note Application Home Page"}