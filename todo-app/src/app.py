from flask import Flask
from flask_bcrypt import Bcrypt

from src.db import db
from src.secret import SQLALCHEMY_DATABASE_URI

# create the app
app = Flask(__name__)

# Bcrypt class wrapper
bcrypt = Bcrypt(app)

# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI

# initialize the app with the extension
db.init_app(app)

# def add_user():
#     user = User()
#     user.name="John Doe"
#     user.email="john@doe.com"
#     user.password_hash="HASH"
#     user.phone="1234-5678"
#     db.session.add(user)
#     db.session.commit()
#     print("User " + user.name + "added with success.")

from src.routes import users_routes
from src.routes import goals_routes
from src.routes import pages_routes
