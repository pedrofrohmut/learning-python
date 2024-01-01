from flask import Flask

app = Flask(__name__)

from app import users_routes
from app import goals_routes

