from pydantic import BaseModel

class Blog(BaseModel):
    title: str
    body: str
    translate: str
    author: str
    editor: str
    translator: str
    published: str