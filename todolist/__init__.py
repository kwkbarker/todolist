from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
# from flask_session import Session
from flask_admin import Admin
import os
import pymysql

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
# db_connection_name = os.environ["CLOUD_SQL_CONNECTION_NAME"]

# if os.environ.get('GAE_ENV') == 'standard':
#     # If deployed, use the local socket interface for accessing Cloud SQL
#     unix_socket = '/cloudsql/{}'.format(db_connection_name)
#     cnx = pymysql.connect(user=db_user, password=db_password,
#                             unix_socket=unix_socket, db=db_name)
# else:
#     # If running locally, use the TCP connections instead
#     # Set up Cloud SQL Proxy (cloud.google.com/sql/docs/mysql/sql-proxy)
#     # so that your application can use 127.0.0.1:3306 to connect to your
#     # Cloud SQL instance
#     host = '127.0.0.1'
#     cnx = pymysql.connect(user=db_user, password=db_password,
#                             host=host, db=db_name)

# with cnx.cursor() as cursor:
#     cursor.execute('YOUR QUERY GOES HERE;')
#     result = cursor.fetchall()
#     current_msg = result[0][0]
# cnx.close()

# # return str(current_msg)