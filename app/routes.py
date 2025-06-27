# filepath: d:\assignment-backend\assignment-backend\app\routes.py
from flask import Blueprint
from flask import Blueprint, jsonify
from .book_review_service import get_all_books
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
    
    return jsonify(books), 200
    
