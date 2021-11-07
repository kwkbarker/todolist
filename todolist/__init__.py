from flask import Flask
from flask_login import LoginManager
from flask_admin import Admin

# initialize app, db, session, hash function, login, admin
app = Flask(__name__, static_url_path='/todolist/static')

app.config['SECRET_KEY'] = '5475298b378974fc7aa4f496'

app.config['SESSION_PERMANENT'] = True
app.config['SESSION_TYPE'] = 'filesystem'

login_manager = LoginManager()
login_manager.init_app(app)

app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
admin = Admin(app, template_mode='bootstrap3')

from todolist import routes

# sqlite db initiation
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todolist.db'
# db = SQLAlchemy(app)