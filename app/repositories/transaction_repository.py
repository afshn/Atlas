from app.database.database import get_connection


class TransactionRepository:

    def save(self, transaction):

        conn = get_connection()

        cur = conn.cursor()

        cur.execute(
            """
            INSERT INTO transactions
            (
                amount,
                transaction_type,
                category,
                description,
                created_at
            )
            VALUES (?,?,?,?,?)
            """,
            (
                transaction.amount,
                transaction.transaction_type,
                transaction.category,
                transaction.description,
                str(transaction.created_at)
            )
        )

        conn.commit()
        conn.close()

    def all(self):

        conn = get_connection()

        cur = conn.cursor()

        cur.execute("""
        SELECT
            id,
            amount,
            transaction_type,
            category,
            description,
            created_at
        FROM transactions
        ORDER BY id DESC
        """)

        rows = cur.fetchall()

        conn.close()

        return rows