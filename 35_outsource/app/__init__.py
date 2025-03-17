from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'you-will-never-guess'

    from .routes import init_routes  # Import routes to register them with the app
    init_routes(app)

    return app
