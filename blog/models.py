from sqlalchemy import Column, Integer, String
from .database import Base

class Blog(Base):
    __tablename__ = 'blog'
    body = Column(String)
    id = Column(Integer,primary_key=True,index=True)
    title = Column(String)
    translate = Column(String)
    author = Column(String)
    editor = Column(String)
    translator = Column(String)
    published = Column(String)