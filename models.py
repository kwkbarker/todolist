from todolist import db
from todolist import bcrypt
from flask_login import UserMixin

class Task(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(length=128), nullable=False)
    description = db.Column(db.String(length=1024), nullable=False)
    user = db.Column(db.Integer(), db.ForeignKey('user.id'))
    def __repr__(self):
        return self.title
    
class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=30), nullable=False, unique=True)
    email_address = db.Column(db.String(length=50), nullable=False, unique=True)
    password_hash = db.Column(db.String(length=60), nullable=False, unique=True)
    tasks = db.relationship('Task', backref='user', lazy=True)

    @property
    def password(self):
        return self.password
    
    @password_setter
    def password(self, unhashed_pw):
        self.password_hash = bcrypt.generate_password_hash(unhashed_pw).decode('utf-8')


    def check_password(self, pass_to_check):
        return bcrypt.check_password_hash(self.password_hash, pass_to_check)