from fastapi import FastAPI
import models
from database import engine
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware
from routers import authentication, blog, user , verify

middleware = [
    Middleware(
        CORSMiddleware,
        allow_origins=['*'],
        allow_credentials=False,
        allow_methods=['*'],
        allow_headers=['*']
    )
]

app = FastAPI(middleware=middleware)

models.Base.metadata.create_all(engine)

app.include_router(verify.router)
app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(user.router)
