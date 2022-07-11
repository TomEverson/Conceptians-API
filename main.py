from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get('/')
def show():
    return {'data':"hi"}


class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]

@app.post('/blog')
def CreateBlog(blog: Blog):
    return {'data':f"{blog.title}"}

