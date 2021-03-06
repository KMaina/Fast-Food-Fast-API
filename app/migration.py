"""
File to manage the connection to the database, creation and deletion of tables
"""
import os
import psycopg2

def db_connection(config=None):
    """Make a connection to the DB"""
    if config == 'testing':
        db_name = os.getenv('DB_TEST')
    else:
        db_name = os.getenv('DB_MAIN')
    user = os.getenv('DB_USER')
    password = os.getenv('DB_PASSWORD')
    host = os.getenv('DB_HOST')
    port = os.getenv('DB_PORT')

    return  psycopg2.connect(user=user, password=password, host=host, port=port, database=db_name)
    

def create_tables(cursor):
    """Create all tables"""
    statements = (
        """
        CREATE TABLE IF NOT EXISTS users (
            user_id SERIAL PRIMARY KEY,
            username VARCHAR(255) NOT NULL UNIQUE,
            password VARcHAR(255) NOT NULL,
            email VARCHAR(255) NOT NULL UNIQUE,
            address VARCHAR(255) NOT NULL,
            telephone VARCHAR(255) NOT NULL,
            admin BOOLEAN NOT NULL
        )
        """,
        """ CREATE TABLE IF NOT EXISTS status (
                status_id SERIAL PRIMARY KEY,
                status_name VARCHAR(255) NOT NULL
            )
        """,
        """
        CREATE TABLE IF NOT EXISTS menus (
                menu_id SERIAL PRIMARY KEY,
                meal_name VARCHAR(255) NOT NULL UNIQUE,
                quantity INTEGER NOT NULL,
                description VARCHAR(255) NOT NULL,
                cost INTEGER NOT NULL
            )
        """,
        """
        CREATE TABLE IF NOT EXISTS orders (
                order_id SERIAL,
                status_table_id INT REFERENCES status(status_id) ON DELETE CASCADE,
                meal_item VARCHAR(255) NOT NULL,
                order_quantity INT NOT NULL,
                order_cost INT NOT NULL,
                user_id INT REFERENCES users(user_id) ON DELETE CASCADE,
                PRIMARY KEY (order_id, status_table_id, user_id)
            )
        """)

    for statement in statements:
        cursor.execute(statement)

def drop_tables(cursor): 
    """Drops all tables"""
    drops = ["DROP TABLE users CASCADE",
             "DROP TABLE orders CASCADE",
             "DROP TABLE menus CASCADE",
             "DROP TABLE status CASCADE"]
    for drop in drops:
        cursor.execute(drop)
    cursor.close()
    connection.commit()

def main(config=None):
    """
    This function is run in the command line to automate the connection to the database
    and creation of tables in the database
    """
    connection = db_connection(config=config)
    cursor = connection.cursor()

    create_tables(cursor)

    connection.commit()

    cursor.close()

    connection.close()

    print('Done')

if __name__ == '__main__':
    main()
