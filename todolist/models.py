from todolist import db, login_manager, admin
from todolist import bcrypt
from flask_login import UserMixin
from flask_admin.contrib.sqla import ModelView


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
    
class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=30), nullable=False, unique=True)
    email = db.Column(db.String(length=50), nullable=False, unique=True)
    password_hash = db.Column(db.String(length=60), nullable=False, unique=True)
    tasks = db.relationship('Task', backref='created_by_user', lazy=True)

    def __str__(self) -> str:
        return self.username

    @property
    def password(self):
        return self.password
    
    @password.setter
    def password(self, unhashed_pw):
        self.password_hash = bcrypt.generate_password_hash(unhashed_pw).decode('utf-8')


    def check_password(self, pass_to_check):
        return bcrypt.check_password_hash(self.password_hash, pass_to_check)


class Task(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(length=128), nullable=False)
    description = db.Column(db.String(length=1024), nullable=False)
    importance = db.Column(db.String(length=12), nullable=False)
    user = db.Column(db.Integer(), db.ForeignKey('user.id'))

    def __repr__(self):
        return self.title

# add db views to admin page
admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Task, db.session))