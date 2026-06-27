from app.database.database import get_connection


def add_memory(
    title,
    memory_type,
    content,
    importance
):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""

    INSERT INTO memories(

        title,

        memory_type,

        content,

        importance

    )

    VALUES(?,?,?,?)

    """,(

        title,

        memory_type,

        content,

        importance

    ))

    conn.commit()

    conn.close()



def get_memories():

    conn=get_connection()

    cursor=conn.cursor()

    cursor.execute("""

    SELECT *

    FROM memories

    ORDER BY id DESC

    """)

    data=cursor.fetchall()

    conn.close()

    return data