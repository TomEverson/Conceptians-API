from sqlalchemy import VARCHAR, Column, Integer, String
from database import Base

class Blogs(Base):
    __tablename__ = 'blogs'
    body = Column(VARCHAR)
    id = Column(Integer,primary_key=True,index=True)
    category = Column(String)
    title = Column(String)
    translate = Column(VARCHAR)
    author = Column(String)
    translator = Column(String)
    published = Column(String)
    read = Column(String)
    photo = Column(String)

class Users(Base):
    __tablename__ = 'users'
    name = Column(VARCHAR)
    email = Column(VARCHAR)
    password = Column(VARCHAR)
    id = Column(Integer,primary_key=True,index=True)

