import os
from flask import Flask, request, render_template
from main_checker import check_proxy


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATES_DIR = os.path.join(BASE_DIR, '..', 'templates')
STATIC_DIR = os.path.join(BASE_DIR, '..', 'static')


app = Flask(__name__, template_folder=TEMPLATES_DIR, static_folder=STATIC_DIR)

@app.route('/', methods=['GET', 'POST'])
def checking():
    result = None
    if request.method == 'POST':
        proxy_variable = request.form.get('proxy')
        if proxy_variable:
            result = check_proxy(proxy_variable)
    return render_template('view_result.html', result=result)


def get_user_ip():
    ip_address = request.remote_addr
    return ip_address


if __name__ == '__main__':
    app.run(debug=True)
