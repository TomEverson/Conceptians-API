from fastapi import APIRouter, Depends
import database, models , schemas
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/admins",
    tags=["Role"]
)

get_db = database.get_db

@router.put('/{id}')
def update(id, request : schemas.Admin,db: Session = Depends(get_db)):
    db.query(models.Users).filter(models.Users.id == id).update(request.dict())
    db.commit()
    return "updated"