from typing import List, Optional
from fastapi import APIRouter, Depends
import database, models , schemas
from sqlalchemy.orm import Session
from hashing import Hash
import Oauth2

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

get_db = database.get_db

@router.post('')
def create(request : schemas.Users, db : Session = Depends(get_db)):
    hashed = Hash.bcrypt(request.password)
    new_email = models.Users(email=request.email, name=request.name, password= hashed, avatar = request.avatar)
    db.add(new_email)
    db.commit()
    db.refresh(new_email)
    return new_email

@router.get('')
def all(db: Session = Depends(get_db)):
    users = db.query(models.Users).all()
    return users

@router.get('/info',response_model=schemas.ShowUsers)
def show(db: Session = Depends(get_db),current_user: schemas.Users = Depends(Oauth2.get_current_user)):
    user = db.query(models.Users).filter(models.Users.id == current_user).first()
    return user

@router.get('/{id}',response_model=schemas.UserInfo)
def show(id,db: Session = Depends(get_db)):
    user = db.query(models.Users).filter(models.Users.id == id).first()
    return user