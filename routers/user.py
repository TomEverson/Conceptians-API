from fastapi import APIRouter, Depends
import database, models , schemas
from sqlalchemy.orm import Session
from passlib.context import CryptContext

router = APIRouter(
    prefix="/email",
    tags=["Users"]
)

get_db = database.get_db
pwd_cxt = CryptContext(schemes=["bcrypt"], deprecated="auto")


@router.post('')
def create(request : schemas.Users, db : Session = Depends(get_db)):
    hashed = pwd_cxt.hash(request.password)
    new_email = models.Users(email=request.email, name=request.name, password= hashed)
    db.add(new_email)
    db.commit()
    db.refresh(new_email)
    return new_email

@router.get('')
def all(db: Session = Depends(get_db)):
    blogs = db.query(models.Users).all()
    return blogs