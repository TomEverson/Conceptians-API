from asyncore import read
from email.mime import image
from unicodedata import category
from fastapi import Depends, FastAPI
from . import schemas,models
from .database import SessionLocal, engine
from sqlalchemy.orm import Session
from typing import List

app = FastAPI()

models.Base.metadata.create_all(engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post('/blog',tags=['blogs'])
def create(request : schemas.Blogs, db : Session = Depends(get_db),):
    new_blog = models.Blogs(title=request.title,category = request.category, body=request.body, translate=request.translate, author = request.author, editor = request.editor, translator = request.translator, published = request.published, read = request.read, photo = request.photo, cowriter = request.cowriter)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

@app.get('/blog', response_model =List[schemas.ShowBlogs],tags=['blogs'])
def all(db: Session = Depends(get_db)):
    blogs = db.query(models.Blogs).all()
    return blogs

@app.get('/blog/{title}', response_model =schemas.ShowBlogs,tags=['blogs'])
def show(title,db: Session = Depends(get_db)):
    blogs = db.query(models.Blogs).filter(models.Blogs.title == title).first()
    return blogs

@app.delete('/blog/{title}',tags=['blogs'])
def delete(title,db: Session = Depends(get_db)):
    db.query(models.Blogs).filter(models.Blogs.title == title).delete(synchronize_session='evaluate')
    db.commit()
    return "deleted"

@app.put('/blog/{title}',tags=['blogs'])
def update(title,request : schemas.Blogs,db: Session = Depends(get_db)):
    db.query(models.Blogs).filter(models.Blogs.title == title).update(request.dict())
    db.commit()
    return "updated"

