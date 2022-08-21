from fastapi import APIRouter, Depends
import schemas, database, models 
from hashing import Hash
from sqlalchemy.orm import Session
import jwttoken

router = APIRouter(
    tags=["Authentication"]
)



@router.post('/login')
def login(request: schemas.Login, db: Session = Depends(database.get_db)):
    user = db.query(models.Users).filter(models.Users.email == request.username).first()
    if not user:
        return "User doesn't exist"
    if not Hash.verify(user.password,request.password):
        return "Incorrect Password"
    access_token = jwttoken.create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}