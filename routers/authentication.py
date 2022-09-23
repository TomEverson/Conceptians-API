from fastapi import APIRouter, Depends, Response , Request
from urllib3 import Retry
import schemas, database, models 
from hashing import Hash
from sqlalchemy.orm import Session
import jwttoken

router = APIRouter(
    prefix=("/login"),
    tags=["Authentication"]
)

@router.post('')
def login(response : Response,request: schemas.Login, db: Session = Depends(database.get_db)):
    user = db.query(models.Users).filter(models.Users.email == request.email).first()
    if not user:
        return "User doesn't exist"
    if not Hash.verify(user.password,request.password):
        return "Incorrect Password"
    refresh_token = jwttoken.create_refresh_token(data={"email": user.email, "id" : user.id})
    response.set_cookie("refresh_token", refresh_token)
    access_token = jwttoken.create_access_token(data={"sub": user.email, "id" : user.id})
    return {"status": "Success", "token": access_token}


@router.get('/refresh')
def refresh(request: Request,db: Session = Depends(database.get_db)):
    refresh_data = request.cookies.get('refresh_token')
    verified = jwttoken.verify_refresh_token(refresh_data)
    user = db.query(models.Users).filter(models.Users.email == verified).first()
    if not user:
        return "Error"
    access_token = jwttoken.create_access_token(data={"sub": user.email, "id" : user.id})
    return {"status": "Success", "token": access_token}

@router.post('/lol')
def login(response : Response,request: schemas.Login):
    response.set_cookie("refresh_token", "lol")