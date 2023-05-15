import mysql.connector

def connect_to_database():
    connect = mysql.connector.connect(
        host='localhost',
        port='3306',
        user='srinivas.account',
        password='@123',
        database='instancesdb'
    )
    return connect

def create_instances_table(cursor):
    create_table_query = """
    CREATE TABLE IF NOT EXISTS instances (
        id INT AUTO_INCREMENT PRIMARY KEY,
        instance_id VARCHAR(255)
    )
    """
    cursor.execute(create_table_query)

def create_audit_table(cursor):
    create_table_query = """
    CREATE TABLE IF NOT EXISTS audit (
        id INT AUTO_INCREMENT PRIMARY KEY,
        instance_id VARCHAR(20),
        start_time DATETIME,
        stop_time DATETIME,
        instance_state VARCHAR(20)
    )
    """
    cursor.execute(create_table_query)

def truncate_table(cursor, table_name):
    truncate_query = f"TRUNCATE TABLE {table_name}"
    cursor.execute(truncate_query)

def insert_instance_id(cursor, instance_id):
    insert_query = "INSERT INTO instances (instance_id) VALUES (%s)"
    cursor.execute(insert_query, (instance_id,))

def update_audit_table(cursor, instance_id, stop_time):
    update_query = "UPDATE audit SET stop_time = %s, instance_state = 'STOPPED' WHERE instance_id = %s AND stop_time IS NULL"
    cursor.execute(update_query, (stop_time, instance_id))

def select_instance_ids(cursor):
    select_query = "SELECT instance_id FROM instances"
    cursor.execute(select_query)
    rows = cursor.fetchall()
    return [row[0] for row in rows]
