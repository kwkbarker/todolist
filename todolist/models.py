from sqlalchemy.sql.schema import ForeignKey
from todolist import login_manager, admin
from flask_login import UserMixin
from flask_admin.contrib.sqla import ModelView
import bcrypt
from todolist.database import Base, db_session
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
    
class User(Base, UserMixin):
    __tablename__ = 'user'
    id = Column(Integer(), primary_key=True)
    username = Column(String(length=30), nullable=False, unique=True)
    email = Column(String(length=50), nullable=False, unique=True)
    password_hash = Column(String(length=60), nullable=False, unique=True)
    tasks = relationship('Task', backref='user_backref', lazy=True)

    def __str__(self) -> str:
        return self.username

    @property
    def password(self):
        return self.password
    
    @password.setter
    def password(self, unhashed_pw):
        self.password_hash = bcrypt.hashpw(unhashed_pw.encode('utf-8'), bcrypt.gensalt())


    def check_password(self, pass_to_check):
        return bcrypt.hashpw(pass_to_check.encode('utf-8'), self.password_hash) == self.password_hash


class Task(Base):
    __tablename__ = 'task'
    id = Column(Integer(), primary_key=True)
    title = Column(String(length=128), nullable=False)
    description = Column(String(length=1024), nullable=False)
    importance = Column(String(length=12), nullable=False)
    user = Column(Integer(), ForeignKey('user.id'))

    def __repr__(self):
        return self.title

# add db views to admin page
admin.add_view(ModelView(User, db_session))
admin.add_view(ModelView(Task, db_session))

# # prints SQL commands for cloud sql table creation
# print(CreateTable(User.__table__))
# print(CreateTable(Task.__table__))