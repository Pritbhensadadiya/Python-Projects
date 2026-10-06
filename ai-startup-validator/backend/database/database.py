import sqlite3
from pathlib import Path

# Database file path
BASE_DIR = Path(__file__).resolve().parent
DATABASE_PATH = BASE_DIR / "startup_validator.db"


def get_connection():
    """
    Returns a SQLite database connection.
    """

    connection = sqlite3.connect(DATABASE_PATH)
    connection.row_factory = sqlite3.Row
    return connection
