import psycopg2
from flask import request, jsonify

from app import migration
from app.api.v2.model_users import get_user_id

connection = migration.db_connection()
cursor = connection.cursor()

class Orders():
    """Class to handle orders"""
    def get_user_order(self, username):
        """Get all orders for a particular user in the database"""
        userid = get_user_id(username)
        try:
            orders_table = "SELECT * FROM orders WHERE user_id = {}".format(userid) 
            cursor.execute(orders_table)
            connection.commit()
            rows = cursor.fetchall()
            print(rows)
            user_orders = []
            if rows is not None and len(rows) > 0:
                for row in rows:
                    order_dict = {
                        "status" : row[1],
                        "meal_name" : row[2],
                        "order_quantity" : row[3],
                        "order_cost" : row[4]
                    }
                    user_orders.append(order_dict)
                return {"orders":user_orders}, 200
            return {'msg': 'No records to fetch'}, 404
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

    def add_order(self, username, meal_item, order_quantity, order_cost):
        """Add an order into the database"""
        userid = get_user_id(username)
        meal_item = request.json.get('meal_item', None)
        order_quantity = request.json.get('order_quantity', None)
        order_cost = request.json.get('order_cost', None)
        
        if not meal_item or not order_quantity or not order_cost:
            return {'msg': 'Missing arguments'}, 400
        
        if not isinstance(meal_item, str) and not isinstance(order_quantity, int) and not isinstance(order_cost, int) :
            return {'msg':'Wrong type'}, 400

        try:
            orders_table = "INSERT INTO orders (status_table_id, meal_item, order_quantity, order_cost, user_id) VALUES (1,'{}','{}','{}','{}')".format(meal_item, order_quantity, order_cost, userid)
            cursor.execute(orders_table)
            connection.commit()
            return {'msg':'Order successfully created'}, 201
        except (Exception, psycopg2.DatabaseError) as error:
            connection.close()
            return {'Error', error}, 400
