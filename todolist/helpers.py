from functools import wraps
from flask import request, redirect, url_for
from flask_login import current_user

# login required decorator for task view
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated:
            return redirect(url_for('login', next=request.url))
        return f(*args, **kwargs)
    return decorated_function