from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_session import Session
from flask_admin import Admin

# initialize app, db, session, hash function, login, admin
app = Flask(__name__, static_url_path='/todolist/static')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todolist.db'
db = SQLAlchemy(app)

app.config['SECRET_KEY'] = '5475298b378974fc7aa4f496'

app.config['SESSION_PERMANENT'] = True
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

bcrypt = Bcrypt(app)

login_manager = LoginManager()
login_manager.init_app(app)

app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
admin = Admin(app, template_mode='bootstrap3')

from todolist import routes


