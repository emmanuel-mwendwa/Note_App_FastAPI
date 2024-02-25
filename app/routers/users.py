from fastapi import APIRouter, status, Depends, HTTPException

from sqlalchemy.orm import Session

from typing import List

from .. import schemas, models, utils
from ..database import get_db


router = APIRouter(
    tags=["Users"],
    prefix="/users"
)


@router.post("/", response_model=schemas.UserOut)
def create_user(user: schemas.UserIn, db: Session = Depends(get_db)):

    hashed_password = utils.hash(user.password)

    user.password = hashed_password

    new_user = models.User(**user.dict())

    db.add(new_user)

    db.commit()

    db.refresh(new_user)

    return new_user


@router.get("/{id}", response_model=schemas.UserOut)
def get_user(id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):

    user = db.query(models.User).filter(models.User.id == id).first()
    
    if not user:

        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id: {id} does not exist")

    return user