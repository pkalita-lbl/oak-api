from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routers import classes, search
from .settings import get_settings


def create_app():
    app = FastAPI(on_startup=[get_settings])
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    app.include_router(classes.router)
    app.include_router(search.router)
    return app


app = create_app()
