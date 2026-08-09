import sqlite3
from pathlib import Path

DB_NAME = Path(__file__).with_name("books.db")


def get_connection():
    connection = sqlite3.connect(DB_NAME)
    connection.row_factory = sqlite3.Row
    return connection


def create_table_books():
    with get_connection() as connection:
        connection.execute("""CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            language TEXT,
            price REAL NOT NULL CHECK(price >= 0),
            published_year INTEGER,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )""")


def row_to_dict(row):
    return dict(row) if row else None


def get_all_books():
    with get_connection() as connection:
        rows = connection.execute("SELECT * FROM books ORDER BY id").fetchall()
    return [row_to_dict(row) for row in rows]


def get_book(book_id):
    with get_connection() as connection:
        row = connection.execute("SELECT * FROM books WHERE id = ?", (book_id,)).fetchone()
    return row_to_dict(row)


def insert_book(title, author, language, price, published_year):
    with get_connection() as connection:
        cursor = connection.execute("INSERT INTO books(title, author, language, price, published_year) VALUES (?, ?, ?, ?, ?)", (title, author, language, price, published_year))
    return get_book(cursor.lastrowid)


def update_book(book_id, title, author, language, price, published_year):
    with get_connection() as connection:
        result = connection.execute("UPDATE books SET title=?, author=?, language=?, price=?, published_year=? WHERE id=?", (title, author, language, price, published_year, book_id))
    return get_book(book_id) if result.rowcount else None


def delete_book(book_id):
    book = get_book(book_id)
    if book:
        with get_connection() as connection:
            connection.execute("DELETE FROM books WHERE id = ?", (book_id,))
    return book


def recreate_table_books():
    with get_connection() as connection:
        connection.execute("DROP TABLE IF EXISTS books")
    create_table_books()


create_table_books()
