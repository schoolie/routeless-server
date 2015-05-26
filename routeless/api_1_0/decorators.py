# Embedded file name: C:\Development\flasky\app\api_1_0\decorators.py
from functools import wraps
from flask import g
from .errors import forbidden

from datetime import timedelta
from flask import make_response, request, current_app
from functools import update_wrapper

def permission_required(permission):

    def decorator(f):

        @wraps(f)
        def decorated_function(*args, **kwargs):
            if not g.current_user.can(permission):
                return forbidden('Insufficient permissions')
            return f(*args, **kwargs)

        return decorated_function

    return decorator