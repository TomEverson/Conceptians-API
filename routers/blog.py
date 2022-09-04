from fastapi import APIRouter, Depends
import Oauth2
import database, models , schemas
from sqlalchemy.orm import Session
from typing import List, Optional 

router = APIRouter(
    prefix="/blog",
    tags=["Blogs"]
)

get_db = database.get_db

@router.get('')
def all(db: Session = Depends(get_db)):
    blogs = db.query(models.Blogs).all()
    return blogs

@router.post('')
def create(request : schemas.Blogs, db : Session = Depends(get_db),):
    new_mail = models.Blogs(title=request.title,category = request.category, body=request.body, translate=request.translate, published = request.published, read = request.read, user_id = request.user_id)
    db.add(new_mail)
    db.commit()
    db.refresh(new_mail)
    return new_mail

@router.get('')
def all(db: Session = Depends(get_db)):
    blogs = db.query(models.Blogs).all()
    return blogs

@router.get('')
def all( category: Optional[str] = None,db: Session = Depends(get_db)):
    blogs = db.query(models.Blogs).all()
    if not category:
        return blogs
    results = db.query(models.Blogs).filter(models.Blogs.category == category).all()
    return results

@router.get('/{title}',response_model=schemas.ShowBlogs)
def show(title,db: Session = Depends(get_db)):
    blogs = db.query(models.Blogs).filter(models.Blogs.title == title).first()
    return blogs

@router.delete('/{title}')
def delete(title,db: Session = Depends(get_db)):
    db.query(models.Blogs).filter(models.Blogs.title == title).delete(synchronize_session='evaluate')
    db.commit()
    return "deleted"

@router.put('/{title}')
def update(title,request : schemas.Blogs,db: Session = Depends(get_db)):
    db.query(models.Blogs).filter(models.Blogs.title == title).update(request.dict())
    db.commit()
    return "updated"