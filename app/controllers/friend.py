from flask import abort
from sqlalchemy.exc import SQLAlchemyError

from app.models import session
from app.models.friend import Friend


def get_friend_state(owner_user, other_user):
    friendship = session.query(Friend).filter(Friend.user_id == owner_user).\
                          filter(Friend.friend_user_id == other_user).first()

    if friendship:
        return True

    return False


def _create_friend(owner_user_id, other_user_id):
    friendship = Friend(user_id=owner_user_id,
                        friend_user_id=other_user_id)

    additional_friendship = Friend(user_id=other_user_id,
                                   friend_user_id=owner_user_id)

    session.add(friendship)
    session.add(additional_friendship)
    session.commit()


def create_new_friend(owner_user, other_user):

    if get_friend_state(owner_user, other_user):
        abort(409, "Already friend!")

    try:
        _create_friend(owner_user, other_user)

    except SQLAlchemyError as e:
        print("[ERROR MESSAGE] " + str(e))
        session.rollback()

        abort(418, "db_error")

    return {
        "message": "Successfully add friend"
    }
