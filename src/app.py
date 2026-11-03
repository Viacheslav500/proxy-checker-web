import os
from flask import Flask, request, render_template
from main_checker import check_proxy
from db import inser_user_table, insert_proxy_data, get_proxy


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATES_DIR = os.path.join(BASE_DIR, '..', 'templates')
STATIC_DIR = os.path.join(BASE_DIR, '..', 'static')


app = Flask(__name__, template_folder=TEMPLATES_DIR, static_folder=STATIC_DIR)

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
        proxy_variable = request.form.get('proxy')
        if proxy_variable:
            result = check_proxy(proxy_variable)
            insert_user_table(proxy_variable, get_user_ip())
            insert_proxy_data(proxy_variable, result)
    return render_template('index.html', result=result)


@app.route('/history')
def get_history():
    rows = get_proxy()
    return render_template('history.html', rows=rows)

if __name__ == '__main__':
    app.run(debug=True)
