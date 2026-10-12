import os
from pathlib import Path

import mysql.connector
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = BASE_DIR.parent
ENV_PATH = PROJECT_ROOT / "AI" / "backend" / ".env"

load_dotenv(ENV_PATH, override=True)


def get_connection():
    password = os.getenv("DB_PASSWORD")

    if not password:
        raise Exception("DB_PASSWORD was not loaded from .env")

    return mysql.connector.connect(
        host=os.getenv("DB_HOST", "localhost"),
        user=os.getenv("DB_USER", "root"),
        password=password,
        database=os.getenv("DB_NAME", "ai_security_db"),
        port=int(os.getenv("DB_PORT", "3306"))
    )
