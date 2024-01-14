from fastapi import APIRouter, status, Depends, HTTPException

from sqlalchemy.orm import Session

from typing import List

from .. import schemas, models
from ..database import get_db


router = APIRouter(
    tags=["Users"],
    prefix="/users"
)


@router.get("/{id}", response_model=schemas.UserOut)
def get_user(id: int, db: Session = Depends(get_db)):

    user = db.query(models.User).filter(models.User.id == id).first()
    
    if not user:

        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id: {id} does not exist")

    return user