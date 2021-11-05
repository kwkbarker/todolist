from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_admin import Admin
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sqlalchemy
import logging

# initialize app, db, session, hash function, login, admin
app = Flask(__name__, static_url_path='/todolist/static')

logger = logging.getLogger()
db_config = {
    "pool_size": 5,
    "max_overflow": 2,
    "pool_timeout": 30,
    "pool_recycle": 1800,
}

engine = create_engine(
    sqlalchemy.engine.url.URL.create(
        drivername="postgresql+pg8000",
        username='kwkbarker',
        password='kwkbarker',
        database='barker-todolist:us-east4:todolist-db',
        query={
            "unix-sock": "{}/{}/.s.PGSQL.5432".format(
                "/cloudsql",
                "barker-todolist:us-east4:todolist-db"
            )
        }
    )
)
Session = sessionmaker(engine)
db = Session()

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