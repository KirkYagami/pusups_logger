'''
This will be used to implement auth
'''

from flask import Blueprint, render_template, request, redirect, url_for
from werkzeug.security import generate_password_hash
from .models import User
from . import db


auth_blueprint = Blueprint('auth', __name__)

@auth_blueprint.route('/signup')
def signup():
    return render_template('signup.html')

@auth_blueprint.route('/signup', methods=['POST'])
def signup_post():
    # Get form data
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')

    # Check if user already exists
    user = User.query.filter_by(email=email).first()

    if user:
        # User already exists
        print("User already exists!")
        return redirect(url_for('auth.signup'))
    
    # Create new user
    new_user = User(
        email=email,
        name=name,
        password=generate_password_hash(password)
    )
    db.session.add(new_user)
    db.session.commit()

    print(f"New user created: {name}")
    
    return redirect(url_for('auth.login'))


@auth_blueprint.route('/login')
def login():
    return render_template('login.html')


@auth_blueprint.route('/login', methods=['POST'])
def login_post():
    # Get form data
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False
    
    # Print to console (for testing)
    print(f"Email: {email}, Password: {password}, Remember: {remember}")
    
    # Redirect to profile page
    return redirect(url_for('main.profile'))


@auth_blueprint.route('/logout')
def logout():
    return render_template('index.html')

