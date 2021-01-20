from flask import abort
from sqlalchemy.exc import SQLAlchemyError

from app.models import session
from app.models.user import get_user_data_by_user_id
from app.models.friend import Friend, get_friendship_data, get_friend_state


def _create_friend(owner_user_id, other_user_id):
    friendship = Friend(user_id=owner_user_id,
                        friend_user_id=other_user_id)

    additional_friendship = Friend(user_id=other_user_id,
                                   friend_user_id=owner_user_id)

    session.add(friendship)
    session.add(additional_friendship)
    session.commit()
    session.close()


def create_new_friend(owner_user, other_user):

    if owner_user == other_user:
        abort(400, "I can’t make yourself a friend")

    if not get_user_data_by_user_id(other_user):
        abort(404, "This user can't find user data")

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


def get_friends(owner_user):

    friendships = get_friendship_data(owner_user)
    friends = []
    for friendship in friendships:
        friends.append(get_user_data_by_user_id(friendship.friend_user_id))

    return {
        "friends": [
            {
                "id": friend.id,
                "img": friend.img,
                "name": friend.name,
                "statusMessage": friend.introduction
            }
        ] for friend in friends
    }
