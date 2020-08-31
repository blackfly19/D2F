from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///original.db'
app.config['SECRET_KEY'] = 'e9d6a017bb132b62162aaea47723d4ff1d0913732a94e8eac120e06d4f8dca71'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manage = LoginManager(app)

from flask_codesprint import routes