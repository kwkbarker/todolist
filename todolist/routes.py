from flask.globals import request
import flask_login
from flask_login.utils import logout_user
from todolist import app, db, login_manager
from flask import render_template, redirect, url_for, session, flash, request
from todolist.models import Task, User
from todolist.forms import LoginForm, RegisterForm, TaskForm
from todolist.helpers import login_required
from flask_login import login_user, current_user

@app.route('/')
@app.route('/index')
def home():
    print(current_user.is_authenticated)
    if current_user.is_authenticated:
        return redirect(url_for('tasks'))
    else:
        return redirect(url_for('login'))


@app.route('/tasks', methods=['GET','POST'])
@login_required
def tasks():
    form = TaskForm()
    if request.method == "POST":
        print(form.kill.data)
        if form.kill.data != "":
            print(form.kill.data)
            done_task = Task.query.filter_by(id=form.kill.data).first()
            db.session.delete(done_task)
            db.session.commit()
        else:
            if form.title.data != '':
                task = Task(title=form.title.data,
                            description=form.description.data,
                            importance=form.importance.data,
                            user=session['user_id'])
            
                db.session.add(task)
                db.session.commit()

    tasks = Task.query.filter_by(user=User.query.filter_by(id=session['user_id']).first().id).all()
    print(f'tasks = {tasks}')

    return render_template('tasks.html', tasks=tasks, form=form)

@app.route('/register', methods = ['GET', 'POST'])
def register():
    form = RegisterForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            user = User(username=form.username.data,
                        email=form.email.data,
                        password=form.password.data)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('login'))
        if form.errors != {}:
            for msg in form.errors.values():
                flash(f'There was an error creating user: {msg}', category='danger')
    
    return render_template('register.html', form=form)

@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            user_id = User.query.filter_by(username=form.username.data).first()
            print(f'user_id={user_id.id}')
            if user_id and user_id.check_password(pass_to_check=form.password.data):
                session['user_id'] = user_id.id
                login_user(user_id)
                flash(f'You are logged in as {user_id.username}', category='success')
                return redirect(url_for('tasks'))
            else:
                flash('Username or password incorrect.', category='danger')

    return render_template('login.html', form=form)

@app.route('/logout')
def logout():
    session.clear()
    logout_user()
    return redirect('/')

# class AdminView(BaseView):
    @expose('/')
    def index(self):
        return self.render('index.html')
    
    def is_accessible(self):
        return login_manager.current_user.is_authenticated()

    def inaccessible_callback(self, name, **kwargs):
        # redirect to login page if user doesn't have access
        return redirect(url_for('login', next=request.url))