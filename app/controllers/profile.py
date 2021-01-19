from flask import abort
from sqlalchemy.exc import SQLAlchemyError

from app.models.user import get_user_data_by_user_id
from app.models.friend import get_friend_state


def get_profile(owner_user_id, other_user_id):

    if owner_user_id == other_user_id:
        abort(409, "Please use 'GET /profile' api")

    user_data = get_user_data_by_user_id(other_user_id)
    friend_state = get_friend_state(owner_user_id, other_user_id)
    # SQLAlchemyError 대한 처리가 동일 하기 때문에 데코레이터로 만들어 함수가 위치한 model에서 처리하는게 나아보임

    return {
        "profileData": {
            "img": user_data.img,
            "name": user_data.name,
            "statusMessage": user_data.introduction
        },
        "state": {
            "friend": True if friend_state else False,
            "block": friend_state.blocking_state
        }
    }
