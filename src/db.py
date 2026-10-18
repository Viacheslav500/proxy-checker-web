import mysql.connector

def get_connection():
    connection = connector.connect (
        host='localhost',
        user='user_name',
        password='password',
        database='database_name'
)
    return connection


def open_connection():
    conn = get_connection()
    cursor = connection.cursor()
    return conn, cursor


def close_connection(conn, cursor):
    if cursor is not None:
        cursor.close()
    if conn is not None:
        conn.close()



