import mysql.connector
from datetime import datetime

def get_connection():
    connection = mysql.connector.connect (
        host='localhost',
        user='user_name',
        password='password',
        database='database_name'
)
    return connection


def open_connection():
    conn = get_connection()
    cursor = conn.cursor()
    return conn, cursor


def close_connection(conn, cursor):
    if cursor is not None:
        cursor.close()
    if conn is not None:
        conn.close()


def get_user_table(conn, proxy, date, ip_addr):
    cur = conn.cursor()
    cur.execute('INSERT INTO users (user_proxy, created_at, user_ip) VALUES (%s, %s, %s)', (proxy, datetime.now(), ip_addr))
    conn.commit()
    cur.close()

def get_proxy_data(conn, proxy, answer):
    cur = conn.cursor()
    cur.execute('INSERT INTO proxy_data (proxy, result) VALUES (%s, %s)', (proxy, answer))
    conn.commit()
    cur.close()
