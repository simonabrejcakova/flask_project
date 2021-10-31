from mdblog.models import User
from flask import session
from flask import redirect
from flask import url_for
from flask import flash
from functools import wraps


def login_required(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        if "logged" not in session:
            flash("You must be logged in and have a permission", "alert-danger")
            return redirect(url_for("main.view_welcome_page"))
        return func(*args, **kwargs)
    return decorated_function


def login_required1(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        if "ahoj" not in session:
            flash("You must be logged in and have a permisson", "alert-danger")
            return redirect(url_for("main.view_welcome_page"))
        return func(*args, **kwargs)
    return decorated_function
