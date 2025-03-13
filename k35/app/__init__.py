from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'you-will-never-guess'

    with app.app_context():
        from . import routes  # Import routes to register them with the app

    return app
