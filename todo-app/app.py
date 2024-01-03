from flask import Flask

from db import db
from src.secret import SQLALCHEMY_DATABASE_URI

# create the app
app = Flask(__name__)

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

from src import users_routes
from src import goals_routes

if __name__ == "__main__":
    app.run(host="0.0.0.0")
