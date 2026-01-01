import os
from flask import Flask
from flask_pymongo import PyMongo
from flask_cors import CORS

mongo = PyMongo()

def create_app():
    app = Flask(__name__)
    # Set a random secret key for session management
    app.secret_key = os.urandom(24)
    app.config.from_object('config.Config')

    CORS(app)
    mongo.init_app(app)

    with app.app_context():
        from .routes import bp
        app.register_blueprint(bp)
        
    return app
