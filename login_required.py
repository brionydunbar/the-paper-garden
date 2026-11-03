from functools import wraps
from flask import session, redirect, request

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "user_id" not in session:
            return redirect(f"/sessions/new?next={request.path}")
        return f(*args, **kwargs)
    return decorated_function
