from app.database.database import get_connection


def create_financial_tables():

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS transactions(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        amount INTEGER,

        transaction_type TEXT,

        category TEXT,

        description TEXT,

        created_at TEXT

    )
    """)

    conn.commit()
    conn.close()