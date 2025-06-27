"Initialize Flask application with SQLAlchemy, Flask-Migrate, and Swagger documentation."


from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flasgger import Swagger
import redis

db = SQLAlchemy()
migrate = Migrate()
r = redis.Redis(host='localhost', port=6379, decode_responses=True)

def create_app():

    """Create and configure the Flask application."""
    
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SWAGGER'] = {'title': 'Book Review API', 'uiversion': 3}

    db.init_app(app)
    migrate.init_app(app, db)
    Swagger(app)

    from .routes import bp as api_bp
    app.register_blueprint(api_bp)

    return app
