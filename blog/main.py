from fnmatch import translate
from fastapi import Depends, FastAPI
from sqlalchemy import false, true
from . import schemas,models
from .database import SessionLocal, engine
from sqlalchemy.orm import Session


app = FastAPI()

models.Base.metadata.create_all(engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post('/blog')
def create(request : schemas.Blog, db : Session = Depends(get_db)):
    new_blog = models.Blog(title=request.title, body=request.body, translate=request.translate, author = request.author, editor = request.editor, translator = request.translator, published = request.published)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

@app.get('/blog')
def all(db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs

@app.get('/blog/{title}')
def show(title,db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).filter(models.Blog.title == title).first()
    return blogs

@app.delete('/blog/{title}')
def delete(title,db: Session = Depends(get_db)):
    db.query(models.Blog).filter(models.Blog.title == title).delete(synchronize_session='evaluate')
    db.commit()
    return "deleted"

@app.put('/blog/{title}')
def update(title,request : schemas.Blog,db: Session = Depends(get_db)):
    db.query(models.Blog).filter(models.Blog.title == title).update(request.dict())
    db.commit()
    return "updated"