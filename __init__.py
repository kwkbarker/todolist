from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import os
from flask_session import Session

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todolist.db'
app.config['SECRET_KEY'] = '5475298b378974fc7aa4f496'
app.config['SESSION_PERMANENT'] = True
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)


from todolist import routes


