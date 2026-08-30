from flask import Flask, request, render_template
from main_checker import check_proxy

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def checking():
    result = None
    if request.method == 'POST':
        proxy_variable = request.form.get('proxy')
        if proxy_variable:
            result = check_proxy(proxy_variable)
    return render_template('view_result.html', result=result)


if __name__ == '__main__':
    app.run(debug=True)
