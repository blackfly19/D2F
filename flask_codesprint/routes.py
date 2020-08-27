from flask_codesprint import app
from flask import render_template,redirect,url_for,flash,request
from flask_codesprint.models import User
from flask_codesprint import bcrypt
from flask_login import login_user

@app.route('/')
def home():
  return 'Welcome! <a href="/login">login here</a>'

@app.route('/login',methods = ['GET','POST'])
def login():
    if request.method == 'POST':
        user = User.query.filter_by(username=request.form['username']).first()
        if user and bcrypt.check_password_hash(user.password,request.form['password']):
            return "Hello bro.You have been logged in"
        else:
            flash('Login unsuccessfull. Please check username and password.','danger')
    return render_template('login.html')
