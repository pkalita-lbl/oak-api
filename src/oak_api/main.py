from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routers import classes, search

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(classes.router)
app.include_router(search.router)
