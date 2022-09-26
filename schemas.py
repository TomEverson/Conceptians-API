from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class Blogs(BaseModel):
    title: str
    category: str
    body: str
    image: str
    published: str
    read: int

    class Config():
        orm_mode = True

class BlogsBase(BaseModel):
    title: str
    category: str
    body: str
    image: str
    published: str
    read: int

    class Config():
        orm_mode = True

class Users(BaseModel):
    name: str
    email: str
    password: str
    avatar: str
    banned: bool = False

class UserInfo(BaseModel):
    name: str
    email: str
    avatar: str
    banned: bool

    class Config():
        orm_mode = True


class ShowUsers(BaseModel):
    name: str
    avatar:str
    blogs: List[BlogsBase] = []

    class Config():
        orm_mode = True

class UsersBase(BaseModel):
    name: str
    avatar: str

    class Config():
        orm_mode = True

class ShowBlogs(BaseModel):
    title: str
    category: str
    body: str
    image: str
    published: str
    read: int
    author: UsersBase

    class Config():
        orm_mode = True

class Verify(BaseModel):
    name: str
    email: str
    password: str

class CodeVerify(BaseModel):
    email: str
    code: str

class Login(BaseModel):
    email: str
    password: str

class Code(BaseModel):
    code: str

class Avatar(BaseModel):
    avatar: str

class Admin(BaseModel):
    admin: bool

class Token(BaseModel):
    access_token: str

class TokenData(BaseModel):
    email: str | None = None
    expires: Optional[datetime]