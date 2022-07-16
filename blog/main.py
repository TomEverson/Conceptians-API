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
def create(request : schemas.Blog, db : Session = Depends(get_db),):
    new_blog = models.Blog(title=request.title,category = request.category, body=request.body, translate=request.translate, author = request.author, editor = request.editor, translator = request.translator, published = request.published, read = request.read, Link = request.Link, cowriter = request.cowriter)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

@app.get('/blog', response_model =List[schemas.ShowBlog],tags=['blogs'])
def all(db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs

@app.get('/blog/{title}', response_model =schemas.ShowBlog,tags=['blogs'])
def show(title,db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).filter(models.Blog.title == title).first()
    return blogs

@app.delete('/blog/{title}',tags=['blogs'])
def delete(title,db: Session = Depends(get_db)):
    db.query(models.Blog).filter(models.Blog.title == title).delete(synchronize_session='evaluate')
    db.commit()
    return "deleted"

@app.put('/blog/{title}',tags=['blogs'])
def update(title,request : schemas.Blog,db: Session = Depends(get_db)):
    db.query(models.Blog).filter(models.Blog.title == title).update(request.dict())
    db.commit()
    return "updated"

@app.post('/user',tags=['users'])
def create_user(request: schemas.User,db: Session = Depends(get_db)):
    new_user = models.User(name=request.name, email=request.email, image=request.image)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@app.get('/user', response_model =List[schemas.ShowUser],tags=['users'])
def all(db: Session = Depends(get_db)):
    users = db.query(models.User).all()
    return users


@app.get('/user/{name}',response_model = schemas.ShowUser,tags=['users'])
def show(name,db: Session = Depends(get_db)):
    users = db.query(models.User).filter(models.User.name == name).first()
    return users

