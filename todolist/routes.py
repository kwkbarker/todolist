from flask.globals import request
from flask_login.utils import logout_user
from todolist import app
from flask import render_template, redirect, url_for, session, flash, request
from todolist.models import Task, User
from todolist.forms import LoginForm, RegisterForm, TaskForm
from todolist.helpers import login_required
from flask_login import login_user, current_user
from todolist.database import db_session, Base, engine

def init_db():
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()
    import todolist.models
    Base.metadata.create_all(bind=engine)

if __name__=='__main__()':
    init_db()


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
        print(request.form.get('protocol'))

        # if 'done' button pressed, delete task from db
        if request.form.get('protocol') == 'delete':
            print(form.delete.data)
            done_task = db_session.query(Task).filter(Task.id==form.delete.data).first()
            db_session.delete(done_task)
            db_session.commit()
        elif request.form.get('protocol') == 'post':
            # ensure at least title entered
            if form.title.data != '':
                # add task to db
                task = Task(title=form.title.data,
                            description=form.description.data,
                            importance=form.importance.data,
                            user=session['user_id'])
            
                db_session.add(task)
                db_session.commit()
        elif request.form.get('protocol') == 'put':
            task = db_session.query(Task).filter(Task.id==request.form.get('id')).first()
            print(task.title)
            task.title = request.form.get('puttitle')
            print(task.title)
            task.description = request.form.get('putdescription')
            db_session.commit()

    # retrieve tasks from db
    tasks = db_session.query(Task).filter(Task.id==db_session.query(User).filter(User.id==session['user_id']).first().id).all()
    return render_template('tasks.html', tasks=tasks, form=form)

@app.route('/register', methods = ['GET', 'POST'])
def register():
    form = RegisterForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            user = User(username=form.username.data,
                        email=form.email.data,
                        password=form.password.data)
            db_session.add(user)
            db_session.commit()
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
            user_id = db_session.query(User).filter(User.username==form.username.data).first()
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

from todolist.database import db_session

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()