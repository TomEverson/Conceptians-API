import re
from tokenize import Token
from fastapi import APIRouter, Depends, Response
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy import true
import schemas, database, models 
from hashing import Hash
from sqlalchemy.orm import Session
import jwttoken

router = APIRouter(
    prefix=("/login"),
    tags=["Authentication"]
)

@router.post('')
def login(request: schemas.Login, db: Session = Depends(database.get_db)):
    user = db.query(models.Users).filter(models.Users.email == request.email).first()
    if not user:
        return "User doesn't exist"
    if not Hash.verify(user.password,request.password):
        return "Incorrect Password"
    access_token = jwttoken.create_access_token(data={"sub": user.email, "id" : user.id})
    return {"status": "Success", "token": access_token}