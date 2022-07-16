from asyncore import read
from cgitb import text
from sqlalchemy import VARCHAR, Column, Integer, String
from .database import Base


class Blog(Base):
    __tablename__ = 'blogs'
    body = Column(VARCHAR)
    id = Column(Integer,primary_key=True,index=True)
    title = Column(String)
    category = Column(String)
    translate = Column(VARCHAR)
    author = Column(String)
    cowriter = Column(String)
    editor = Column(String)
    translator = Column(String)
    published = Column(String)
    read = Column(String)
    Link = Column(String)


class User(Base):
    __tablename__ = 'users'
    name = Column(String)
    id = Column(Integer,primary_key=True,index=True)
    email = Column(String)
    image = Column(String)