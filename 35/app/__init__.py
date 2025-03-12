from flask import Flask
from .models import init_db

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'you-will-never-guess'

    with app.app_context():
        from . import routes
        init_db()  # Initialize the database

    return app
