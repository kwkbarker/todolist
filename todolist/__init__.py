from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
# from flask_session import Session
from flask_admin import Admin
import os
import sqlalchemy

# initialize app, db, session, hash function, login, admin
app = Flask(__name__, static_url_path='/todolist/static')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todolist.db'
db = SQLAlchemy(app)

app.config['SECRET_KEY'] = '5475298b378974fc7aa4f496'

app.config['SESSION_PERMANENT'] = True
app.config['SESSION_TYPE'] = 'filesystem'
# Session(app)

login_manager = LoginManager()
login_manager.init_app(app)

app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
admin = Admin(app, template_mode='bootstrap3')

from todolist import routes

# db_user = os.environ["CLOUD_SQL_USERNAME"]
# db_password = os.environ["CLOUD_SQL_PASSWORD"]
# db_name = os.environ["CLOUD_SQL_DATABASE_NAME"]
# db_host = os.environ["CLOUD_SQL_CONNECTION_NAME"]

# # Extract port from db_host if present,
# # otherwise use DB_PORT environment variable.
# host_args = db_host.split(":")
# if len(host_args) == 1:
#     db_hostname = db_host
#     db_port = os.environ["DB_PORT"]
# elif len(host_args) == 2:
#     db_hostname, db_port = host_args[0], int(host_args[1])

# db = sqlalchemy.create_engine(
#     # Equivalent URL:
#     # mysql+pymysql://<db_user>:<db_pass>@<db_host>:<db_port>/<db_name>
#     sqlalchemy.engine.url.URL.create(
#         drivername="mysql+pymysql",
#         username=db_user,  # e.g. "my-database-user"
#         password=db_password,  # e.g. "my-database-password"
#         host=db_hostname,  # e.g. "127.0.0.1"
#         port=db_port,  # e.g. 3306
#         database=db_name,  # e.g. "my-database-name"
#     ),
#     # **db_config
# )

# app.config['SQLALCHEMY_DATABASE_URI'] = f'{db_user}:{db_password}@{db_hostname}:{db_port}'
# db = SQLAlchemy(app)