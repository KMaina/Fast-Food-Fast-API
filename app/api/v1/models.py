from flask import jsonify, request

USERS_LIST = []

USERS_DICT = []

class Users():

    user_id = 0

    def register_user(self, name, password, username, email, address, telephone, admin):
        """Returns a message confirm if registration was succesful or not"""
        global USERS_DICT
        global USERS_LIST

        USERS_DICT = {
            'name' : name,
            'password' : password,
            'username' : username,
            'email' : email,
            'address' : address,
            'telephone' : telephone,
            'id' : int(Users.user_id + 1),
            'admin' : admin
        }

        Users.user_id += 1
        USERS_LIST.append(USERS_DICT)

        response = jsonify({'msg':'User added sucessfully'})
        response.status_code = 201

        return response
    
    def get_all_users(self):
        global USERS_LIST
        if len(USERS_LIST) == 0:
            response = jsonify({'msg':'No users yet'})
            response.status_code = 404
            return response
        else:
            response = jsonify({'users': USERS_LIST})
            response.status_code == 200
            return response
    
    def login_user(self, username, password):
        """Logs in a user given the password and username are correct and valid"""
        username = request.json.get('username', None)
        password = request.json.get('password', None)

        if not username and password:
            return jsonify({'msg':'Username or passowrd is invalid or missing'}), 401
        else:
            global USERS_LIST
            user = [user for user in USERS_LIST if user['username'] == username and user['password'] == password]
            if user:
                response =  jsonify({'msg' : 'Successfully logged in'})
                response.status_code = 200
                return response
            else:
                response = jsonify({'msg' : 'Sorry, problem logging you in'})
                response.status_code = 400
                return response
