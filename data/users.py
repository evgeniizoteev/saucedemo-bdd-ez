import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv(Path(__file__).resolve().parent.parent / ".env")
BACKPACK = "Sauce Labs Backpack"


def get_user(role: str) -> tuple[str, str]:
    key = role.strip().upper()

    if not key.endswith("_USER"):
        key = f"{key}_USER"

    raw = os.getenv(key, "")

    if "/" not in raw:
        raise KeyError(f"{key} must be login/password in .env")

    login, password = raw.split("/", 1)
    return login, password
