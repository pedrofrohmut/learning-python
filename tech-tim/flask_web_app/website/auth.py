from flask import Blueprint, render_template, request, flash, redirect, url_for
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import login_user, login_required, logout_user, current_user

from .models import User
from . import db

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Get form vaues
        email = request.form.get('email') or ""
        password = request.form.get('password') or ""
        # Form validation
        if len(email) < 4:
            flash('E-mail must be greater than 3 characters', category='error')
            return render_template('login.html')
        elif len(password) < 6:
            flash('Password must be greater than 5 characters', category='error')
            return render_template('login.html')
        # Query db for user with matching e-mail
        user = User.query.filter_by(email=email).first()
        if not user:
            flash('E-mail does not exist. Please try again or sign up if you are not registered', category='error')
            return render_template('login.html')
        passwordsMatch = check_password_hash(user.password_hash, password)
        if not passwordsMatch:
            flash('Incorrect password. Please, try again', category='error')
            return render_template('login.html')
        login_user(user, remember=True)
        flash('Log in successfully', category='success')
        return redirect(url_for('views.home'))
    return render_template('login.html', user=current_user)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        # Get submitted form vaues
        email = request.form.get('email') or ""
        first_name = request.form.get('firstName') or ""
        password = request.form.get('password') or ""
        confirmPassword = request.form.get('confirmPassword') or ""
        # Validate form fields
        if len(email) < 4:
            flash('E-mail must be greater than 3 characters', category='error')
            return render_template('signup.html')
        elif len(first_name) < 2:
            flash('First name must be greater than 1 character', category='error')
            return render_template('signup.html')
        elif len(password) < 6:
            flash('Password must be greater than 5 characters', category='error')
            return render_template('signup.html')
        elif password != confirmPassword:
            flash('Password and confirm password must match', category='error')
            return render_template('signup.html')
        # Check if e-mail is already taken (must be unique)
        user = User.query.filter_by(email=email).first()
        if user:
            flash('E-mail already been taken. Please sing up with a different one or log in', category='error')
            return render_template('signup.html')
        # Generate hash
        password_hash = generate_password_hash(password, method='sha256')
        # Save new user to db
        new_user = User(email=email, first_name=first_name, password_hash=password_hash)
        db.session.add(new_user)
        db.session.commit()
        flash('Account created', category='success')
        login_user(user, remember=True)
        # Redirect to home page
        return redirect(url_for('views.home'))
    return render_template('signup.html', user=current_user)
