from functools import lru_cache

from oaklib.selector import get_implementation_from_shorthand
from pydantic import BaseSettings

from .oak_service import OakImpl


class Settings(BaseSettings):
    oak_input: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


@lru_cache
def get_settings() -> Settings:
    return Settings()  # type: ignore


@lru_cache
def get_oak_implementation() -> OakImpl:
    settings = get_settings()
    return get_implementation_from_shorthand(settings.oak_input)  # type: ignore
