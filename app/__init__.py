from flask import Flask
from app.routes.books import books_bp
from app.routes.members import members_bp
from app.error_handlers import register_error_handlers
from flask import Flask
from app.routes.books import books_bp
from app.routes.members import members_bp
from app.error_handlers import register_error_handlers

def create_app():
    app = Flask(__name__)
    app.register_blueprint(books_bp, url_prefix='/api')
    app.register_blueprint(members_bp, url_prefix='/api')
    register_error_handlers(app)
    return app

def create_app():
    app = Flask(__name__)
    app.register_blueprint(books_bp, url_prefix='/api')
    app.register_blueprint(members_bp, url_prefix='/api')
    register_error_handlers(app)
    return app

