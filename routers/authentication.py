from os import stat
from fastapi import APIRouter, Depends, Response , Request, status
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
        return "User doesn't Exist"
    if not Hash.verify(user.password,request.password):
        return "Password Error"
    refresh_token = jwttoken.create_refresh_token(data={"email": user.email, "id" : user.id})
    response.set_cookie("refresh_token", refresh_token, httponly=True, secure=True, samesite="none", max_age=604800)
    access_token = jwttoken.create_access_token(data={"sub": user.email, "id" : user.id})
    return {"status": "Success", "token": access_token}


@router.get('/refresh')
def refresh(request: Request,response : Response, db: Session = Depends(database.get_db)):
    refresh_data = request.cookies.get('refresh_token')
    if not refresh_data:
        response.status_code = status.HTTP_401_UNAUTHORIZED
        return
    verified = jwttoken.verify_refresh_token(refresh_data)
    user = db.query(models.Users).filter(models.Users.email == verified).first()
    if not user:
        return "Error"
    access_token = jwttoken.create_access_token(data={"sub": user.email, "id" : user.id})
    return {"status": "Success", "token": access_token}

