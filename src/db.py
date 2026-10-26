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


def insert_user_table(proxy, ip_addr):
    conn, cur = open_connection()
    cur.execute('INSERT INTO users (user_proxy, created_at, user_ip) VALUES (%s, %s, %s)', (proxy, datetime.now(), ip_addr))
    conn.commit()
    close_connection(conn, cur)


def insert_proxy_data(proxy, answer):
    conn, cur = open_connection()
    cur.execute('INSERT INTO proxy_data (proxy, result) VALUES (%s, %s)', (proxy, answer))
    conn.commit()
    close_connection(conn, cur)


def get_proxy():
    conn, cur = open_connection()
    cur.execute('SELECT proxy, result FROM proxy_data ORDERED BY proxy_id DESC')
    return cur.fetchall()
    close_connection(conn, cur)
