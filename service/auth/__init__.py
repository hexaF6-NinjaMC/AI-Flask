"""Add Login routes"""
# pylint: disable=line-too-long
from flask import Blueprint, Response, current_app, flash, redirect, render_template
from flask_login import current_user, login_required, login_user, logout_user
from service.forms import LoginForm, RegisterForm
from service.models import User
from service.extensions import database

auth_bp = Blueprint('auth_bp', __name__)

@auth_bp.get('/register')
def register():
    """Returns the initial auth resonse"""
    if current_user.is_authenticated:
        logout_user()
    return render_template('register.html', form=RegisterForm())

@auth_bp.post('/register')
def register_post():
    """Register the user"""
    if current_user.is_authenticated:
        logout_user()
    form = RegisterForm()
    response = redirect("/register", 422)
    if form.validate_on_submit():
        email_data = form.username.data.lower()
        password_data = form.password.data
        user = User.get_user_by_name(name=email_data)
        if user is not None:
            if user.username.lower() == email_data:
                flash('User already exists.', 'info')
                response = redirect("/login", 302)
        else:
            user = User()
            user.create(user_name=email_data, password_text=password_data)
            flash('User created.', 'success')
            response = redirect("/login", 201)
    return response

@auth_bp.get('/login')
def auth_index():
    """Returns the initial auth resonse"""
    if current_user.is_authenticated:
        logout_user()
    return render_template('login.html', form=LoginForm())

@auth_bp.post('/login')
def login() -> Response:
    """Login the user"""
    if current_user.is_authenticated:
        logout_user()
    response = redirect("/login", 401)
    form = LoginForm()
    if form.validate_on_submit():
        email_data = form.username.data.lower()
        password_data = form.password.data

        form.username.data = ''
        form.password.data = ''
        user = User.get_user_by_email(email=email_data)
        database.session.close()
        if user and user.verify_password(password_text=password_data) and user.id == current_app.config['ADMIN_USER_ID']:
            login_user(user)
            flash('Logged in.', 'success')
            response = redirect("/upload", 302)
            # response.access_control_allow_credentials = True
    else:
        flash('Invalid email or password.', 'error')
        response = redirect("/login", 401)
    return response

# Create Logout page
@auth_bp.get("/logout")
@login_required
def logout():
    """Logout the user"""
    logout_user()
    flash('Logged out.', 'info')
    response = redirect("/login", 302)
    return response
