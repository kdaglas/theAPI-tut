from flask import Flask

app = Flask(__name__)

from app import views

''' This file is meant to initialize the flask app '''