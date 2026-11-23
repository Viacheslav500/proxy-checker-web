import os
from dotenv import load_dotenv
from flask import Flask, request, render_template, redirect, url_for, flash, session
from .db import (
        insert_user_table, 
        insert_proxy_data, 
        get_proxy, 
        insert_into_users_data, 
        get_user_for_check, 
        check_hash
)
from .main_checker import check_proxy


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATES_DIR = os.path.join(BASE_DIR, '..', 'templates')
STATIC_DIR = os.path.join(BASE_DIR, '..', 'static')


app = Flask(__name__, template_folder=TEMPLATES_DIR, static_folder=STATIC_DIR)


load_dotenv()
app.secret_key = os.getenv('SECRET_KEY', 'fallback-secret-key')


@app.route('/')
def showing_main_page():
    return render_template('description.html')


def get_user_ip():
    ip_address = request.remote_addr
    return ip_address


@app.route('/index', methods=['GET', 'POST'])
def checking():
    result = None
    if request.method == 'POST':
        proxy_variable = request.form.get('proxy', '')
        if proxy_variable:
            result = check_proxy(proxy_variable)
            insert_user_table(proxy_variable, get_user_ip())
            insert_proxy_data(proxy_variable, result)
    return render_template('index.html', result=result)


@app.route('/history')
def get_history():
    rows = get_proxy()
    return render_template('history.html', rows=rows)


@app.route('/registration', methods=['GET', 'POST'])
def registrate_user():
    if request.method == 'POST':
        user_name = request.form.get('nickname', '').strip()
        password = request.form.get('user_password', '')
        password_2 = request.form.get('pass_confirmation', '')
        if len(user_name) < 3:
            flash('Name should be at least three characters', 'alert-danger')
        elif len(password) < 8:
            flash('Password should be at least eight characters', 'alert-danger')
        elif password != password_2:
            flash('Passwords must match', 'alert-danger')
        elif get_user_for_check(user_name):
            flash('This nickname is used, enter another one', 'alert-danger')
        else:
            insert_into_users_data(user_name, password, get_user_ip())
            flash('Registration is completed', 'alert-success')
        return redirect(url_for('showing_main_page'))
    return render_template('registration.html')


@app.route('/login', methods=['GET', 'POST'])
def login_user():
    if request.method == 'POST':
        name = request.form.get('user_name', '').strip()
        password = request.form.get('login_password', '')
        result = check_hash(name, password)
        if result is True:
            session.clear()
            session['name'] = name
            session['logged_in'] = True
            flash('You are logged in', 'alert-success')
            return redirect(url_for('showing_main_page'))
        elif result is False:
            flash('Incorrect password', 'alert-danger')
        else:
            flash('User is not found', 'alert-danger')
        return redirect(url_for('login_user'))
    return render_template('login.html')


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('showing_main_page'))


if __name__ == '__main__':
    app.run(debug=True)
