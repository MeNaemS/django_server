from typing import Literal, List
from dataclasses import dataclass


@dataclass(slots=True)
class Database:
    host: str
    port: int
    user: str
    password: str
    name: str


@dataclass(slots=True)
class Django:
    secret_key: str
    allowed_hosts: List[str]


@dataclass(slots=True)
class Configs:
    log_level: Literal["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]
    debug: bool
    database: Database
    django: Django
