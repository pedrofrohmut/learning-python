from flask_login import UserMixin
from sqlalchemy.sql import func

from . import db

# timezone=True respects the current timezone
# func.now() return the current time when called


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True)
    email = db.Column(db.String(150), unique=True)
    password_hash = db.Column(db.String(150))
    created_at = db.Column(db.DateTime(timezone=True), default=func.now())
    
    posts = db.relationship("Post", backref="user")
    comments = db.relationship("Comment", backref="user")
    likes = db.relationship("Like", backref="user")


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    
    comments = db.relationship("Comment", backref="post")
    likes = db.relationship("Like", backref="post")


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey("post.id"), nullable=False)


class Like(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey("post.id"), nullable=False)
    
