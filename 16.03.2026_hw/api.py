from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import dal

app = FastAPI(title="SQLite Books API")


class BookInput(BaseModel):
    title: str
    author: str
    language: str | None = None
    price: float = Field(ge=0)
    published_year: int | None = None


@app.get("/books")
def get_books():
    return dal.get_all_books()


@app.get("/books/{book_id}")
def get_book(book_id: int):
    book = dal.get_book(book_id)
    if book is None:
        raise HTTPException(404, "Book not found")
    return book


@app.post("/books", status_code=201)
def create_book(book: BookInput):
    return dal.insert_book(**book.model_dump())


@app.put("/books/{book_id}")
def update_book(book_id: int, book: BookInput):
    updated = dal.update_book(book_id, **book.model_dump())
    if updated is None:
        raise HTTPException(404, "Book not found")
    return updated


@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    deleted = dal.delete_book(book_id)
    if deleted is None:
        raise HTTPException(404, "Book not found")
    return deleted


@app.delete("/tables/books")
def recreate_books_table():
    dal.recreate_table_books()
    return {"message": "books table recreated"}
