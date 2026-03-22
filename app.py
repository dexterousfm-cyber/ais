from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///school.db'
db = SQLAlchemy(app)
login_manager = LoginManager(app)

# Routes for authentication, students, teachers, classes, attendance, grades


if __name__ == '__main__':
    app.run(debug=True)