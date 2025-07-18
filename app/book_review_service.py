""" Book Review Service Module
This module provides services related to book reviews, including fetching all books."""
from app import db
from app.models import Book  # Adjust import as needed

def get_all_books():
    # Dummy data for demonstration; replace with DB logic as needed
    return Book.query.all()

def create_books(book_list):
    """
    Adds a list of books to the database with validations:
    - No duplicate titles in the payload
    - No title already exists in the database
    Returns the list of created books with assigned IDs.
    Raises ValueError with a message for validation errors.
    """
    # Check for duplicate titles in the payload
    titles = [book.get("title") for book in book_list]
    if len(titles) != len(set(titles)):
        raise ValueError("Duplicate titles found in payload.")

    # Check for existing titles in the database
    existing_titles = {b.title for b in Book.query.filter(Book.title.in_(titles)).all()}
    duplicate_existing = [title for title in titles if title in existing_titles]
    if duplicate_existing:
        raise ValueError(f"Titles already exist: {', '.join(duplicate_existing)}")

    created_books = []
    for book_data in book_list:
        new_book = Book(
            title=book_data.get("title"),
            author=book_data.get("author"),
            description=book_data.get("description")
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

def get_reviews_by_book_id(book_id):
    """Fetches all reviews for a given book ID."""
    from app.models import Book, Review  # Adjust import as needed
    book = Book.query.get(book_id)
    if not book:
        return None
    return Review.query.filter_by(book_id=book_id).all()


def add_review_to_book(book_id, review_data):
    """ Adds a review to a book with the given ID."""
    from app.models import Book, Review
    book = Book.query.get(book_id)
    if not book:
        return None
    reviewer = review_data.get('reviewer')
    comment = review_data.get('comment')
    review = Review(
        book_id=book_id,
        reviewer=reviewer,
        content=comment
    )
    db.session.add(review)
    db.session.commit()
    return review