from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # Type string and max_len=10000
    content = db.Column(db.String(10000))
    # default=func.now() SQLAlchemy will set the default value to current date
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    # FOREIGN_KEY Note.user_id => User.id
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    # Type string, max_len=150 and unique value
    email = db.Column(db.String(150), unique=True)
    # Type string and max_len=150
    password_hash = db.Column(db.String(150))
    # Type string and max_len=150
    first_name = db.Column(db.String(150))
    # field created by SQLAlchemy that contains the Notes owned by this user
    notes = db.relationship('Note')
