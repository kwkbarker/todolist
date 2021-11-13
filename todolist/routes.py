from flask.globals import request
from flask_login.utils import logout_user
from todolist import app, db
from flask import render_template, redirect, url_for, session, flash, request
from todolist.models import Task, User
from todolist.forms import LoginForm, RegisterForm, TaskForm
from todolist.helpers import login_required
from flask_login import login_user, current_user
import psycopg2
from todolist.storage import get_profile_pic, upload_blob, file_in_storage
import os
from dotenv import load_dotenv

load_dotenv()

@app.route('/')
@app.route('/index')
def home():
    if current_user.is_authenticated:
        return redirect(url_for('tasks'))
    else:
        return redirect(url_for('login'))


@app.route('/tasks', methods=['GET','POST'])
@login_required
def tasks():
    form = TaskForm()
    if request.method == "POST":

        # if 'done' button pressed, delete task from db
        if request.form.get('protocol') == 'delete':
            done_task = Task.query.filter_by(id=form.delete.data).first()
            db.session.delete(done_task)
            db.session.commit()
        elif request.form.get('protocol') == 'post':
            # ensure at least title entered
            if form.title.data != '':
                # add task to db
                task = Task(title=form.title.data,
                            description=form.description.data,
                            importance=form.importance.data,
                            user=session['user_id'])
            
                db.session.add(task)
                db.session.commit()
        elif request.form.get('protocol') == 'put':
            task = Task.query.filter_by(id=request.form.get('id')).first()
            task.title = request.form.get('puttitle')
            task.description = request.form.get('putdescription')
            db.session.commit()

    # retrieve tasks from db
    tasks = Task.query.filter_by(user=User.query.filter_by(id=session['user_id']).first().id).all()
    return render_template('tasks.html', tasks=tasks, form=form)

@app.route('/register', methods = ['GET', 'POST'])
def register():
    form = RegisterForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            print('validated')
            user = User(username=form.username.data,
                        email=form.email.data,
                        password=form.password.data)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('login'))
        
        # error handling
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
            print(user_id)
            if user_id and user_id.check_password(pass_to_check=form.password.data):
                session['user_id'] = user_id.id
                login_user(user_id)
                flash(f'You are logged in as {user_id.username}', category='success')
                return redirect(url_for('tasks'))
           
            # error handling
            else:
                flash('Username or password incorrect.', category='danger')

    return render_template('login.html', form=form)

@app.route('/logout')
def logout():
    session.clear()
    logout_user()
    return redirect('/')


@app.route('/upload', methods = ['POST'])
@login_required
def upload():
    
    bucket_name = "todolist-bucket"
    profile_pic = request.files["profile_pic"]
    dest_filename = f"{current_user.username}-profile-pic"
    upload_blob(bucket_name, profile_pic, dest_filename)

    return redirect(url_for('profile'))

@app.route('/profile')
@login_required
def profile():
    # get profile pic
    bucket = "todolist-bucket"
    filename = f"{current_user.username}-profile-pic"
    public_url = get_profile_pic(bucket, filename)
    print(public_url)
    if file_in_storage(bucket, filename):
        profile_pic = public_url
    else:
        profile_pic = 'https://storage.googleapis.com/todolist-bucket/default-profile-pic'
    return render_template('profile.html', profile_pic=profile_pic)
    