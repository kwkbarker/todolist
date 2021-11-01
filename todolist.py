from flask.globals import request
from todolist import app
from todolist import db
from flask import render_template, redirect, url_for, session, flash, request
from todolist.models import Task, User
from todolist.forms import LoginForm, RegisterForm, TaskForm

from models import Task, User



@app.route('/')
@app.route('/index')
@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/tasks', methods=['GET','POST'])
def tasks():
    tasks = Task.query.filter_by(username=session.get('user_id'))

@app.route('/register', methods = ['GET', 'POST'])
def register():
    form = RegisterForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            user = User(username=form.username.data,
                        email=form.email.data,
                        password=form.password.data)
            db.sessoin.add(user)
            db.commit()
            return redirect(url_for('tasks'))
        if form.errors != {}:
            for msg in form.errors.values():
                flash(f'There was an error creating user: {msg}', category='danger')
    else:
        return render_template('register.html')

@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            user_id = User.query.filter_by(username=form.username.data).first()
            if user_id and user_id.check_password(password=form.password.data):
                session['user_id'] = user_id
                flash(f'You are logged in as {user_id.username}', category='success')
                return redirect(url_for('tasks'))
            else:
                flash('Password incorrect.', category='danger')
        else:
            return render_template('login.html', form=form)
    else:
        return render_template('login.html', form=form)

