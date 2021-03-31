from functools import wraps
from flask import request, abort


def validate_json(model):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                instance = model(getattr(request, 'json'))
                instance.validate()
            except:
                abort(400, "check JSON key and values")

            return func(*args, **kwargs)
        return wrapper
    return decorator


def validate_args(model):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                instance = model(getattr(request, 'args'))
                instance.validate()
            except:
                abort(400, "check args")

            return func(*args, **kwargs)

        return wrapper

    return decorator
