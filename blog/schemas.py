from pydantic import BaseModel
from sqlalchemy import true

class Blogs(BaseModel):
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
    photo: str

class ShowBlogs(Blogs):
    class Config():
        orm_mode = true

class Emails(BaseModel):
    email: str

class ShowEmails(Emails):
    class Config():
        orm_mode = true