import sqlite3

from app.config import DATABASE_NAME


def get_connection():

    return sqlite3.connect(DATABASE_NAME)