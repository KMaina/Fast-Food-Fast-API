"""
the __init__.py file

included to make app a module
"""

from flask import Flask

app = Flask(__name__)

from app import views
