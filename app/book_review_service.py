""" Book Review Service Module
This module provides services related to book reviews, including fetching all books."""

from app.models import Book  # Adjust import as needed

def get_all_books():
    # Dummy data for demonstration; replace with DB logic as needed
    return Book.query.all()