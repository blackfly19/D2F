from flask_codesprint import db

class User(db.Model):

    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(100),nullable=False,unique=True)
    password = db.Column(db.String(60),nullable=False)