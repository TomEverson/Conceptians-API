from codecs import Codec
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

class Users(BaseModel):
    name: str
    email: str
    password: str

class Login(BaseModel):
    username: str
    password: str

class Code(BaseModel):
    code: str