from app.database.database import get_connection


def create_database():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""

    CREATE TABLE IF NOT EXISTS memories(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        title TEXT NOT NULL,

        memory_type TEXT NOT NULL,

        content TEXT,

        importance INTEGER DEFAULT 3,

        status TEXT DEFAULT 'active',

        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

    )

    """)

    conn.commit()

    conn.close()