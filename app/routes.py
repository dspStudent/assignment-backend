# filepath: d:\assignment-backend\assignment-backend\app\routes.py
from flask import Blueprint
from flask import Blueprint, jsonify, request
from .book_review_service import get_all_books, create_books, get_reviews_by_book_id
from flasgger import swag_from

bp = Blueprint('api_bp', __name__)


@bp.route('/books', methods=['GET'])
@swag_from({
    'responses': {
        200: {
            'description': 'A list of books was successfully retrieved',
            'content': {
                'application/json': {
                    'schema': {
                        'type': 'array',
                        'items': {
                            'type': 'object'
                        }
                    }
                }
            }
        },
        404: {
            'description': 'No books were found',
            'content': {
                'application/json': {
                    'schema': {
                        'type': 'object',
                        'properties': {
                            'message': {
                                'type': 'string',
                                'example': 'No books found'
                            }
                        }
                    }
                }
            }
        }
    }
})
def get_books():
    books = get_all_books()
    # Convert each Book object to a dictionary
    books_list = [
        {
            "id": book.id,
            "title": book.title,
            "author": book.author,
            "description": book.description
        }
        for book in books
    ]
    return jsonify(books_list), 200
    
@bp.route('/books', methods=['POST'])
@swag_from({
    'tags': ['Books'],
    'consumes': ['application/json'],
    'produces': ['application/json'],
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'array',
                'items': {
                    'type': 'object',
                    'properties': {
                        'title': {'type': 'string'},
                        'author': {'type': 'string'},
                        'description': {'type': 'string'}
                    },
                    'required': ['title', 'author']
                }
            }
        }
    ],
    'responses': {
        201: {
            'description': 'Books created successfully',
            'schema': {
                'type': 'array',
                'items': {
                    'type': 'object',
                    'properties': {
                        'id': {'type': 'integer'},
                        'title': {'type': 'string'},
                        'author': {'type': 'string'}
                    }
                }
            }
        },
        400: {
            'description': 'Invalid input',
            'schema': {
                'type': 'object',
                'properties': {
                    'message': {'type': 'string'}
                }
            }
        }
    }
})
def add_books():
    data = request.get_json()
    if (
        not isinstance(data, list) or
        not all(
            isinstance(book, dict) and
            'title' in book and book['title'].strip() and
            'author' in book and book['author'].strip()
            for book in data
        )
    ):
        return jsonify({'message': 'Each book must have a non-empty title and author'}), 400
    try:
        created = create_books(data)
        return jsonify(created), 201
    except ValueError as e:
        return jsonify({'message': str(e)}), 400
    
@bp.route('/books/<int:book_id>/reviews', methods=['GET'])
@swag_from({
    'tags': ['Reviews'],
    'parameters': [
        {
            'name': 'book_id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'ID of the book'
        }
    ],
    'responses': {
        200: {
            'description': 'List of reviews for the book',
            'schema': {
                'type': 'array',
                'items': {
                    'type': 'object',
                    'properties': {
                        'id': {'type': 'integer'},
                        'book_id': {'type': 'integer'},
                        'reviewer': {'type': 'string'},
                        'rating': {'type': 'integer'},
                        'comment': {'type': 'string'}
                    }
                }
            }
        },
        404: {
            'description': 'Book not found or no reviews',
            'schema': {
                'type': 'object',
                'properties': {
                    'message': {'type': 'string'}
                }
            }
        }
    }
})
def get_book_reviews(book_id):
    from .book_review_service import get_reviews_by_book_id
    reviews = get_reviews_by_book_id(book_id)
    if reviews is None:
        return jsonify({'message': 'Book not found'}), 404
    if not reviews:
        return jsonify([]), 200
    return jsonify([
        {
            'id': review.id,
            'book_id': review.book_id,
            'reviewer': review.reviewer,
            'content': review.content
        } for review in reviews
    ]), 200

@bp.route('/books/<int:book_id>/reviews', methods=['POST'])
@swag_from({
    'tags': ['Reviews'],
    'parameters': [
        {
            'name': 'book_id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'ID of the book'
        },
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'reviewer': {'type': 'string'},
                    'rating': {'type': 'integer'},
                    'comment': {'type': 'string'}
                },
                'required': ['reviewer', 'rating']
            }
        }
    ],
    'responses': {
        201: {
            'description': 'Review created successfully',
            'schema': {
                'type': 'object',
                'properties': {
                    'id': {'type': 'integer'},
                    'book_id': {'type': 'integer'},
                    'reviewer': {'type': 'string'},
                    'rating': {'type': 'integer'},
                    'comment': {'type': 'string'}
                }
            }
        },
        400: {
            'description': 'Invalid input',
            'schema': {
                'type': 'object',
                'properties': {
                    'message': {'type': 'string'}
                }
            }
        },
        404: {
            'description': 'Book not found',
            'schema': {
                'type': 'object',
                'properties': {
                    'message': {'type': 'string'}
                }
            }
        }
    }
})
def add_review(book_id):
    from .book_review_service import add_review_to_book
    data = request.get_json()
    if not data or 'reviewer' not in data :
        return jsonify({'message': 'Reviewer  are required'}), 400
    try:
        review = add_review_to_book(book_id, data)
        if review is None:
            return jsonify({'message': 'Book not found'}), 404
        return jsonify({
            'id': review.id,
            'book_id': review.book_id,
            'reviewer': review.reviewer,
            'content': review.content
        }), 201
    except ValueError as e:
        return jsonify({'message': str(e)}), 400