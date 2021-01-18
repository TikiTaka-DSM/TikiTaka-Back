from flask import abort
from flask_jwt_extended import create_access_token
from werkzeug.security import generate_password_hash
from sqlalchemy.exc import SQLAlchemyError

from app.models import session
from app.models.user import User
from app.services.auth import is_current_password


def get_user_data_by_user_id(user_id):
    return session.query(User).filter(User.id == user_id).first()


def _create_user(user_id, user_password, user_name):

    user = User(id=user_id,
                password=generate_password_hash(user_password),
                name=user_name,
                img='default.png',
                introduction='')

    session.add(user)
    session.commit()


def sign_up(user_id, user_password, user_name):
    if get_user_data_by_user_id(user_id):
        abort(409, "This id is already signed up")

    try:
        _create_user(user_id, user_password, user_name)

    except SQLAlchemyError as e:
        print("[ERROR MESSAGE] " + str(e))

        session.rollback()
        abort(418, "db_error")

    return {
        "message": "Successfully signed up"
    }, 201


def login(user_id, user_password):

    user = get_user_data_by_user_id(user_id)

    if user:
        if is_current_password(user.password, user_password):
            access_token = create_access_token(identity=user_id)

            return {
                "tokens": {
                    "accessToken": access_token
                }
            }
        else:
            abort(400, "The password is incorrect")
    else:
        abort(404, "The user not found")
