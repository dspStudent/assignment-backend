""""
Models for the application.
"""
from . import db

class Book(db.Model):
    """ Model representing a book in the database."""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    reviews = db.relationship('Review', backref='book', lazy=True)
    deleted = db.Column(db.Boolean, default=False)

class Review(db.Model):
    """ Model representing a review for a book."""
    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'), nullable=False)
    reviewer = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)

    __table_args__ = (
        db.Index('idx_reviews_book_id', 'book_id'),
    )
