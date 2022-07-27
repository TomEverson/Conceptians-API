from pydantic import BaseModel
from sqlalchemy import true

class Blogs(BaseModel):
    title: str
    category: str
    body: str
    translate: str
    author: str
    translator: str
    published: str
    read: str
    photo: str

class Emails(BaseModel):
    email: str
