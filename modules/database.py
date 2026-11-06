
import sqlite3


def create_database():
    """Create database tables and prevent duplicate favorites."""

    connection = sqlite3.connect("giftgenius.db")
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS favorites (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            gift_name TEXT NOT NULL,
            price REAL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS search_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            recipient TEXT,
            interests TEXT,
            occasion TEXT,
            budget REAL,
            search_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    # Remove existing duplicate favorites
    cursor.execute("""
        DELETE FROM favorites
        WHERE id NOT IN (
            SELECT MIN(id)
            FROM favorites
            GROUP BY gift_name
        )
    """)

    # Prevent future duplicate favorites
    cursor.execute("""
        CREATE UNIQUE INDEX IF NOT EXISTS
        unique_favorite_name
        ON favorites(gift_name)
    """)

    connection.commit()
    connection.close()


def add_favorite(gift_name, price):
    """Save a gift only if it is not already in favorites."""

    connection = sqlite3.connect("giftgenius.db")
    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT OR IGNORE INTO favorites (gift_name, price)
        VALUES (?, ?)
        """,
        (gift_name, price)
    )

    saved = cursor.rowcount == 1

    connection.commit()
    connection.close()

    return saved


def get_favorites():
    """Retrieve all saved favorite gifts."""

    connection = sqlite3.connect("giftgenius.db")
    cursor = connection.cursor()

    cursor.execute("""
        SELECT * FROM favorites
        ORDER BY id
    """)

    favorites = cursor.fetchall()

    connection.close()

    return favorites


def add_search_history(recipient, interests, occasion, budget):
    """Save a user's gift search."""

    connection = sqlite3.connect("giftgenius.db")
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO search_history
        (recipient, interests, occasion, budget)
        VALUES (?, ?, ?, ?)
    """, (
        recipient,
        ";".join(interests),
        occasion,
        budget
    ))

    connection.commit()
    connection.close()


def get_search_history():
    """Retrieve previous gift searches, newest first."""

    connection = sqlite3.connect("giftgenius.db")
    cursor = connection.cursor()

    cursor.execute("""
        SELECT recipient, interests, occasion, budget, search_date
        FROM search_history
        ORDER BY id DESC
    """)

    history = cursor.fetchall()

    connection.close()

    return history


def delete_search_history():
    """Delete all previous gift searches."""

    connection = sqlite3.connect("giftgenius.db")
    cursor = connection.cursor()

    cursor.execute("DELETE FROM search_history")

    connection.commit()
    connection.close()
