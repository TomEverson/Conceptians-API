from email.policy import default
from sqlalchemy import VARCHAR, Column, ForeignKey, Integer, String , Boolean
from database import Base
from pydantic import BaseModel,BaseSettings
from sqlalchemy.orm import relationship

class Blogs(Base):
    __tablename__ = 'blogs'
    body = Column(VARCHAR)
    id = Column(Integer,primary_key=True,index=True)
    category = Column(String)
    title = Column(String)
    image = Column(String)
    published = Column(String)
    read = Column(Integer)
    user_id = Column(Integer, ForeignKey('users.id'))

    author = relationship("Users", back_populates= "blogs")

class Users(Base):
    __tablename__ = 'users'
    name = Column(VARCHAR)
    email = Column(VARCHAR)
    password = Column(VARCHAR)
    id = Column(Integer,primary_key=True,index=True)
    banned = Column(Boolean, unique=False, default=False)
    avatar = Column(VARCHAR)
    blogs = relationship("Blogs", back_populates= "author")

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str = None

class Settings(BaseSettings):
    twilio_account_sid: str
    twilio_auth_token: str
    twilio_verify_service: str

    class Config:
        env_file = '.env'