from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase

from src.secret import SQLALCHEMY_DATABASE_URI

class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)



# create the app
app = Flask(__name__)

# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI

# initialize the app with the extension
db.init_app(app)



from datetime import datetime
from sqlalchemy import Integer, String, DateTime
from sqlalchemy.orm import mapped_column


class TimestampMixin(object):
    created_at = mapped_column(DateTime, default=datetime.utcnow)
    updated_at = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class User(TimestampMixin, db.Model):
    __tablename__ = "users"

    id = mapped_column(Integer, primary_key=True)
    name = mapped_column(String, nullable=False)
    email = mapped_column(String, unique=True, nullable=False)
    password_hash = mapped_column(String, nullable=False)
    phone = mapped_column(String)


def add_user():
    user = User()
    user.name="John Doe"
    user.email="john@doe.com"
    user.password_hash="HASH"
    user.phone="1234-5678"
    db.session.add(user)
    db.session.commit()
    print("User " + user.name + "added with success.")


# @app.route("/user/add")
# def route_add_user():
#     add_user()
#     return "User Added"


from src import users_routes
from src import goals_routes

if __name__ == "__main__":
    app.run(host="0.0.0.0")
