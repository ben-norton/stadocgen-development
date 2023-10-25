from flask import Flask

app = Flask(__name__)

from app import routes

app.config.from_pyfile("config.py")
