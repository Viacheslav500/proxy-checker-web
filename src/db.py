import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()


def get_connection():
    connection = mysql.connector.connect(
        host=os.getenv('HOST', 'localhost'),
        user=os.getenv('USER'),
        password=os.getenv('PASSWORD'),
        database=os.getenv('DATABASE'),
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
    try:
        cur.execute(
            """
                INSERT INTO users (user_proxy, user_ip) 
                VALUES (%s, %s)
            """,
            (proxy, ip_addr)
        )
        conn.commit()
    except mysql.connector.Error:
        conn.rollback()
        raise
    finally:
        close_connection(conn, cur)


def insert_proxy_data(proxy, answer):
    conn, cur = open_connection()
    try:
        cur.execute(
            """
                INSERT INTO proxy_data (proxy, result) 
                VALUES (%s, %s)
            """,
            (proxy, answer)
        )
        conn.commit()
    except mysql.connector.Error:
        conn.rollback()
        raise
    finally:
        close_connection(conn, cur)


def get_proxy():
    conn = get_connection()
    cur = conn.cursor(dictionary=True)
    try:
        cur.execute(
            """
            SELECT proxy, result, created_at FROM proxy_data 
            ORDER BY proxy_id DESC"""
        )
        rows = cur.fetchall()
        return rows
    except mysql.connector.Error:
        raise
    finally:
        close_connection(conn, cur)
