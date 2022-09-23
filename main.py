from fastapi import FastAPI
import models
from database import engine
from fastapi.middleware.cors import CORSMiddleware
from routers import authentication, blog, user , verify , avatar , role


app = FastAPI()

origins = [
    "http://www.conceptians.org",
    "https://www.conceptians.org",
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

models.Base.metadata.create_all(engine)

app.include_router(verify.router)
app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(user.router)
app.include_router(avatar.router)
app.include_router(role.router)
