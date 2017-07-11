from datetime import datetime
from flask import Flask, render_template,  redirect, url_for, flash

app = Flask(__name__)
app.config['SECRET_KEY'] = "#5|\x0f\xd7\xee\xe2\xc6\t\xe5\xc5Z%\x91\xc2w\xc4\xce'Y\xe0cv\x8c"


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/add', methods=['GET', 'POST'])
def add():
    return render_template('add.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def server_error(e):
    return render_template('500.html'), 500


if __name__ == "__main__":
    app.run(debug=True)
