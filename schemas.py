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

class BlogsBase(BaseModel):
    title: str
    category: str
    body: str
    translate: str
    published: str
    read: str

    class Config():
        orm_mode = True

class Users(BaseModel):
    name: str
    email: str
    password: str
    avatar: str = "https://media.discordapp.net/attachments/987011683245522944/1011219957402587146/Screenshot_2022-08-22_at_4.56.57_PM.png?width=726&height=671"
    admin: bool = False

class ShowUsers(BaseModel):
    name: str
    email:str
    blogs: List[BlogsBase] = []

    class Config():
        orm_mode = True

class UsersBase(BaseModel):
    name: str
    email:str

    class Config():
        orm_mode = True

class ShowBlogs(BaseModel):
    title: str
    category: str
    body: str
    translate: str
    published: str
    read: str
    author: UsersBase

    class Config():
        orm_mode = True

class Login(BaseModel):
    username: str
    password: str

class Code(BaseModel):
    code: str