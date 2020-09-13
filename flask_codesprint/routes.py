from flask_codesprint import app, db
from flask import render_template, redirect, url_for, flash, request
from flask_codesprint.models import User
from flask_codesprint import bcrypt
from flask_login import login_user, current_user

"""@app.route('/')
def home():
  return 'Welcome! <a href="/login">login here</a>"""


@app.route('/', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return render_template('main.html')

    if request.method == 'POST':
        user = User.query.filter_by(username=request.form['username']).first()
        if user and bcrypt.check_password_hash(user.password, request.form['password']):
            return render_template('main.html')
        else:
            flash('Login unsuccessfull. Please check username and password.', 'danger')
    return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return render_template('main.html')

    if request.method == 'POST':
        hashed_pass = bcrypt.generate_password_hash(
            request.form['password']).decode('utf-8')
        user = User(username=request.form['username'], password=hashed_pass)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))

    return render_template('register.html')


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    return render_template('upload.html')
