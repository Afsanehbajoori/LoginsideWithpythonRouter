from flask import Flask, render_template,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
from sqlserver import adgsqlserver

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'localhost'

db = SQLAlchemy(app)


@app.route('/login')
def index():
    return render_template("login.html")


@app.route('/register')
def new_user():
    return render_template("register.html")


@app.route('/profile')
def profile():
    return render_template("profile.html")


if __name__ == '__main__':
    app.run(debug=True)
