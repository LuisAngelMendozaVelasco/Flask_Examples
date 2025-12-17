import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_utils import database_exists, create_database

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.secret_key = os.urandom(24)
    app.config.from_object('config.Config')

    db.init_app(app)

    with app.app_context():
        from .routes import bp
        app.register_blueprint(bp)
        # Create the database if it doesn't exist
        if not database_exists(db.engine.url):
            create_database(db.engine.url)
        db.create_all()
        
    return app
