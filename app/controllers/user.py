from flask import abort
from flask_jwt_extended import create_access_token
from werkzeug.security import generate_password_hash

from app.models.user import UserModel
from app.services.auth import is_current_password


def sign_up(user_id, user_password, user_name):
    if UserModel.get_user_data_by_user_id(user_id):
        abort(409, "This id is already signed up")

    UserModel.insert_user(user_id, generate_password_hash(user_password), user_name)

    return {
        "message": "Successfully signed up"
    }, 201


def login(user_id, user_password):

    user = UserModel.get_user_data_by_user_id(user_id)

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
