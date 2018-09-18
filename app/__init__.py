"""
the __init__.py file

included to make app a package
"""

from flask import Flask

# from app import app

app = Flask(__name__)

from app.api.v1 import views