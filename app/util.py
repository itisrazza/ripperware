from typing import TypeVar
from os import environ

T = TypeVar("T")


_app_version_cache: str | None = None

def app_version():
    global _app_version_cache

    if _app_version_cache is None:
        with open("assets/version") as f:
            _app_version_cache = f.read().strip()
    return _app_version_cache


def ifnone(value: T | None, default: T) -> T:
    if value is None:
        return default
    return value


def istestmode():
    env = environ.get("RIPPERWARE_ENV")
    if env == "prod":
        return True

    return False
