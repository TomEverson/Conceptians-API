from pydantic import BaseModel
from typing import List, Optional

class Blogs(BaseModel):
    title: str
    category: str
    body: str
    translate: str
    published: str
    read: str
    user_id: int

    class Config():
        orm_mode = True

class Users(BaseModel):
    name: str
    email: str
    password: str
    admin: bool = False

class ShowUsers(BaseModel):
    name: str
    email:str
    blogs: List[Blogs] = []

    class Config():
        orm_mode = True

class ShowBlogs(BaseModel):
    title: str
    category: str
    body: str
    translate: str
    published: str
    read: str
    author: ShowUsers

    class Config():
        orm_mode = True

class Login(BaseModel):
    username: str
    password: str

class Code(BaseModel):
    code: str