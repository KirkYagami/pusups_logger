'''
This will be used to implement auth
'''

from flask import Blueprint, render_template, request, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required
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
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False
    
    # Check if user exists
    user = User.query.filter_by(email=email).first()
    
    # Check if user exists and password is correct
    if not user or not check_password_hash(user.password, password):
        print("Invalid email or password")
        return redirect(url_for('auth.login'))
    
    # Login user
    login_user(user, remember=remember)
    print(f"User {user.name} logged in successfully!")
    
    return redirect(url_for('main.profile'))

@auth_blueprint.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))



