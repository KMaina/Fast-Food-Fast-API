import psycopg2
from flask import request, jsonify

from app import migration
from app.api.v1.model import get_user_id

connection = migration.db_connection()
cursor = connection.cursor()

class Orders():
    """Class to handle orders"""
    def add_order(self, username, meal_id, quantity, cost):
        """Add an order into the database"""
        active_user = get_user_id(username)
        if not active_user:
            return {'msg':'error getting the user'}, 404

        meal_id = request.json.get('meal_id', None)
        quantity = request.json.get('quantity', None)
        cost = request.json.get('cost', None)

        if len(meal_id) != len(quantity) and len(cost):
            return {'msg':'Not equal length'}, 400

        total_cost = 0
        for quantity, cost in zip(quantity,cost):
            total_cost = total_cost + (quantity * cost)
        
        order_quantity = request.json.get('quantity', None)
        order_cost = request.json.get('cost', None)

        try:
            orders_table = "INSERT INTO orders \
                            (status_id, user_id, total_cost) \
                            VALUES \
                            (1, '{}' , '{}') RETURNING order_id" .format(active_user , total_cost) 
            
            cursor.execute(orders_table)
            connection.commit()
            
            orders_table_id = cursor.fetchone()[0]
            print(meal_id, order_quantity, order_cost)
            for meal_id, order_quantity, order_cost in zip(meal_id, order_quantity, order_cost):
                users_orders = "INSERT INTO users_orders \
                        (users_order_id, order_quantity, meal_id, order_cost) \
                        VALUES \
                        ('{}','{}','{}','{}')" .format(orders_table_id, order_quantity, meal_id, order_cost)
                    
                cursor.execute(users_orders)
                connection.commit()
            return {'msg':'Order successfully created'}, 201
        except (Exception, psycopg2.DatabaseError) as error:
            print('h')
            connection.close()
            return {'Error', error}, 400
