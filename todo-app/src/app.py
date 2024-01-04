from flask import Flask
from flask_bcrypt import Bcrypt

from src.db import db
from src.secret import SQLALCHEMY_DATABASE_URI, APP_SECRET_KEY

# create the app
app = Flask(__name__)

# Bcrypt class wrapper
bcrypt = Bcrypt(app)

# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI

app.secret_key = APP_SECRET_KEY

# initialize the app with the extension
db.init_app(app)

from src.routes import users_routes
from src.routes import goals_routes
from src.routes import pages_routes
