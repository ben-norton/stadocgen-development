from flask import Flask
from yaml import load, Loader


app = Flask(__name__)

from app import routes