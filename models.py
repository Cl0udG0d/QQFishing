from exts import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(20), nullable=False)
    username = db.Column(db.String(50), nullable=False)
    pw_hash = db.Column(db.String(128), nullable=False)

    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.set_password(password)

    def set_password(self, password):
        self.pw_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.pw_hash, password)

class Target(db.Model):
    __tablename__ = 'target'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username=db.Column(db.String(50), nullable=False)
    password=db.Column(db.String(100), nullable=False)
    logindate=db.Column(db.DateTime, default=datetime.now)
