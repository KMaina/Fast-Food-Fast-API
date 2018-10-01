"""
This module is used to interact with the database
"""
import psycopg2
from flask_jwt_extended import create_access_token
from flask import request, jsonify

from app import migration

connection = migration.db_connection()
cursor = connection.cursor()

class Users():
    """Class to handle users"""
    def register_user(self, username, password, confirm_password, email, address, telephone, admin):
        """Method to register a user"""
        username = request.json.get('username', None)
        password = request.json.get('password', None)
        confirm_password = request.json.get('confirm_password', None)
        email = request.json.get('email', None)
        address = request.json.get('address', None)
        telephone = request.json.get('telephone', None)
        admin = request.json.get('admin', None)
        if isinstance(username, str):
            print(type(username))
            response = jsonify({'msg':'Username must be a string'})
            response.status_code = 400
            return response
        if isinstance(password, str) and isinstance(confirm_password, str):
            response = jsonify({'msg':'Password must be a string'})
            response.status_code = 400
            return response
        if isinstance(email, str):
            response = jsonify({'msg':'Email must be a string'})
            response.status_code = 400
            return response
        if isinstance(address, str):
            response = jsonify({'msg':'Address must be a string'})
            response.status_code = 400
            return response
        if isinstance(telephone, str):
            response = jsonify({'msg':'Telephone number must be a string'})
            response.status_code = 400
            return response
        if isinstance(admin, bool):
            response = jsonify({'msg':'Admin must be a boolean'})
            response.status_code = 400
            return response
        if password != confirm_password:
            response = jsonify({'msg':'Passwords must match'})
            response.status_code = 400
            return response
        try:
            if admin is True:
                add_user = "INSERT INTO \
                            users \
                            (username, password, email, address, telephone, admin) \
                            VALUES \
                            ('" + username +"', '" + password +"', '" + email + "', \
                             '" + address + "', '" + telephone + "',  true )"
            if admin is False:
                add_user = "INSERT INTO \
                            users \
                            (username, password, email, address, telephone, admin) \
                            VALUES ('" + username +"', '" + password +"', '" + email + "', \
                             '" + address + "', '" + telephone + "',  false )"
            cursor.execute(add_user)
            connection.commit()
            response = jsonify({'msg':'User successfully added to the databse'})
            response.status_code = 201
            return response
        except (Exception, psycopg2.DatabaseError) as error:
            response = jsonify({'msg':'Problem inserting into the databse'})
            response.status_code = 400
            return response

    def login(self, username, password):
        """Method to login a user"""
        username = request.json.get('username', None)
        password = request.json.get('password', None)
        if isinstance(username, str):
            print(type(username))
            response = jsonify({'msg' : 'Username must be a string'})
            response.status_code = 400
            return response
        if isinstance(username, str):
            response = jsonify({'msg' : 'Password must be a string'})
            response.status_code = 400
            return response
        try:
            get_user = "SELECT username, password \
                        FROM users \
                        WHERE username = '" + username + "' AND password = '" + password +  "'"
            cursor.execute(get_user)
            row = cursor.fetchone()
            if row is not None:
                row = cursor.fetchone()
                access_token = create_access_token(identity=username)
                print(access_token)
                response = jsonify({"msg":"Successfully logged in", "access_token":access_token})
                response.status_code = 200
                return response
            response = jsonify({"msg" : "Error logging in, credentials not found"})
            response.status_code = 401
            return response
        except (Exception, psycopg2.DatabaseError) as error:
            print("Error executing", error)
            return jsonify({"msg" : "Error, check the database {}".format(error)})
        