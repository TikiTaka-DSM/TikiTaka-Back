from werkzeug.security import check_password_hash


def is_current_password(current_hash_password, input_password):
    return check_password_hash(current_hash_password, input_password)