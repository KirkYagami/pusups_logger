"""
 When we run Flask app using the flask run command, Flask looks for a function named create_app (or app) in your module by default.
 --> application factory (a callable that returns a Flask app instance).
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# Initialize database
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    
    # Configuration
    app.config['SECRET_KEY'] = 'your-secret-key-change-this'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
    
    # Initialize database with app
    db.init_app(app)
    
    # Initialize login manager

    # Initialize login manager
    login_manager = LoginManager()
    '''
    This object will handle user login/logout, session management, and protection of routes that require authentication.
    '''

    login_manager.login_view = 'auth.login'
    '''
    Specifies the endpoint (i.e., the route name) that Flask-Login should redirect to when an unauthenticated user tries to access a protected page.

    If a user isn't logged in and tries to visit a page that requires login,
    → They'll be redirected to the route named auth.login 

    '''
    login_manager.init_app(app)

    '''
    Binds the LoginManager instance to your Flask application (app).
    This activates Flask-Login's functionality (e.g., managing session cookies, protecting views, etc.).
    '''
    from .models import User
    
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    
    # Register blueprints
    from .main import main_blueprint
    app.register_blueprint(main_blueprint)
    
    from .auth import auth_blueprint
    app.register_blueprint(auth_blueprint)
    
    return app