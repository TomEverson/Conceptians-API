from fastapi import APIRouter, Depends
import Oauth2
import database, models , schemas
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/avatars",
    tags=["Avatars"]
)

get_db = database.get_db

@router.put('/{id}')
def update(id, request : schemas.Avatar,db: Session = Depends(get_db)):
    db.query(models.Users).filter(models.Users.id == id).update(request.dict())
    db.commit()
    return "updated"