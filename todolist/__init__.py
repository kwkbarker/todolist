from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_admin import Admin

# initialize app, db, session, hash function, login, admin
app = Flask(__name__, static_url_path='/todolist/static')


PASSWORD ="theBusiness"
PUBLIC_IP_ADDRESS ="34.145.154.60"
DBNAME ="todolist-db"
INSTANCE_NAME ="barker-todolist:us-east4:todolist-db"
 
# configuration

# DB_URI = "postgresql+pg8000://kwkbarker:{PASSWORD}@/{DBNAME}?unix_sock=<socket_path>/<cloud_sql_instance_name>/.s.PGSQL.5432"

app.config["SQLALCHEMY_DATABASE_URI"]= f'postgresql+psycopg2://kwkbarker:{PASSWORD}@/{DBNAME}?host={PUBLIC_IP_ADDRESS}'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]= True

# initialize database
db = SQLAlchemy(app)
db.drop_all()
db.create_all()


app.config['SECRET_KEY'] = '5475298b378974fc7aa4f496'

app.config['SESSION_PERMANENT'] = True
app.config['SESSION_TYPE'] = 'filesystem'

login_manager = LoginManager()
login_manager.init_app(app)

app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
admin = Admin(app, template_mode='bootstrap3')

from todolist import routes
