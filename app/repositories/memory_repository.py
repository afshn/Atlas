import json

from app.database.database import get_connection


class MemoryRepository:

    def save(self, memory):

        conn = get_connection()

        cur = conn.cursor()

        cur.execute(
            """
            INSERT INTO memories
            (
                text,
                created_at,
                category,
                action,
                importance,
                follow_up,
                entities,
                tags
            )

            VALUES
            (?,?,?,?,?,?,?,?)
            """,

            (

                memory.text,

                str(memory.created_at),

                memory.category,

                memory.action,

                memory.importance,

                int(memory.follow_up),

                json.dumps(memory.entities, ensure_ascii=False),

                json.dumps(memory.tags, ensure_ascii=False)

            )

        )

        conn.commit()

        conn.close()

    def all(self):

        conn = get_connection()

        cur = conn.cursor()

        cur.execute("SELECT * FROM memories ORDER BY id DESC")

        rows = cur.fetchall()

        conn.close()

        return rows