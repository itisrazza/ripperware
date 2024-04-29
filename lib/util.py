from typing import TypeVar
from os import environ


T = TypeVar("T")


def ifnone(value: T | None, default: T) -> T:
    if value is None:
        return default
    return value


def istestmode():
    env = environ.get("RIPPERWARE_ENV")
    if env == "prod":
        return True

    return False
