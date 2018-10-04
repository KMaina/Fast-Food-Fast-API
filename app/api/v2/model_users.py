"""
This module is used to interact with the database
"""
import psycopg2
from flask_jwt_extended import create_access_token
from flask import request, jsonify

from app import migration

connection = migration.db_connection()
cursor = connection.cursor()

def get_user_id(name):
    if not isinstance(name,str):
        return {"msg":"Name must be a string"}
    cursor.execute("SELECT user_id FROM users WHERE username = '{}'".format(name))
    connection.commit()
    userid = cursor.fetchone()
    if userid:
        return userid[0]
    return {'msg':'Problem getting the user id'}

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
        if not isinstance(username, str):
            print(type(username))
            response = jsonify({'msg':'Username must be a string'})
            response.status_code = 400
            return response
        if not isinstance(password, str) and isinstance(confirm_password, str):
            response = jsonify({'msg':'Password must be a string'})
            response.status_code = 400
            return response
        if not isinstance(email, str):
            response = jsonify({'msg':'Email must be a string'})
            response.status_code = 400
            return response
        if not isinstance(address, str):
            response = jsonify({'msg':'Address must be a string'})
            response.status_code = 400
            return response
        if not isinstance(telephone, str):
            response = jsonify({'msg':'Telephone number must be a string'})
            response.status_code = 400
            return response
        if not isinstance(admin, bool):
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
            response = jsonify({'msg':'User successfully added to the database'})
            response.status_code = 201
            return response
        except (Exception, psycopg2.DatabaseError) as error:
            response = jsonify({'msg':'Problem inserting into the database'})
            response.status_code = 400
            return response

    def login(self, username, password):
        """Method to login a user"""
        username = request.json.get('username', None)
        password = request.json.get('password', None)
        if not isinstance(username, str):
            print(type(username))
            response = jsonify({'msg' : 'Username must be a string'})
            response.status_code = 400
            return response
        if not isinstance(username, str):
            response = jsonify({'msg' : 'Password must be a string'})
            response.status_code = 400
            return response
        try:
            get_user = "SELECT username, password, admin \
                        FROM users \
                        WHERE username = '" + username + "' AND password = '" + password +  "'"
            cursor.execute(get_user)
            row = cursor.fetchone()
            if row is not None:
                dbusername = row[0] 
                dbadmin = row[2]
                if not dbusername or dbadmin:
                    return {'msg':'Error, problem getting credentials from the database'}, 400
                print(dbusername,dbadmin)
                access_token = create_access_token(identity={"username": dbusername, "admin": dbadmin})
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
        