from unicodedata import category
from fastapi import Depends, FastAPI
from . import schemas,models
from .database import SessionLocal, engine
from sqlalchemy.orm import Session
from typing import List, Optional
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

models.Base.metadata.create_all(engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post('/blog',tags=['blogs'])
def create(request : schemas.Blogs, db : Session = Depends(get_db),):
    new_mail = models.Blogs(title=request.title,category = request.category, body=request.body, translate=request.translate, author = request.author, editor = request.editor, translator = request.translator, published = request.published, read = request.read, photo = request.photo, cowriter = request.cowriter)
    db.add(new_mail)
    db.commit()
    db.refresh(new_mail)
    return new_mail

@app.get('/blog', tags=['blogs'])
def all(db: Session = Depends(get_db)):
    blogs = db.query(models.Blogs).all()
    return blogs

@app.get('/blog/',tags=['blogs'])
def all( category: Optional[str] = None,db: Session = Depends(get_db)):
    blogs = db.query(models.Blogs).all()
    if not category:
        return blogs
    results = db.query(models.Blogs).filter(models.Blogs.category == category).all()
    return results

@app.get('/blog/{title}',tags=['blogs'])
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

@app.post('/email',tags=['emails'])
def create(request : schemas.Emails, db : Session = Depends(get_db)):
    new_email = models.Emails(email=request.email)
    db.add(new_email)
    db.commit()
    db.refresh(new_email)
    return new_email

@app.get('/email',tags=['emails'])
def all(db: Session = Depends(get_db)):
    blogs = db.query(models.Emails).all()
    return blogs