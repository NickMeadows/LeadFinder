from flask import Flask
from app.db import init_db

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'change_this_later'

    with app.app_context():
        init_db()

    from app.routes import main
    app.register_blueprint(main)

    return app
