from flask import abort

from app.services.user import get_user_data_by_user_id
from app.services.friend import get_friendship_data, get_friend_state, insert_friend


def create_new_friend(owner_user, other_user):

    if owner_user == other_user:
        abort(400, "I can’t make yourself a friend")

    if not get_user_data_by_user_id(other_user):
        abort(404, "This user can't find user data")

    if get_friend_state(owner_user, other_user):
        abort(409, "Already friend!")

    insert_friend(owner_user, other_user)

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
                "name": friend.name
            } for friend in friends
        ]
    }


def search_friend_by_user_id(user_id):
    user = get_user_data_by_user_id(user_id)

    if not user:
        abort(404, "This user id not found")

    return {
        "message": "I find that user!"
    }
