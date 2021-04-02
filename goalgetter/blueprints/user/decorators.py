from functools import wraps

from flask import flash, redirect
from flask_login import current_user

def anonymous_required(func):
    @wraps(func)
    def wrapper(url='/home', *args):
        if current_user.is_authenticated:
            return redirect(url)
        return func(*args)
    return wrapper