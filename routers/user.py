from typing import List
from fastapi import APIRouter, Depends
import database, models , schemas
from sqlalchemy.orm import Session
from hashing import Hash

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

get_db = database.get_db

@router.post('')
def create(request : schemas.Users, db : Session = Depends(get_db)):
    hashed = Hash.bcrypt(request.password)
    new_email = models.Users(email=request.email, name=request.name, password= hashed)
    db.add(new_email)
    db.commit()
    db.refresh(new_email)
    return new_email

@router.get('', response_model=List[schemas.ShowUsers])
def all(db: Session = Depends(get_db)):
    blogs = db.query(models.Users).all()
    return blogs