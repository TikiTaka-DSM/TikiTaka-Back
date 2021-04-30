from flask import abort

from app.models.user import UserModel
from app.models.friend import FriendModel


def create_new_friend(owner_user, other_user):

    if owner_user == other_user:
        abort(400, "I can’t make yourself a friend")

    if not UserModel.get_user_data_by_user_id(other_user):
        abort(404, "This user can't find user data")

    if FriendModel.get_friend_state(owner_user, other_user):
        abort(409, "Already friend!")

    FriendModel.insert_friend(owner_user, other_user)

    return {
        "message": "Successfully add friend"
    }


def get_friends(owner_user):

    friendships = FriendModel.get_friendship_data(owner_user)
    friends = []
    for friendship in friendships:
        if friendship.blocking_state:
            continue
        friends.append(UserModel.get_user_data_by_user_id(friendship.friend_user_id))

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
    user = UserModel.get_user_data_by_user_id(user_id)

    if not user:
        abort(404, "This user id not found")

    return {
        "message": "I find that user!"
    }


def search_friend_by_user_name(owner, user_name):
    users = UserModel.get_user_data_by_user_name(owner, user_name)

    return {
        "users": [{
            "id": user.id,
            "img": user.img,
            "name": user.name
        } for user in users]
    }


def block_friend(owner, user_id):
    if not UserModel.get_user_data_by_user_id(user_id):
        abort(404, "User Not Found")

    if not FriendModel.get_friend_state(owner, user_id):
        abort(409, "Not Friend")

    FriendModel.switching_blocking_state(owner, user_id)

    return {
        "message": "Switching Blocking State"
    }
