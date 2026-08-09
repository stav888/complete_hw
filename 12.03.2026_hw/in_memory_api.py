from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(title="In-memory Books API")


class BookInput(BaseModel):
    title: str
    author: str
    year: int = Field(ge=0)
    description: str | None = None


class Book(BookInput):
    id: int


books = [
    Book(id=1, title="The Hobbit", author="J.R.R. Tolkien", year=1937, description="Fantasy novel"),
    Book(id=2, title="1984", author="George Orwell", year=1949, description="Dystopian novel"),
]


def find_book(book_id):
    return next((book for book in books if book.id == book_id), None)


@app.get("/books", response_model=list[Book])
def get_books():
    return books


@app.get("/books/{book_id}", response_model=Book)
def get_book(book_id: int):
    book = find_book(book_id)
    if book is None:
        raise HTTPException(404, "Book not found")
    return book


@app.post("/books", response_model=Book, status_code=201)
def create_book(book: BookInput):
    created = Book(id=max((item.id for item in books), default=0) + 1, **book.model_dump())
    books.append(created)
    return created


@app.put("/books/{book_id}", response_model=Book)
def replace_book(book_id: int, book: BookInput):
    existing = find_book(book_id)
    if existing is None:
        raise HTTPException(404, "Book not found")
    replacement = Book(id=book_id, **book.model_dump())
    books[books.index(existing)] = replacement
    return replacement


@app.patch("/books/{book_id}", response_model=Book)
def patch_book(book_id: int, changes: dict):
    existing = find_book(book_id)
    if existing is None:
        raise HTTPException(404, "Book not found")
    updated = existing.model_copy(update=changes)
    books[books.index(existing)] = updated
    return updated


@app.delete("/books/{book_id}", response_model=Book)
def delete_book(book_id: int):
    existing = find_book(book_id)
    if existing is None:
        raise HTTPException(404, "Book not found")
    books.remove(existing)
    return existing
