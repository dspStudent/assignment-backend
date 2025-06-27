""" Book Review Service Module
This module provides services related to book reviews, including fetching all books."""
from app import db
from app.models import Book  # Adjust import as needed

def get_all_books():
    # Dummy data for demonstration; replace with DB logic as needed
    return Book.query.all()

def create_books(book_list):
    """
    Adds a list of books to the database.
    Each book in book_list should be a dict with 'title', 'author', and optionally 'description'.
    Returns the list of created books with assigned IDs.
    """
    created_books = []
    for book_data in book_list:
        new_book = Book(
            title=book_data.get("title"),
            author=book_data.get("author"),
            description=book_data.get("description")  # Optional
        )
        db.session.add(new_book)
        created_books.append(new_book)

    db.session.commit()

    return [
        {
            "id": book.id,
            "title": book.title,
            "author": book.author,
            "description": book.description
        } for book in created_books
    ]