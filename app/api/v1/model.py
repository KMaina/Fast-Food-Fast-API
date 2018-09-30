import psycopg2
import os

from flask import request, jsonify
from app import migration

connection = migration.db_connection()
cursor = connection.cursor()

class Users():
    """Class to handle users"""
    
    def register_user(self, username, password, confirm_password, email, address, telephone, admin):
        pass