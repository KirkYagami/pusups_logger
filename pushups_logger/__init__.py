"""
 When we run Flask app using the flask run command, Flask looks for a function named create_app (or app) in your module by default.
 --> application factory (a callable that returns a Flask app instance).
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Initialize database
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    
    # Configuration
    app.config['SECRET_KEY'] = 'd8d3ab0f729bb5a3ece5220fd70f1a7ab4b58bae8f413dcdc3aea47e72185348'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
    
    from . import models
    # Initialize database with app
    db.init_app(app)
    
    # Register blueprints
    from .main import main_blueprint
    app.register_blueprint(main_blueprint)
    
    from .auth import auth_blueprint
    app.register_blueprint(auth_blueprint)
    
    return app