# filepath: d:\assignment-backend\assignment-backend\app\routes.py
from flask import Blueprint
from flask import Blueprint, jsonify, request
from .book_review_service import get_all_books, create_books
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
    if not isinstance(data, list) or not all('title' in book and 'author' in book for book in data):
        return jsonify({'message': 'Each book must have a title and author'}), 400
    created = create_books(data)
    return jsonify(created), 201
