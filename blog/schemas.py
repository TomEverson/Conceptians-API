from csv import writer
from unicodedata import category
from pydantic import BaseModel
from sqlalchemy import true

class Blog(BaseModel):
    title: str
    category: str
    body: str
    translate: str
    author: str
    cowriter: str
    editor: str
    translator: str
    published: str
    read: str
    Link: str

class ShowBlog(Blog):
    class Config():
        orm_mode = true

class User(BaseModel):
    name: str
    email: str
    image: str

class ShowUser(User):
    class Config():
        orm_mode = true
