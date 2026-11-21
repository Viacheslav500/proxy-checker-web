import os
import mysql.connector
from dotenv import load_dotenv
from werkzeug.security import generate_password_hash, check_password_hash

load_dotenv()


def get_connection():
    connection = mysql.connector.connect(
        host=os.getenv('HOST', 'localhost'),
        port=3306,
        user=os.getenv('USERNAME'),
        password=os.getenv('PASSWORD_MYSQL'),
        database=os.getenv('DATABASE_NAME'),
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


def insert_into_users_data(name, password, ip_addr):
    conn, cur = open_connection()
    try:
        cur.execute(
            """
            INSERT INTO users_data (nickname, password_hash, user_ip)
            VALUES (%s, %s, %s)
            """,
            (name, generate_password_hash(password), ip_addr)
        )
        conn.commit()
    except mysql.connector.Error:
        conn.rollback()
        raise
    finally:
        close_connection(conn, cur)


def get_user_for_check(user_name):
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute(
                """
                SELECT nickname FROM users_data
                WHERE nickname = %s
                """,
                (user_name,)
        )
        data= cur.fetchone()
        return data
    except mysql.connector.Error:
        raise
    finally:
        close_connection(conn, cur)


def get_nickname_to_check_hash(user_name):
    conn = get_connection()
    cur = conn.cursor(dictionary=True)
    try:
        cur.execute(
            """ 
            SELECT users_id, nickname, password_hash
            FROM users_data
            WHERE nickname = %s
            """, 
            (user_name,)
        )
        data = cur.fetchone()
        return data
    except mysql.connector.Error:
        raise
    finally:
        close_connection(conn, cur)


def check_hash(name, password):
    user = get_nickname_to_check_hash(name)

    if user is None:
        return None

    is_valid = check_password_hash(user['password_hash'], password)

    if not is_valid:
        return False

    else:
        return True
